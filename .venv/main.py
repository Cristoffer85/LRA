from kivy.app import App
from kivy.lang import Builder
from Index import index
from FUNStart import FUNStart
from FUNRegister import FUNRegister
from FUNWarmup import FUNWarmup
from FUNLiveboard import FUNLiveboard
from FUNResult import FUNResult
from FUNCountdownToStart import FUNCountdownToStart
from screen_manager import MyScreenManager

# Load the kv files for each screen
Builder.load_file('KV/GLOBAL.kv') # done
Builder.load_file('KV/index.kv') # done
Builder.load_file('KV/FUNStart.kv') # done
Builder.load_file('KV/FUNRegister.kv') # done
Builder.load_file('KV/FUNWarmup.kv') # done
Builder.load_file('KV/FUNCountdownToStart.kv') # done
Builder.load_file('KV/FUNLiveboard.kv') # done
Builder.load_file('KV/FUNResult.kv') # done

# Left to do: 

# When transponder data works to be input in application, fix forms and views for how to look

# When above fixed implement simpler pages for the start Free practice and Time Trial

# Tell Martin to buy a touch screen monitor for the application

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
