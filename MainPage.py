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
    page.theme_mode = ft.ThemeMode.LIGHT  # Установка темы
    page.bgcolor = "#E0E0E0"  # Серый фон для всего приложения

    # Создаем компонент для рейтинга
    def create_rating(rating_value):
        stars = []
        for i in range(5):
            if i < rating_value:
                stars.append(ft.Icon(ft.icons.STAR, color="orange"))
            else:
                stars.append(ft.Icon(ft.icons.STAR_BORDER, color="grey"))
        return ft.Row(stars, spacing=2)

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
                
                # Пятая секция - рейтинг и ссылки
                ft.Row(
                    [
                        create_rating(4.7),  # Создаем рейтинг 4.7 звезд
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

# Запуск приложения
ft.app(target=main)