from flet import (
    Event,
    Text,
    FloatingActionButton,
    Page,
    Icons,
    TextField,
    run,
    Checkbox,
    Column,
    Row,
)


def add_clicked(e: Event, page: Page, new_task: TextField):
    if new_task.value == "":
        return
    page.add(Checkbox(label=new_task.value.capitalize()))
    new_task.value = ""
    page.update()


def darken_color(color: str, amount: float) -> str:
    color = color.lstrip("#")
    r: int = int(color[0:2], 16)
    g: int = int(color[2:4], 16)
    b: int = int(color[4:6], 16)

    r: int = max(0, min(255, int(r * (1 - amount))))
    g: int = max(0, min(255, int(g * (1 - amount))))
    b: int = max(0, min(255, int(b * (1 - amount))))

    return f"#{r:02x}{g:02x}{b:02x}"


def FloatingBtn(handle_click) -> FloatingActionButton:
    button = FloatingActionButton(
        icon=Icons.ADD,
        on_click=handle_click,
        focus_color=darken_color("#D2BEF0", 0.2),
        bgcolor="#D2BEF0",
        elevation=5,
    )
    return button


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
