import flet as ft

def main(page: ft.Page):
    # Настройка страницы
    page.title = "Конфигуратор ПК"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER  # Выравнивание по центру по вертикали
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER  # Выравнивание по центру по горизонтали
    page.padding = 20
    page.spacing = 10
    page.window_width = 800  # Фиксированный размер окна по ширине
    page.window_height = 600  # Фиксированный размер окна по высоте
    page.bgcolor = "#F0F0F0"  # Однородный фон для всего приложения

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

    # Кнопка "Назад"
    back_button = ft.ElevatedButton(
        "Назад",
        on_click=lambda _: page.go("/"),  # Возвращаемся на главную страницу
        width=100,
        height=40,
    )

    help_button = ft.ElevatedButton(
        "помощь",
        #здесь будет функционал
        width=100,
        height=40,
    )

    # Общий контейнер
    main_container = ft.Container(
        content=ft.Column(
            [
                # Заголовок с кнопкой "Назад"
                ft.Row(
                    [
                        ft.Text("Создание сборки", size=20, weight=ft.FontWeight.BOLD),
                        back_button,  # Кнопка "Назад" справа
                        help_button
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

    # Добавление основного контейнера на страницу
    page.add(main_container)

# Запуск приложения
ft.app(target=main)