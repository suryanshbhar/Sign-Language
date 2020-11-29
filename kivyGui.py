from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.pagelayout import PageLayout

from set_hand_hist import get_hand_hist
 
class SimpleApp(App):
    def build(self):
        def set_hand_hist_button(instance,value):
            print("Setting hand hist.")
            get_hand_hist()
        layout = PageLayout()
        btn=Button(text='Set Your Hand histogram.',background_color=(1,0,0,1))
        #btn.bind(state=set_hand_hist_button)
        layout.add_widget(btn)
        layout.add_widget(Button(text='world',background_color=(0,1,0,1)))
        layout.add_widget(Button(text='welcome to',background_color=(1,1,1,1)))
        layout.add_widget(Button(text='edureka',background_color=(0,1,1,1)))
        return layout
 
 
if __name__ == "__main__":
    SimpleApp().run()