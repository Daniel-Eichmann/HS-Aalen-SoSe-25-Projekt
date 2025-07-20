import json
import os
DATEI=os.path.join(os.path.dirname(__file__), "escapegame.json")
MAX_EINTRAEGE=10
def lade_highscores():
    if os.path.exists(DATEI):
        try:
            with open(DATEI, "r") as f:
                return json.load(f)
        except:
            return []
    return []
def speichere_highscore(zeit):
    einträge=lade_highscores()
    einträge.append(zeit)
    einträge=sorted(einträge, reverse=True)[:MAX_EINTRAEGE]
    with open(DATEI, "w") as f:
        json.dump(einträge, f)
def zeige_highscores():
    einträge = lade_highscores()
    print("\nTop 10 Highscores (Labyrinthspiel):")
    for i, zeit in enumerate(einträge, start=1):
        print(f"Platz {i}: {zeit} Sekunden")