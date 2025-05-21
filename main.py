#Damit alles läuft muss man Kivy mit Hilfe von Pip installieren!
from kivy.config import Config
Config.set("kivy", "audio", "ffpyplayer") #ffpyplayer muss installiert sein!!! *pip install ffpyplayer* // Außerdem muss die Config Zeile mit dem Import ganz oben stehen, sonst bekommen wir einen Fehler!
#FIXME: Es kommt beim Starten eine GStreamer Warnung --> Letzendlich läuft alles, aber es fucked ein bisschen ab. Hat irgendwas mit der Hintergrund Musik zu tun.
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.core.audio import SoundLoader  #ffpyplayer muss installiert sein!!! *pip install ffpyplayer* im cmd.
from kivy.uix.video import Video



class MainFenster(FloatLayout):        #Für das Layout Verwantwortlich.
    def __init__(self, **kwargs):   
        super().__init__(**kwargs)
        video = Video(source="Hintergrund_Bild.mp4", state="play", options={"eos":"loop"})
        video.allow_stretch = True
        video.keep_ratio = False
        self.add_widget(video)
        
        
        button1 = Button(text ="SPIEL STARTEN")
        button1.size_hint = 0.3, 0.1
        button1.pos_hint = {"center_x" : 0.28, "center_y" : 0.75}
        button2 = Button(text ="HIGHSCORE")
        button2.size_hint = 0.3 , 0.1
        button2.pos_hint = {"center_x" : 0.28, "center_y" : 0.55}
        button3 = Button(text ="OPTIONEN")
        button3.size_hint = 0.3 , 0.1
        button3.pos_hint = {"center_x" : 0.28, "center_y" : 0.35}
        button4 = Button(text ="CREDITS")
        button4.size_hint = 0.3 , 0.1
        button4.pos_hint = {"center_x" : 0.28, "center_y" : 0.15}
        self.add_widget(button1)
        self.add_widget(button2)
        self.add_widget(button3)
        self.add_widget(button4)

#TODO: Möglichkeit zwischen Musik zu wechseln
#TODO: Highscore mit ScrollLayout
#TODO: Optionen mit Keybind änderung / Lautstärke / Sprache
#TODO: Credits Scene



        

class MainWidget(Widget):
    pass

class ArcadeApp(App):           #Startet das Main Fenster unserer App
    def build(self):
        self.music = SoundLoader.load("hintergrund_musik1.mp3")
        if self.music:
            self.music.loop = True
            self.music.play()
        return MainFenster()

ArcadeApp().run()