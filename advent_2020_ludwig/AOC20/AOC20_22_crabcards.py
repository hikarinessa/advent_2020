# https://adventofcode.com/2020/day/22

from copy import deepcopy as deep

debug = False
printit = False
part2 = True
testinfinite = True

def p(text = "", override = False): #prints as string 
    if debug or printit or override:
        print(text, flush=True)
def pp(subject, name = "", override = False): #prints anything with a name as string 
    if debug or printit or override:
        #print("\n", name, ": ", subject)
        #   print()
        print(name, ": ", subject)
def ppp(subject, name = "", override = False, isDictionary=False): #prints list entries
    if debug or printit or override:
        #print("\n", name, ": ", subject)
        print()
        print(name, ": ")
        for item in subject:
            if isDictionary:
                print(item, ":", end="")
                print(subject[item])
            else:
                print(item)
def pppp(subject, name = "", override = False, isDictionary=False): #prints list's list entries
    if debug or printit or override:
        #print("\n", name, ": ", subject)
        print()
        print(name, ": ")
        for item in subject:
            if isDictionary:
                print(item, ":", end="")
                print(subject[item])
            else:
                for tile in item:
                    print()
                    for line in tile: 
                        print(line)

print("\n----------------------------------")   # reading file

DATA = """Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10"""

if not debug:
    file = "advent_2020_ludwig/AOC20/DATA_aoc20_22.txt"
    with open(file) as f:
        DATA = f.read()
if debug and testinfinite and part2:
    DATA = """Player 1:
43
19

Player 2:
2
29
14"""


winner = ""
winner_score = 0
deck1, deck2 = [[int(c) for c in d.split("\n")[1:]] for d in DATA.split("\n\n")]
pp(deck1), pp(deck2)

def turn(deck1, deck2):
    pp(deck1, "Player 1's deck")
    pp(deck2, "Player 2's deck")
    card1, card2 = deck1.pop(0), deck2.pop(0)
    pp(card1, "Player 1 plays")
    pp(card2, "Player 2 plays")
    if card1 > card2:
        deck1.append(card1)
        deck1.append(card2)
        pp("Player 1 wins this round", "Result")
    else:
        deck2.append(card2)
        deck2.append(card1)
        pp("Player 2 wins this round", "Result")
    return deck1, deck2

def score(deck):
    score = 0
    multiplier = len(deck)
    for i, card in enumerate(deck):
        score += card * (multiplier - i)
    return score

turns = 0
deck1part1, deck2part1 = deep(deck1), deep(deck2)

if not part2:
    while len(deck1part1) > 0 and len(deck2part1) > 0:
        
        turns += 1
        pp(turns, "Turn")
        deck1part1, deck2part1 = turn(deck1part1, deck2part1)
        #pp(deck1part1), pp(deck2part1)

    if len(deck1part1) == 0:
        winner = "Player 2"
        winner_score = score(deck2part1)
    else:
        winner = "Player 1"
        winner_score = score(deck1part1)

    print(f"\nPart1: {winner} won with a score of {winner_score}! The game lasted {turns} turns.")


# ------ Part 2 -----------

def subgame(deck1, deck2):
    global _GAMES, _PAIRS, _TURNS
    turns = 0
    subgame_winner = ""
    subgame_score = 0
    _GAMES += 1
    _PAIRS[_GAMES] = [] # clearing turn memory if game starts on the same sub-level that was finished before

    pp(f"=================== Game {_GAMES} ==================", "", True)

    while len(deck1) > 0 and len(deck2) > 0:
        _TURNS += 1
        turns += 1
        p(f"\nGame {_GAMES}, Turn {turns}")

        turn_memory = "+".join([",".join(str(c) for c in deck1), ",".join(str(b) for b in deck2)])
        pp(turn_memory, "memory of current turn and decks")

        if turn_memory not in _PAIRS[_GAMES]:  # configuration of decks is joined to string and written to a dictionary entry per game
            _PAIRS[_GAMES].append(turn_memory) # to prevent infinite looping
        else:
            p("loop protector triggered") 
            subgame_winner = "Player 1" 
            subgame_score = score(deck1)
            break  

        deck1, deck2 = turn_rec(deck1, deck2)


    if subgame_winner == "":

        if len(deck1) == 0:
            subgame_winner = "Player 2"
            subgame_score = score(deck2)

        else:
            subgame_winner = "Player 1"
            subgame_score = score(deck1)

    pp(subgame_winner, f"Winner of game {_GAMES}")
    return subgame_winner, subgame_score

def turn_rec(deck1, deck2):
    global _GAMES
    pp(deck1, "Player 1's deck")
    pp(deck2, "Player 2's deck")
    card1, card2 = deck1.pop(0), deck2.pop(0)
    pp(card1, "Player 1 plays")
    pp(card2, "Player 2 plays")

    if card1 <= len(deck1) and card2 <= len(deck2):
        
        pp("Starting sub-game...")
        subwinner, subscore = subgame(deck1[:card1], deck2[:card2])

        if subwinner == "Player 1":
            deck1.append(card1)
            deck1.append(card2)
            pp("Player 1 wins this sub-game round", "Result")

        else:
            deck2.append(card2)
            deck2.append(card1)
            pp("Player 2 wins this sub-game and round", "Result", True)

        _GAMES -= 1 # decrementing game id after subgame is finished to return to appropriate turn memory
        pp(f"========== Game {_GAMES} ============", "Back to", True)

    else:
        if card1 > card2:
            deck1.append(card1)
            deck1.append(card2)
            pp("Player 1 wins this round", "Result")
        else:
            deck2.append(card2)
            deck2.append(card1)
            pp("Player 2 wins this round", "Result")                
    return deck1, deck2

pp("="*100)

_PAIRS = {}
_TURNS = 0
_GAMES = 0
deck1part2, deck2part2 = deep(deck1), deep(deck2)

winner, winner_score = subgame(deck1part1, deck2part1)

print(f"\nPart 2: {winner} won with a score of {winner_score}! The game lasted {_TURNS} turns.")