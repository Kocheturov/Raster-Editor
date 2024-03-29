class Toolbar:
    def __init__(self):
        self.tools = {
            "brush": {"icon": "brush.png", "action": self.activate_brush},
            "eraser": {"icon": "eraser.png", "action": self.activate_eraser},
            # ...
        }

    def display_toolbar(self):
        # Отображение кнопок инструментов
        for tool_name, data in self.tools.items():
            # ...

    def activate_brush(self):
        # Активация инструмента "Кисть"
        # ...

    # ... другие методы для инструментов
