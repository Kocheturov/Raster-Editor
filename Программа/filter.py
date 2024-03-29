class Filter:
    def __init__(self, type):
        self.type = type
        # ...

    def apply_filter(self, image):
        # Применение фильтра к изображению
        if self.type == "blur":
            # ... размытие изображения
        elif self.type == "sharpen":
            # ... повышение резкости изображения
        # ...
