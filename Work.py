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

        #смена темы
        ft.Row([ft.IconButton(Icons.SUNNY, on_click = changeTheme)], alignment = ft.MainAxisAlignment.START), 

        ft.Row([ft.Text("Конфигуратор ПК")], alignment = ft.MainAxisAlignment.CENTER) 
    )

# Запускаем приложение
ft.app(target=main, view = ft.AppView.FLET_APP)