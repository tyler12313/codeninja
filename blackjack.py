import display
import random


class card:
    def __init__(self,suit,rank,value):
        self.suit = suit
        self.rank = rank
        self.value = value
        self.facedown = False
        
    def print_card(self):
        print('['+self.rank + 'of' + self.suit + ']')
        
class game:
    def __init__(self,init_reserves, win_condition):
        pass
    def setup(self):
        pass
    def phase0(self):
        pass
    def phase1(self):
        pass
    def draw(self):
        pass
    def calculate_score(self,score1,score2):
        pass
        
class player:
    def __init(self,name,reserves,dealer=False):
        self.hand = []
        self.reserves = reserves
        self.name = name
    def setup(self):
        pass
    def get_score(self):
        pass
    
def new_deck():
    deck = []
    suits = ['\u2664','\u2661','\u2667','\u2662']
    ranks = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    values = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    for i in suits:
        for r, v in zip(ranks,values):
            deck.append(card(i,r,v))
            
    return deck

def getscore(deck):
    score = 0
    for card in deck:
        if card.rank == "A":
            score += cal_ace(score)
        else:
            score += card.value
        
    return score

def dealer_cards():
    dealerscore = getscore(dealer_deck)
    while True:
        if dealerscore > 16:
            break
        dealer_deck.append(deck.pop())
        dealerscore = getscore(dealer_deck)

def cal_ace(score):
    if score+11 > 21:
        return(1)
    else:
        return(11)
        

money = 500
dealerscore = 0
deck = []
player_deck = []
dealer_deck = []
deck.extend(new_deck())
deck.extend(new_deck())
deck.extend(new_deck())
random.shuffle(deck)
#print(len(deck))
#deck.pop().print_card()
#deck.pop().print_card()
#print(len(deck))

#print(len(deck))
#display.display_cards([deck.pop(),deck.pop()])
#print(len(deck))

print("get 5000 dollars to win")
while True:
    dealer_deck = []
    player_deck = []
    dealer_deck.append(deck.pop())
    dealer_deck.append(deck.pop())
    print("dealer\n")
    dealer_deck[1].facedown = True
    display.display_cards(dealer_deck)
    
    print("player\n")
    
    print("how much you wanna bet\n you currently got",money,"dollars")
    
    while True:
        bet = int(input())
        if bet > money:
            print("nuh uh lil bro try again")
        else:
            break
        
    money -= bet
    
    while True:
    
        print("hit or stand")
        answer = input()
        if answer == "hit":
            
            player_deck.append(deck.pop())
            display.display_cards(player_deck)
            playerscore = getscore(player_deck)
            print(playerscore)
            if playerscore >21:
                print("you lost haha")
                break
        if answer == "stand":
            playerscore = getscore(player_deck)
            print(playerscore)
            dealer_deck[1].facedown = False
            dealer_cards()
            print("dealer")
            display.display_cards(dealer_deck)
            dealerscore = getscore(dealer_deck)
            print(dealerscore)
            if playerscore < 22 and playerscore > dealerscore:
                print("you win wowzer")
                money += 2 * bet
            elif dealerscore > 21:
                print("you win wowzer")
                money += 2 * bet
            elif dealerscore == playerscore:
                print("its a draw harhar")
            elif dealerscore == playerscore == 21:
                print("bro what in the bombodino crocodino is happening idk what to say man")
            else:
                print("you lose haha")
            break
                
    
    if money <= 0:
        print("lmao bankrupt imagine")
        break
    print("ya got",money,"dollars now")
    if money > 5000:
        print("wow you beat the game good job")
        break
    playagain = input("play again? (y to play again)")
    if playagain == "y":
        pass
    else:
        print("oh alr then")
        break
    
    

#dealer action
# reveal both card
# count total points

