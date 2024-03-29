class CorrectionTool:
    def __init__(self, type):
        self.type = type
        # ...

    def apply_correction(self, image, value):
        # Применение коррекции к изображению
        if self.type == "brightness":
            # ... изменить яркость
        elif self.type == "contrast":
            # ... изменить контраст
        # ...
