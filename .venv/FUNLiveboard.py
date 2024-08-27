from kivy.uix.screenmanager import Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle

class FUNLiveboard(Screen):
    def on_enter(self):
        self.update_table()

    def update_table(self):
        # Clear previous widgets
        self.ids.table_layout.clear_widgets()

        # Create a GridLayout with 8 rows and 8 columns
        grid_layout = GridLayout(cols=8, rows=8)

        for row in range(8):
            for col in range(8):
                # Create a label for each cell
                cell_label = Label(
                    text=f"{row+1},{col+1}",
                    halign='center',
                    valign='middle',
                    size_hint=(1, 1),
                    color=(0, 0, 0, 1)
                )
                grid_layout.add_widget(cell_label)
        
        # Add the grid_layout to the table_layout
        self.ids.table_layout.add_widget(grid_layout)
