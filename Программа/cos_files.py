class FileManager:
    """
    Класс для управления файлами, включая открытие, сохранение, 
    проверку поддерживаемых форматов, импорт и экспорт изображений.
    """

    def __init__(self):
        """
        Инициализирует экземпляр FileManager с заданным списком 
        поддерживаемых форматов файлов.
        """
        self.supported_formats = ["PSD", "TIFF", "JPEG", "PNG"]

    def open_file(self, filename):
        """
        Открывает файл изображения.

        Аргументы:
            filename (str): Имя файла изображения.

        Вызывает:
            ValueError: Если формат файла не поддерживается.
        """
        # Проверка формата файла
        if not self.is_supported_format(filename):
            raise ValueError("Unsupported file format")

        # Открытие файла в зависимости от формата
        if filename.endswith(".psd"):
            # ... открыть PSD файл
        elif filename.endswith(".tiff"):
            # ... открыть TIFF файл
        # ...

    def save_file(self, filename, format):
        """
        Сохраняет файл изображения в заданном формате.

        Аргументы:
            filename (str): Имя файла для сохранения.
            format (str): Формат файла для сохранения.

        Вызывает:
            ValueError: Если формат файла не поддерживается.
        """
        # Проверка формата файла
        if format not in self.supported_formats:
            raise ValueError("Unsupported file format")

        # Сохранение файла в зависимости от формата
        if format == "PSD":
            # ... сохранить как PSD файл
        elif format == "TIFF":
            # ... сохранить как TIFF файл
        # ...

    def is_supported_format(self, filename):
        """
        Проверяет, поддерживается ли формат файла.

        Аргументы:
            filename (str): Имя файла для проверки.

        Возвращает:
            bool: True, если формат поддерживается, False - иначе.
        """
        # Проверка, поддерживается ли формат файла
        for format in self.supported_formats:
            if filename.endswith(f".{format.lower()}"):
                return True
        return False
