from kivy.uix.screenmanager import Screen
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button

class FUNStart(Screen):
    def __init__(self, **kwargs):
        super(FUNStart, self).__init__(**kwargs)

        # Create DropDowns for each button
        self.class_dropdown = DropDown()
        classes = ["2WD", "4WD", "Custom.."]
        for class_name in classes:
            btn = Button(text=class_name, size_hint_y=None, height='44dp')
            btn.bind(on_release=self.set_class)
            self.class_dropdown.add_widget(btn)

        self.heatlength_dropdown = DropDown()
        for minute in [5, 10, 15, 20]:
            btn = Button(text=str(minute), size_hint_y=None, height='44dp')
            btn.bind(on_release=self.set_heatlength)
            self.heatlength_dropdown.add_widget(btn)

        self.registrationtime_dropdown = DropDown()
        for minute in range(1, 6):
            btn = Button(text=str(minute), size_hint_y=None, height='44dp')
            btn.bind(on_release=self.set_registrationtime)
            self.registrationtime_dropdown.add_widget(btn)

        self.warmup_dropdown = DropDown()
        for minute in range(1, 6):
            btn = Button(text=str(minute), size_hint_y=None, height='44dp')
            btn.bind(on_release=self.set_warmup)
            self.warmup_dropdown.add_widget(btn)

    def open_heatlength_dropdown(self, button):
        self.heatlength_dropdown.open(button)

    def open_registrationtime_dropdown(self, button):
        self.registrationtime_dropdown.open(button)

    def open_warmup_dropdown(self, button):
        self.warmup_dropdown.open(button)

    def open_class_dropdown(self, button):
        self.class_dropdown.open(button)

    def set_heatlength(self, instance):
        self.ids.heatlength_button.text = f'Heatlength (min): {instance.text}'

    def set_registrationtime(self, instance):
        self.ids.registrationtime_button.text = f'Registrationtime (min): {instance.text}'

    def set_warmup(self, instance):
        self.ids.warmup_button.text = f'Warmup (min): {instance.text}'

    def set_class(self, instance):
        self.ids.class_button.text = f'Class: {instance.text}'
