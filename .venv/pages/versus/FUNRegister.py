from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from kivy.properties import StringProperty, BooleanProperty

class FUNRegister(Screen):
    countdown_event = None
# ------------------------------ (Kivy) Property saving, of values in dropdown lists ------------------------------
    class_selection = StringProperty()
    registrationtime_selection = StringProperty()
    heatlength_selection = StringProperty()
    warmup_selection = StringProperty()
    shortest_laptime_selection = StringProperty()
    auto_start_after_warmup = BooleanProperty(False)
# ------------------------------ Countdown ------------------------------
    def start_countdown(self, countdown_label, start_button):
        if self.countdown_event:
            return

        start_button.disabled = True
        start_button.opacity = 0

        registration_time_str = self.registrationtime_selection.split()[0]
        registration_time = int(registration_time_str) * 60
        self.countdown_time = registration_time

        countdown_label.opacity = 1 
        self.countdown_event = Clock.schedule_interval(lambda dt: self.update_countdown(countdown_label), 1)

    def update_countdown(self, countdown_label):
        minutes, seconds = divmod(self.countdown_time, 60)
        
        countdown_label.text = (
        f"[color=#BBBBBB]Drive participating cars past startline![/color] "
        f"[color=#FFFFFF][b]{minutes:02d}:{seconds:02d}[/b][/color]"
    )
        if self.countdown_time <= 0:
            self.countdown_event.cancel()
            self.countdown_event = None
            self.reset_countdown(countdown_label, self.ids.start_button)
            self.go_to_funwarmup()
        self.countdown_time -= 1

    def reset_countdown(self, countdown_label, start_button):
        if self.countdown_event:
            self.countdown_event.cancel()
            self.countdown_event = None
            self.countdown_time = 0

        countdown_label.opacity = 0

        start_button.disabled = False
        start_button.opacity = 1
# ------------------------------ Navigation ------------------------------
    # Back, to FUNStart
    def go_to_funstart(self):
        countdown_label = self.ids.countdown_label
        start_button = self.ids.start_button
        self.reset_countdown(countdown_label, start_button)
        self.manager.transition.direction = 'right'
        self.manager.current = 'FUNStart'

    # Forward, to FUNWarmup
    def go_to_funwarmup(self):
        countdown_label = self.ids.countdown_label
        start_button = self.ids.start_button
        self.reset_countdown(countdown_label, start_button)  # Ensure reset (of countdown) happen before navigation
        
        self.manager.transition.direction = 'left'
        self.manager.current = 'FUNWarmup'