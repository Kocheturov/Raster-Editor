class MainMenu:
    def __init__(self):
        self.menu_items = {
            "File": ["New", "Open", "Save", "Exit"],
            "Edit": ["Undo", "Redo", "Cut", "Copy", "Paste"],
            "Image": ["Adjustments", "Filters", "Layers"],
            "Help": ["About"]
        }

    def display_menu(self):
        # Отображение пунктов меню
        for menu_name, items in self.menu_items.items():
            print(f"{menu_name}:")
            for item in items:
                print(f"\t- {item}")

    def handle_menu_selection(self, selection):
        # Обработка выбора пункта меню
        # ...
