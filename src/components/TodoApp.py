from components.floating_btn import FloatingBtn
from flet import (
    Event,
    Page,
    TextField,
    Checkbox,
    Column,
    Row,
)

class TodoApp(Column):

    def __init__(self):
        super().__init__()
        self.new_task = TextField(label="What needs to be done?", expand=True)
        self.tasks_view = Column()

        self.controls = [
            Row(
                controls=[
                    self.new_task,
                    FloatingBtn(handle_click=self.add_clicked),
                ]
            ),
            self.tasks_view,
        ]

    def add_clicked(self, _: Event):
        if self.new_task.value == "":
            return
        self.tasks_view.controls.append(
            Checkbox(label=self.new_task.value.capitalize())
        )
        self.new_task.value = ""
        self.update()