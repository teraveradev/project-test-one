from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.screen import Screen
from kivymd.uix.textfield import MDTextField
from kivy.lang import Builder
from kivymd.theming import ThemeManager
from kivy.uix.screenmanager import ScreenManager
from template1 import navigation_helper
from kivy.properties import ObjectProperty
from kivmob import KivMob, TestIds,RewardedListenerInterface

username_bar= """
MDTextField:
 hint_text:'What aare you looking for'
 pos_hint: {'center_x':0.5,'center_y':0.5}

"""
def change_screen(self,screen):
      ScreenManager.ids.screen_m.current="freelance"


# configuring kivy window size and collor
Window.size = (360, 600)
Window.clearcolor=(0,0,0,0)
#difining the navigation barss


#definfing the screens
#building the appsm= ScreenManager()
 

class scriptmotion (MDApp):
    add=KivMob(TestIds.APP)
    def build(self):
        self.add.new_banner(TestIds.BANNER,True)
        self.add.request_banner()
        self.add.show_banner()
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Teal"
        self.theme_cls.accent_palette="Cyan"
        self.sm = ScreenManager()
        self.sm.add_widget(Screen(name="homepage"))
        self.sm.add_widget(Screen(name="freelance"))
        
        screen= Builder.load_string(navigation_helper)
        return screen
       

scriptmotion().run()
