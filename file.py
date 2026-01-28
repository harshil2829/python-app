from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class Calculator(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.orientation = "vertical"

        self.display = TextInput(
            font_size=40,
            readonly=True,
            halign="right",
            size_hint_y=0.2
        )

        self.add_widget(self.display)

        buttons = [
            "7","8","9","/",
            "4","5","6","*",
            "1","2","3","-",
            "0",".","=","+"
        ]

        grid = BoxLayout()
        grid.orientation = "vertical"

        row = None
        count = 0

        for b in buttons:
            if count % 4 == 0:
                row = BoxLayout()
                grid.add_widget(row)

            btn = Button(
                text=b,
                font_size=30,
                on_press=self.on_button
            )

            row.add_widget(btn)
            count += 1

        self.add_widget(grid)

    def on_button(self, btn):

        text = btn.text

        if text == "=":
            try:
                self.display.text = str(
                    eval(self.display.text)
                )
            except:
                self.display.text = "Error"
        else:
            self.display.text += text


class CalculatorApp(App):

    def build(self):
        return Calculator()


if __name__ == "__main__":
    CalculatorApp().run()
