import flet as ft
from datetime import datetime


def main(page: ft.Page):
    page.title = "Моё первое приложение"
    page.window_width = 400
    page.window_height = 600
    page.vertical_alignment = ft.MainAxisAlignment.START

    name_field = ft.TextField(label="Введите ваше имя:")
    history = ft.Column()

    def greet(e):
        name = name_field.value.strip()
        if not name:
            return

        now = datetime.now()
        hour = now.hour

        if 6 <= hour < 12:
            greeting = "Доброе утро"
        elif 12 <= hour < 18:
            greeting = "Добрый день"
        elif 18 <= hour < 24:
            greeting = "Добрый вечер"
        else:
            greeting = "Доброй ночи"

        # Показываем уведомление
        page.snack_bar = ft.SnackBar(ft.Text(f"{greeting}, {name}!"))
        page.snack_bar.open = True

        # Добавляем запись в историю
        history.controls.append(
            ft.Text(f"{now.strftime('%Y-%m-%d %H:%M:%S')} → {greeting}, {name}!")
        )
        page.update()

    def clear_history(e):
        history.controls.clear()
        page.update()

    page.add(
        ft.Text("Моё первое приложение", size=20, weight="bold"),
        name_field,
        ft.Row(
            [
                ft.ElevatedButton("Поздороваться", on_click=greet),
                ft.ElevatedButton("Очистить историю", on_click=clear_history, color="red"),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        ),
        ft.Text("История приветствий:", size=16, weight="bold"),
        history,
    )

ft.app(target=main)