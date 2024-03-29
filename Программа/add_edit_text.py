class TextTool:
    """
    Класс TextTool
    """
    def __init__(self):
        self.active_text_box = None

    def add_text(self, text, position):
        """Создание нового текстового блока

        Args:
          text: string.
          position: int.
    
        Returns:
          Text box.
        """
        text_box = TextBox(text, position)
        self.active_text_box = text_box
        return text_box

    def edit_text(self, text):
        """Редактирование активного текстового блока

        Args:
          text: string.
    
        """
        # 
        if self.active_text_box:
            self.active_text_box.text = text

    def handle_input(self, event):
        """Обработка ввода пользователя для редактирования текста

        Args:
          event: event.

        """
        if self.active_text_box:
            # ...
