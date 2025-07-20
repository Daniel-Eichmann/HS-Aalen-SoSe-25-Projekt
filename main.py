from kivy.config import Config
Config.set("kivy", "audio", "ffpyplayer") #ffpyplayer muss installiert sein!!! *pip install ffpyplayer* // Außerdem muss die Config Zeile mit dem Import ganz oben stehen, sonst bekommen wir einen Fehler!
from kivy.app import App
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
from Raspberry import Raspberry
import time

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
        self.spiel_starten_button = Button(text ="SPIEL STARTEN", font_name="GUI_Grafiken\\ka1.ttf", font_size=23, background_color = [0,0,0,0])
        self.spiel_starten_button.size_hint = 0.3, 0.1
        self.spiel_starten_button.pos_hint = {"center_x" : 0.28, "center_y" : 0.75}
        self.add_widget(self.spiel_starten_button)
        self.spiel_starten_button.bind(on_press = go_to_spiel_starten)

        #Button 2
        def go_to_highscore(click):
            self.parent.manager.current ="highscore"
        self.highscore_button = Button(text ="HIGHSCORE", font_name="GUI_Grafiken\\ka1.ttf", font_size=23, background_color = [0,0,0,0])
        self.highscore_button.size_hint = 0.3 , 0.1
        self.highscore_button.pos_hint = {"center_x" : 0.28, "center_y" : 0.55}
        self.add_widget(self.highscore_button)
        self.highscore_button.bind(on_press = go_to_highscore)

        #Button 3
        def go_to_optionen(click):
            self.parent.manager.current ="optionen"
        self.optionen_button = Button(text ="OPTIONEN", font_name="GUI_Grafiken\\ka1.ttf", font_size=23, background_color = [0,0,0,0])
        self.optionen_button.size_hint = 0.3 , 0.1
        self.optionen_button.pos_hint = {"center_x" : 0.28, "center_y" : 0.35}
        self.add_widget(self.optionen_button)
        self.optionen_button.bind(on_press = go_to_optionen)

        #Button4 
        def go_to_credits(click):
            self.parent.manager.current ="credits"
        self.credits_button = Button(text ="CREDITS", font_name="GUI_Grafiken\\ka1.ttf", font_size=23, background_color = [0,0,0,0])
        self.credits_button.size_hint = 0.3 , 0.1
        self.credits_button.pos_hint = {"center_x" : 0.28, "center_y" : 0.15}
        self.add_widget(self.credits_button)
        self.credits_button.bind(on_press = go_to_credits)


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
            app.stop_raspberry_input()
            if app.music:
                app.music.volume = 0.0                                                                     #Das hier ist unglaublich wichtig und sehr verwirrend, aber es muss so, weil er sonst die Hardcoded Variante nimmt, und das ist ziemlich shit!
            dir_path = os.path.dirname(os.path.realpath(__file__))                                          #auf jeden Fall nimmt er hier die Working Directory und nicht irgendwie den Gesamtpfad oder so, keine Ahnung was hier abgeht.
            pfad_spiel1 = os.path.join(dir_path,"Arcadeordner", "autobahn.py")                             
            subprocess.run(["python", pfad_spiel1])
            if app.music:
                app.music.volume = 0.01
            app.start_raspberry_input()

        def arcade_escapegame_starten(click):
            app = App.get_running_app()
            app.stop_raspberry_input()                                                              #Das hier ist unglaublich wichtig und sehr verwirrend, aber es muss so, weil er sonst die Hardcoded Variante nimmt, und das ist ziemlich shit!
            dir_path = os.path.dirname(os.path.realpath(__file__))                                          #auf jeden Fall nimmt er hier die Working Directory und nicht irgendwie den Gesamtpfad oder so, keine Ahnung was hier abgeht.
            pfad_spiel2 = os.path.join(dir_path,"Arcadeordner", "Escapegame.py")                             
            subprocess.run(["python", pfad_spiel2])
            app.start_raspberry_input()

        def arcade_pong_starten(click):
            app = App.get_running_app()
            app.stop_raspberry_input()                                                                      #Das hier ist unglaublich wichtig und sehr verwirrend, aber es muss so, weil er sonst die Hardcoded Variante nimmt, und das ist ziemlich shit!
            dir_path = os.path.dirname(os.path.realpath(__file__))                                          #auf jeden Fall nimmt er hier die Working Directory und nicht irgendwie den Gesamtpfad oder so, keine Ahnung was hier abgeht.
            pfad_spiel3 = os.path.join(dir_path,"Spiel_Drei", "Pong.py")                             
            subprocess.run(["python", pfad_spiel3])
            app.start_raspberry_input()


        self.spiel1 = Button(text ="Autobahn", font_name="GUI_Grafiken\\ka1.ttf", font_size=23, background_color = [0,0,0,0])
        self.spiel1.size_hint = 0.3, 0.1
        self.spiel1.pos_hint = {"center_x" : 0.28, "center_y" : 0.75}
        self.add_widget(self.spiel1)
        self.spiel1.bind(on_press = arcade_autobahn_starten)

        self.spiel2 = Button(text ="Escapegame", font_name="GUI_Grafiken\\ka1.ttf", font_size=23, background_color = [0,0,0,0])
        self.spiel2.size_hint = 0.3, 0.1
        self.spiel2.pos_hint = {"center_x" : 0.28, "center_y" : 0.55}
        self.add_widget(self.spiel2)
        self.spiel2.bind(on_press = arcade_escapegame_starten)

        self.spiel3 = Button(text ="Pong", font_name="GUI_Grafiken\\ka1.ttf", font_size=23, background_color = [0,0,0,0]) # Korrigiert: Neuer Button für spiel3
        self.spiel3.size_hint = 0.3, 0.1
        self.spiel3.pos_hint = {"center_x" : 0.28, "center_y" : 0.35}
        self.add_widget(self.spiel3)
        self.spiel3.bind(on_press = arcade_pong_starten)

        self.back_button = Button(text = "BACK", font_name="GUI_Grafiken\\ka1.ttf", font_size=23, background_color = [0,0,0,0])
        self.back_button.size_hint = 0.3, 0.1
        self.back_button.pos_hint = {"center_x" : 0.9, "center_y" : 0.9}
        self.back_button.bind(on_press = back_button_click1)
        self.add_widget(self.back_button)

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

        self.back_button = Button(text = "BACK", font_name="GUI_Grafiken\\ka1.ttf", font_size=23, background_color = [0,0,0,0])
        self.back_button.size_hint = 0.3, 0.1
        self.back_button.pos_hint = {"center_x" : 0.9, "center_y" : 0.9}
        self.back_button.bind(on_press = back_button_click)
        self.add_widget(self.back_button)

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

        self.lautstärke_slider = Slider(min=0, max=1, value = App.get_running_app().music.volume)
        self.lautstärke_slider.size_hint = 0.3, 0.05
        self.lautstärke_slider.pos_hint = {"center_x" : 0.28, "center_y" : 0.70}
        self.add_widget(self.lautstärke_slider)

        def lautstärke_anpassung(instance, value):
            App.get_running_app().music.volume = value
        self.lautstärke_slider.bind(value = lautstärke_anpassung)

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

        self.musik1_button = Button(text ="Spaceship Arcade", font_name="GUI_Grafiken\\ka1.ttf", font_size=23, background_color = [0,0,0,0])
        self.musik1_button.size_hint = 0.3 , 0.1
        self.musik1_button.pos_hint = {"center_x" : 0.28, "center_y" : 0.4}
        self.musik1_button.bind(on_press = musik_wechsel1)
        self.add_widget(self.musik1_button)

        self.musik2_button = Button(text ="Retro Game Arcade", font_name="GUI_Grafiken\\ka1.ttf", font_size=23, background_color = [0,0,0,0])
        self.musik2_button.size_hint = 0.3 , 0.1
        self.musik2_button.pos_hint = {"center_x" : 0.28, "center_y" : 0.3}
        self.musik2_button.bind(on_press = musik_wechsel2)
        self.add_widget(self.musik2_button)

        self.musik3_button = Button(text ="8-bit Arcade Mode", font_name="GUI_Grafiken\\ka1.ttf", font_size=23, background_color = [0,0,0,0])
        self.musik3_button.size_hint = 0.3 , 0.1
        self.musik3_button.pos_hint = {"center_x" : 0.28, "center_y" : 0.2}
        self.musik3_button.bind(on_press = musik_wechsel3)
        self.add_widget(self.musik3_button)
        
        self.back_button = Button(text = "BACK", font_name="GUI_Grafiken\\ka1.ttf", font_size=23, background_color = [0,0,0,0])
        self.back_button.size_hint = 0.3, 0.1
        self.back_button.pos_hint = {"center_x" : 0.9, "center_y" : 0.9}
        self.back_button.bind(on_press = back_button_click1)
        self.add_widget(self.back_button)

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

        hintergrundbild_highscore = Video(source="Hintergrund_Bild.mp4", state="play", options={"eos":"loop"})
        hintergrundbild_highscore.allow_stretch = True
        hintergrundbild_highscore.keep_ratio = False
        self.add_widget(hintergrundbild_highscore)

        self.back_button = Button(text = "BACK", font_name="GUI_Grafiken\\ka1.ttf", font_size=23, background_color = [0,0,0,0])
        self.back_button.size_hint = 0.3, 0.1
        self.back_button.pos_hint = {"center_x" : 0.9, "center_y" : 0.9}
        self.back_button.bind(on_press = back_button_click1)
        self.add_widget(self.back_button)

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
        

class ArcadeProjektApp(App):
    DEBOUNCE_DELAY = 0.2

    def build(self):
        self.music = SoundLoader.load("GUI_Grafiken\\hintergrund_musik1.mp3")
        if self.music:
            self.music.loop = True
            self.music.volume = 0.01
            self.music.play()

        self.raspberry_pi = Raspberry()
        self._input_event = None

        self._last_press_time = {
            "w": 0, "s": 0, "a": 0, "d": 0, "escape": 0, "enter": 0
        }
        self._current_button_states = {
    "w": False, "s": False, "a": False, "d": False, "escape": False, "enter": False
}

        sm = ScreenManager()
        sm.add_widget(Intro1(name = "intro1"))
        sm.add_widget(Intro2(name = "intro2"))
        sm.add_widget(MainHauptmenüWidget(name = "hauptmenü"))
        sm.add_widget(CreditsWidget(name = "credits"))
        sm.add_widget(OptionenWidget(name = "optionen"))
        sm.add_widget(HighscoreWidget(name = "highscore"))
        sm.add_widget(Spiel_StartenWidget(name = "spiel_starten"))
        Clock.schedule_once(self._start_raspberry_input_reading, 0.2)
        return sm

    def _start_raspberry_input_reading(self, dt):
        self.start_raspberry_input()

    def start_raspberry_input(self):
        if not self.raspberry_pi.ser:
            self.raspberry_pi = Raspberry()
        if self._input_event is None:
            self._input_event = Clock.schedule_interval(self.raspberry_input_lesen, 0.1)

    def stop_raspberry_input(self):
        if self._input_event:
            self._input_event.cancel()
            self._input_event = None
    # 💥 Serielle Verbindung vollständig schließen:
        if self.raspberry_pi.ser:
            self.raspberry_pi.ser.close()
            self.raspberry_pi.ser = None

    
    def raspberry_input_lesen(self,data):
        if self.raspberry_pi.ser:
            line = self.raspberry_pi.readline()
            if line:
                self.process_raspberry_command(line)

    def process_raspberry_command(self, command_line):
        
        current_time = time.time()
        try:
            button_names = ["w", "s", "a", "d", "escape", "enter"]
            pressed_keys = command_line.strip().split(',') if command_line.strip() else []
            values = {key: (key in pressed_keys) for key in button_names}
            w_pressed = values["w"]
            s_pressed = values["s"]
            a_pressed = values["a"]
            d_pressed = values["d"]
            escape_pressed = values["escape"]
            enter_pressed = values["enter"]
            current_screen_name = self.root.current
            current_screen = self.root.get_screen(current_screen_name)

            if isinstance(current_screen, MainHauptmenüWidget):
                main_menu_layout = current_screen.layout
                buttons_order = [
                    main_menu_layout.spiel_starten_button,
                    main_menu_layout.highscore_button,
                    main_menu_layout.optionen_button,
                    main_menu_layout.credits_button
                ]
                
                if not hasattr(self, '_current_menu_button_index'):
                    self._current_menu_button_index = 0
                
                for i, btn in enumerate(buttons_order):
                    if i == self._current_menu_button_index:
                        btn.background_color = [1, 0, 0, 0.5]
                    else:
                        btn.background_color = [0, 0, 0, 0]

                if s_pressed and (current_time - self._last_press_time["s"]) > self.DEBOUNCE_DELAY:
                    self._last_press_time["s"] = current_time
                    self._current_menu_button_index = (self._current_menu_button_index + 1) % len(buttons_order)
                
                elif w_pressed and (current_time - self._last_press_time["w"]) > self.DEBOUNCE_DELAY:
                    self._last_press_time["w"] = current_time
                    self._current_menu_button_index = (self._current_menu_button_index - 1 + len(buttons_order)) % len(buttons_order)
                
                elif enter_pressed and (current_time - self._last_press_time["enter"]) > self.DEBOUNCE_DELAY:
                    self._last_press_time["enter"] = current_time
                    buttons_order[self._current_menu_button_index].dispatch('on_press')

            elif isinstance(current_screen, Spiel_StartenWidget):
                spiel_starten_layout = current_screen.layout
                spiel_buttons_order = [
                    spiel_starten_layout.spiel1,
                    spiel_starten_layout.spiel2,
                    spiel_starten_layout.spiel3
                ]
                if not hasattr(self, '_current_spiel_button_index') or self._current_spiel_button_index >= len(spiel_buttons_order):
                    self._current_spiel_button_index = 0
                
                for i, btn in enumerate(spiel_buttons_order):
                    if i == self._current_spiel_button_index:
                        btn.background_color = [1, 0, 0, 0.5]
                    else:
                        btn.background_color = [0, 0, 0, 0]

                if s_pressed and (current_time - self._last_press_time["s"]) > self.DEBOUNCE_DELAY:
                    self._last_press_time["s"] = current_time
                    self._current_spiel_button_index = (self._current_spiel_button_index + 1) % len(spiel_buttons_order)
                
                elif w_pressed and (current_time - self._last_press_time["w"]) > self.DEBOUNCE_DELAY:
                    self._last_press_time["w"] = current_time
                    self._current_spiel_button_index = (self._current_spiel_button_index - 1 + len(spiel_buttons_order)) % len(spiel_buttons_order)
                
                elif enter_pressed and (current_time - self._last_press_time["enter"]) > self.DEBOUNCE_DELAY:
                    self._last_press_time["enter"] = current_time
                    spiel_buttons_order[self._current_spiel_button_index].dispatch('on_press')

            elif isinstance(current_screen, OptionenWidget):
                optionen_layout = current_screen.layout
                
                if a_pressed and (current_time - self._last_press_time["a"]) > self.DEBOUNCE_DELAY: # Lautstärke leiser
                    self._last_press_time["a"] = current_time
                    optionen_layout.lautstärke_slider.value = max(0, optionen_layout.lautstärke_slider.value - 0.1)
                
                elif d_pressed and (current_time - self._last_press_time["d"]) > self.DEBOUNCE_DELAY: # Lautstärke lauter
                    self._last_press_time["d"] = current_time
                    optionen_layout.lautstärke_slider.value = min(1, optionen_layout.lautstärke_slider.value + 0.1)

                musik_buttons_order = [
                    optionen_layout.musik1_button,
                    optionen_layout.musik2_button,
                    optionen_layout.musik3_button
                ]
                if not hasattr(self, '_current_musik_button_index') or self._current_musik_button_index >= len(musik_buttons_order):
                    self._current_musik_button_index = 0

                for i, btn in enumerate(musik_buttons_order):
                    if i == self._current_musik_button_index:
                        btn.background_color = [1, 0, 0, 0.5]
                    else:
                        btn.background_color = [0, 0, 0, 0]

                if s_pressed and (current_time - self._last_press_time["s"]) > self.DEBOUNCE_DELAY:
                    self._last_press_time["s"] = current_time
                    self._current_musik_button_index = (self._current_musik_button_index + 1) % len(musik_buttons_order)
                
                elif w_pressed and (current_time - self._last_press_time["w"]) > self.DEBOUNCE_DELAY:
                    self._last_press_time["w"] = current_time
                    self._current_musik_button_index = (self._current_musik_button_index - 1 + len(musik_buttons_order)) % len(musik_buttons_order)
                
                elif enter_pressed and (current_time - self._last_press_time["enter"]) > self.DEBOUNCE_DELAY:
                    self._last_press_time["enter"] = current_time
                    musik_buttons_order[self._current_musik_button_index].dispatch('on_press')

            if escape_pressed and (current_time - self._last_press_time["escape"]) > self.DEBOUNCE_DELAY:
                self._last_press_time["escape"] = current_time
                if current_screen_name in ["credits", "optionen", "highscore", "spiel_starten"]:
                    if hasattr(current_screen.layout, 'back_button'):
                        current_screen.layout.back_button.dispatch('on_press')

        except ValueError as e:
            print(f"Fehler beim Parsen der Raspberry Pi Daten: {e}")
        except Exception as e:
            print(f"Ein unerwarteter Fehler ist aufgetreten: {e}")
    
    def musikauswahl(self, pfad):
        if self.music:
            self.music.stop()
        self.music = SoundLoader.load(pfad)
        if self.music:
            self.music.loop = True
            self.music.volume = 0.01
            self.music.play()

            

ArcadeProjektApp().run()