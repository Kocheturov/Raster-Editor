class Layer:
    """
    Класс представляет слой изображения с настраиваемым именем, 
    режимом наложения и прозрачностью.
    """

    def __init__(self, name):
        """
        Инициализирует экземпляр Layer.

        Аргументы:
            name (str): Имя слоя.
        """
        self.name = name
        self.blend_mode = "normal"
        self.opacity = 1.0

    def set_blend_mode(self, mode):
        """
        Устанавливает режим наложения для слоя.

        Аргументы:
            mode (str): Режим наложения (например, "normal", "multiply").
        """
        # Установка режима наложения
        self.blend_mode = mode

    def set_opacity(self, opacity):
        """
        Устанавливает прозрачность слоя.

        Аргументы:
            opacity (float): Прозрачность (от 0.0 до 1.0).
        """
        # Установка прозрачности
        self.opacity = opacity
