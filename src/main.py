from flet import run, Page

from components.TodoApp import TodoApp


def main(page: Page):
    page.title = "To-Do List App"

    todo_app = TodoApp()

    page.add(todo_app)


run(main)
