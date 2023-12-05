import re

def splitlines(line):
    find_doublepoint = line.find(':')
    find_pipe = line.find('|')
    gamenumber = int(line[:find_doublepoint].replace('Card ', '').strip())
    
    winning_number = re.findall(r'\d+',line[find_doublepoint+1:find_pipe].strip())
    voucher = re.findall(r'\d+',line[find_pipe+1:].strip())
    return gamenumber, winning_number, voucher
    
def get_winning_number(winning_number, voucher):
    count = 0
    for i in winning_number:
        if i in voucher:
            count += 1
    return count

def calc_points(wins):
    if wins == 0:
        return 0
    return 2**(wins-1)
         

if __name__ == '__main__':
    cards = {}
    with open('input') as f:
        lines = f.readlines()
        for line in lines:
            gamenumber, winning_number, voucher = splitlines(line)
            wins = get_winning_number(winning_number, voucher)
            cards[gamenumber] = {'count': 1, 'wins': wins }
    
    for nr, card in cards.items():
        print(f"Card {nr} has {card['count']} winning tickets and {card['wins']} winning numbers")        
        if card['wins'] >= 1:
            for i in range(1, card['wins']+1):
                if nr+i not in cards:
                    continue
                cards[nr+i]['count'] += card['count']
                print(nr, nr+i, cards[nr+i])

    sum = 0
    for card in cards.values():
        sum += card['count']
        
    print(sum)