class FileManager:
    # ... (методы open_file, save_file, is_supported_format)

    def import_image(self, filename):
        """
        Импортирует изображение из файла.

        Аргументы:
            filename (str): Имя файла изображения.

        Возвращает:
            Image: Объект изображения.
        """
        # Открытие файла изображения
        image = self.open_file(filename)

        # Преобразование изображения в нужный формат (если необходимо)
        # ...

        return image

    def export_image(self, image, filename, format):
        """
        Экспортирует изображение в файл с заданным именем и форматом.

        Аргументы:
            image (Image): Объект изображения.
            filename (str): Имя файла для экспорта.
            format (str): Формат файла для экспорта.
        """
        # Преобразование изображения в формат экспорта (если необходимо)
        # ...

        # Сохранение изображения
        self.save_file(filename, format)
