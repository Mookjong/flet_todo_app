from utils.functions import darken_color
from flet import FloatingActionButton, Icons

def FloatingBtn(handle_click) -> FloatingActionButton:
    button = FloatingActionButton(
        icon=Icons.ADD,
        on_click=handle_click,
        focus_color=darken_color("#D2BEF0", 0.2),
        bgcolor="#D2BEF0",
        elevation=5
    )
    return button



if __name__ == "__main__":
    print(darken_color("#D2BEF0", 0.2))