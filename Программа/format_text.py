class TextBox:
    def __init__(self, text, position):
        self.text = text
        self.position = position
        self.font_family = "Arial"
        self.font_size = 12
        self.color = (0, 0, 0)
        # ... другие параметры форматирования

    def set_font_family(self, font_family):
        # Установка семейства шрифтов
        self.font_family = font_family

    def set_font_size(self, font_size):
        # Установка размера шрифта
        self.font_size = font_size

    # ... другие методы для форматирования текста

    def transform(self, type, **kwargs):
        # Трансформация текстового блока (поворот, масштабирование)
        # ...
