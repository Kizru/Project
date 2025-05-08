import flet as ft

# Функция для создания строки таблицы
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

# Функция для создания страницы с деталями сборки
def build_details_page(page: ft.Page, build_name: str):
    # Таблица характеристик
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

    # Кнопка "Назад"
    back_button = ft.ElevatedButton(
        "Назад",
        on_click=lambda _: page.go("/"),  # Возвращаемся на главную страницу
        width=100,
        height=40,
    )

    # Основной контейнер
    main_container = ft.Container(
        content=ft.Column(
            [
                ft.Row(
                    [
                        ft.Text(f"Характеристики сборки: {build_name}", size=20, weight=ft.FontWeight.BOLD),  # Теперь заголовок слева
                        back_button,  # Теперь кнопка "Назад" справа
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                ft.Divider(height=1, color="black"),
                ft.Row(
                    [
                        table,  # Левая часть с таблицей
                        right_section,  # Правая часть с итоговой стоимостью и кнопкой
                    ],
                    spacing=20,
                    alignment=ft.MainAxisAlignment.CENTER,  # Горизонтальное выравнивание
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,  # Вертикальное выравнивание
                ),
            ],
            spacing=20,
        ),
        padding=20,
        border_radius=10,
        bgcolor="#F0F0F0",
    )

    # Возвращаем страницу с комплектующими
    return ft.View("/details", controls=[main_container])

# Основная функция приложения
def main(page: ft.Page):
    # Настройка страницы
    page.title = "Конфигуратор ПК"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 20
    page.spacing = 10
    page.window_width = 800  # Фиксированный размер окна по ширине
    page.window_height = 600  # Фиксированный размер окна по высоте
    page.bgcolor = "#E0E0E0"  # Серый фон для всего приложения

    # Основной контейнер
    main_container = ft.Container(
        content=ft.Column(
            [
                # Заголовок
                ft.Row(
                    [
                        ft.Text("Конфигуратор ПК", size=20, weight=ft.FontWeight.BOLD),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                ft.Divider(height=1, color="black"),

                # Первая секция - популярные сборки
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

                # Вторая секция - фильтры
                ft.Row(
                    [
                        ft.OutlinedButton("Все"),
                        ft.OutlinedButton("Офисные"),
                        ft.OutlinedButton("Игровые"),
                    ],
                    spacing=10,
                ),

                # Третья секция - кнопки сборок
                ft.Container(
                    content=ft.Row(
                        [
                            ft.ElevatedButton(
                                content=ft.Text(f"Компьютер {i}", size=14),
                                width=100,
                                height=100,
                                style=ft.ButtonStyle(
                                    shape=ft.RoundedRectangleBorder(radius=5),
                                    color={"": "white"},
                                    bgcolor={"": "#ADD8E6"},
                                ),
                                on_click=lambda e, name=f"Компьютер {i}": page.go(f"/details/{name}"),
                            ) for i in range(1, 21)
                        ],
                        scroll="auto",  # Добавляем прокрутку
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        spacing=10,
                    ),
                    padding=10,
                    border=ft.border.all(1, "lightgray"),  # Добавляем границу
                    border_radius=10,
                ),

                # Четвертая секция - подписка на новости
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Row(
                                [
                                    ft.Text("Хочу быть в курсе акций и новинок!", size=14),
                                    ft.TextField(label="Введите адрес электронной почты"),
                                    ft.ElevatedButton("Подписаться"),
                                ],
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                spacing=10,
                            ),
                        ],
                        spacing=5,
                    ),
                    padding=10,
                    border=ft.border.all(1, "lightgray"),  # Добавляем границу
                    border_radius=10,
                ),

                # Пятая секция - ссылки
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

    # Добавление основного контейнера на страницу
    page.add(main_container)

    # Навигация
    def route_change(route):
        if page.route == "/":
            page.views.clear()
            page.views.append(ft.View("/", controls=[main_container]))
        elif page.route.startswith("/details/"):
            build_name = page.route.split("/")[-1]
            page.views.append(build_details_page(page, build_name))
        page.update()

    # Удаление текущего представления при нажатии "Назад"
    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    # Обработка изменения маршрута
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    # Установка начального маршрута
    page.go("/")

# Запуск приложения
ft.app(target=main)