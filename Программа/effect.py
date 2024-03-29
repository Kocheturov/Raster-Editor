class Effect:
    def __init__(self, type):
        self.type = type
        # ...

    def apply_effect(self, image):
        # Применение эффекта к изображению
        if self.type == "shadow":
            # ... добавить тень к изображению
        elif self.type == "glow":
            # ... добавить свечение к изображению
        # ...
