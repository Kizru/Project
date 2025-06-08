import flet as ft
import os
import subprocess
import sys
import datetime
import tkinter as tk
from tkinter import filedialog
from DataBase import ComponentDB, component_options
import json
import pyperclip

db = ComponentDB()


def open_help_file(e):
    help_file = "usermanual.chm"
    try:
        if os.path.exists(help_file):
            subprocess.Popen(["hh.exe", help_file], shell=True)
        else:
            print(f"Файл справки {help_file} не найден!")
    except Exception as ex:
        print(f"Ошибка при открытии файла справки: {ex}")

# Генерация списка сборок
gaming_builds = [f"Игровая сборка {i}" for i in range(1, 11)]
office_builds = [f"Офисная сборка {i}" for i in range(1, 11)]

all_builds = gaming_builds + office_builds  # Все 20 сборок

build_details = {
    "Игровая сборка 1": {
        "Процессор": ("Intel Core i5-13600K", 25000),
        "Охлаждение": ("Cooler Master Hyper 212 RGB", 1200),
        "Материнская плата": ("ASUS ROG Strix B660-A WIFI", 15000),
        "Оперативная память": ("Corsair Vengeance LPX 32GB (2x16GB) DDR4 3600MHz", 6000),
        "SSD": ("Samsung 980 Pro 1TB NVMe M.2", 10000),
        "Жесткий диск": ("Western Digital Blue 6TB SATA III", 4500),
        "Видеокарта": ("NVIDIA GeForce RTX 4070 Ti", 45000),
        "Блок питания": ("Corsair RMx 850W Gold", 4000),
        "Корпус": ("Fractal Design Define Mini XL", 3000),
    },
    "Игровая сборка 2": {
        "Процессор": ("AMD Ryzen 7 7800X", 28000),
        "Охлаждение": ("Noctua NH-U12A", 2500),
        "Материнская плата": ("MSI MAG B660M Mortar WiFi", 12000),
        "Оперативная память": ("G.Skill Trident Z Neo 32GB (2x16GB) DDR5 6000MHz", 8000),
        "SSD": ("WD Black SN850X 2TB NVMe M.2", 15000),
        "Жесткий диск": ("Hitachi GST Ultrastar 6TB SATA III", 6000),
        "Видеокарта": ("AMD Radeon RX 7900 XT", 50000),
        "Блок питания": ("EVGA SuperNOVA 850 G3 850W", 5000),
        "Корпус": ("NZXT Kraken X73", 3000),
    },
    "Игровая сборка 3": {
        "Процессор": ("Intel Core i9-13900KF", 35000),
        "Охлаждение": ("Corsair Hydro X Series H115i RGB Platinum", 4000),
        "Материнская плата": ("Gigabyte Z790 AORUS Elite AX", 20000),
        "Оперативная память": ("Kingston FURY Beast 32GB (2x16GB) DDR4 3200MHz", 5000),
        "SSD": ("Kingston KC2500 2TB NVMe M.2", 12000),
        "Жесткий диск": ("Seagate BarraCuda 4TB SATA III", 3500),
        "Видеокарта": ("NVIDIA GeForce RTX 4080", 60000),
        "Блок питания": ("Seasonic PRIME TX 850W Gold", 4500),
        "Корпус": ("BitFenix Aegis Mini", 2800),
    },
    "Игровая сборка 4": {
        "Процессор": ("AMD Ryzen 9 7900X", 40000),
        "Охлаждение": ("NZXT Kraken X73", 3000),
        "Материнская плата": ("ASRock X670E Taichi", 25000),
        "Оперативная память": ("Crucial Ballistix 32GB (2x16GB) DDR5 6400MHz", 7000),
        "SSD": ("Sabrent Rocket 4 Plus 2TB NVMe M.2", 13000),
        "Жесткий диск": ("Toshiba P300 4TB SATA III", 4000),
        "Видеокарта": ("AMD Radeon RX 7800 XT", 55000),
        "Блок питания": ("Thermaltake Toughpower GF1 850W Gold", 5500),
        "Корпус": ("Phanteks Enthoo Pro Mini", 3500),
    },
    "Игровая сборка 5": {
        "Процессор": ("Intel Core i7-13700", 22000),
        "Охлаждение": ("Cooler Master Hyper 212 EVO", 1000),
        "Материнская плата": ("ASUS TUF B660M-PLUS WIFI", 10000),
        "Оперативная память": ("Corsair Value Select 16GB (2x8GB) DDR4 3200MHz", 3000),
        "SSD": ("Samsung 870 QVO 500GB SATA III", 3000),
        "Жесткий диск": ("Hitachi GST Ultrastar 4TB SATA III", 5500),
        "Видеокарта": ("NVIDIA GeForce GT 730 2GB", 1500),
        "Блок питания": ("Corsair RMx 550W Gold", 3000),
        "Корпус": ("Fractal Design Node 304", 2000),
    },
    "Игровая сборка 6": {
        "Процессор": ("AMD Ryzen 5 7600", 15000),
        "Охлаждение": ("Noctua NH-L9A", 1500),
        "Материнская плата": ("MSI B660M PRO WIFI", 8000),
        "Оперативная память": ("G.Skill Ripjaws S 16GB (2x8GB) DDR5 5600MHz", 4000),
        "SSD": ("WD Blue SN550 500GB NVMe M.2", 4000),
        "Жесткий диск": ("Western Digital Blue 4TB SATA III", 4500),
        "Видеокарта": ("AMD Radeon R5 230 2GB", 1000),
        "Блок питания": ("EVGA SuperNOVA 550 G3 550W", 3500),
        "Корпус": ("NZXT H440", 2200),
    },
    "Игровая сборка 7": {
        "Процессор": ("Intel Core i5-13400", 18000),
        "Охлаждение": ("DeepCool Gammaxx 400", 2000),
        "Материнская плата": ("Gigabyte B660M DS3H", 9000),
        "Оперативная память": ("Kingston ValueRAM 16GB (2x8GB) DDR4 2666MHz", 2000),
        "SSD": ("Kingston A400 480GB SATA III", 2000),
        "Жесткий диск": ("Seagate Barracuda 2TB SATA III", 2500),
        "Видеокарта": ("AMD Radeon RX 640 2GB", 3000),
        "Блок питания": ("Seasonic Prime TX 550W Gold", 3200),
        "Корпус": ("BitFenix Aurora", 2500),
    },
    "Игровая сборка 8": {
        "Процессор": ("AMD Ryzen 7 7700", 20000),
        "Охлаждение": ("Arctic Freezer 34 eSports", 2200),
        "Материнская плата": ("ASRock B660M Pro RS", 7000),
        "Оперативная память": ("Crucial Ballistix 16GB (2x8GB) DDR5 5200MHz", 3500),
        "SSD": ("Sabrent Rocket 4 500GB NVMe M.2", 3500),
        "Жесткий диск": ("Toshiba P300 2TB SATA III", 3000),
        "Видеокарта": ("NVIDIA GeForce MX550 2GB", 2500),
        "Блок питания": ("Thermaltake Toughpower GF1 550W Gold", 3800),
        "Корпус": ("Phanteks Eclipse P300", 2800),
    },
    "Игровая сборка 9": {
        "Процессор": ("Intel Core i7-13700", 22000),
        "Охлаждение": ("Noctua NH-U12A", 2500),
        "Материнская плата": ("ASUS ROG Strix B660-A WIFI", 15000),
        "Оперативная память": ("G.Skill Trident Z Neo 32GB (2x16GB) DDR5 6000MHz", 8000),
        "SSD": ("WD Black SN850X 2TB NVMe M.2", 15000),
        "Жесткий диск": ("Hitachi GST Ultrastar 6TB SATA III", 6000),
        "Видеокарта": ("NVIDIA GeForce RTX 4070 Ti", 45000),
        "Блок питания": ("Corsair RMx 850W Gold", 4000),
        "Корпус": ("NZXT H510 Elite", 2500),
    },
    "Игровая сборка 10": {
        "Процессор": ("AMD Ryzen 9 7900X", 40000),
        "Охлаждение": ("NZXT Kraken X73", 3000),
        "Материнская плата": ("ASRock X670E Taichi", 25000),
        "Оперативная память": ("Crucial Ballistix 32GB (2x16GB) DDR5 6400MHz", 7000),
        "SSD": ("Samsung 980 Pro 1TB NVMe M.2", 10000),
        "Жесткий диск": ("Seagate BarraCuda 4TB SATA III", 3500),
        "Видеокарта": ("AMD Radeon RX 7800 XT", 55000),
        "Блок питания": ("Seasonic PRIME TX 850W Gold", 4500),
        "Корпус": ("Phanteks Eclipse P300", 2800),
    },
    # Офисные сборки
    "Офисная сборка 1": {
        "Процессор": ("Intel Core i5-13400", 18000),
        "Охлаждение": ("Cooler Master Hyper 212 EVO", 1000),
        "Материнская плата": ("ASUS TUF B660M-PLUS WIFI", 10000),
        "Оперативная память": ("Kingston ValueRAM 16GB (2x8GB) DDR4 2666MHz", 2000),
        "SSD": ("Kingston A400 480GB SATA III", 2000),
        "Жесткий диск": ("Seagate Barracuda 2TB SATA III", 2500),
        "Видеокарта": ("Intel UHD Graphics 730", 0),
        "Блок питания": ("EVGA SuperNOVA 550 G3 550W", 3500),
        "Корпус": ("NZXT H440", 2200),
    },
    "Офисная сборка 2": {
        "Процессор": ("AMD Ryzen 5 7600", 15000),
        "Охлаждение": ("Noctua NH-L9A", 1500),
        "Материнская плата": ("MSI B660M PRO WIFI", 8000),
        "Оперативная память": ("Corsair Value Select 16GB (2x8GB) DDR4 3200MHz", 3000),
        "SSD": ("Samsung 870 QVO 500GB SATA III", 3000),
        "Жесткий диск": ("Western Digital Blue 4TB SATA III", 4500),
        "Видеокарта": ("Integrated Graphics", 0),
        "Блок питания": ("Seasonic Prime TX 550W Gold", 3200),
        "Корпус": ("Fractal Design Node 304", 2000),
    },
    "Офисная сборка 3": {
        "Процессор": ("Intel Core i5-13600K", 25000),
        "Охлаждение": ("Cooler Master Hyper 212 RGB", 1200),
        "Материнская плата": ("Gigabyte B660M DS3H", 9000),
        "Оперативная память": ("G.Skill Ripjaws S 16GB (2x8GB) DDR5 5600MHz", 4000),
        "SSD": ("Sabrent Rocket 4 500GB NVMe M.2", 3500),
        "Жесткий диск": ("Toshiba P300 2TB SATA III", 3000),
        "Видеокарта": ("Integrated Graphics", 12000),
        "Блок питания": ("Thermaltake Toughpower GF1 550W Gold", 3800),
        "Корпус": ("BitFenix Aegis Mini", 2800),
    },
    "Офисная сборка 4": {
        "Процессор": ("AMD Ryzen 5 7600", 15000),
        "Охлаждение": ("Noctua NH-U12A", 2500),
        "Материнская плата": ("ASRock B660M Pro RS", 7000),
        "Оперативная память": ("Kingston ValueRAM 16GB (2x8GB) DDR4 2666MHz", 2000),
        "SSD": ("Kingston A400 480GB SATA III", 2000),
        "Жесткий диск": ("Western Digital Blue 4TB SATA III", 4500),
        "Видеокарта": ("Intel HD Graphics 630", 0),
        "Блок питания": ("Corsair RMx 550W Gold", 3000),
        "Корпус": ("NZXT H440", 2200),
    },
    "Офисная сборка 5": {
        "Процессор": ("Intel Core i5-13400", 18000),
        "Охлаждение": ("Cooler Master Hyper 212 EVO", 1000),
        "Материнская плата": ("ASUS TUF B660M-PLUS WIFI", 10000),
        "Оперативная память": ("Corsair Value Select 16GB (2x8GB) DDR4 3200MHz", 3000),
        "SSD": ("WD Blue SN550 500GB NVMe M.2", 3000),
        "Жесткий диск": ("Seagate Barracuda 2TB SATA III", 2500),
        "Видеокарта": ("Integrated Graphics", 0),
        "Блок питания": ("EVGA SuperNOVA 550 G3 550W", 3500),
        "Корпус": ("Fractal Design Node 304", 2000),
    },
    "Офисная сборка 6": {
        "Процессор": ("AMD Ryzen 5 7600", 15000),
        "Охлаждение": ("Noctua NH-L9A", 1500),
        "Материнская плата": ("MSI B660M PRO WIFI", 8000),
        "Оперативная память": ("G.Skill Ripjaws S 16GB (2x8GB) DDR5 5600MHz", 4000),
        "SSD": ("Samsung 870 QVO 500GB SATA III", 3000),
        "Жесткий диск": ("Toshiba P300 2TB SATA III", 3000),
        "Видеокарта": ("Intel UHD Graphics 730", 0),
        "Блок питания": ("Seasonic Prime TX 550W Gold", 3200),
        "Корпус": ("BitFenix Aurora", 2500),
    },
    "Офисная сборка 7": {
        "Процессор": ("Intel Core i5-13400", 18000),
        "Охлаждение": ("Cooler Master Hyper 212 EVO", 1000),
        "Материнская плата": ("Gigabyte B660M DS3H", 9000),
        "Оперативная память": ("Kingston ValueRAM 16GB (2x8GB) DDR4 2666MHz", 2000),
        "SSD": ("Sabrent Rocket 4 500GB NVMe M.2", 3500),
        "Жесткий диск": ("Seagate Barracuda 2TB SATA III", 2500),
        "Видеокарта": ("Integrated Graphics", 0),
        "Блок питания": ("Thermaltake Toughpower GF1 550W Gold", 3800),
        "Корпус": ("Phanteks Eclipse P300", 2800),
    },
    "Офисная сборка 8": {
        "Процессор": ("AMD Ryzen 5 7600", 15000),
        "Охлаждение": ("Noctua NH-L9A", 1500),
        "Материнская плата": ("ASRock B660M Pro RS", 7000),
        "Оперативная память": ("Corsair Value Select 16GB (2x8GB) DDR4 3200MHz", 3000),
        "SSD": ("Samsung 870 QVO 500GB SATA III", 3000),
        "Жесткий диск": ("Western Digital Blue 4TB SATA III", 4500),
        "Видеокарта": ("Integrated Graphics", 0),
        "Блок питания": ("Seasonic Prime TX 550W Gold", 3200),
        "Корпус": ("NZXT H440", 2200),
    },
    "Офисная сборка 9": {
        "Процессор": ("Intel Core i5-13600K", 25000),
        "Охлаждение": ("Cooler Master Hyper 212 EVO", 1000),
        "Материнская плата": ("ASUS TUF B660M-PLUS WIFI", 10000),
        "Оперативная память": ("Kingston ValueRAM 16GB (2x8GB) DDR4 2666MHz", 2000),
        "SSD": ("Kingston A400 480GB SATA III", 2000),
        "Жесткий диск": ("Toshiba P300 2TB SATA III", 3000),
        "Видеокарта": ("Intel UHD Graphics 730", 0),
        "Блок питания": ("EVGA SuperNOVA 550 G3 550W", 3500),
        "Корпус": ("Fractal Design Node 304", 2000),
    },
    "Офисная сборка 10": {
        "Процессор": ("AMD Ryzen 5 7600", 15000),
        "Охлаждение": ("Noctua NH-L9A", 1500),
        "Материнская плата": ("MSI B660M PRO WIFI", 8000),
        "Оперативная память": ("G.Skill Ripjaws S 16GB (2x8GB) DDR5 5600MHz", 4000),
        "SSD": ("Sabrent Rocket 4 500GB NVMe M.2", 3500),
        "Жесткий диск": ("Seagate Barracuda 2TB SATA III", 2500),
        "Видеокарта": ("Integrated Graphics", 0),
        "Блок питания": ("Thermaltake Toughpower GF1 550W Gold", 3800),
        "Корпус": ("BitFenix Aegis Mini", 2800),
    },
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
            )], alignment = ft.MainAxisAlignment.SPACE_BETWEEN),
            ft.Divider(height=1, color="black"),
            ft.Row([
                ft.Text("Популярные сборки", size=16),
                ft.Row([
                    ft.ElevatedButton("Помощь", on_click=open_help_file),
                    ft.ElevatedButton("Создать сборку", on_click=lambda _: page.go("/create")),
                    ft.ElevatedButton("Сравнение комплектующих", on_click=lambda _: page.go("/compare")),
                    ft.ElevatedButton("Загрузить сборку", on_click=lambda _: load_build_from_file()),
                ], spacing=10),
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            filter_controls,
            builds_container,
            ft.Container(
                content=ft.Column([
                    ft.Row([
                        ft.Text("Хочу быть в курсе акций и новинок!", size=14),
                        ft.TextField(label="Введите адрес электронной почты", expand=True),
                        ft.ElevatedButton("Подписаться"),
                    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN, spacing=10),
                ], spacing=5),
                padding=10,
                border=ft.border.all(1, "lightgray"),
                border_radius=10,
            ),
            ft.Row([
                ft.ElevatedButton("Отзывы о сервисе"),
                ft.ElevatedButton("Служба поддержки", on_click=lambda _: page.go("/support")),
            ], alignment=ft.MainAxisAlignment.END, spacing=10),
        ], spacing=20),
        padding=20,
        border_radius=10,
        bgcolor="#F0F0F0",
    )

    # Обновляемая строка таблицы с кнопкой выбора
    def create_table_row(title, description, component_type, update_callback):
        if isinstance(description, tuple):
            label_text = description[0]
            price_text = f"{description[1]} рублей"
        else:
            label_text = description or "..."
            price_text = "... рублей"

        label = ft.Text(label_text, size=12)
        price_label = ft.Text(price_text, size=12)

        menu_items = [
            ft.PopupMenuItem(
                text=f"{name} ({price} руб)",
                on_click=lambda e, item=(name, price): update_callback(title, item, label, price_label)
            )
            for name, price in db.get_by_category(component_type)
        ]

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

        # Вычисляем общую стоимость изначально по данным сборки
        total_price = sum(item[1] for item in details.values() if isinstance(item, tuple) and len(item) == 2)
        
        # Текстовое поле для общей стоимости
        total_cost_label = ft.Text(f"Итоговая стоимость ПК\n{total_price} рублей", size=16, weight=ft.FontWeight.BOLD)

        def update_component(component_title, new_value, label, price_label):
            nonlocal total_price
            
            old_value = details.get(component_title)
            if isinstance(old_value, tuple) and len(old_value) == 2:
                total_price -= old_value[1]

            # Обновляем текущее значение
            details[component_title] = new_value
            label.value = new_value[0]
            price_label.value = f"{new_value[1]} рублей"
            total_price += new_value[1]
            total_cost_label.value = f"Итоговая стоимость ПК\n{total_price} рублей"
            page.update()

        table = ft.Column([
            create_table_row("Процессор", details.get("Процессор", ("...", 0)), "Процессор", update_component),
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
            "Процессор": "",
            "Охлаждение": "",
            "Материнская плата": "",
            "Оперативная память": "",
            "SSD": "",
            "Жесткий диск": "",
            "Видеокарта": "",
            "Блок питания": "",
            "Корпус": "",
        }

        total_price = 0
        # Объявление total_cost_label
        total_cost_label = ft.Text("Итоговая стоимость ПК\n... рублей", size=16, weight=ft.FontWeight.BOLD)

        def update_component(component_title, new_value, label, price_label):
            nonlocal total_price

            # Удаляем старое значение из общей суммы, если оно было
            if current_build.get(component_title):
                old_value = current_build[component_title]
                for item in component_options.get(component_title, []):
                    if item[0] == old_value:
                        total_price -= item[1]

            current_build[component_title] = new_value[0]
            label.value = new_value[0]
            price_label.value = f"{new_value[1]} рублей"
            total_price += new_value[1]
            total_cost_label.value = f"Итоговая стоимость ПК\n{total_price} рублей"
            page.update()

        table = ft.Column([
            create_table_row("Процессор", current_build["Процессор"], "Процессор", update_component),
            create_table_row("Охлаждение", current_build["Охлаждение"], "Охлаждение", update_component),
            create_table_row("Материнская плата", current_build["Материнская плата"], "Материнская плата", update_component),
            create_table_row("Оперативная память", current_build["Оперативная память"], "Оперативная память", update_component),
            create_table_row("SSD", current_build["SSD"], "SSD", update_component),
            create_table_row("Жесткий диск", current_build["Жесткий диск"], "Жесткий диск", update_component),
            create_table_row("Видеокарта", current_build["Видеокарта"], "Видеокарта", update_component),
            create_table_row("Блок питания", current_build["Блок питания"], "Блок питания", update_component),
            create_table_row("Корпус", current_build["Корпус"], "Корпус", update_component),
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
                "Сохранить сборку",
                width=300,
                height=50,
                on_click=lambda e: save_build_to_file("Пользовательская_сборка", current_build)
            ),
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

    def compare_components_page(page: ft.Page):
        compare_component_options = {
            "Процессор": ["AMD Ryzen 7 7800X3D", "Intel Core i9-13900K"],
            "Охлаждение": ["Noctua NH-D15", "NZXT Kraken X73"],
            "SSD": ["Samsung 990 Pro", "Samsung 980 Pro"]
        }

        # Создаем элементы управления до их использования
        component1_dropdown = ft.Dropdown(width=200)
        component2_dropdown = ft.Dropdown(width=200)
        
        def update_component_fields(e):
            selected_type = component_type_dropdown.value
            if selected_type:
                components_row.controls[0].controls[0].value = f"{selected_type} 1"
                components_row.controls[1].controls[0].value = f"{selected_type} 2"
                
                options = compare_component_options.get(selected_type, [])
                component1_dropdown.options = [ft.dropdown.Option(opt) for opt in options]
                component2_dropdown.options = [ft.dropdown.Option(opt) for opt in options]
                
                if options:
                    component1_dropdown.value = options[0]
                    component2_dropdown.value = options[1] if len(options) > 1 else options[0]
                
                page.update()
        
        header = ft.Row(
            controls=[
                ft.Text("Сравнение комплектующих", size=24, weight=ft.FontWeight.BOLD),
                ft.IconButton(
                    icon=ft.icons.ARROW_BACK,
                    on_click=lambda _: page.go("/"),
                    tooltip="Вернуться на главную"
                )
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            width=page.width
        )
        
        # Создаем выпадающий список для выбора типа компонента
        component_type_dropdown = ft.Dropdown(
            label="Выберите комплектующие для сравнения",
            options=[
                ft.dropdown.Option("Процессор"),
                ft.dropdown.Option("Охлаждение"),
                ft.dropdown.Option("SSD"),
            ],
            width=400,
            on_change=update_component_fields
        )
        
        # Центрируем выпадающий список
        dropdown_container = ft.Container(
            content=ft.Column(
                [
                    component_type_dropdown  # Используем уже созданный элемент
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            padding=ft.padding.only(bottom=20)
        )
        
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
        
        # Центрируем кнопку сравнения
        compare_button_container = ft.Container(
            content=ft.ElevatedButton(
                text="Сравнить",
                width=200,
                height=50
            ),
            alignment=ft.alignment.center,
            padding=ft.padding.only(top=20)
        )
        
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
        
        return ft.View("/compare", controls=[content], scroll=ft.ScrollMode.AUTO)

    def support_page(page: ft.Page):
        message_display = ft.Text("", color=ft.colors.RED, size=14)
        
        # Сначала создаем все элементы формы
        name_field = ft.TextField(label="Ваше имя", width=400)
        email_field = ft.TextField(label="Ваш email для связи", width=400)
        issue_field = ft.TextField(label="Тема проблемы", width=400)
        message_field = ft.TextField(
            label="Опишите Вашу проблему", 
            multiline=True, 
            min_lines=3,
            max_lines=5,
            width=400
        )
        
        def submit_form(e):
            if not name_field.value:
                message_display.value = "Вы заполнили не все поля!"
                message_display.color = ft.colors.RED
                page.update()
                return
            if not email_field.value:
                message_display.value = "Вы заполнили не все поля!"
                message_display.color = ft.colors.RED
                page.update()
                return
            if not issue_field.value:
                message_display.value = "Вы заполнили не все поля!"
                message_display.color = ft.colors.RED
                page.update()
                return
            if not message_field.value:
                message_display.value = "Вы заполнили не все поля!"
                message_display.color = ft.colors.RED
                page.update()
                return
                
            # Здесь должна быть реальная отправка формы
            print(f"Отправлено: {name_field.value}, {email_field.value}")
            
            message_display.value = "Заявка успешно отправлена! Ожидайте ответ от техподдержки"
            message_display.color = ft.colors.GREEN
            
            name_field.value = ""
            email_field.value = ""
            issue_field.value = ""
            message_field.value = ""
            page.update()
        
        # Создаем заголовок
        header = ft.Row(
            controls=[
                ft.Text("Служба поддержки", size=24, weight=ft.FontWeight.BOLD),
                ft.IconButton(
                    icon=ft.icons.ARROW_BACK,
                    tooltip="Вернуться на главную",
                    on_click=lambda _: page.go("/")
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            width=page.width
        )
        
        # Создаем основную структуру страницы
        content = ft.Column(
            scroll=ft.ScrollMode.AUTO,
            expand=True,
            spacing=20,
            controls=[
                header,  # Добавляем заголовок
                ft.Text("Часто задаваемые вопросы", 
                       size=20, 
                       weight=ft.FontWeight.BOLD,
                       text_align=ft.TextAlign.CENTER),
                
                ft.Column(
                    controls=[
                        ft.ExpansionTile(
                            title=ft.Text("Как связаться с поддержкой?"),
                            controls=[
                                ft.ListTile(title=ft.Text("Используйте форму ниже или контактные данные в конце страницы."))
                            ]
                        ),
                        ft.ExpansionTile(
                            title=ft.Text("Какие часы работы у поддержки?"),
                            controls=[
                                ft.ListTile(title=ft.Text("Мы работаем 24/7."))
                            ]
                        ),
                    ],
                    spacing=10,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                ),
                
                ft.Divider(),
                
                ft.Text("Форма обращения в поддержку", 
                       size=20, 
                       weight=ft.FontWeight.BOLD,
                       text_align=ft.TextAlign.CENTER),
                
                ft.Column(
                    controls=[
                        name_field,
                        email_field,
                        issue_field,
                        message_field,
                        message_display,
                        ft.ElevatedButton(
                            "Отправить", 
                            on_click=submit_form,
                            width=400
                        )
                    ],
                    spacing=10,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                ),
                
                ft.Divider(),
                
                ft.Text("Контактная информация", 
                       size=20, 
                       weight=ft.FontWeight.BOLD,
                       text_align=ft.TextAlign.CENTER),
                
                ft.Column(
                    controls=[
                        ft.ListTile(
                            leading=ft.Icon(ft.icons.PHONE),
                            title=ft.Text("Телефон: +7 (123) 456-78-90")
                        ),
                        ft.ListTile(
                            leading=ft.Icon(ft.icons.EMAIL),
                            title=ft.Text("Email: support@example.com")
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

            db = ComponentDB()

            # получение ID
            result = {}
            for category, component in build_data.items():
                if isinstance(component, tuple):
                    name = component[0]
                elif isinstance(component, str):
                    name = component
                else:
                    continue

                # нахождение ID
                cursor = db.conn.cursor()
                cursor.execute("SELECT id FROM components WHERE name = ?", (name,))
                row = cursor.fetchone()
                result[category] = row[0] if row else None

            db.close()

            # сохранение
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

            db = ComponentDB()

            build_data = {}
            for category, component_id in component_ids.items():
                cursor = db.conn.cursor()
                cursor.execute("SELECT name, price FROM components WHERE id = ?", (component_id,))
                row = cursor.fetchone()
                if row:
                    build_data[category] = (row[0], row[1])
                else:
                    build_data[category] = ("Не найдено", 0)

            db.close()

            # переход на страницу со сборкой
            page.views.append(build_details_page(page, build_name, loaded_details=build_data))
            page.update()

        except Exception as e:
            print(f"Ошибка при загрузке сборки: {e}")

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go("/")

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


ft.app(target=main)