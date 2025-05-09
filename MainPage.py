import flet as ft

# Генерация списка сборок
gaming_builds = [f"Игровая сборка {i}" for i in range(1, 11)]
office_builds = [f"Офисная сборка {i}" for i in range(1, 11)]
all_builds = gaming_builds + office_builds  # Все 20 сборок

build_details = {
    # Игровые сборки
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
        "Охлаждение": "Corsair Hydro X Series H115i RGB Platinum",
        "Материнская плата": "Gigabyte Z790 AORUS Elite AX",
        "Оперативная память": "Kingston FURY Beast 32GB (2x16GB) DDR4 3200MHz",
        "SSD": "Kingston KC2500 2TB NVMe M.2",
        "Жесткий диск": "Toshiba P300 4TB SATA III",
        "Видеокарта": "NVIDIA GeForce RTX 4080",
        "Блок питания": "Seasonic PRIME TX 850W Gold",
        "Корпус": "BitFenix Aegis Mini",
    },
    "Игровая сборка 4": {
        "Процессор": "AMD Ryzen 9 7900X",
        "Охлаждение": "NZXT Kraken X73",
        "Материнская плата": "ASRock X670E Taichi",
        "Оперативная память": "Crucial Ballistix 32GB (2x16GB) DDR5 6400MHz",
        "SSD": "Sabrent Rocket 4 Plus 2TB NVMe M.2",
        "Жесткий диск": "Hitachi GST Ultrastar 6TB SATA III",
        "Видеокарта": "AMD Radeon RX 7800 XT",
        "Блок питания": "Thermaltake Toughpower GF1 850W Gold",
        "Корпус": "Phanteks Enthoo Pro Mini",
    },
    "Игровая сборка 5": {
        "Процессор": "Intel Core i5-13600K",
        "Охлаждение": "Cooler Master Hyper 212 EVO",
        "Материнская плата": "ASUS TUF B660M-PLUS WIFI",
        "Оперативная память": "Corsair Value Select 16GB (2x8GB) DDR4 3200MHz",
        "SSD": "Samsung 870 QVO 500GB SATA III",
        "Жесткий диск": "Seagate Barracuda 2TB SATA III",
        "Видеокарта": "NVIDIA GeForce RTX 4070",
        "Блок питания": "Corsair RMx 650W Gold",
        "Корпус": "Fractal Design Node 304",
    },
    "Игровая сборка 6": {
        "Процессор": "AMD Ryzen 7 7800X",
        "Охлаждение": "Noctua NH-L9A",
        "Материнская плата": "MSI B660M PRO WIFI",
        "Оперативная память": "G.Skill Ripjaws S 16GB (2x8GB) DDR5 5600MHz",
        "SSD": "WD Blue SN550 500GB NVMe M.2",
        "Жесткий диск": "Western Digital Blue 4TB SATA III",
        "Видеокарта": "AMD Radeon RX 7700 XT",
        "Блок питания": "EVGA SuperNOVA 750 G3 750W",
        "Корпус": "NZXT H440",
    },
    "Игровая сборка 7": {
        "Процессор": "Intel Core i9-13900KF",
        "Охлаждение": "DeepCool Gammaxx 400",
        "Материнская плата": "Gigabyte B660M DS3H",
        "Оперативная память": "Kingston ValueRAM 16GB (2x8GB) DDR4 2666MHz",
        "SSD": "Kingston A400 480GB SATA III",
        "Жесткий диск": "Toshiba P300 2TB SATA III",
        "Видеокарта": "NVIDIA GeForce RTX 4080 SUPER",
        "Блок питания": "Seasonic Prime TX 750W Gold",
        "Корпус": "BitFenix Aurora",
    },
    "Игровая сборка 8": {
        "Процессор": "AMD Ryzen 9 7900X",
        "Охлаждение": "Arctic Freezer 34 eSports",
        "Материнская плата": "ASRock B660M Pro RS",
        "Оперативная память": "Crucial Ballistix 16GB (2x8GB) DDR5 5200MHz",
        "SSD": "Sabrent Rocket 4 500GB NVMe M.2",
        "Жесткий диск": "Hitachi GST Ultrastar 4TB SATA III",
        "Видеокарта": "AMD Radeon RX 7900 GRE",
        "Блок питания": "Thermaltake Toughpower GF1 750W Gold",
        "Корпус": "Phanteks Eclipse P300",
    },
    "Игровая сборка 9": {
        "Процессор": "Intel Core i7-13700",
        "Охлаждение": "Cooler Master Hyper 212 RGB",
        "Материнская плата": "ASUS ROG Strix B660-A WIFI",
        "Оперативная память": "Corsair Vengeance LPX 32GB (2x16GB) DDR4 3600MHz",
        "SSD": "Samsung 980 Pro 1TB NVMe M.2",
        "Жесткий диск": "Seagate BarraCuda 4TB SATA III",
        "Видеокарта": "NVIDIA GeForce RTX 4070",
        "Блок питания": "Corsair RMx 750W Gold",
        "Корпус": "Fractal Design Define Mini XL",
    },
    "Игровая сборка 10": {
        "Процессор": "AMD Ryzen 7 7700",
        "Охлаждение": "Noctua NH-U12A",
        "Материнская плата": "MSI MAG B660M Mortar WiFi",
        "Оперативная память": "G.Skill Trident Z Neo 32GB (2x16GB) DDR5 6000MHz",
        "SSD": "WD Black SN850X 2TB NVMe M.2",
        "Жесткий диск": "Western Digital Blue 6TB SATA III",
        "Видеокарта": "AMD Radeon RX 7800 XT",
        "Блок питания": "EVGA SuperNOVA 750 G3 750W",
        "Корпус": "NZXT H510 Elite",
    },

    # Офисные сборки
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
        "Процессор": "Intel Core i7-13700",
        "Охлаждение": "DeepCool Gammaxx 400",
        "Материнская плата": "Gigabyte B660M DS3H",
        "Оперативная память": "Kingston ValueRAM 16GB (2x8GB) DDR4 2666MHz",
        "SSD": "Kingston A400 480GB SATA III",
        "Жесткий диск": "Toshiba P300 2TB SATA III",
        "Видеокарта": "NVIDIA GeForce MX550 2GB",
        "Блок питания": "Seasonic Prime TX 550W Gold",
        "Корпус": "BitFenix Aurora",
    },
    "Офисная сборка 4": {
        "Процессор": "AMD Ryzen 7 7700",
        "Охлаждение": "Arctic Freezer 34 eSports",
        "Материнская плата": "ASRock B660M Pro RS",
        "Оперативная память": "Crucial Ballistix 16GB (2x8GB) DDR5 5200MHz",
        "SSD": "Sabrent Rocket 4 500GB NVMe M.2",
        "Жесткий диск": "Hitachi GST Ultrastar 4TB SATA III",
        "Видеокарта": "AMD Radeon RX 640 2GB",
        "Блок питания": "Thermaltake Toughpower GF1 550W Gold",
        "Корпус": "Phanteks Eclipse P300",
    },
    "Офисная сборка 5": {
        "Процессор": "Intel Core i5-13400",
        "Охлаждение": "Cooler Master Hyper 212 RGB",
        "Материнская плата": "ASUS ROG Strix B660-A WIFI",
        "Оперативная память": "Corsair Value Select 16GB (2x8GB) DDR4 3200MHz",
        "SSD": "Samsung 870 QVO 500GB SATA III",
        "Жесткий диск": "Seagate Barracuda 2TB SATA III",
        "Видеокарта": "NVIDIA GeForce GT 730 2GB",
        "Блок питания": "Corsair RMx 550W Gold",
        "Корпус": "Fractal Design Node 304",
    },
    "Офисная сборка 6": {
        "Процессор": "AMD Ryzen 5 7600",
        "Охлаждение": "Noctua NH-L9A",
        "Материнская плата": "MSI MAG B660M Mortar WiFi",
        "Оперативная память": "G.Skill Ripjaws S 16GB (2x8GB) DDR5 5600MHz",
        "SSD": "WD Blue SN550 500GB NVMe M.2",
        "Жесткий диск": "Western Digital Blue 4TB SATA III",
        "Видеокарта": "AMD Radeon R5 230 2GB",
        "Блок питания": "EVGA SuperNOVA 550 G3 550W",
        "Корпус": "NZXT H440",
    },
    "Офисная сборка 7": {
        "Процессор": "Intel Core i7-13700",
        "Охлаждение": "DeepCool Gammaxx 400",
        "Материнская плата": "Gigabyte B660M DS3H",
        "Оперативная память": "Kingston ValueRAM 16GB (2x8GB) DDR4 2666MHz",
        "SSD": "Kingston A400 480GB SATA III",
        "Жесткий диск": "Toshiba P300 2TB SATA III",
        "Видеокарта": "NVIDIA GeForce MX550 2GB",
        "Блок питания": "Seasonic Prime TX 550W Gold",
        "Корпус": "BitFenix Aurora",
    },
    "Офисная сборка 8": {
        "Процессор": "AMD Ryzen 7 7700",
        "Охлаждение": "Arctic Freezer 34 eSports",
        "Материнская плата": "ASRock B660M Pro RS",
        "Оперативная память": "Crucial Ballistix 16GB (2x8GB) DDR5 5200MHz",
        "SSD": "Sabrent Rocket 4 500GB NVMe M.2",
        "Жесткий диск": "Hitachi GST Ultrastar 4TB SATA III",
        "Видеокарта": "AMD Radeon RX 640 2GB",
        "Блок питания": "Thermaltake Toughpower GF1 550W Gold",
        "Корпус": "Phanteks Eclipse P300",
    },
    "Офисная сборка 9": {
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
    "Офисная сборка 10": {
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

    # Row для кнопок сборок
    builds_row = ft.Row(scroll="auto", spacing=10, alignment=ft.MainAxisAlignment.SPACE_BETWEEN)

    # Заполнение начальных кнопок
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

    # Контейнер для сборок
    builds_container = ft.Container(
        content=builds_row,
        padding=10,
        border=ft.border.all(1, "lightgray"),
        border_radius=10,
    )

    # Функция фильтрации
    def set_filter(category):
        builds_row.controls.clear()

        if category == "Все":
            builds_row.controls.extend(create_buttons(all_builds))
        elif category == "Игровые":
            builds_row.controls.extend(create_buttons(gaming_builds))
        elif category == "Офисные":
            builds_row.controls.extend(create_buttons(office_builds))

        page.update()

    # Кнопки фильтрации
    filter_controls = ft.Row(
        [
            ft.OutlinedButton("Все", on_click=lambda _: set_filter("Все")),
            ft.OutlinedButton("Офисные", on_click=lambda _: set_filter("Офисные")),
            ft.OutlinedButton("Игровые", on_click=lambda _: set_filter("Игровые")),
        ],
        spacing=10,
    )

    # Основной контейнер страницы
    main_container = ft.Container(
        content=ft.Column(
            [
                ft.Row([ft.Text("Конфигуратор ПК", size=20, weight=ft.FontWeight.BOLD)]),
                ft.Divider(height=1, color="black"),

                ft.Row(
                    [
                        ft.Text("Популярные сборки", size=16),
                        ft.Row(
                            [
                                ft.ElevatedButton("Создать сборку"),
                                ft.ElevatedButton("Сравнение комплектаций"),
                                ft.ElevatedButton("Сохраненные сборки"),
                            ],
                            spacing=10,
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),

                filter_controls,
                builds_container,

                ft.Container(
                    content=ft.Column(
                        [
                            ft.Row(
                                [
                                    ft.Text("Хочу быть в курсе акций и новинок!", size=14),
                                    ft.TextField(label="Введите адрес электронной почты", expand=True),
                                    ft.ElevatedButton("Подписаться"),
                                ],
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                spacing=10,
                            ),
                        ],
                        spacing=5,
                    ),
                    padding=10,
                    border=ft.border.all(1, "lightgray"),
                    border_radius=10,
                ),

                ft.Row(
                    [
                        ft.ElevatedButton("Отзывы о сервисе"),
                        ft.ElevatedButton("Служба поддержки"),
                    ],
                    alignment=ft.MainAxisAlignment.END,
                    spacing=10,
                ),
            ],
            spacing=20,
        ),
        padding=20,
        border_radius=10,
        bgcolor="#F0F0F0",
    )

    # --- Страница деталей сборки ---
    def build_details_page(page: ft.Page, build_name: str):
        # Получаем детали сборки из словаря
        details = build_details.get(build_name, {})

        # Создаем функцию для создания строки таблицы
        def create_table_row(title, description, price):
            return ft.Row(
                [
                    ft.Container(
                        content=ft.Text(title, size=14, weight=ft.FontWeight.BOLD),
                        alignment=ft.alignment.center_left,
                        padding=ft.padding.only(left=10),
                        width=150,  # Фиксированная ширина левой колонки
                        height=50,  # Фиксированная высота строки
                        bgcolor="#FFFFFF",
                        border_radius=5,
                    ),
                    ft.Container(
                        content=ft.Column(
                            [
                                ft.Text(description, size=12),
                                ft.Text(f"{price} рублей", size=12),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                        alignment=ft.alignment.center,
                        padding=ft.padding.only(left=10),
                        width=300,  # Фиксированная ширина правой колонки
                        height=50,  # Фиксированная высота строки
                        bgcolor="#FFFFFF",
                        border_radius=5,
                    ),
                ],
                spacing=10,
                height=50,  # Высота строки
            )

        # Создаем таблицу характеристик
        table = ft.Column(
            [
                create_table_row("Процессор", details.get("Процессор", "..."), "..."),
                create_table_row("Охлаждение", details.get("Охлаждение", "..."), "..."),
                create_table_row("Материнская плата", details.get("Материнская плата", "..."), "..."),
                create_table_row("Оперативная память", details.get("Оперативная память", "..."), "..."),
                create_table_row("SSD", details.get("SSD", "..."), "..."),
                create_table_row("Жесткий диск", details.get("Жесткий диск", "..."), "..."),
                create_table_row("Видеокарта", details.get("Видеокарта", "..."), "..."),
                create_table_row("Блок питания", details.get("Блок питания", "..."), "..."),
                create_table_row("Корпус", details.get("Корпус", "..."), "..."),
            ],
            spacing=10,
        )

        # Правая часть - итоговая стоимость и кнопка сохранения
        right_section = ft.Column(
            [
                ft.Container(
                    content=ft.Text("Итоговая стоимость ПК\n... рублей", size=16, weight=ft.FontWeight.BOLD),
                    padding=20,
                    width=300,
                    height=150,
                    bgcolor="#FFFFFF",
                    border_radius=5,
                ),
                ft.ElevatedButton("Сохранить сборку", width=300, height=50),
            ],
            alignment=ft.MainAxisAlignment.CENTER,  # Вертикальное выравнивание
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
        )

        # Общий контейнер
        details_content = ft.Container(
            content=ft.Row(
                [
                    table,  # Левая часть с таблицей
                    right_section,  # Правая часть с итоговой стоимостью и кнопкой
                ],
                spacing=20,
                alignment=ft.MainAxisAlignment.CENTER,  # Горизонтальное выравнивание
                vertical_alignment=ft.CrossAxisAlignment.CENTER,  # Вертикальное выравнивание
            ),
            padding=20,
            border_radius=10,
            bgcolor="#F0F0F0",
        )

        # Назад
        back_button = ft.ElevatedButton(
            "Назад",
            on_click=lambda _: page.go("/"),
            width=100,
            height=40,
        )

        # Главный контейнер страницы
        main_content = ft.Container(
            content=ft.Column(
                [
                    ft.Row(
                        [
                            ft.Text(f"Детали сборки: {build_name}", size=20, weight=ft.FontWeight.BOLD),
                            back_button,
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    ),
                    ft.Divider(height=1, color="black"),
                    details_content,
                ],
                spacing=20,
            ),
            padding=20,
            border_radius=10,
            bgcolor="#F0F0F0",
        )

        return ft.View("/details", controls=[main_content])

    # --- Навигация ---
    def route_change(route):
        if page.route == "/":
            page.views.clear()
            page.views.append(ft.View("/", controls=[main_container]))
        elif page.route.startswith("/details/"):
            build_name = page.route.split("/")[-1]
            page.views.append(build_details_page(page, build_name))
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop

    page.go("/")

# Запуск приложения
ft.app(target=main)