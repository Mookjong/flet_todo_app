from flet import (
    Event,
    Page,
    TextField,
    run,
    Checkbox,
    Column,
    Row,
)


from components.floating_btn import FloatingBtn

def add_clicked(e: Event, page: Page, new_task: TextField):
    if new_task.value == "":
        return
    page.add(Checkbox(label=new_task.value.capitalize()))
    new_task.value = ""
    page.update()


def main(page: Page):
    page.title = "Hello, Flet!"

    new_task = TextField(label="What needs to be done?", expand=True)

    tasks_view = Column()

    view = Column(
        width=800,
        controls=[
            Row(
                controls=[
                    new_task,
                    FloatingBtn(handle_click=lambda e: add_clicked(e, page, new_task)),
                ]
            ),
            tasks_view,
        ],
    )

    page.add(view)


run(main)
