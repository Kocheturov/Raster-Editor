class TextTool:
    """
    Класс TextTool предназначен для работы с текстовыми блоками.
    """

    def __init__(self):
        """
        Инициализирует экземпляр TextTool без активного текстового блока.
        """
        self.active_text_box = None

    def add_text(self, text, position):
        """
        Создает новый текстовый блок с заданным текстом и позицией.

        Аргументы:
            text (str): Текст для нового текстового блока.
            position (tuple): Позиция нового текстового блока (x, y).

        Возвращает:
            TextBox: Созданный текстовый блок.
        """
        text_box = TextBox(text, position)
        self.active_text_box = text_box
        return text_box

    def edit_text(self, text):
        """
        Редактирует текст активного текстового блока.

        Аргументы:
            text (str): Новый текст для активного текстового блока.
        """
        # 
        if self.active_text_box:
            self.active_text_box.text = text

    def handle_input(self, event):
        """
        Обрабатывает ввод пользователя для редактирования текста в 
        активном текстовом блоке.

        Аргументы:
            event (Event): Событие ввода пользователя для обработки.
        """
        if self.active_text_box:
            # ...
