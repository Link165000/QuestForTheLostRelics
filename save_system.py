def save_player_data(player_data):
    with open('player_data.json', 'w') as f:
        json.dump(player_data, f)

def load_player_data():
    try:
        with open('player_data.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_game_state(game_state):
    with open('game_state.json', 'w') as f:
        json.dump(game_state, f)

def load_game_state():
    try:
        with open('game_state.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
