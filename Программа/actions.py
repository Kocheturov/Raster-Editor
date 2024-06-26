class AutomationManager:
    """
    Класс для управления задачами автоматизации, включая пакетную обработку 
    изображений, запись и выполнение пользовательских действий.
    """

    # ... (метод batch_process_images)

    def record_action(self):
        """
        Начинает запись пользовательского действия. 
        Последующие действия, выполняемые пользователем, будут 
        записываться до вызова метода `stop_recording`.
        """
        # Начать запись операции
        # ...

    def stop_recording(self):
        """
        Останавливает запись текущего пользовательского действия.
        """
        # Остановить запись операции
        # ...

    def run_action(self, action_name, image):
        """
        Выполняет ранее записанное действие над предоставленным изображением.

        Аргументы:
            action_name (str): Имя, присвоенное записанному действию.
            image (Image): Объект изображения, к которому должно быть 
                          применено действие.
        """
        # Запуск записанной операции
        # ...
