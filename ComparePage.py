import flet as ft
from flet.core.icons import Icons
import requests

#
#font_family = "Roboto"

def turnToPage(e):
    pass

def main(page: ft.Page):
    def dropdown_changed(e):
        page.show_snack_bar(ft.SnackBar(ft.Text(f"Выбрано: {e.control.value}")))

    page.title = "Сравнение комплектующих"
    page.update()

    firstText = ft.Text("Сравнение комплектующих", size=20)
    secondButton = ft.ElevatedButton(text="Конфигуратор ПК")

    page.add(
        ft.Row([firstText, secondButton], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
    )

    page.add(
        ft.Row([ft.Text("Выберете комплектующие для сравнения", size=16)])
    )

    firstFrame = ft.ElevatedButton(text="Процессор")
    secondFrame = ft.ElevatedButton(text="Охлаждение")
    thirdFrame = ft.ElevatedButton(text="SSD")

    page.add(
        ft.Row(controls=[firstFrame, secondFrame, thirdFrame], spacing=20)
    )

    page.add(
        ft.Row(spacing=25)
    )

    page.add(
        ft.Divider(height=1, thickness=2, color="black")
    )

    firstProcessor = ft.Container(content=ft.Text("Процессор 1", size=18), border=ft.border.all(2, "black"), padding=10, margin=ft.margin.only(left=300))
    secondProcessor = ft.Container(content=ft.Text("Процессор 2", size=18), border=ft.border.all(2, "black"), padding=10, margin=ft.margin.only(right=50))

    page.add(
        ft.Row(controls=[firstProcessor, secondProcessor], spacing=350)
    )

    firstDropdownContainer = ft.Container(content = ft.Dropdown(
        options=[
            ft.dropdown.Option("option1", "Вариант 1"),
            ft.dropdown.Option("option2", "Вариант 2"),
        ],
        width=200,
        on_change=dropdown_changed,
    ), margin=ft.margin.only(left=270))

    secondDropdownContainer = ft.Container(content = ft.Dropdown(
        options=[
            ft.dropdown.Option("option1", "Вариант 1"),
            ft.dropdown.Option("option2", "Вариант 2"),
        ],
        width=200,
        on_change=dropdown_changed,
    ))

    page.add(
        ft.Row(controls=[firstDropdownContainer, secondDropdownContainer], spacing=280)
    )

    button = ft.Container(
        content=ft.ElevatedButton(
            text="Сравнить",
            width=200, 
            height=60,
            style=ft.ButtonStyle(
                padding=ft.padding.symmetric(horizontal=20, vertical=15), 
                overlay_color=ft.colors.with_opacity(0.2, "blue"),
                animation_duration=300,
            ),
        ),
        alignment=ft.alignment.center)
    page.add(button)

ft.app(target=main, view = ft.AppView.FLET_APP)
