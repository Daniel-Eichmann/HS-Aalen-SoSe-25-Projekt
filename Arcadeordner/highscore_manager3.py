import json
import os
DATEI=os.path.join(os.path.dirname(__file__), "autobahnspiel.json")
MAX_EINTRAEGE=10
def lade_autobahn_highscores():
    if os.path.exists(DATEI):
        with open(DATEI, "r") as f:
            return json.load(f)
        return []
def speichere_autobahn_highscore(score):
    eintraege=lade_autobahn_highscores()
    eintraege.append(score)
    eintraege=sorted(eintraege, reverse=True)[:MAX_EINTRAEGE]
    with open(DATEI, "w") as f:
        json.dump(eintraege, f)
def zeige_autobahn_highscores():
    eintraege=lade_autobahn_highscores()
    print("\nPlace Top 10 Punktezahlen (Autobahnspiel):")
    for i, punktezahl in enumerate(eintraege, start=1):
        print(f"Top {i}: hat {punktezahl} Punkte erreicht")