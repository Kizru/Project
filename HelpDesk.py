import flet as ft
import os
import subprocess
import tkinter as tk
from tkinter import filedialog
import json
import pyperclip

from CheckCompatibility import check_full_build_compatibility
from DataBaseClass import ComponentDB
from ComponentComparison.ComponentsComparison import compare_components_page
from HelpFile import open_help_file

db = ComponentDB()

# Генерация списка сборок
gaming_builds = [f"Игровая сборка {i}" for i in range(1, 11)]
office_builds = [f"Офисная сборка {i}" for i in range(1, 11)]
all_builds = gaming_builds + office_builds

build_details = {
    # Здесь остаются данные о сборках (как в оригинале)
}

def main(page: ft.Page):
    def open_helpdesk(e=None):
        if page.route == "/":
            help_file = "main_help.chm"
        elif page.route == "/create":
            help_file = "create_help.chm"
        elif page.route.startswith("/details/"):
            help_file = "details_help.chm"
        elif page.route == "/compare":
            help_file = "compare_help.chm"
        elif page.route == "/support":
            help_file = "support_help.chm"
        full_path = os.path.abspath(help_file)
        if not os.path.exists(full_path):
            print(f"Файл {full_path} не найден!")
            return
        try:
            subprocess.Popen(["hh.exe", full_path], shell=False)
        except Exception as ex:
            print(f"Ошибка при открытии файла справки: {ex}")

    def on_keyboard(e: ft.KeyboardEvent):
        if e.key == "F1":
            open_helpdesk()

    page.title = "Конфигуратор ПК"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 20
    page.spacing = 10
    page.window_width = 800
    page.window_height = 600
    page.bgcolor = "#E0E0E6"
    page.on_keyboard_event = on_keyboard

    builds_row = ft.Row(scroll="auto", spacing=10, alignment=ft.MainAxisAlignment.SPACE_BETWEEN)

    def create_buttons(build_list):
        return [
            ft.ElevatedButton(
                content=ft.Text(build, size=14),
                width=100,
                height=100,
                style=ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=5),
                    color={"": "white"},
                    bgcolor={"": "#ADD8E6"},
                ),
                on_click=lambda e, name=build: page.go(f"/details/{name}"),
            ) for build in build_list
        ]

    builds_row.controls = create_buttons(all_builds)

    builds_container = ft.Container(
        content=builds_row,
        padding=10,
        border=ft.border.all(1, "lightgray"),
        border_radius=10,
    )

    def set_filter(category):
        builds_row.controls.clear()
        if category == "Все":
            builds_row.controls.extend(create_buttons(all_builds))
        elif category == "Игровые":
            builds_row.controls.extend(create_buttons(gaming_builds))
        elif category == "Офисные":
            builds_row.controls.extend(create_buttons(office_builds))
        page.update()

    filter_controls = ft.Row(
        [
            ft.OutlinedButton("Все", on_click=lambda _: set_filter("Все")),
            ft.OutlinedButton("Офисные", on_click=lambda _: set_filter("Офисные")),
            ft.OutlinedButton("Игровые", on_click=lambda _: set_filter("Игровые")),
        ],
        spacing=10,
    )

    main_container = ft.Container(
        content=ft.Column([
            ft.Row([ft.Text("Конфигуратор ПК", size=20, weight=ft.FontWeight.BOLD), ft.IconButton(
                icon=ft.icons.POWER_SETTINGS_NEW,
                tooltip="Выйти из приложения",
                on_click=lambda e: page.window.close()
            )], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            ft.Divider(height=1, color="black"),
            ft.Row([
                ft.Text("Популярные сборки", size=16),
                ft.Row([
                    ft.ElevatedButton("Создать сборку", on_click=lambda _: page.go("/create")),
                    ft.ElevatedButton("Сравнение комплектующих", on_click=lambda _: page.go("/compare")),
                    ft.ElevatedButton("Загрузить сборку", on_click=lambda _: load_build_from_file()),
                ], spacing=10),
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            filter_controls,
            builds_container,
            ft.Row([
                ft.ElevatedButton("Помощь", on_click=open_help_file),
                ft.ElevatedButton("Служба поддержки", on_click=lambda _: page.go("/support")),
            ], alignment=ft.MainAxisAlignment.END, spacing=10),
        ], spacing=20),
        padding=20,
        border_radius=10,
        bgcolor="#F0F0F0",
    )

    # Создание строки таблицы с кнопкой выбора
    def create_table_row(title, description, component_type, update_callback):
        # Если описание — это кортеж (название, цена), разделяем его
        if isinstance(description, tuple):
            label_text = description[0]
            price_text = f"{description[1]} рублей"
        else:
            label_text = description or "..."
            price_text = "... рублей"

        label = ft.Text(label_text, size=12)
        price_label = ft.Text(price_text, size=12)

        # Используем метод get_full_by_category для получения данных
        menu_items = []
        try:
            # Получаем данные из базы данных
            category_data = db.get_full_by_category(component_type.lower())
            for row in category_data:
                name, price = row[1], row[2]  # Предполагается, что структура: id, name, price, ...
                menu_items.append(
                    ft.PopupMenuItem(
                        text=f"{name} ({price} руб)",
                        on_click=lambda e, item=(name, price): update_callback(title, item, label, price_label)
                    )
                )
        except ValueError as ex:
            print(f"Ошибка при получении данных для категории {component_type}: {ex}")

        popup_menu = ft.PopupMenuButton(
            icon=ft.icons.ARROW_FORWARD_IOS_ROUNDED,
            tooltip="Изменить комплектующую",
            items=menu_items,
            icon_size=20,
            bgcolor="#FFFFFF"
        )

        return ft.Row([
            ft.Container(
                content=ft.Text(title, size=14, weight=ft.FontWeight.BOLD),
                alignment=ft.alignment.center_left,
                padding=ft.padding.only(left=10),
                width=150,
                height=50,
                bgcolor="#FFFFFF",
                border_radius=5,
            ),
            ft.Container(
                content=ft.Column([
                    label,
                    price_label,
                ], alignment=ft.MainAxisAlignment.CENTER),
                alignment=ft.alignment.center,
                padding=ft.padding.only(left=10),
                width=300,
                height=50,
                bgcolor="#FFFFFF",
                border_radius=5,
            ),
            ft.Container(
                content=popup_menu,
                alignment=ft.alignment.center_right,
                padding=ft.padding.only(right=10),
                width=50,
                height=50,
                bgcolor="#FFFFFF",
                border_radius=5,
            ),
        ], spacing=10, height=50)

    def build_details_page(page: ft.Page, build_name: str, loaded_details: dict = None):
        details = loaded_details if loaded_details else build_details.get(build_name, {})
        total_price = sum(item[1] for item in details.values() if isinstance(item, tuple) and len(item) == 2)
        total_cost_label = ft.Text(f"Итоговая стоимость ПК\n{total_price} рублей", size=16, weight=ft.FontWeight.BOLD)
        compatibility_result = ft.Text("", size=14, color=ft.colors.RED)

        def update_component(component_title, new_value, label, price_label):
            nonlocal total_price
            old_value = details.get(component_title)
            if isinstance(old_value, tuple) and len(old_value) == 2:
                total_price -= old_value[1]
            details[component_title] = new_value
            label.value = new_value[0]
            price_label.value = f"{new_value[1]} рублей"
            total_price += new_value[1]
            total_cost_label.value = f"Итоговая стоимость ПК\n{total_price} рублей"
            page.update()

        def check_compatibility_button_click(e):
            issues = check_full_build_compatibility(details)
            if not issues:
                compatibility_result.value = "Сборка полностью совместима."
                compatibility_result.color = ft.colors.GREEN
            else:
                compatibility_result.value = "Проблемы совместимости:\n" + "\n".join(issues)
                compatibility_result.color = ft.colors.RED
            page.update()

        table = ft.Column([
            create_table_row("Процессор", details.get("Процессор", ("...", 0)), "processor", update_component),
            create_table_row("Охлаждение", details.get("Охлаждение", ("...", 0)), "Охлаждение", update_component),
            create_table_row("Материнская плата", details.get("Материнская плата", ("...", 0)), "Материнская плата", update_component),
            create_table_row("Оперативная память", details.get("Оперативная память", ("...", 0)), "Оперативная память", update_component),
            create_table_row("SSD", details.get("SSD", ("...", 0)), "SSD", update_component),
            create_table_row("Жесткий диск", details.get("Жесткий диск", ("...", 0)), "Жесткий диск", update_component),
            create_table_row("Видеокарта", details.get("Видеокарта", ("...", 0)), "Видеокарта", update_component),
            create_table_row("Блок питания", details.get("Блок питания", ("...", 0)), "Блок питания", update_component),
            create_table_row("Корпус", details.get("Корпус", ("...", 0)), "Корпус", update_component),
        ], spacing=10)

        right_section = ft.Column([
            ft.Container(
                content=total_cost_label,
                padding=20,
                width=300,
                height=150,
                bgcolor="#FFFFFF",
                border_radius=5,
            ),
            ft.ElevatedButton(
                "Проверить совместимость",
                width=300,
                height=50,
                on_click=check_compatibility_button_click,
            ),
            ft.Row([
                ft.ElevatedButton(
                    "Сохранить сборку",
                    width=140,
                    on_click=lambda e: save_build_to_file(build_name, details)
                ),
                ft.ElevatedButton(
                    "Копировать в буфер обмена",
                    width=140,
                    on_click=lambda e: copy_build_to_clipboard(build_name, details)
                ),
            ], spacing=20),
            compatibility_result,
        ], alignment=ft.MainAxisAlignment.CENTER, spacing=20)

        back_button = ft.ElevatedButton("Назад", on_click=lambda _: page.go("/"), width=100, height=40)
        help_button = ft.ElevatedButton("Помощь", width=100, height=40, on_click=open_help_file)

        main_content = ft.Container(
            content=ft.Column([
                ft.Row([
                    ft.Text(f"Детали сборки: {build_name}", size=20, weight=ft.FontWeight.BOLD),
                    ft.Row([back_button, help_button], spacing=10),
                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                ft.Divider(height=1, color="black"),
                ft.Row([
                    table,
                    right_section,
                ], spacing=20, alignment=ft.MainAxisAlignment.CENTER),
            ], spacing=20),
            padding=20,
            border_radius=10,
            bgcolor="#F0F0F0",
        )

        return ft.View(f"/details/{build_name}", controls=[main_content])

    def create_build_page(page: ft.Page):
        current_build = {
            "Процессор": ("", 0),
            "Охлаждение": ("", 0),
            "Материнская плата": ("", 0),
            "Оперативная память": ("", 0),
            "SSD": ("", 0),
            "Жесткий диск": ("", 0),
            "Видеокарта": ("", 0),
            "Блок питания": ("", 0),
            "Корпус": ("", 0),
        }
        total_price = 0
        total_cost_label = ft.Text("Итоговая стоимость ПК\n... рублей", size=16, weight=ft.FontWeight.BOLD)
        compatibility_result = ft.Text("", size=14, color=ft.colors.RED)

        def update_component(component_title, new_value, label, price_label):
            nonlocal total_price
            old_value = current_build.get(component_title)
            if isinstance(old_value, tuple) and len(old_value) == 2:
                total_price -= old_value[1]
            current_build[component_title] = new_value
            label.value = new_value[0]
            price_label.value = f"{new_value[1]} рублей"
            total_price += new_value[1]
            total_cost_label.value = f"Итоговая стоимость ПК\n{total_price} рублей"
            page.update()

        def check_compatibility_button_click(e):
            issues = check_full_build_compatibility(current_build)
            if not issues:
                compatibility_result.value = "Сборка полностью совместима."
                compatibility_result.color = ft.colors.GREEN
            else:
                compatibility_result.value = "Проблемы совместимости:\n" + "\n".join(issues)
                compatibility_result.color = ft.colors.RED
            page.update()

        table = ft.Column([
            create_table_row("Процессор", current_build["Процессор"], "processor", update_component),
            create_table_row("Охлаждение", current_build["Охлаждение"], "cooler", update_component),
            create_table_row("Материнская плата", current_build["Материнская плата"], "motherboard", update_component),
            create_table_row("Оперативная память", current_build["Оперативная память"], "ram", update_component),
            create_table_row("SSD", current_build["SSD"], "storage", update_component),
            create_table_row("Жесткий диск", current_build["Жесткий диск"], "storage", update_component),
            create_table_row("Видеокарта", current_build["Видеокарта"], "graphics_card", update_component),
            create_table_row("Блок питания", current_build["Блок питания"], "power_supply", update_component),
            create_table_row("Корпус", current_build["Корпус"], "case", update_component),
        ], spacing=10)

        right_section = ft.Column([
            ft.Container(
                content=total_cost_label,
                padding=20,
                width=300,
                height=150,
                bgcolor="#FFFFFF",
                border_radius=5,
            ),
            ft.ElevatedButton(
                "Проверить совместимость",
                width=300,
                height=50,
                on_click=check_compatibility_button_click,
            ),
            ft.Row([
                ft.ElevatedButton(
                    "Сохранить сборку",
                    width=140,
                    on_click=lambda e: save_build_to_file("Пользовательская_сборка", current_build)
                ),
                ft.ElevatedButton(
                    "Копировать в буфер обмена",
                    width=140,
                    on_click=lambda e: copy_build_to_clipboard("Пользовательская_сборка", current_build)
                ),
            ], spacing=20),
            compatibility_result,
        ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=20)

        back_button = ft.ElevatedButton("Назад", on_click=lambda _: page.go("/"), width=100, height=40)
        help_button = ft.ElevatedButton("Помощь", width=100, height=40, on_click=open_help_file)

        top_row = ft.Row([
            ft.Text("Создание сборки", size=20, weight=ft.FontWeight.BOLD),
            ft.Row([back_button, help_button], spacing=10),
        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)

        details_content = ft.Container(
            content=ft.Row([table, right_section], spacing=20, alignment=ft.MainAxisAlignment.CENTER),
            padding=20,
            border_radius=10,
            bgcolor="#F0F0F0",
        )

        main_content = ft.Container(
            content=ft.Column([
                top_row,
                ft.Divider(height=1, color="black"),
                details_content,
            ], spacing=20),
            padding=20,
            border_radius=10,
            bgcolor="#F0F0F0",
        )

        return ft.View("/create", controls=[main_content])

    def support_page(page: ft.Page):
        back_button = ft.ElevatedButton("Назад", on_click=lambda _: page.go("/"), width=100, height=40)
        help_button = ft.ElevatedButton("Помощь", width=100, height=40, on_click=open_help_file)

        header = ft.Row([
            ft.Text("Служба поддержки", size=24, weight=ft.FontWeight.BOLD),
            ft.Row([back_button, help_button], spacing=10),
        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)

        content = ft.Column(
            scroll=ft.ScrollMode.AUTO,
            expand=True,
            spacing=20,
            controls=[
                header,
                ft.Text("Часто задаваемые вопросы", size=20, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                ft.Column(
                    controls=[
                        ft.ExpansionTile(
                            title=ft.Text("Как связаться с поддержкой?"),
                            controls=[
                                ft.ListTile(title=ft.Text("Используйте контактные данные, указанные в конце страницы."))
                            ]
                        ),
                        ft.ExpansionTile(
                            title=ft.Text("Какие часы работы у поддержки?"),
                            controls=[
                                ft.ListTile(title=ft.Text("Мы работаем ежедневно с 8:00 до 17:00 по Перми."))
                            ]
                        ),
                    ],
                    spacing=10,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                ),
                ft.Divider(),
                ft.Text("Контактная информация", size=20, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                ft.Column(
                    controls=[
                        ft.ListTile(
                            leading=ft.Icon(ft.icons.EMAIL),
                            title=ft.Text("Email (Вронский Михаил Александрович): mavronskii@edu.hse.ru")
                        ),
                        ft.ListTile(
                            leading=ft.Icon(ft.icons.EMAIL),
                            title=ft.Text("Email (Проскуряков Егор Андреевич): eaproskuriakov@edu.hse.ru")
                        ),
                        ft.ListTile(
                            leading=ft.Icon(ft.icons.EMAIL),
                            title=ft.Text("Email (Туров Всеволод Алексеевич): vsalturov@edu.hse.ru")
                        ),
                    ],
                    spacing=5,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                )
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )

        return ft.View(
            "/support",
            controls=[content],
            scroll=ft.ScrollMode.AUTO
        )

    def route_change(route):
        page.views.clear()
        if page.route == "/":
            page.views.append(ft.View("/", controls=[main_container]))
        elif page.route.startswith("/details/"):
            build_name = page.route.split("/")[-1]
            page.views.append(build_details_page(page, build_name))
        elif page.route == "/create":
            page.views.append(create_build_page(page))
        elif page.route == "/compare":
            page.views.append(compare_components_page(page))
        elif page.route == "/support":
            page.views.append(support_page(page))
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    def save_build_to_file(build_name: str, build_data: dict):
        try:
            root = tk.Tk()
            root.withdraw()
            root.attributes("-topmost", True)
            default_filename = f"{build_name.replace(' ', '_')}.json"
            file_path = filedialog.asksaveasfilename(
                defaultextension=".json",
                filetypes=[("JSON files", "*.json")],
                initialfile=default_filename,
                title="Сохранить сборку как...",
                parent=root
            )
            root.destroy()
            if not file_path:
                return

            result = {}
            for category, component in build_data.items():
                if isinstance(component, tuple):
                    name = component[0]
                elif isinstance(component, str):
                    name = component
                else:
                    continue
                cursor = db.conn.cursor()
                cursor.execute("SELECT id FROM components WHERE name = ?", (name,))
                row = cursor.fetchone()
                result[category] = row[0] if row else None

            with open(file_path, "w", encoding="utf-8") as f:
                json.dump({
                    "build_name": build_name,
                    "components": result
                }, f, indent=4, ensure_ascii=False)
            print(f"Сборка сохранена в файл: {file_path}")
        except Exception as e:
            print(f"Ошибка при сохранении сборки: {e}")

    def load_build_from_file():
        try:
            root = tk.Tk()
            root.withdraw()
            root.attributes("-topmost", True)
            file_path = filedialog.askopenfilename(
                defaultextension=".json",
                filetypes=[("JSON files", "*.json")],
                title="Открыть сборку",
                parent=root
            )
            root.destroy()
            if not file_path:
                return

            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            build_name = data.get("build_name", "Загруженная сборка")
            component_ids = data.get("components", {})
            build_data = {}

            for category, component_id in component_ids.items():
                cursor = db.conn.cursor()
                cursor.execute("SELECT name, price FROM components WHERE id = ?", (component_id,))
                row = cursor.fetchone()
                if row:
                    build_data[category] = (row[0], row[1])
                else:
                    build_data[category] = ("Не найдено", 0)

            page.views.append(build_details_page(page, build_name, loaded_details=build_data))
            page.update()
        except Exception as e:
            print(f"Ошибка при загрузке сборки: {e}")

    def copy_build_to_clipboard(build_name: str, build_data: dict):
        try:
            lines = [f"Название сборки: {build_name}\n"]
            total = 0
            for key, value in build_data.items():
                if isinstance(value, tuple):
                    name, price = value
                elif isinstance(value, str):
                    name = value
                    price = "не указано"
                else:
                    continue
                lines.append(f"{key}: {name} — {price} руб")
                if isinstance(price, int):
                    total += price
            lines.append(f"\nИтоговая стоимость: {total} руб")
            pyperclip.copy("\n".join(lines))
            print("Сборка скопирована в буфер обмена!")
        except Exception as e:
            print(f"Ошибка при копировании в буфер: {e}")

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go("/")

ft.app(target=main)