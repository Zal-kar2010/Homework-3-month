import flet as ft


def main(page: ft.Page): 
    page.title = "Моё первое приложение на flet"

    greeting_text = ft.Text(f"привет, мир")

    page.theme_mode = ft.ThemeMode.LIGHT

    name_input = ft.TextField(label='Веедите имя')

    def on_button_clik(_):
        name = name_input.value.strip()
        print(name)

        if name:
            greeting_text.value = f'Привет, {name}'
        else:
            greeting_text.value = f'Привет, {name}'

             
    page.update()

    greet_button = ft.ElevatedButton('Send', on_click=on_button_clik)    


    page.add(greeting_text, name_input, greet_button)



#ft.app(target=main)    
ft.app(target=main, view=ft.WEB_BROWSER)