class DrawingTool:
    def __init__(self, type):
        self.type = type
        # ... другие параметры, например, размер, цвет, форма

    def activate(self):
        # Активация инструмента
        # ...

    def deactivate(self):
        # Деактивация инструмента
        # ...

    def handle_input(self, event):
        # Обработка ввода пользователя (нажатие, перемещение мыши)
        if self.type == "brush":
            # ... рисование кистью
        elif self.type == "pencil":
            # ... рисование карандашом
        # ...
