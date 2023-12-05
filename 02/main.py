maxcubes = {
    'red': 12,
    'blue': 14,
    'green': 13,
}

def parse_games(input_text):
    games = {}
    
    # Split the input text into individual games
    
    find_separator = input_text.find(':')
    
    game_strings = input_text[find_separator+1:].split(';')
    game_nr = int(input_text[:find_separator].replace('Game ',''))
    for i, game_str in enumerate(game_strings):
        results = [item.strip().split() for item in game_str.split(',')]
        
        # Create a dictionary entry for each game
        game_data = {}
        for team_result in results:
            team = team_result[1]
            count = int(team_result[0])
            game_data[team] = count
        
        games[i] = game_data
    
    return game_nr, games


def check_line(parts):
    for part in parts:
        if part in maxcubes:
            if parts[part] > maxcubes[part]:
                return False
    return True

def get_max_cubes(plays):
    max_cubes = {
        'red': [],
        'blue': [],
        'green': [],
    }
    for play in plays.values():
        for part in play:
            max_cubes[part].append(play[part])
    return {
        'red': max(max_cubes['red']),
        'blue': max(max_cubes['blue']),
        'green': max(max_cubes['green']),
    }

if __name__ == '__main__':

    with open('input') as f:
        lines = f.read().splitlines()

    sum = 0
    for line in lines:
        games, parts = parse_games(line)
        invalid = False
        for part in parts:
            if not check_line(parts[part]):
                invalid = True
                break
        if not invalid:
            sum += games
    print('Sum: {}'.format(sum))
    sum = 0
    for line in lines:
        games, parts = parse_games(line)        
        max_cubes = get_max_cubes(parts)
        sum += max_cubes['red']*max_cubes['blue']*max_cubes['green']
    print('Sum: {}'.format(sum))