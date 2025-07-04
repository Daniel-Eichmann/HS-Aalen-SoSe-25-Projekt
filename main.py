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
from kivy.uix.label import Label
from kivy.clock import Clock
import subprocess
import os


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

        hintergrundbild_spiel_starten = Video(source="Hintergrund_Bild.mp4", state="play", options={"eos":"loop"})
        hintergrundbild_spiel_starten.allow_stretch = True
        hintergrundbild_spiel_starten.keep_ratio = False
        self.add_widget(hintergrundbild_spiel_starten)
        
        def arcade_autobahn_starten(click):
            app = App.get_running_app()
            if app.music:
                app.music.volume = 0.0                                                           #Das hier ist unglaublich wichtig und sehr verwirrend, aber es muss so, weil er sonst die Hardcoded Variante nimmt, und das ist ziemlich shit!
            dir_path = os.path.dirname(os.path.realpath(__file__))                                      #auf jeden Fall nimmt er hier die Working Directory und nicht irgendwie den Gesamtpfad oder so, keine Ahnung was hier abgeht.
            pfad_spiel1 = os.path.join(dir_path,"Arcadeordner", "autobahn.py")                          
            subprocess.run(["python", pfad_spiel1])
            if app.music:
                app.music.volume = 0.01

        def arcade_escapegame_starten(click):                                                              #Das hier ist unglaublich wichtig und sehr verwirrend, aber es muss so, weil er sonst die Hardcoded Variante nimmt, und das ist ziemlich shit!
            dir_path = os.path.dirname(os.path.realpath(__file__))                                      #auf jeden Fall nimmt er hier die Working Directory und nicht irgendwie den Gesamtpfad oder so, keine Ahnung was hier abgeht.
            pfad_spiel2 = os.path.join(dir_path,"Arcadeordner", "Escapegame.py")                          
            subprocess.run(["python", pfad_spiel2])

        def arcade_pong_starten(click):                                                              #Das hier ist unglaublich wichtig und sehr verwirrend, aber es muss so, weil er sonst die Hardcoded Variante nimmt, und das ist ziemlich shit!
            dir_path = os.path.dirname(os.path.realpath(__file__))                                      #auf jeden Fall nimmt er hier die Working Directory und nicht irgendwie den Gesamtpfad oder so, keine Ahnung was hier abgeht.
            pfad_spiel3 = os.path.join(dir_path,"Spiel_Drei", "Pong.py")                          
            subprocess.run(["python", pfad_spiel3])


        spiel1 = Button(text ="Autobahn", font_name="GUI_Grafiken\\ka1.ttf", font_size=23, background_color = [0,0,0,0])
        spiel1.size_hint = 0.3, 0.1
        spiel1.pos_hint = {"center_x" : 0.28, "center_y" : 0.75}
        self.add_widget(spiel1)
        spiel1.bind(on_press = arcade_autobahn_starten)

        spiel2 = Button(text ="Escapegame", font_name="GUI_Grafiken\\ka1.ttf", font_size=23, background_color = [0,0,0,0])
        spiel2.size_hint = 0.3, 0.1
        spiel2.pos_hint = {"center_x" : 0.28, "center_y" : 0.55}
        self.add_widget(spiel2)
        spiel2.bind(on_press = arcade_escapegame_starten)

        spiel3 = spiel1 = Button(text ="Pong", font_name="GUI_Grafiken\\ka1.ttf", font_size=23, background_color = [0,0,0,0])
        spiel3.size_hint = 0.3, 0.1
        spiel3.pos_hint = {"center_x" : 0.28, "center_y" : 0.35}
        self.add_widget(spiel3)
        spiel3.bind(on_press = arcade_pong_starten)

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

        hintergrundbild_optionen = Video(source="Hintergrund_Bild.mp4", state="play", options={"eos":"loop"})
        hintergrundbild_optionen.allow_stretch = True
        hintergrundbild_optionen.keep_ratio = False
        self.add_widget(hintergrundbild_optionen)

        lautstärke_label = Label(text="Volume", font_name="GUI_Grafiken\\ka1.ttf", font_size=23, color = [1,1,1,1])
        lautstärke_label.size_hint = 0.3, 0.1
        lautstärke_label.pos_hint = {"center_x" : 0.28, "center_y" : 0.75}
        self.add_widget(lautstärke_label)

        lautstärke_slider = Slider(min=0, max=1, value = App.get_running_app().music.volume)
        lautstärke_slider.size_hint = 0.3, 0.05
        lautstärke_slider.pos_hint = {"center_x" : 0.28, "center_y" : 0.70}
        self.add_widget(lautstärke_slider)

        def lautstärke_anpassung(instance, value):
            App.get_running_app().music.volume = value
        lautstärke_slider.bind(value = lautstärke_anpassung)

        musik_label = Label(text = "Musikauswahl", font_name="GUI_Grafiken\\ka1.ttf", font_size = 23, color = (1,1,1,1))
        musik_label.size_hint = 0.3, 0.1
        musik_label.pos_hint = {"center_x" : 0.28, "center_y" : 0.5}
        self.add_widget(musik_label)

        def musik_wechsel1(instance):
            App.get_running_app().musikauswahl("GUI_Grafiken/hintergrund_musik1.mp3")
        
        def musik_wechsel2(instance):
            App.get_running_app().musikauswahl("GUI_Grafiken/hintergrund_musik2.mp3")

        def musik_wechsel3(instance):
            App.get_running_app().musikauswahl("GUI_Grafiken/hintergrund_musik3.mp3")

        musik1_button = Button(text ="Spaceship Arcade", font_name="GUI_Grafiken\\ka1.ttf", font_size=23, background_color = [0,0,0,0])
        musik1_button.size_hint = 0.3 , 0.1
        musik1_button.pos_hint = {"center_x" : 0.28, "center_y" : 0.4}
        musik1_button.bind(on_press = musik_wechsel1)
        self.add_widget(musik1_button)

        musik2_button = Button(text ="Retro Game Arcade", font_name="GUI_Grafiken\\ka1.ttf", font_size=23, background_color = [0,0,0,0])
        musik2_button.size_hint = 0.3 , 0.1
        musik2_button.pos_hint = {"center_x" : 0.28, "center_y" : 0.3}
        musik2_button.bind(on_press = musik_wechsel2)
        self.add_widget(musik2_button)

        musik3_button = Button(text ="8-bit Arcade Mode", font_name="GUI_Grafiken\\ka1.ttf", font_size=23, background_color = [0,0,0,0])
        musik3_button.size_hint = 0.3 , 0.1
        musik3_button.pos_hint = {"center_x" : 0.28, "center_y" : 0.2}
        musik3_button.bind(on_press = musik_wechsel3)
        self.add_widget(musik3_button)

        

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

class Intro1(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()
        logo_hs_aalen = Image(source="GUI_Grafiken\\hs_aalen.png", allow_stretch = True, keep_ratio = True)
        layout.add_widget(logo_hs_aalen)
        self.add_widget(layout)
        Clock.schedule_once(self.wechsel_zu_intro2, 2.5)
    
    def wechsel_zu_intro2(self, zeit):
        self.manager.current = "intro2"

class Intro2(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()
        logo = Image(source="GUI_Grafiken\\credits_placeholder.jpg", allow_stretch=True, keep_ratio=False)
        layout.add_widget(logo)
        self.add_widget(layout)
        Clock.schedule_once(self.wechsle_zu_hauptmenü, 5)

    def wechsle_zu_hauptmenü(self, zeit):
        self.manager.current = "hauptmenü"
        


class ArcadeProjektApp(App):           #Startet das Main Fenster unserer App
    def build(self):
        self.music = SoundLoader.load("GUI_Grafiken\\hintergrund_musik1.mp3")
        if self.music:
            self.music.loop = True
            self.music.volume = 0.01
            self.music.play()

        sm = ScreenManager()
        sm.add_widget(Intro1(name = "intro1"))
        sm.add_widget(Intro2(name = "intro2"))
        sm.add_widget(MainHauptmenüWidget(name = "hauptmenü"))
        sm.add_widget(CreditsWidget(name = "credits"))
        sm.add_widget(OptionenWidget(name = "optionen"))
        sm.add_widget(HighscoreWidget(name = "highscore"))
        sm.add_widget(Spiel_StartenWidget(name = "spiel_starten"))
        return sm
    
    def musikauswahl(self, pfad):
        if self.music:
            self.music.stop()
        self.music = SoundLoader.load(pfad)
        if self.music:
            self.music.loop
            self.music.volume = 0.01
            self.music.play()

ArcadeProjektApp().run()