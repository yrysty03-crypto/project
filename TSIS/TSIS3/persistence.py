import json

def load_leaderboard():
    try:
        with open("leaderboard.json") as f:
            return json.load(f)
    except:
        return []

def save_score(name, score):
    data = load_leaderboard()
    data.append({"name": name, "score": score})
    data = sorted(data, key=lambda x: x["score"], reverse=True)[:10]

    with open("leaderboard.json","w") as f:
        json.dump(data, f, indent=4)

def load_settings():
    try:
        with open("settings.json") as f:
            return json.load(f)
    except:
        return {"sound":True,"difficulty":"medium","car_color":"red"}

def save_settings(s):
    with open("settings.json","w") as f:
        json.dump(s,f,indent=4)