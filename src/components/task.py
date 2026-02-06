from dataclasses import field
import flet as ft
from typing import Callable


@ft.control
class Task(ft.Column):

    def __init__(
        self,
        task_name: str = "",
        on_task_delete: Callable[["Task"], None] = field(default=lambda task: None),
    ):
        super().__init__()
        self.task_name = task_name
        self.on_task_delete = on_task_delete
        self.display_task = ft.Checkbox(label=self.task_name.capitalize(), value=False)
        self.edit_name = ft.TextField(expand=1)

        self.display_view = ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                self.display_task,
                ft.Row(
                    spacing=1,
                    controls=[
                        ft.IconButton(
                            icon=ft.Icons.CREATE_OUTLINED,
                            tooltip="Edit task",
                            on_click=self.edit_clicked,
                        ),
                        ft.IconButton(
                            icon=ft.Icons.DELETE_OUTLINE,
                            tooltip="Delete task",
                            on_click=self.delete_clicked,
                        ),
                    ],
                ),
            ],
        )

        self.edit_view = ft.Row(
            visible=False,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                self.edit_name,
                ft.IconButton(
                    icon=ft.Icons.DONE_OUTLINE_OUTLINED,
                    icon_color=ft.Colors.GREEN,
                    tooltip="Save changes",
                    on_click=self.save_clicked,
                ),
            ],
        )

        self.controls = [self.display_view, self.edit_view]

    def edit_clicked(self, _: ft.Event):
        self.edit_name.value = self.display_task.label
        self.display_view.visible = False
        self.edit_view.visible = True
        self.update()

    def delete_clicked(self, _: ft.Event):
        self.on_task_delete(self)

    def save_clicked(self, _: ft.Event):
        self.display_task.label = self.edit_name.value.capitalize()
        self.display_view.visible = True
        self.edit_view.visible = False
        self.update()