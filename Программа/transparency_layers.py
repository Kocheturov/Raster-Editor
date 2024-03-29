class Layer:
    def __init__(self, name):
        self.name = name
        self.blend_mode = "normal"
        self.opacity = 1.0

    def set_blend_mode(self, mode):
        # Установка режима наложения
        self.blend_mode = mode

    def set_opacity(self, opacity):
        # Установка прозрачности
        self.opacity = opacity
