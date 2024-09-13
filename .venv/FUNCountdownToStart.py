import random
import os
from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.core.audio import SoundLoader

class FUNCountdownToStart(Screen):
    countdown_event = None
# ------------------------------ Initialisation + load sounds on start ------------------------------
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        sound_dir = os.path.join(os.path.dirname(__file__), 'sounds')
        
        self.sounds = {
            10: SoundLoader.load(os.path.join(sound_dir, '10.wav')),
            9: SoundLoader.load(os.path.join(sound_dir, '9.wav')),
            8: SoundLoader.load(os.path.join(sound_dir, '8.wav')),
            7: SoundLoader.load(os.path.join(sound_dir, '7.wav')),
            6: SoundLoader.load(os.path.join(sound_dir, '6.wav')),
            5: SoundLoader.load(os.path.join(sound_dir, '5.wav')),
            4: SoundLoader.load(os.path.join(sound_dir, '4.wav')),
            0: SoundLoader.load(os.path.join(sound_dir, 'race start.mp3'))
        }
# ------------------------------ Take value from FUNStart checkbox autostart saved property on_enter, use on this screen ------------------------------
    def on_pre_enter(self, *args):
        auto_start = self.manager.get_screen('FUNStart').auto_start_after_warmup
        if auto_start:
            # Start countdown automatically if checkbox is checked
            self.start_countdown(self.ids.countdown_label, self.ids.next_button)
        else:
            # Show the Start Countdown button if checkbox is unchecked
            self.ids.next_button.opacity = 1
# ------------------------------ Countdown ------------------------------
    def start_countdown(self, countdown_label, next_button):
        if self.countdown_event:
            return

        next_button.opacity = 0

        for widget in self.children:
            if isinstance(widget, Button) and widget != next_button:
                widget.opacity = 0

        countdown_label.opacity = 1
        countdown_label.text = "10"  # Start countdown from 10 seconds
        self.countdown_time = 10
        self.countdown_event = Clock.schedule_interval(lambda dt: self.update_countdown(countdown_label), 1)
        # sound for numbers 10 to 4

    def update_countdown(self, countdown_label):
        if self.countdown_time <= 0:
            self.sounds[0].play()
            self.countdown_event.cancel()
            self.countdown_event = None
            self.go_to_funliveboard()
            return

        if self.countdown_time > 3:
            countdown_label.text = f"{self.countdown_time:02d}"
        else:
            countdown_label.text = ""  # Hide the countdown label for numbers 3 to 0

        if self.countdown_time in self.sounds:
            self.sounds[self.countdown_time].play()

        # Random delay for the start sound
        if self.countdown_time == 3:
            self.start_time = Clock.get_time()
            self.random_delay = random.uniform(1.0, 4.0)  # Random delay between 1 and 4 seconds
            Clock.schedule_once(self.play_random_start_sound, self.random_delay)

        self.countdown_time -= 1

    def reset_manual_start(self):
        if self.countdown_event:
            self.countdown_event.cancel()
            self.countdown_event = None

        self.ids.next_button.opacity = 1

        self.ids.countdown_label.opacity = 0

        self.ids.countdown_label.text = "10"
# ------------------------------ Start sound ------------------------------
    def play_random_start_sound(self, dt):
        self.sounds[0].play()  # Play the start sound
        self.go_to_funliveboard()
# ------------------------------ Navigation ------------------------------
    # Back, to index
    def go_to_home(self):
        # Navigate to the home screen
        self.manager.transition.direction = 'down'
        self.manager.current = 'index'
    # Forward, to FUNLiveboard
    def go_to_funliveboard(self):
        # Next to FunLiveboard screen
        self.manager.transition.direction = 'left'
        self.manager.current = 'FUNLiveboard'