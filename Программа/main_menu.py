class MainMenu:
    """
    Класс представляет главное меню приложения, отображающее 
    доступные пункты меню и обрабатывающее выбор пользователя.
    """

    def __init__(self):
        """
        Инициализирует экземпляр MainMenu со словарем пунктов меню.
        """
        self.menu_items = {
            "File": ["New", "Open", "Save", "Exit"],
            "Edit": ["Undo", "Redo", "Cut", "Copy", "Paste"],
            "Image": ["Adjustments", "Filters", "Layers"],
            "Help": ["About"]
        }

    def display_menu(self):
        """
        Отображает пункты меню на экране.
        """
        # Отображение пунктов меню
        for menu_name, items in self.menu_items.items():
            print(f"{menu_name}:")
            for item in items:
                print(f"\t- {item}")

    def handle_menu_selection(self, selection):
        """
        Обрабатывает выбор пункта меню пользователем.

        Аргументы:
            selection (str): Выбранный пункт меню.
        """
        # Обработка выбора пункта меню
        # ...
