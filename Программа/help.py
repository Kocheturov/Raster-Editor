class HelpSystem:
    def __init__(self):
        self.help_topics = {
            "tools": "Information about available tools",
            "layers": "How to work with layers",
            # ...
        }

    def display_help(self, topic):
        # Отображение справки по заданной теме
        if topic in self.help_topics:
            print(self.help_topics[topic])
        else:
            print("Help topic not found")
