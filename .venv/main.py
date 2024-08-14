from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from screens import StartScreen, OptionsScreen

# Load the kv files for each screen
Builder.load_file('KV/startscreen.kv')
Builder.load_file('KV/optionsscreen.kv')
Builder.load_file('KV/widgets.kv')

class MyScreenManager(ScreenManager):
    pass

class MyApp(App):
    def build(self):
        self.sm = MyScreenManager()
        self.sm.add_widget(StartScreen(name='start'))
        self.sm.add_widget(OptionsScreen(name='FUNRace'))
        return self.sm

    def option_selected(self, instance):
        print(f'{instance.text} selected')

    def go_back(self):
        if self.sm.current != 'start':
            self.sm.current = 'start'

    def class_selection(self, selected_option):
        print(f'Selected Class: {selected_option}')

if __name__ == '__main__':
    MyApp().run()