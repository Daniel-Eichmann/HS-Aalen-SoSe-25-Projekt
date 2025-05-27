#Damit alles läuft muss man Kivy mit Hilfe von Pip installieren!
from kivy.config import Config
Config.set("kivy", "audio", "ffpyplayer") #ffpyplayer muss installiert sein!!! *pip install ffpyplayer* // Außerdem muss die Config Zeile mit dem Import ganz oben stehen, sonst bekommen wir einen Fehler!
#FIXME: Es kommt beim Starten eine GStreamer Warnung --> Letzendlich läuft alles, aber es fucked ein bisschen ab. Hat irgendwas mit der Hintergrund Musik zu tun.
from kivy.app import App
#from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.core.audio import SoundLoader  #ffpyplayer muss installiert sein!!! *pip install ffpyplayer* im cmd.
from kivy.uix.video import Video
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.uix.slider import Slider
import subprocess
import os
#test -marco
#tets2


class MainHauptmenüWidget(Screen):      #Diese Klasse macht aus unseren MainHauptmenü ein Widget, damit es mit dem ScreenManager geändert werden kann!
    def __init__(self, **kwargs):   
        super().__init__(**kwargs)
        self.layout = MainHauptmenü()
        self.add_widget(self.layout)

class MainHauptmenü(FloatLayout):        #Für das Layout Verwantwortlich. Ist unser Main Fenster
    def __init__(self, **kwargs):   
        super().__init__(**kwargs)
        video = Video(source="Hintergrund_Bild.mp4", state="play", options={"eos":"loop"})
        video.allow_stretch = True
        video.keep_ratio = False
        self.add_widget(video)
        
        #Button1
        def go_to_spiel_starten(click):
            self.parent.manager.current ="spiel_starten"
        spiel_starten_button = Button(text ="SPIEL STARTEN", font_name="GUI_Grafiken\\ka1.ttf", font_size=23, background_color = [0,0,0,0])
        spiel_starten_button.size_hint = 0.3, 0.1
        spiel_starten_button.pos_hint = {"center_x" : 0.28, "center_y" : 0.75}
        self.add_widget(spiel_starten_button)
        spiel_starten_button.bind(on_press = go_to_spiel_starten)

        #Button 2
        def go_to_highscore(click):
            self.parent.manager.current ="highscore"
        highscore_button = Button(text ="HIGHSCORE", font_name="GUI_Grafiken\\ka1.ttf", font_size=23, background_color = [0,0,0,0])
        highscore_button.size_hint = 0.3 , 0.1
        highscore_button.pos_hint = {"center_x" : 0.28, "center_y" : 0.55}
        self.add_widget(highscore_button)
        highscore_button.bind(on_press = go_to_highscore)

        #Button 3
        def go_to_optionen(click):
            self.parent.manager.current ="optionen"
        optionen_button = Button(text ="OPTIONEN", font_name="GUI_Grafiken\\ka1.ttf", font_size=23, background_color = [0,0,0,0])
        optionen_button.size_hint = 0.3 , 0.1
        optionen_button.pos_hint = {"center_x" : 0.28, "center_y" : 0.35}
        self.add_widget(optionen_button)
        optionen_button.bind(on_press = go_to_optionen)

        #Button4 
        def go_to_credits(click):
            self.parent.manager.current ="credits"
        credits_button = Button(text ="CREDITS", font_name="GUI_Grafiken\\ka1.ttf", font_size=23, background_color = [0,0,0,0])
        credits_button.size_hint = 0.3 , 0.1
        credits_button.pos_hint = {"center_x" : 0.28, "center_y" : 0.15}
        self.add_widget(credits_button)
        credits_button.bind(on_press = go_to_credits)


#TODO: Möglichkeit zwischen Musik zu wechseln
#TODO: Highscore mit ScrollLayout
#TODO: Optionen mit Keybind änderung / Lautstärke / Sprache
#TODO: Credits Scene

class Spiel_StartenWidget(Screen):      #Diese Klasse macht aus unseren Optionen ein Widget, damit es mit dem ScreenManager geändert werden kann!
    def __init__(self, **kwargs):   
        super().__init__(**kwargs)
        self.layout = Spiel_Starten()
        self.add_widget(self.layout)

class Spiel_Starten(FloatLayout):
    def __init__(self, **kwargs):   
        super().__init__(**kwargs)
        def back_button_click1(click):
            self.parent.manager.current = "hauptmenü"

        hintergrundbild_spiel_starten = Image(source="GUI_Grafiken\\spiel_starten_placeholder.jpg")
        self.add_widget(hintergrundbild_spiel_starten)
        
        def arcade_grundlagen_starten(click):                                                           #Das hier ist unglaublich wichtig und sehr verwirrend, aber es muss so, weil er sonst die Hardcoded Variante nimmt, und das ist ziemlich shit!
            dir_path = os.path.dirname(os.path.realpath(__file__))                                      #auf jeden Fall nimmt er hier die Working Directory und nicht irgendwie den Gesamtpfad oder so, keine Ahnung was hier abgeht.
            pfad_spiel1 = os.path.join(dir_path,"Arcadeordner", "autobahn.py")                          
            subprocess.run(["python", pfad_spiel1])

        def alien_invasion_starten(click):                                                              #Das hier ist unglaublich wichtig und sehr verwirrend, aber es muss so, weil er sonst die Hardcoded Variante nimmt, und das ist ziemlich shit!
            dir_path = os.path.dirname(os.path.realpath(__file__))                                      #auf jeden Fall nimmt er hier die Working Directory und nicht irgendwie den Gesamtpfad oder so, keine Ahnung was hier abgeht.
            pfad_spiel2 = os.path.join(dir_path,"Spiel_Zwei", "alien_invasion.py")                          
            subprocess.run(["python", pfad_spiel2])


        spiel1 = Button(text ="SPIEL 1", font_name="GUI_Grafiken\\ka1.ttf", font_size=23, background_color = [0,0,0,0])
        spiel1.size_hint = 0.3, 0.1
        spiel1.pos_hint = {"center_x" : 0.28, "center_y" : 0.75}
        self.add_widget(spiel1)
        spiel1.bind(on_press = arcade_grundlagen_starten)

        spiel2 = Button(text ="SPIEL 2", font_name="GUI_Grafiken\\ka1.ttf", font_size=23, background_color = [0,0,0,0])
        spiel2.size_hint = 0.3, 0.1
        spiel2.pos_hint = {"center_x" : 0.28, "center_y" : 0.55}
        self.add_widget(spiel2)
        spiel2.bind(on_press = alien_invasion_starten)

        back_button = Button(text = "BACK", font_name="GUI_Grafiken\\ka1.ttf", font_size=23, background_color = [0,0,0,0])
        back_button.size_hint = 0.3, 0.1
        back_button.pos_hint = {"center_x" : 0.9, "center_y" : 0.9}
        back_button.bind(on_press = back_button_click1)
        self.add_widget(back_button)

class CreditsWidget(Screen):    #Diese Klasse macht aus unseren Credits ein Widget, damit es mit dem ScreenManager geändert werden kann!
    def __init__(self, **kwargs):   
        super().__init__(**kwargs)
        self.layout = Credits()
        self.add_widget(self.layout)

class Credits(FloatLayout):
    def __init__(self, **kwargs):   
        super().__init__(**kwargs)
        def back_button_click(click):
            self.parent.manager.current = "hauptmenü"

        hintergrundbild_credits = Image(source="GUI_Grafiken\\credits_placeholder.jpg")
        self.add_widget(hintergrundbild_credits)

        back_button = Button(text = "BACK", font_name="GUI_Grafiken\\ka1.ttf", font_size=23, background_color = [0,0,0,0])
        back_button.size_hint = 0.3, 0.1
        back_button.pos_hint = {"center_x" : 0.9, "center_y" : 0.9}
        back_button.bind(on_press = back_button_click)
        self.add_widget(back_button)

#TODO: Credits Intro Roll erstellen
class OptionenWidget(Screen):      #Diese Klasse macht aus unseren Optionen ein Widget, damit es mit dem ScreenManager geändert werden kann!
    def __init__(self, **kwargs):   
        super().__init__(**kwargs)
        self.layout = Optionen()
        self.add_widget(self.layout)

class Optionen(FloatLayout):
    def __init__(self, **kwargs):   
        super().__init__(**kwargs)
        def back_button_click1(click):
            self.parent.manager.current = "hauptmenü"

        hintergrundbild_optionen = Image(source="GUI_Grafiken\\optionen_placeholder.jpg")
        self.add_widget(hintergrundbild_optionen)

        back_button = Button(text = "BACK", font_name="GUI_Grafiken\\ka1.ttf", font_size=23, background_color = [0,0,0,0])
        back_button.size_hint = 0.3, 0.1
        back_button.pos_hint = {"center_x" : 0.9, "center_y" : 0.9}
        back_button.bind(on_press = back_button_click1)
        self.add_widget(back_button)

class HighscoreWidget(Screen):      #Diese Klasse macht aus unseren Highscore ein Widget, damit es mit dem ScreenManager geändert werden kann!
    def __init__(self, **kwargs):   
        super().__init__(**kwargs)
        self.layout = Highscore()
        self.add_widget(self.layout)

class Highscore(FloatLayout):
    def __init__(self, **kwargs):   
        super().__init__(**kwargs)
        def back_button_click1(click):
            self.parent.manager.current = "hauptmenü"

        hintergrundbild_highscore = Image(source="GUI_Grafiken\\highscore_placeholder.jpg")
        self.add_widget(hintergrundbild_highscore)

        back_button = Button(text = "BACK", font_name="GUI_Grafiken\\ka1.ttf", font_size=23, background_color = [0,0,0,0])
        back_button.size_hint = 0.3, 0.1
        back_button.pos_hint = {"center_x" : 0.9, "center_y" : 0.9}
        back_button.bind(on_press = back_button_click1)
        self.add_widget(back_button)

class ArcadeProjektApp(App):           #Startet das Main Fenster unserer App
    def build(self):
        self.music = SoundLoader.load("GUI_Grafiken\\hintergrund_musik1.mp3")
        if self.music:
            self.music.loop = True
            self.music.play()

        sm = ScreenManager()
        sm.add_widget(MainHauptmenüWidget(name = "hauptmenü"))
        sm.add_widget(CreditsWidget(name = "credits"))
        sm.add_widget(OptionenWidget(name = "optionen"))
        sm.add_widget(HighscoreWidget(name = "highscore"))
        sm.add_widget(Spiel_StartenWidget(name = "spiel_starten"))
        return sm

ArcadeProjektApp().run()