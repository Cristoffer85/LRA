from kivy.app import App
from kivy.lang import Builder
from index import index
from FUNStart import FUNStart
from FUNRegister import FUNRegister
from FUNWarmup import FUNWarmup
from FUNLiveboard import FUNLiveboard
from FUNResult import FUNResult
from FUNCountdownToStart import FUNCountdownToStart
from screen_manager import MyScreenManager

# Load the kv files for each screen
Builder.load_file('KV/GLOBAL.kv')
Builder.load_file('KV/index.kv')
Builder.load_file('KV/FUNStart.kv')
Builder.load_file('KV/FUNRegister.kv')
Builder.load_file('KV/FUNWarmup.kv')
Builder.load_file('KV/FUNCountdownToStart.kv')
Builder.load_file('KV/FUNLiveboard.kv')
Builder.load_file('KV/FUNResult.kv')

class LateraRaceTracer(App):
    def build(self):
        self.sm = MyScreenManager()
        self.sm.add_widget(index(name='index'))
        self.sm.add_widget(FUNStart(name='FUNStart'))
        self.sm.add_widget(FUNRegister(name='FUNRegister'))
        self.sm.add_widget(FUNWarmup(name='FUNWarmup'))
        self.sm.add_widget(FUNCountdownToStart(name='FUNCountdownToStart'))
        self.sm.add_widget(FUNLiveboard(name='FUNLiveboard'))
        self.sm.add_widget(FUNResult(name='FUNResult'))
        return self.sm

if __name__ == '__main__':
    LateraRaceTracer().run()
