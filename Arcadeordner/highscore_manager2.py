import json
import os

DATEI="labyrinth_highscores.json"
MAX_EINTRÄGE=10
def lade_highscores():
    if os.path.exists(DATEI):
        with open(DATEI, "r") as f:
            return json.load(f)
    else:
        return []
def speichere_highscore(zeit):
    einträge=lade_highscores()
    einträge.append(zeit)
    einträge=sorted(einträge, reverse=True)[:MAX_EINTRÄGE]
    with open(DATEI, "w") as f:
        json.dump(einträge, f)
def zeige_highscores():
    return lade_highscores
            