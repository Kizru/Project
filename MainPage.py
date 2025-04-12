import flet as ft
from flet.core.icons import Icons
import requests

def main(page: ft.Page):
    page.title = "Конфигуратор ПК"
    page.theme_mode = 'light'
    page.update()

    def changeTheme(e):
        page.theme_mode = 'light' if page.theme_mode == 'dark' else 'dark'
        page.update()

    page.add(
    # Главный контейнер для размещения элементов
    ft.Column(
        [
            # Первая строка с кнопкой
            ft.Row(
                [
                    ft.Text("Конфигуратор ПК", size=24, font_family="Roboto"),
                    ft.IconButton(Icons.SUNNY, on_click=changeTheme),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN  # Разносим текст и кнопку по краям
            ),

            # Пропуск строки
            ft.Container(height=5),

            # Вторая строка
            ft.Row(
                [
                    ft.Text("Популярные сборки", size=16, font_family="Roboto"),

                    # Вложенный Row для кнопок
                    ft.Row(
                        [
                            ft.ElevatedButton(text="Сохраненные сборки"),
                            ft.ElevatedButton(text="Сравнение комплектующих"),
                        ],
                        alignment=ft.MainAxisAlignment.END  # Выравниваем кнопки вправо
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN  # Разносим текст и кнопки по краям
            ),

            # Пропуск строки
            ft.Container(height=2),

            # Третья строка
            ft.Row(
                [
                    ft.ElevatedButton(text="Все"),
                    ft.ElevatedButton(text="Офисные"),
                    ft.ElevatedButton(text="Игровые"),
                ]
            )
        ],
        expand=True  # Разрешаем Column занимать всё доступное пространство
    )
)
# Запускаем приложение
ft.app(target=main, view = ft.AppView.FLET_APP)