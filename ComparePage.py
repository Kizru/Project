import flet as ft

def main(page: ft.Page):
    page.title = "Сравнение комплектующих"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 20
    
    def go_back(e):
        pass
    
    component_options = {
        "Процессор": ["AMD Ryzen 7 7800X3D", "Intel Core i9-13900K"],
        "Охлаждение": ["Noctua NH-D15", "NZXT Kraken X73"],
        "SSD": ["Samsung 990 Pro", "Samsung 980 Pro"]
    }
    
    def update_component_fields(e):
        selected_type = component_type_dropdown.value
        if selected_type:
            components_row.controls[0].controls[0].value = f"{selected_type} 1"
            components_row.controls[1].controls[0].value = f"{selected_type} 2"
            
            options = component_options.get(selected_type, [])
            component1_dropdown.options = [ft.dropdown.Option(opt) for opt in options]
            component2_dropdown.options = [ft.dropdown.Option(opt) for opt in options]
            
            if options:
                component1_dropdown.value = options[0]
                component2_dropdown.value = options[1] if len(options) > 1 else options[0]
            
            page.update()
    
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
        width=400,
        on_change=update_component_fields
    )
    
    component1_dropdown = ft.Dropdown(
        width=200
    )
    
    component2_dropdown = ft.Dropdown(
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