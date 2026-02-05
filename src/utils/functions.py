def darken_color(color: str, amount: float) -> str:
    color = color.lstrip("#")
    r: int = int(color[0:2], 16)
    g: int = int(color[2:4], 16)
    b: int = int(color[4:6], 16)

    r: int = max(0, min(255, int(r * (1 - amount))))
    g: int = max(0, min(255, int(g * (1 - amount))))
    b: int = max(0, min(255, int(b * (1 - amount))))

    return f"#{r:02x}{g:02x}{b:02x}"