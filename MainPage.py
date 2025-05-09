import flet as ft

# Генерация списка сборок
gaming_builds = [f"Игровая сборка {i}" for i in range(1, 11)]
office_builds = [f"Офисная сборка {i}" for i in range(1, 11)]
all_builds = gaming_builds + office_builds  # Все 20 сборок

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
                create_table_row("Процессор", "Характеристики комплектующего", "..."),
                create_table_row("Охлаждение", "Характеристики комплектующего", "..."),
                create_table_row("Материнская плата", "Характеристики комплектующего", "..."),
                create_table_row("Оперативная память", "Характеристики комплектующего", "..."),
                create_table_row("SSD", "Характеристики комплектующего", "..."),
                create_table_row("Жесткий диск", "Характеристики комплектующего", "..."),
                create_table_row("Видеокарта", "Характеристики комплектующего", "..."),
                create_table_row("Блок питания", "Характеристики комплектующего", "..."),
                create_table_row("Корпус", "Характеристики комплектующего", "..."),
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