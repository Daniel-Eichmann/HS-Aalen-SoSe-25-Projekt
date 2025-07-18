import json
import os
DATEI=os.path.join(os.path.dirname(__file__), "Escapegame.json")
MAX_EINTRAEGE=10
def lade_highscores():
    if os.path.exists(DATEI):
        with open(DATEI, "r") as f:
            return json.load(f)
    else:
        return []
def speichere_highscore(zeit):
    eintraege=lade_highscores()
    eintraege.append(zeit)
    eintraege=sorted(eintraege, reverse=True)[:MAX_EINTRAEGE]
    with open(DATEI, "w") as f:
        json.dump(eintraege, f)
def zeige_highscores():
    eintraege=lade_highscores()
    print("\nPlace Top 10 Überlebenszeiten:")
    for i, zeit in enumerate(eintraege, start=1):
        print(f"Top {i}: hat {zeit} Sekunden überlebt")
if __name__=="__main__":
    speichere_highscore(30)
    speichere_highscore(25)
    zeige_highscores()