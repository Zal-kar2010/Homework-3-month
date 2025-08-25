port flet as ft
import sqlite3
from datetime import datetime

# Подключение к базе
conn = sqlite3.connect("tasks.db", check_same_thread=False)
cur = conn.cursor()

# Создаём таблицу
cur.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    text TEXT,
    done BOOLEAN,
    created_at TEXT
)
""")
conn.commit()

def main(page: ft.Page):
    page.title = "ToDo"
    task_input = ft.TextField(label="Новая задача", max_length=100, width=250)
    tasks_column = ft.Column()

    # Флаги сортировки
    sort_by_date = True
    sort_done_last = False

    # Загрузка задач
    def load_tasks():
        tasks_column.controls.clear()

        query = "SELECT * FROM tasks ORDER BY "
        if sort_done_last:
            query += "done ASC, "
        else:
            query += "done DESC, "

        if sort_by_date:
            query += "created_at DESC"
        else:
            query += "created_at ASC"

        for task in cur.execute(query).fetchall():
            tasks_column.controls.append(
                ft.Checkbox(
                    label=f"{task[1]} (🕒 {task[3]})",
                    value=bool(task[2]),
                    on_change=lambda e, task_id=task[0]: toggle_done(task_id, e.control.value)
                )
            )
        page.update()

    # Добавление задачи
    def add_task(e):
        if len(task_input.value.strip()) == 0:
            return
        cur.execute("INSERT INTO tasks (text, done, created_at) VALUES (?, ?, ?)",
                    (task_input.value, False, datetime.now().strftime("%Y-%m-%d %H:%M")))
        conn.commit()
        task_input.value = ""
        load_tasks()

    # Переключение выполнена/не выполнена
    def toggle_done(task_id, value):
        cur.execute("UPDATE tasks SET done=? WHERE id=?", (value, task_id))
        conn.commit()
        load_tasks()

    # Переключение сортировки по дате
    def sort_date(e):
        nonlocal sort_by_date
        sort_by_date = not sort_by_date
        load_tasks()

    # Переключение сортировки по статусу
    def sort_status(e):
        nonlocal sort_done_last
        sort_done_last = not sort_done_last
        load_tasks()

    # Интерфейс
    page.add(
        ft.Row([task_input, ft.ElevatedButton("Добавить", on_click=add_task)]),
        ft.Row([
            ft.ElevatedButton("📅 Сортировка по дате", on_click=sort_date),
            ft.ElevatedButton("✅ Сортировка по статусу", on_click=sort_status)
        ]),
        tasks_column
    )

    load_tasks()

ft.app(target=main)
