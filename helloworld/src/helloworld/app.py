import toga
from toga.style import Pack
from toga.style.pack import COLUMN, CENTER

from .voice_chat import connect_user , disconnect_user


class ToggleButtonApp(toga.App):
    def startup(self):
        # Create the main window
        self.main_window = toga.MainWindow(title='better call erfan')

        # Define button styles
        green_button_style = Pack(
            flex=1,
            padding=10,
            font_size=18,
            color='white',
            background_color='#4CAF50',  # Hex code for green
            alignment=CENTER,
        )

        red_button_style = Pack(
            flex=1,
            padding=10,
            font_size=18,
            color='white',
            background_color='#F44336',  # Hex code for red
            alignment=CENTER,
        )

        # Create buttons
        self.green_button = toga.Button(
            'Call',
            on_press=self.green_button_action,
            style=green_button_style,
        )

        self.red_button = toga.Button(
            'Cancel',
            on_press=self.red_button_action,
            style=red_button_style,
        )

        # Initially, only the green button is visible
        self.red_button.style.visibility = 'hidden'

        # Create a box to hold the buttons
        box = toga.Box(
            children=[self.green_button, self.red_button],
            style=Pack(direction=COLUMN, alignment=CENTER, padding=20)
        )

        # Add the box to the main window
        self.main_window.content = box
        self.main_window.show()

    
    def green_button_action(self, widget):
        self.green_button.style.visibility = 'hidden'
        self.red_button.style.visibility = 'visible'
        connect_user()

    def red_button_action(self, widget):
        if disconnect_user():
            self.green_button.style.visibility = 'visible'
            self.red_button.style.visibility = 'hidden'
        else:
            self.main_window.info_dialog(
            "مشکل!",
            "چی شده؟",
            )
        


def main():
    return ToggleButtonApp('Toggle Button App', 'com.example.togglebutton')


if __name__ == '__main__':
    app = main()
    app.main_loop()
