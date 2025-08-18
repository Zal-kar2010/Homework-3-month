import flet as ft 


def main(page: ft.Page):
    page.title = "Мое первое приложение на Flet!"
    greeting_text = ft.Text("Привет, мир!")

    page.theme_mode = ft.ThemeMode.LIGHT

    greeting_history = []

    name_input = ft.TextField(label='Введите имя')

    def update_history_view():
        history_controls = [ft.Text("История приветствий:", size="bodyMedium")]
        for idx, name in enumerate(greeting_history):
            history_controls.append(
                ft.Row([ft.Text(name), 
                        ft.IconButton(icon=ft.Icons.CLOSE, on_click=lambda e, i=idx: remove_name_from_history(i))
                        ])
            )
            history_column.controls = history_controls
            page.update()

    def remove_name_from_history(index):
        if 0 <= index < len(greeting_history):
            del greeting_history[index]
            update_history_view()

    def on_button_click(_):
        name = name_input.value.strip()
        print(name)

        # greeting_text = ft.Text(f'Привет, {name}')

        if name:
            greeting_text.value = f'Привет, {name}'
            greeting_history.append(name)
            update_history_view()
        else:
            greeting_text.value = "Пожалуйста, введите имя!"


        page.update()

    def toggle_theme(_):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
        page.update()


    greet_button = ft.ElevatedButton('send', on_click=on_button_click)
    greet_button_text = ft.TextButton('send', on_click=on_button_click)

    greet_button_icon = ft.IconButton(
        icon=ft.Icons.SEND, tooltip='Отправить', on_click=on_button_click, icon_color=ft.Colors.GREEN)
    
    theme_button = ft.IconButton(icon=ft.Icons.BRIGHTNESS_7, on_click=toggle_theme)
    
    history_column = ft.Column([])
    update_history_view()



    # page.add(greeting_text, name_input, greet_button, history_column)

    # page.add(ft.Column([greeting_text, name_input, greet_button, history_column], alignment=ft.MainAxisAlignment.CENTER))

    page.add(ft.Column(controls=[
        ft.Row([theme_button, name_input, greet_button], alignment=ft.MainAxisAlignment.CENTER), 
        greeting_text, history_column], alignment=ft.MainAxisAlignment.CENTER))


# ft.app(target=main)
ft.app(target=main, view=ft.WEB_BROWSER)