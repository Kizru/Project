import flet as ft

def main(page: ft.Page):
    page.title = "Служба поддержки"
    page.horizontal_alignment = "center"
    page.scroll = "adaptive"

    message_display = ft.Text("", color=ft.colors.RED, size=14)
    
    def go_home(e):
        pass
    
    header = ft.Row(
        controls=[
            ft.Text("Служба поддержки", size=24, weight="bold"),
            ft.IconButton(
                icon=ft.icons.ARROW_BACK,
                tooltip="Вернуться на главную",
                on_click=go_home
            ),
        ],
        alignment="spaceBetween",
        width=page.width
    )
    
    faq_title = ft.Text("Часто задаваемые вопросы", size=20, weight="bold")
    
    faq_items = ft.Column(
        controls=[
            ft.ExpansionTile(
                title=ft.Text("Как связаться с поддержкой?"),
                controls=[
                    ft.ListTile(title=ft.Text("Используйте форму ниже или контактные данные в конце страницы."))
                ]
            ),
            ft.ExpansionTile(
                title=ft.Text("Какие часы работы у поддержки?"),
                controls=[
                    ft.ListTile(title=ft.Text("Мы работаем 24/7."))
                ]
            ),
        ],
        spacing=10
    )
    
    form_title = ft.Text("Форма обращения в поддержку", size=20, weight="bold")
    
    name_field = ft.TextField(label="Ваше имя", width=400)
    email_field = ft.TextField(label="Ваш email для связи", width=400)
    issue_field = ft.TextField(label="Тема проблемы", width=400)
    message_field = ft.TextField(
        label="Опишите Вашу проблему", 
        multiline=True, 
        min_lines=1,
        width=400
    )
    
    def submit_form(e):
        if not name_field.value:
            message_display.value = "Вы заполнили не все поля!"
            message_display.color = ft.colors.RED
            page.update()
            return
        if not email_field.value:
            message_display.value = "Вы заполнили не все поля!"
            message_display.color = ft.colors.RED
            page.update()
            return
        if not issue_field.value:
            message_display.value = "Вы заполнили не все поля!"
            message_display.color = ft.colors.RED
            page.update()
            return
        if not message_field.value:
            message_display.value = "Вы заполнили не все поля!"
            message_display.color = ft.colors.RED
            page.update()
            return
            
        # Здесь должна быть реальная отправка формы
        print(f"Отправлено: {name_field.value}, {email_field.value}")
        
        message_display.value = "Заявка успешно отправлена! Ожидайте ответ от техподдержки"
        message_display.color = ft.colors.GREEN
        
        name_field.value = ""
        email_field.value = ""
        issue_field.value = ""
        message_field.value = ""
        page.update()
    
    submit_button = ft.ElevatedButton(
        "Отправить", 
        on_click=submit_form,
        width=400
    )
    
    contacts_title = ft.Text("Контактная информация", size=20, weight="bold")
    
    contacts_content = ft.Column(
        controls=[
            ft.ListTile(
                leading=ft.Icon(ft.icons.PHONE),
                title=ft.Text("Телефон: ")
            ),
            ft.ListTile(
                leading=ft.Icon(ft.icons.EMAIL),
                title=ft.Text("Email: ")
            ),
        ],
        spacing=5
    )

    page.add(
        header,
        ft.Divider(),
        faq_title,
        faq_items,
        ft.Divider(),
        form_title,
        name_field,
        email_field,
        issue_field,
        message_field,
        message_display,
        submit_button,
        ft.Divider(),
        contacts_title,
        contacts_content
    )

ft.app(target=main)