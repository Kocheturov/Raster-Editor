class TextEffect:
    def __init__(self, type):
        self.type = type
        # ...

    def apply_effect(self, text_box):
        # Применение текстового эффекта к текстовому блоку
        if self.type == "shadow":
            # ... добавить тень
        elif self.type == "outline":
            # ... добавить обводку
        # ...
