import flet as ft
from flet.core.icons import Icons

def main(page: ft.Page):
    page.title = "Конфигуратор ПК"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Функция для обработки нажатия на кнопку
    def button_click(e):
        print(f"Кнопка нажата: {e.control.data}")

    # Шапка
    header = ft.Row(
        [
            ft.Text("Конфигуратор ПК", size=24, font_family="Roboto"),
            ft.Row(
                [
                    ft.ElevatedButton("Сравнение комплектующих"),
                    ft.ElevatedButton("Сохраненные сборки")
                ],
                alignment=ft.MainAxisAlignment.END
            )
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )

    # Навигация по компьютерам
    navigation = ft.Row(
        [
            ft.Container(
                content=ft.CircleAvatar(content=ft.Icon(Icons.ARROW_BACK_IOS)),
                on_click=lambda e: button_click(e)  # Обработка нажатия через Container
            ),
            ft.ElevatedButton("Компьютер 1"),
            ft.ElevatedButton("Компьютер 2"),
            ft.ElevatedButton("Компьютер 3"),
            ft.ElevatedButton("Компьютер 4"),
            ft.ElevatedButton("Компьютер 5"),
            ft.ElevatedButton("Компьютер 6"),
            ft.ElevatedButton("Компьютер 7"),
            ft.Container(
                content=ft.CircleAvatar(content=ft.Icon(Icons.ARROW_FORWARD_IOS)),
                on_click=lambda e: button_click(e)  # Обработка нажатия через Container
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=10
    )

    # Таблица характеристик комплектующих
    table = ft.Column(
        [
            ft.Row(
                [
                    ft.Container(content=ft.Text("Процессор"), padding=10),
                    ft.Container(content=ft.Text("Характеристики комплектующей ... рублей"), padding=10),
                    ft.Container(content=ft.Icon(Icons.SWAP_HORIZONTAL_CIRCLE_OUTLINED), padding=10)
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            ),
            ft.Row(
                [
                    ft.Container(content=ft.Text("Охлаждение"), padding=10),
                    ft.Container(content=ft.Text("Характеристики комплектующей ... рублей"), padding=10),
                    ft.Container(content=ft.Icon(Icons.SWAP_HORIZONTAL_CIRCLE_OUTLINED), padding=10)
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            ),
            ft.Row(
                [
                    ft.Container(content=ft.Text("Материнская плата"), padding=10),
                    ft.Container(content=ft.Text("Характеристики комплектующей ... рублей"), padding=10),
                    ft.Container(content=ft.Icon(Icons.SWAP_HORIZONTAL_CIRCLE_OUTLINED), padding=10)
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            ),
            ft.Row(
                [
                    ft.Container(content=ft.Text("Оперативная память"), padding=10),
                    ft.Container(content=ft.Text("Характеристики комплектующей ... рублей"), padding=10),
                    ft.Container(content=ft.Icon(Icons.SWAP_HORIZONTAL_CIRCLE_OUTLINED), padding=10)
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            ),
            ft.Row(
                [
                    ft.Container(content=ft.Text("SSD"), padding=10),
                    ft.Container(content=ft.Text("Характеристики комплектующей ... рублей"), padding=10),
                    ft.Container(content=ft.Icon(Icons.SWAP_HORIZONTAL_CIRCLE_OUTLINED), padding=10)
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            ),
            ft.Row(
                [
                    ft.Container(content=ft.Text("Жесткий диск"), padding=10),
                    ft.Container(content=ft.Text("Характеристики комплектующей ... рублей"), padding=10),
                    ft.Container(content=ft.Icon(Icons.SWAP_HORIZONTAL_CIRCLE_OUTLINED), padding=10)
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            ),
            ft.Row(
                [
                    ft.Container(content=ft.Text("Видеокарта"), padding=10),
                    ft.Container(content=ft.Text("Характеристики комплектующей ... рублей"), padding=10),
                    ft.Container(content=ft.Icon(Icons.SWAP_HORIZONTAL_CIRCLE_OUTLINED), padding=10)
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            ),
            ft.Row(
                [
                    ft.Container(content=ft.Text("Блок питания"), padding=10),
                    ft.Container(content=ft.Text("Характеристики комплектующей ... рублей"), padding=10),
                    ft.Container(content=ft.Icon(Icons.SWAP_HORIZONTAL_CIRCLE_OUTLINED), padding=10)
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            ),
            ft.Row(
                [
                    ft.Container(content=ft.Text("Корпус"), padding=10),
                    ft.Container(content=ft.Text("Характеристики комплектующей ... рублей"), padding=10),
                    ft.Container(content=ft.Icon(Icons.SWAP_HORIZONTAL_CIRCLE_OUTLINED), padding=10)
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            )
        ]
    )

    # Совместимость комплектующих
    compatibility = ft.Container(
        content=ft.CircleAvatar(radius=50, content=ft.Text("?", size=30)),
        width=150,
        height=150,
        border_radius=50,
        border=ft.border.all(2, ft.colors.BLUE_GREY_300)
    )

    # Итоговая стоимость
    total_cost = ft.Container(
        content=ft.Column(
            [
                ft.Text("Итоговая стоимость ПК", size=18),
                ft.Text("... рублей", size=16)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=5
        ),
        width=300,
        height=150,
        border_radius=10,
        border=ft.border.all(1, ft.colors.GREY_300)
    )

    # Действия
    actions = ft.Row(
        [
            ft.ElevatedButton("Собрать"),
            ft.ElevatedButton("Сохранить сборку"),
            ft.ElevatedButton("Поделиться сборкой")
        ],
        alignment=ft.MainAxisAlignment.END
    )

    # Подписка на новости
    subscription_form = ft.Row(
        [
            ft.Text("Хочу быть в курсе акций и новинок!"),
            ft.TextField(label="Введите адрес электронной почты"),
            ft.ElevatedButton("Подписаться")
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=10
    )

    # Рейтинг и ссылки
    rating_and_links = ft.Row(
        [
            ft.Container(
                content=ft.Row(
                    [
                        ft.Text("4.7"),
                        ft.Icon(Icons.STAR, color=ft.colors.AMBER)
                    ],
                    spacing=5
                ),
                padding=5,
                border_radius=5,
                border=ft.border.all(1, ft.colors.GREY_300)
            ),
            ft.ElevatedButton("Отзывы о сервисе"),
            ft.ElevatedButton("Служба поддержки")
        ],
        alignment=ft.MainAxisAlignment.END,
        spacing=10
    )

    # Главный контейнер
    page.add(
        header,
        ft.Text("Популярные сборки", size=16),
        navigation,
        ft.Text("Сборка 2", size=18),
        ft.Row(
            [
                table,
                ft.Column(
                    [
                        compatibility,
                        total_cost,
                        actions
                    ],
                    spacing=20
                )
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        ),
        subscription_form,
        rating_and_links
    )

# Запуск приложения
ft.app(target=main)