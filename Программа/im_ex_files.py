class FileManager:
    # ... (методы open_file, save_file, is_supported_format)

    def import_image(self, filename):
        # Открытие файла изображения
        image = self.open_file(filename)

        # Преобразование изображения в нужный формат (если необходимо)
        # ...

        return image

    def export_image(self, image, filename, format):
        # Преобразование изображения в формат экспорта (если необходимо)
        # ...

        # Сохранение изображения
        self.save_file(filename, format)
