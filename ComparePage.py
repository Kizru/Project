import flet as ft

def main(page: ft.Page):
    page.title = "Сравнение комплектующих"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 20
    
    def go_back(e):
        pass
    
    header = ft.Row(
        controls=[
            ft.Text("Сравнение комплектующих", size=24, weight=ft.FontWeight.BOLD),
            ft.IconButton(
                icon=ft.icons.ARROW_BACK,
                on_click=go_back,
                tooltip="Вернуться на главную"
            )
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        width=page.width
    )
    
    component_type_dropdown = ft.Dropdown(
        label="Выберите комплектующие для сравнения",
        options=[
            ft.dropdown.Option("Процессор"),
            ft.dropdown.Option("Охлаждение"),
            ft.dropdown.Option("SSD"),
        ],
        width=400
    )
    
    component1_dropdown = ft.Dropdown(
        options=[
            ft.dropdown.Option("Вариант 1"),
            ft.dropdown.Option("Вариант 2"),
        ],
        width=200
    )
    
    component2_dropdown = ft.Dropdown(
        options=[
            ft.dropdown.Option("Вариант 1"),
            ft.dropdown.Option("Вариант 2"),
        ],
        width=200
    )
    
    components_row = ft.Row(
        controls=[
            ft.Column(
                controls=[
                    ft.Text("Комплектующее 1", weight=ft.FontWeight.BOLD),
                    component1_dropdown
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=10
            ),
            ft.Column(
                controls=[
                    ft.Text("Комплектующее 2", weight=ft.FontWeight.BOLD),
                    component2_dropdown
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=10
            )
        ],
        spacing=50,
        alignment=ft.MainAxisAlignment.CENTER
    )
    
    compare_button = ft.ElevatedButton(
        text="Сравнить",
        width=200,
        height=50
    )
    
    page.add(
        header,
        ft.Divider(height=20, color=ft.colors.TRANSPARENT),
        component_type_dropdown,
        ft.Divider(height=30, color=ft.colors.TRANSPARENT),
        components_row,
        ft.Divider(height=30, color=ft.colors.TRANSPARENT),
        compare_button
)

ft.app(target=main)