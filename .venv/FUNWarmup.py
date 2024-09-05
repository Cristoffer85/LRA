from kivy.uix.screenmanager import Screen
from kivy.clock import Clock

class FUNWarmup(Screen):
    countdown_event = None
# ------------------------------ Take value from FUNRegister saved warmup time property on_enter, use on this screen ------------------------------
    def on_enter(self):
        warmup_time_str = self.manager.get_screen('FUNRegister').warmup_selection.split()[0]
        warmup_time = int(warmup_time_str) * 60
        self.start_countdown(warmup_time)
# ------------------------------ Countdown ------------------------------
    def start_countdown(self, warmup_time):
        countdown_label = self.ids.countdown_label
        self.countdown_time = warmup_time
        self.countdown_event = Clock.schedule_interval(lambda dt: self.update_countdown(countdown_label), 1)

    def update_countdown(self, countdown_label):
        minutes, seconds = divmod(self.countdown_time, 60)
        countdown_label.text = f"Time Remaining: {minutes:02d}:{seconds:02d}"
        if self.countdown_time <= 0:
            if self.countdown_event:
                self.countdown_event.cancel()
                self.countdown_event = None
            self.go_to_funcountdown()
        self.countdown_time -= 1
# ------------------------------ Navigation ------------------------------
    # Back, to FUNRegister
    def go_to_funregister(self):
        if self.countdown_event:
            self.countdown_event.cancel()
            self.countdown_event = None
        
        fun_register_screen = self.manager.get_screen('FUNRegister')
        countdown_label = fun_register_screen.ids.countdown_label
        start_button = fun_register_screen.ids.start_button
        
        countdown_label.text = "Time Remaining: "
        start_button.disabled = False
        start_button.opacity = 1

        self.manager.transition.direction = 'right'
        self.manager.current = 'FUNRegister'
    # Next, to FUNCountdown
    def go_to_funcountdown(self):

        if self.countdown_event:
            self.countdown_event.cancel()
            self.countdown_event = None
        self.manager.transition.direction = 'left'
        self.manager.current = 'FUNCountdownToStart'
