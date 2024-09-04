from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty, ListProperty, BooleanProperty
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import json
import os

class FUNStart(Screen):
    # Properties to store selected dropdown values
    class_selection = StringProperty("2WD")
    registrationtime_selection = StringProperty("1 min")
    heatlength_selection = StringProperty("5 min")
    warmup_selection = StringProperty("1 min")
    classes = ListProperty(["FWD", "Touring Justock", "Touring mod", "Super touring", "Touring 13.5T", "1/12 MOD", "1/12 STOCK", "Tank", "+ Add new class"])
    auto_start_after_warmup = BooleanProperty(False)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.load_classes()

    def on_class_selection(self, instance, value):
        if value == "+ Add new class":
            self.show_add_class_popup()

    def show_add_class_popup(self):
        content = BoxLayout(orientation='vertical', padding=10, spacing=10)
        text_input = TextInput(hint_text="Enter class name", multiline=False)
        content.add_widget(text_input)

        def add_class(instance):
            new_class = text_input.text.strip()
            if new_class and new_class not in self.classes:
                self.classes.insert(-1, new_class)  # Insert before "+ Add new class"
                self.save_classes()
                self.ids.class_spinner.text = new_class
            popup.dismiss()

        add_button = Button(text="Add", size_hint=(1, 0.3), on_press=add_class)
        content.add_widget(add_button)

        popup = Popup(title="Add New Class", content=content, size_hint=(0.8, 0.5))
        popup.open()

# ------------------------------ Save and load classes to/from a local .json file ------------------------------
    def save_classes(self):
        with open("classes.json", "w") as f:
            json.dump(self.classes[:-1], f)  # Save all except "+ Add new class"

    def load_classes(self):
        if os.path.exists("classes.json"):
            with open("classes.json", "r") as f:
                saved_classes = json.load(f)
                self.classes = saved_classes + ["+ Add new class"]

# ------------------------------ Navigation ------------------------------
    # Forward, to FUNStart
    def go_to_funregister(self):
        funregister_screen = self.manager.get_screen('FUNRegister')
        funregister_screen.class_selection = self.class_selection
        funregister_screen.registrationtime_selection = self.registrationtime_selection
        funregister_screen.heatlength_selection = self.heatlength_selection
        funregister_screen.warmup_selection = self.warmup_selection
        funregister_screen.shortest_laptime_selection = self.shortest_laptime_selection
        funregister_screen.auto_start_after_warmup = self.auto_start_after_warmup

        self.manager.transition.direction = 'left'
        self.manager.current = 'FUNRegister'
    
    # Backward, to index
    def go_to_index(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'index'