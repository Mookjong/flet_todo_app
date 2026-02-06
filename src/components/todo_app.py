from components.floating_btn import FloatingBtn
from components.task import Task
import flet as ft
from flet import (
    Event,
    TextField,
    Checkbox,
    Column,
    Row,
)

@ft.control
class TodoApp(Column):

    def __init__(self):
        super().__init__()
        self.new_task = TextField(label="What needs to be done?", expand=True)
        self.tasks = Column()

        self.controls = [
            Row(
                controls=[
                    self.new_task,
                    FloatingBtn(handle_click=self.add_clicked),
                ]
            ),
            self.tasks,
        ]

    def add_clicked(self, _: Event):
        if self.new_task.value == "":
            return
        
        task = Task(task_name=self.new_task.value, on_task_delete=self.delete_task)        
        self.tasks.controls.append(task)
        self.new_task.value = ""
        self.update()
        
        
    def delete_task(self, task: Task):
        self.tasks.controls.remove(task)
        self.update()