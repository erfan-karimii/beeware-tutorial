"""
My first application
"""

import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class HelloWorld(toga.App):
    def startup(self):
        main_box = toga.Box(style=Pack(direction=COLUMN))

        name_box = toga.Box(style=Pack(direction=ROW, padding=5))

        button = toga.Button(
            "Say Hello!",
            on_press=self.say_hello,
            style=Pack(padding=5),
        )

        main_box.add(name_box)
        main_box.add(button)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def say_hello(self, widget):
        self.main_window.info_dialog(
            f"Hello",
            "Hi there!",
        )


def main():
    return HelloWorld()
