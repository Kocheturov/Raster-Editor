class FileManager:
    def __init__(self):
        self.supported_formats = ["PSD", "TIFF", "JPEG", "PNG"]

    def open_file(self, filename):
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
        # Проверка, поддерживается ли формат файла
        for format in self.supported_formats:
            if filename.endswith(f".{format.lower()}"):
                return True
        return False
