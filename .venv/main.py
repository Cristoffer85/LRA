from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from Index import Index
from FUNStart import FUNStart
from FUNRegister import FUNRegister
from FUNWarmup import FUNWarmup
from FUNCountdownToStart import FUNCountdownToStart

# Load the kv files for each screen
Builder.load_file('KV/GLOBAL.kv')
Builder.load_file('KV/Index.kv')
Builder.load_file('KV/FUNStart.kv')
Builder.load_file('KV/FUNRegister.kv')
Builder.load_file('KV/FUNWarmup.kv')
Builder.load_file('KV/FUNCountdownToStart.kv')

class MyScreenManager(ScreenManager):
    pass

class LateraRaceTracer(App):
    def build(self):
        self.sm = MyScreenManager()
        self.sm.add_widget(Index(name='Index'))
        self.sm.add_widget(FUNStart(name='FUNStart'))
        self.sm.add_widget(FUNRegister(name='FUNRegister'))
        self.sm.add_widget(FUNWarmup(name='FUNWarmup'))
        self.sm.add_widget(FUNCountdownToStart(name='FUNCountdownToStart'))
        return self.sm

if __name__ == '__main__':
    LateraRaceTracer().run()