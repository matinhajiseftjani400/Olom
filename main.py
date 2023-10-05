from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label

class OlomHashtomApp(App):
    def calculate_percentage(self, instance):
        try:
            num1 = float(self.textinput1.text)
            num2 = float(self.textinput2.text)
            num3 = float(self.textinput3.text)
            result = num1 + num2 
            result2 = num3 / result
            result3 = result2 * 100

            self.label.text = f"Answer: {result3}%"
        except ValueError:
            self.label.text = "Enter all options completely and correctly"
    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.textinput1 = TextInput(hint_text="Hallal")
        self.textinput2 = TextInput(hint_text="Hal Shavande")
        self.textinput3 = TextInput(hint_text="Percentage of which number?")
        button = Button(text="Computing")
        button.bind(on_press=self.calculate_percentage)
        self.label = Label(text="The text box is empty")
        layout.add_widget(self.textinput1)
        layout.add_widget(self.textinput2)
        layout.add_widget(self.textinput3)
        layout.add_widget(button)
        layout.add_widget(self.label)
        return layout

if __name__ == "__main__":
    OlomHashtomApp().run()