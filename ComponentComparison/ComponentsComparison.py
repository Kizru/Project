import flet as ft
from ComponentComparison.DisplayDetails import *
from DataBaseClass import ComponentDB
from HelpFile import open_help_file

db = ComponentDB()
CATEGORY_MAPPING = {
    "Процессор": "processor",
    "Охлаждение": "cooler",
    "Материнская плата": "motherboard",
    "Оперативная память": "ram",
    "SSD": "storage",
    "Жесткий диск": "storage",
    "Видеокарта": "graphics_card",
    "Блок питания": "power_supply",
    "Корпус": "case",
}

def compare_components_page(page: ft.Page):
    # Выпадающие списки для выбора компонентов
    component1_dropdown = ft.Dropdown(width=200)
    component2_dropdown = ft.Dropdown(width=200)

    def update_component_fields(e):
        # Получаем выбранный тип компонента на русском языке
        component_type_ru = e.control.value
        component_type_en = CATEGORY_MAPPING.get(component_type_ru)

        if not component_type_en:
            print(f"Ошибка: Категория '{component_type_ru}' не найдена в словаре.")
            return

        # Получаем полные данные о компонентах для выбранной категории
        components = db.get_full_by_category(component_type_en)
        if not components:
            print("Ошибка: Нет доступных компонентов для выбранной категории.")
            return

        # Обновляем выпадающие списки для выбора компонентов
        component1_dropdown.options = [
            ft.dropdown.Option(text=f"{name} ({price} руб)", data=(id, name, price))
            for id, name, price, *_ in components
        ]
        component2_dropdown.options = component1_dropdown.options.copy()

        # Устанавливаем значения по умолчанию
        if components:
            component1_dropdown.value = components[0][1]
            component2_dropdown.value = components[1][1] if len(components) > 1 else components[0][1]

        page.update()

    # Метод для сравнения компонентов
    def compare_components(e):
        component1_data = component1_dropdown.value
        component2_data = component2_dropdown.value

        if not component1_data or not component2_data:
            print("Ошибка: Выберите оба компонента для сравнения.")
            return

        component1_data = " ".join(component1_data.split(" ")[:-2])
        component2_data = " ".join(component2_data.split(" ")[:-2])

        component1_id = db.get_id_by_name(component1_data)
        component2_id = db.get_id_by_name(component2_data)

        component1_details = db.get_component_details(component1_id)
        component2_details = db.get_component_details(component2_id)

        category = db.get_category_by_id(component1_id)

        if category == "processor":
            display_comparison_processor(component1_details, component2_details, page)
        elif category == "graphics_card":
            display_comparison_graphics_card(component1_details, component2_details, page)
        elif category == "cooler":
            display_comparison_cooler(component1_details, component2_details, page)
        elif category == "motherboard":
            display_comparison_motherboard(component1_details, component2_details, page)
        elif category == "ram":
            display_comparison_ram(component1_details, component2_details, page)
        elif category == "storage":
            display_comparison_storage(component1_details, component2_details, page)
        elif category == "power_supply":
            display_comparison_power_supply(component1_details, component2_details, page)
        elif category == "case":
            display_comparison_case(component1_details, component2_details, page)

    # Кнопки "Назад" и "Помощь"
    back_button = ft.ElevatedButton("Назад", on_click=lambda _: page.go("/"), width=100, height=40)
    help_button = ft.ElevatedButton("Помощь", width=100, height=40, on_click=open_help_file)

    # Заголовок страницы
    header = ft.Row([
        ft.Text("Сравнение комплектующих", size=24, weight=ft.FontWeight.BOLD),
        ft.Row([back_button, help_button], spacing=10),
    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)

    # Выпадающий список для выбора типа компонента
    component_type_dropdown = ft.Dropdown(
        label="Выберите комплектующие для сравнения",
        options=[
            ft.dropdown.Option("Процессор"),
            ft.dropdown.Option("Охлаждение"),
            ft.dropdown.Option("Материнская плата"),
            ft.dropdown.Option("Оперативная память"),
            ft.dropdown.Option("SSD"),
            ft.dropdown.Option("Жесткий диск"),
            ft.dropdown.Option("Видеокарта"),
            ft.dropdown.Option("Блок питания"),
            ft.dropdown.Option("Корпус"),
        ],
        width=400,
        on_change=update_component_fields
    )

    # Центрируем выпадающий список
    dropdown_container = ft.Container(
        content=ft.Column([component_type_dropdown]),
        padding=ft.padding.only(bottom=20)
    )

    # Строка с выпадающими списками для выбора компонентов
    components_row = ft.Row(
        controls=[
            ft.Column(
                controls=[
                    ft.Text("Комплектующее 1", weight=ft.FontWeight.BOLD),
                    component1_dropdown
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=10
            ),
            ft.Column(
                controls=[
                    ft.Text("Комплектующее 2", weight=ft.FontWeight.BOLD),
                    component2_dropdown
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=10
            )
        ],
        spacing=50,
        alignment=ft.MainAxisAlignment.CENTER
    )

    # Кнопка "Сравнить"
    compare_button_container = ft.Container(
        content=ft.ElevatedButton(
            text="Сравнить",
            width=200,
            height=50,
            on_click=compare_components
        ),
        alignment=ft.alignment.center,
        padding=ft.padding.only(top=20)
    )

    # Основной контент страницы
    content = ft.Column(
        controls=[
            header,
            dropdown_container,
            components_row,
            compare_button_container
        ],
        scroll=ft.ScrollMode.AUTO,
        expand=True,
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=20
    )

    # Возвращаем страницу
    return ft.View("/compare", controls=[content], scroll=ft.ScrollMode.AUTO)