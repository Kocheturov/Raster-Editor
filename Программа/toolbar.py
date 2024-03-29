class Toolbar:
    """
    Класс представляет панель инструментов, отображающую кнопки 
    инструментов и обрабатывающую их выбор.
    """

    def __init__(self):
        """
        Инициализирует экземпляр Toolbar со словарем инструментов, 
        содержащим информацию об иконках и действиях.
        """
        self.tools = {
            "brush": {"icon": "brush.png", "action": self.activate_brush},
            "eraser": {"icon": "eraser.png", "action": self.activate_eraser},
            # ...
        }

    def display_toolbar(self):
        """
        Отображает кнопки инструментов на экране.
        """
        # Отображение кнопок инструментов
        for tool_name, data in self.tools.items():
            # ...

    def activate_brush(self):
        """
        Активирует инструмент "Кисть".
        """
        # Активация инструмента "Кисть"
        # ...

    # ... другие методы для инструментов
