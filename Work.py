import flet as ft
from flet.core.icons import Icons
import requests

def main(page: ft.Page):
    page.title = "Сборка ПК"
    page.theme_mode = 'light'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = 'light' if page.theme_mode == 'dark' else 'dark'
    page.update()

    page.add(

    )

# Запускаем приложение
ft.app(target=main, view = ft.AppView.FLET_APP)