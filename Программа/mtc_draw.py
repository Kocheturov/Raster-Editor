class TransformTool:
    def __init__(self, type):
        self.type = type
        # ...

    def activate(self):
        # Активация инструмента трансформации
        # ...

    def deactivate(self):
        # Деактивация инструмента трансформации
        # ...

    def handle_input(self, event):
        # Обработка ввода пользователя для трансформации
        if self.type == "move":
            # ... перемещение
        elif self.type == "scale":
            # ... масштабирование
        # ...
