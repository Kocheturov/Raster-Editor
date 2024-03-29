class SelectionTool:
    def __init__(self, type):
        self.type = type
        # ...

    def activate(self):
        # Активация инструмента выделения
        # ...

    def deactivate(self):
        # Деактивация инструмента выделения
        # ...

    def handle_input(self, event):
        # Обработка ввода пользователя для создания выделения
        if self.type == "rectangle":
            # ... прямоугольное выделение
        elif self.type == "ellipse":
            # ... овальное выделение
        # ...
