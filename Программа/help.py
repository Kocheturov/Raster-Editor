class HelpSystem:
    """
    Класс представляет систему справки, предоставляющую информацию по 
    различным темам.
    """

    def __init__(self):
        """
        Инициализирует экземпляр HelpSystem со словарем тем справки.
        """
        self.help_topics = {
            "tools": "Information about available tools",
            "layers": "How to work with layers",
            # ...
        }

    def display_help(self, topic):
        """
        Отображает справку по заданной теме.

        Аргументы:
            topic (str): Тема справки для отображения.
        """
        # Отображение справки по заданной теме
        if topic in self.help_topics:
            print(self.help_topics[topic])
        else:
            print("Help topic not found")
