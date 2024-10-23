from kivy.app import App
from kivy.lang import Builder
from pages.Index import index
from pages.versus.FUNStart import FUNStart 
from pages.versus.FUNRegister import FUNRegister
from pages.versus.FUNWarmup import FUNWarmup
from pages.versus.FUNLiveboard import FUNLiveboard
from pages.versus.FUNResult import FUNResult
from pages.versus.FUNCountdownToStart import FUNCountdownToStart
from screen_manager import MyScreenManager

# Load the kv files for each screen
Builder.load_file('design/GLOBAL.kv') # done
Builder.load_file('design/index.kv') # done
Builder.load_file('design/versus/FUNStart.kv') # done
Builder.load_file('design/versus/FUNRegister.kv') # done
Builder.load_file('design/versus/FUNWarmup.kv') # done
Builder.load_file('design/versus/FUNCountdownToStart.kv') # done
Builder.load_file('design/versus/FUNLiveboard.kv') # done
Builder.load_file('design/versus/FUNResult.kv') # done

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
