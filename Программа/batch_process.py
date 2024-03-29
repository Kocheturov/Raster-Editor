class AutomationManager:
    def __init__(self):
        # ...

    def batch_process_images(self, image_filenames, actions):
        # Пакетная обработка изображений
        for filename in image_filenames:
            image = self.open_image(filename)
            for action in actions:
                self.run_action(action, image)
            self.save_image(image, filename)
