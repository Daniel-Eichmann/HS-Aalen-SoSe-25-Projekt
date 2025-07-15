import json
import os
BASE_PATH=os.path.join(os.path.dirname(__file__), "highscores")
def get_file_(autobahn):
    if not os.path.exists(BASE_PATH):
        os.makedirs(BASE_PATH)
    return os.path.join(BASE_PATH, f"{"autobahn"}.json")
def speichere_highscores(autobahn, name ,score):
    pfad=get_file_(autobahn)
    data=[]

    if os.path.exists(pfad):
        with open(pfad, "r") as f:
            try:
                data=json.load(f)
            except json.JSONDecodeError:
                pass
    data.append({"name": name, "score": score})
    data.sort(key=lambda x: x["score"], reverse=True)
    data=data[:10] #Top 10
    with open(pfad, "w") as f:
        json.dump(data, f, indent=2)
def load_highscores(Escapegame):
    pfad=get_file_(Escapegame)
    if not os.path.exists(pfad):
        return []
    with open(pfad, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []
            

