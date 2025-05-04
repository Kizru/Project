import flet as ft

def main(page: ft.Page):
    # Настройка страницы
    page.title = "Конфигуратор ПК"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 20
    page.spacing = 10
    page.window_width = 800  # Фиксированный размер окна по ширине
    page.window_height = 600  # Фиксированный размер окна по высоте
    page.bgcolor = "#F0F0F0"  # Однородный фон для всего приложения

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
                
                # Первая секция - сохраненные сборки
                ft.Row(
                    [
                        ft.Text("Сохраненные сборки", size=16),
                        ft.ElevatedButton("Назад"),  # Кнопка "Назад"
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
                
                # Третья секция - карточки компьютеров
                ft.Container(
                    content=ft.Row(
                        [
                            ft.Container(
                                content=ft.Text(f"Компьютер {i}", size=14),
                                width=100,
                                height=100,
                                bgcolor="#ADD8E6",
                                border_radius=5,
                                alignment=ft.alignment.center,
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