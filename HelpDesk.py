import flet as ft
import os
import subprocess
import sys

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

# Словарь с деталями сборок
build_details = {
    "Игровая сборка 1": {
        "Процессор": "Intel Core i5-13600K",
        "Охлаждение": "Cooler Master Hyper 212 RGB",
        "Материнская плата": "ASUS ROG Strix B660-A WIFI",
        "Оперативная память": "Corsair Vengeance LPX 32GB (2x16GB) DDR4 3600MHz",
        "SSD": "Samsung 980 Pro 1TB NVMe M.2",
        "Жесткий диск": "Seagate BarraCuda 4TB SATA III",
        "Видеокарта": "NVIDIA GeForce RTX 4070 Ti",
        "Блок питания": "Corsair RMx 850W Gold",
        "Корпус": "Fractal Design Define Mini XL",
    },
    "Игровая сборка 2": {
        "Процессор": "AMD Ryzen 7 7800X",
        "Охлаждение": "Noctua NH-U12A",
        "Материнская плата": "MSI MAG B660M Mortar WiFi",
        "Оперативная память": "G.Skill Trident Z Neo 32GB (2x16GB) DDR5 6000MHz",
        "SSD": "WD Black SN850X 2TB NVMe M.2",
        "Жесткий диск": "Western Digital Blue 6TB SATA III",
        "Видеокарта": "AMD Radeon RX 7900 XT",
        "Блок питания": "EVGA SuperNOVA 850 G3 850W",
        "Корпус": "NZXT H510 Elite",
    },
    "Игровая сборка 3": {
        "Процессор": "Intel Core i9-13900KF",
        "Охлаждение": "DeepCool Gammaxx 400",
        "Материнская плата": "ASRock X670E Taichi",
        "Оперативная память": "Kingston FURY Beast 32GB (2x16GB) DDR4 3200MHz",
        "SSD": "Kingston KC2500 2TB NVMe M.2",
        "Жесткий диск": "Toshiba P300 4TB SATA III",
        "Видеокарта": "NVIDIA GeForce RTX 4080",
        "Блок питания": "Seasonic PRIME TX 850W Gold",
        "Корпус": "BitFenix Aegis Mini",
    },
    "Игровая сборка 4": {
        "Процессор": "AMD Ryzen 9 7900X",
        "Охлаждение": "Arctic Freezer 34 eSports",
        "Материнская плата": "Gigabyte Z790 AORUS Elite AX",
        "Оперативная память": "Crucial Ballistix 32GB (2x16GB) DDR5 6400MHz",
        "SSD": "Sabrent Rocket 4 Plus 2TB NVMe M.2",
        "Жесткий диск": "Hitachi GST Ultrastar 6TB SATA III",
        "Видеокарта": "AMD Radeon RX 7800 XT",
        "Блок питания": "Thermaltake Toughpower GF1 850W Gold",
        "Корпус": "Phanteks Enthoo Pro Mini",
    },
    "Игровая сборка 5": {
        "Процессор": "Intel Core i7-13700",
        "Охлаждение": "Cooler Master Hyper 212 EVO",
        "Материнская плата": "ASUS TUF B660M-PLUS WIFI",
        "Оперативная память": "Corsair Value Select 16GB (2x8GB) DDR4 3200MHz",
        "SSD": "Samsung 870 QVO 500GB SATA III",
        "Жесткий диск": "Seagate Barracuda 2TB SATA III",
        "Видеокарта": "NVIDIA GeForce GT 730 2GB",
        "Блок питания": "Corsair RMx 550W Gold",
        "Корпус": "Fractal Design Node 304",
    },
    "Игровая сборка 6": {
        "Процессор": "AMD Ryzen 5 7600",
        "Охлаждение": "Noctua NH-L9A",
        "Материнская плата": "MSI B660M PRO WIFI",
        "Оперативная память": "G.Skill Ripjaws S 16GB (2x8GB) DDR5 5600MHz",
        "SSD": "WD Blue SN550 500GB NVMe M.2",
        "Жесткий диск": "Western Digital Blue 4TB SATA III",
        "Видеокарта": "AMD Radeon R5 230 2GB",
        "Блок питания": "EVGA SuperNOVA 550 G3 550W",
        "Корпус": "NZXT H440",
    },
    "Игровая сборка 7": {
        "Процессор": "Intel Core i5-13400",
        "Охлаждение": "Cooler Master Hyper 212 RGB",
        "Материнская плата": "ASUS ROG Strix B660-A WIFI",
        "Оперативная память": "Corsair Vengeance LPX 32GB (2x16GB) DDR4 3600MHz",
        "SSD": "Samsung 980 Pro 1TB NVMe M.2",
        "Жесткий диск": "Seagate BarraCuda 4TB SATA III",
        "Видеокарта": "NVIDIA GeForce RTX 4070 Ti",
        "Блок питания": "Corsair RMx 850W Gold",
        "Корпус": "Fractal Design Define Mini XL",
    },
    "Игровая сборка 8": {
        "Процессор": "AMD Ryzen 7 7800X",
        "Охлаждение": "Noctua NH-U12A",
        "Материнская плата": "MSI MAG B660M Mortar WiFi",
        "Оперативная память": "G.Skill Trident Z Neo 32GB (2x16GB) DDR5 6000MHz",
        "SSD": "WD Black SN850X 2TB NVMe M.2",
        "Жесткий диск": "Western Digital Blue 6TB SATA III",
        "Видеокарта": "AMD Radeon RX 7900 XT",
        "Блок питания": "EVGA SuperNOVA 850 G3 850W",
        "Корпус": "NZXT H510 Elite",
    },
    "Игровая сборка 9": {
        "Процессор": "Intel Core i9-13900KF",
        "Охлаждение": "DeepCool Gammaxx 400",
        "Материнская плата": "ASRock X670E Taichi",
        "Оперативная память": "Kingston FURY Beast 32GB (2x16GB) DDR4 3200MHz",
        "SSD": "Kingston KC2500 2TB NVMe M.2",
        "Жесткий диск": "Toshiba P300 4TB SATA III",
        "Видеокарта": "NVIDIA GeForce RTX 4080",
        "Блок питания": "Seasonic PRIME TX 850W Gold",
        "Корпус": "BitFenix Aegis Mini",
    },
    "Игровая сборка 10": {
        "Процессор": "AMD Ryzen 9 7900X",
        "Охлаждение": "Arctic Freezer 34 eSports",
        "Материнская плата": "Gigabyte Z790 AORUS Elite AX",
        "Оперативная память": "Crucial Ballistix 32GB (2x16GB) DDR5 6400MHz",
        "SSD": "Sabrent Rocket 4 Plus 2TB NVMe M.2",
        "Жесткий диск": "Hitachi GST Ultrastar 6TB SATA III",
        "Видеокарта": "AMD Radeon RX 7800 XT",
        "Блок питания": "Thermaltake Toughpower GF1 850W Gold",
        "Корпус": "Phanteks Enthoo Pro Mini",
    },
    "Офисная сборка 1": {
        "Процессор": "Intel Core i5-13400",
        "Охлаждение": "Cooler Master Hyper 212 EVO",
        "Материнская плата": "ASUS TUF B660M-PLUS WIFI",
        "Оперативная память": "Corsair Value Select 16GB (2x8GB) DDR4 3200MHz",
        "SSD": "Samsung 870 QVO 500GB SATA III",
        "Жесткий диск": "Seagate Barracuda 2TB SATA III",
        "Видеокарта": "NVIDIA GeForce GT 730 2GB",
        "Блок питания": "Corsair RMx 550W Gold",
        "Корпус": "Fractal Design Node 304",
    },
    "Офисная сборка 2": {
        "Процессор": "AMD Ryzen 5 7600",
        "Охлаждение": "Noctua NH-L9A",
        "Материнская плата": "MSI B660M PRO WIFI",
        "Оперативная память": "G.Skill Ripjaws S 16GB (2x8GB) DDR5 5600MHz",
        "SSD": "WD Blue SN550 500GB NVMe M.2",
        "Жесткий диск": "Western Digital Blue 4TB SATA III",
        "Видеокарта": "AMD Radeon R5 230 2GB",
        "Блок питания": "EVGA SuperNOVA 550 G3 550W",
        "Корпус": "NZXT H440",
    },
    "Офисная сборка 3": {
        "Процессор": "Intel Core i5-13600K",
        "Охлаждение": "Cooler Master Hyper 212 RGB",
        "Материнская плата": "ASUS ROG Strix B660-A WIFI",
        "Оперативная память": "Corsair Vengeance LPX 32GB (2x16GB) DDR4 3600MHz",
        "SSD": "Samsung 980 Pro 1TB NVMe M.2",
        "Жесткий диск": "Seagate BarraCuda 4TB SATA III",
        "Видеокарта": "NVIDIA GeForce RTX 4070 Ti",
        "Блок питания": "Corsair RMx 850W Gold",
        "Корпус": "Fractal Design Define Mini XL",
    },
    "Офисная сборка 4": {
        "Процессор": "AMD Ryzen 7 7800X",
        "Охлаждение": "Noctua NH-U12A",
        "Материнская плата": "MSI MAG B660M Mortar WiFi",
        "Оперативная память": "G.Skill Trident Z Neo 32GB (2x16GB) DDR5 6000MHz",
        "SSD": "WD Black SN850X 2TB NVMe M.2",
        "Жесткий диск": "Western Digital Blue 6TB SATA III",
        "Видеокарта": "AMD Radeon RX 7900 XT",
        "Блок питания": "EVGA SuperNOVA 850 G3 850W",
        "Корпус": "NZXT H510 Elite",
    },
    "Офисная сборка 5": {
        "Процессор": "Intel Core i9-13900KF",
        "Охлаждение": "DeepCool Gammaxx 400",
        "Материнская плата": "ASRock X670E Taichi",
        "Оперативная память": "Kingston FURY Beast 32GB (2x16GB) DDR4 3200MHz",
        "SSD": "Kingston KC2500 2TB NVMe M.2",
        "Жесткий диск": "Toshiba P300 4TB SATA III",
        "Видеокарта": "NVIDIA GeForce RTX 4080",
        "Блок питания": "Seasonic PRIME TX 850W Gold",
        "Корпус": "BitFenix Aegis Mini",
    },
    "Офисная сборка 6": {
        "Процессор": "AMD Ryzen 9 7900X",
        "Охлаждение": "Arctic Freezer 34 eSports",
        "Материнская плата": "Gigabyte Z790 AORUS Elite AX",
        "Оперативная память": "Crucial Ballistix 32GB (2x16GB) DDR5 6400MHz",
        "SSD": "Sabrent Rocket 4 Plus 2TB NVMe M.2",
        "Жесткий диск": "Hitachi GST Ultrastar 6TB SATA III",
        "Видеокарта": "AMD Radeon RX 7800 XT",
        "Блок питания": "Thermaltake Toughpower GF1 850W Gold",
        "Корпус": "Phanteks Enthoo Pro Mini",
    },
    "Офисная сборка 7": {
        "Процессор": "Intel Core i7-13700",
        "Охлаждение": "Cooler Master Hyper 212 EVO",
        "Материнская плата": "ASUS TUF B660M-PLUS WIFI",
        "Оперативная память": "Corsair Value Select 16GB (2x8GB) DDR4 3200MHz",
        "SSD": "Samsung 870 QVO 500GB SATA III",
        "Жесткий диск": "Seagate Barracuda 2TB SATA III",
        "Видеокарта": "NVIDIA GeForce GT 730 2GB",
        "Блок питания": "Corsair RMx 550W Gold",
        "Корпус": "Fractal Design Node 304",
    },
    "Офисная сборка 8": {
        "Процессор": "AMD Ryzen 5 7600",
        "Охлаждение": "Noctua NH-L9A",
        "Материнская плата": "MSI B660M PRO WIFI",
        "Оперативная память": "G.Skill Ripjaws S 16GB (2x8GB) DDR5 5600MHz",
        "SSD": "WD Blue SN550 500GB NVMe M.2",
        "Жесткий диск": "Western Digital Blue 4TB SATA III",
        "Видеокарта": "AMD Radeon R5 230 2GB",
        "Блок питания": "EVGA SuperNOVA 550 G3 550W",
        "Корпус": "NZXT H440",
    },
    "Офисная сборка 9": {
        "Процессор": "Intel Core i5-13400",
        "Охлаждение": "Cooler Master Hyper 212 RGB",
        "Материнская плата": "ASUS ROG Strix B660-A WIFI",
        "Оперативная память": "Corsair Vengeance LPX 32GB (2x16GB) DDR4 3600MHz",
        "SSD": "Samsung 980 Pro 1TB NVMe M.2",
        "Жесткий диск": "Seagate BarraCuda 4TB SATA III",
        "Видеокарта": "NVIDIA GeForce RTX 4070 Ti",
        "Блок питания": "Corsair RMx 850W Gold",
        "Корпус": "Fractal Design Define Mini XL",
    },
    "Офисная сборка 10": {
        "Процессор": "AMD Ryzen 7 7800X",
        "Охлаждение": "Noctua NH-U12A",
        "Материнская плата": "MSI MAG B660M Mortar WiFi",
        "Оперативная память": "G.Skill Trident Z Neo 32GB (2x16GB) DDR5 6000MHz",
        "SSD": "WD Black SN850X 2TB NVMe M.2",
        "Жесткий диск": "Western Digital Blue 6TB SATA III",
        "Видеокарта": "AMD Radeon RX 7900 XT",
        "Блок питания": "EVGA SuperNOVA 850 G3 850W",
        "Корпус": "NZXT H510 Elite",
    },
}

# Список всех возможных вариантов комплектующих
component_options = {
    "Процессор": [
        "Intel Core i5-13600K",
        "AMD Ryzen 7 7800X",
        "Intel Core i9-13900KF",
        "AMD Ryzen 9 7900X",
        "Intel Core i5-13400",
        "AMD Ryzen 5 7600",
        "Intel Core i7-13700",
        "AMD Ryzen 7 7700",
    ],
    "Охлаждение": [
        "Cooler Master Hyper 212 RGB",
        "Noctua NH-U12A",
        "Corsair Hydro X Series H115i RGB Platinum",
        "NZXT Kraken X73",
        "Cooler Master Hyper 212 EVO",
        "Noctua NH-L9A",
        "DeepCool Gammaxx 400",
        "Arctic Freezer 34 eSports",
    ],
    "Материнская плата": [
        "ASUS ROG Strix B660-A WIFI",
        "MSI MAG B660M Mortar WiFi",
        "Gigabyte Z790 AORUS Elite AX",
        "ASRock X670E Taichi",
        "ASUS TUF B660M-PLUS WIFI",
        "MSI B660M PRO WIFI",
        "Gigabyte B660M DS3H",
        "ASRock B660M Pro RS",
    ],
    "Оперативная память": [
        "Corsair Vengeance LPX 32GB (2x16GB) DDR4 3600MHz",
        "G.Skill Trident Z Neo 32GB (2x16GB) DDR5 6000MHz",
        "Kingston FURY Beast 32GB (2x16GB) DDR4 3200MHz",
        "Crucial Ballistix 32GB (2x16GB) DDR5 6400MHz",
        "Corsair Value Select 16GB (2x8GB) DDR4 3200MHz",
        "G.Skill Ripjaws S 16GB (2x8GB) DDR5 5600MHz",
        "Kingston ValueRAM 16GB (2x8GB) DDR4 2666MHz",
        "Crucial Ballistix 16GB (2x8GB) DDR5 5200MHz",
    ],
    "SSD": [
        "Samsung 980 Pro 1TB NVMe M.2",
        "WD Black SN850X 2TB NVMe M.2",
        "Kingston KC2500 2TB NVMe M.2",
        "Sabrent Rocket 4 Plus 2TB NVMe M.2",
        "Samsung 870 QVO 500GB SATA III",
        "WD Blue SN550 500GB NVMe M.2",
        "Kingston A400 480GB SATA III",
        "Sabrent Rocket 4 500GB NVMe M.2",
    ],
    "Жесткий диск": [
        "Seagate BarraCuda 4TB SATA III",
        "Western Digital Blue 6TB SATA III",
        "Toshiba P300 4TB SATA III",
        "Hitachi GST Ultrastar 6TB SATA III",
        "Seagate Barracuda 2TB SATA III",
        "Western Digital Blue 4TB SATA III",
        "Toshiba P300 2TB SATA III",
        "Hitachi GST Ultrastar 4TB SATA III",
    ],
    "Видеокарта": [
        "NVIDIA GeForce RTX 4070 Ti",
        "AMD Radeon RX 7900 XT",
        "NVIDIA GeForce RTX 4080",
        "AMD Radeon RX 7800 XT",
        "NVIDIA GeForce GT 730 2GB",
        "AMD Radeon R5 230 2GB",
        "NVIDIA GeForce MX550 2GB",
        "AMD Radeon RX 640 2GB",
    ],
    "Блок питания": [
        "Corsair RMx 850W Gold",
        "EVGA SuperNOVA 850 G3 850W",
        "Seasonic PRIME TX 850W Gold",
        "Thermaltake Toughpower GF1 850W Gold",
        "Corsair RMx 550W Gold",
        "EVGA SuperNOVA 550 G3 550W",
        "Seasonic Prime TX 550W Gold",
        "Thermaltake Toughpower GF1 550W Gold",
    ],
    "Корпус": [
        "Fractal Design Define Mini XL",
        "NZXT H510 Elite",
        "BitFenix Aegis Mini",
        "Phanteks Enthoo Pro Mini",
        "Fractal Design Node 304",
        "NZXT H440",
        "BitFenix Aurora",
        "Phanteks Eclipse P300",
    ],
}

def main(page: ft.Page):
    page.title = "Конфигуратор ПК"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 20
    page.spacing = 10
    page.window_width = 800
    page.window_height = 600
    page.bgcolor = "#E0E0E6"

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
            ft.Row([ft.Text("Конфигуратор ПК", size=20, weight=ft.FontWeight.BOLD)]),
            ft.Divider(height=1, color="black"),
            ft.Row([
                ft.Text("Популярные сборки", size=16),
                ft.Row([
                    ft.ElevatedButton("Помощь", on_click=open_help_file),
                    ft.ElevatedButton("Создать сборку", on_click=lambda _: page.go("/create")),
                    ft.ElevatedButton("Сравнение комплектаций"),
                    ft.ElevatedButton("Сохраненные сборки"),
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
                ft.ElevatedButton("Служба поддержки"),
            ], alignment=ft.MainAxisAlignment.END, spacing=10),
        ], spacing=20),
        padding=20,
        border_radius=10,
        bgcolor="#F0F0F0",
    )

    # Обновляемая строка таблицы с кнопкой выбора
    def create_table_row(title, description, component_type, update_callback):
        # Текстовое поле, которое будет обновляться
        label = ft.Text(description or "...", size=12)
        menu_items = [
            ft.PopupMenuItem(text=item, on_click=lambda e, item=item: update_callback(title, item, label))
            for item in component_options.get(component_type, [])
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
                content=label,
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

    def build_details_page(page: ft.Page, build_name: str):
        details = build_details.get(build_name, {})

        def update_component(component_title, new_value, label):
            details[component_title] = new_value
            label.value = new_value
            page.update()

        table = ft.Column([
            create_table_row("Процессор", details.get("Процессор", "..."), "Процессор", update_component),
            create_table_row("Охлаждение", details.get("Охлаждение", "..."), "Охлаждение", update_component),
            create_table_row("Материнская плата", details.get("Материнская плата", "..."), "Материнская плата", update_component),
            create_table_row("Оперативная память", details.get("Оперативная память", "..."), "Оперативная память", update_component),
            create_table_row("SSD", details.get("SSD", "..."), "SSD", update_component),
            create_table_row("Жесткий диск", details.get("Жесткий диск", "..."), "Жесткий диск", update_component),
            create_table_row("Видеокарта", details.get("Видеокарта", "..."), "Видеокарта", update_component),
            create_table_row("Блок питания", details.get("Блок питания", "..."), "Блок питания", update_component),
            create_table_row("Корпус", details.get("Корпус", "..."), "Корпус", update_component),
        ], spacing=10)

        right_section = ft.Column([
            ft.Container(
                content=ft.Text("Итоговая стоимость ПК\n... рублей", size=16, weight=ft.FontWeight.BOLD),
                padding=20,
                width=300,
                height=150,
                bgcolor="#FFFFFF",
                border_radius=5,
            ),
            ft.ElevatedButton("Сохранить сборку", width=300, height=50),
        ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=20)

        back_button = ft.ElevatedButton("Назад", on_click=lambda _: page.go("/"), width=100, height=40)
        help_button = ft.ElevatedButton("Помощь", width=100, height=40, on_click=open_help_file)

        details_content = ft.Container(
            content=ft.Row([table, right_section], spacing=20, alignment=ft.MainAxisAlignment.CENTER),
            padding=20,
            border_radius=10,
            bgcolor="#F0F0F0",
        )

        main_content = ft.Container(
            content=ft.Column([
                ft.Row([
                    ft.Text(f"Детали сборки: {build_name}", size=20, weight=ft.FontWeight.BOLD),
                    ft.Row([back_button, help_button], spacing=10),
                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                ft.Divider(height=1, color="black"),
                details_content,
            ], spacing=20),
            padding=20,
            border_radius=10,
            bgcolor="#F0F0F0",
        )

        return ft.View("/details", controls=[main_content])

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

        def update_component(component_title, new_value, label):
            current_build[component_title] = new_value
            label.value = new_value
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
                content=ft.Text("Итоговая стоимость ПК\n... рублей", size=16, weight=ft.FontWeight.BOLD),
                padding=20,
                width=300,
                height=150,
                bgcolor="#FFFFFF",
                border_radius=5,
            ),
            ft.ElevatedButton("Сохранить сборку", width=300, height=50),
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

    def route_change(route):
        if page.route == "/":
            page.views.clear()
            page.views.append(ft.View("/", controls=[main_container]))
        elif page.route.startswith("/details/"):
            build_name = page.route.split("/")[-1]
            page.views.append(build_details_page(page, build_name))
        elif page.route == "/create":
            page.views.append(create_build_page(page))
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go("/")

ft.app(target=main)