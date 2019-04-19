import random

Cards = ( "Ace", "2", "3", "4", "5", "6", "7","8", "9", "10", "Jack", "Queen", "King" )


class Player(object):

    #Class Object Attribute
    l = []
    sump = 0
    def __init__(self):
        pass

    def pick_card(self):
        return random.choice(Cards)


    def track_card(self, x):
        Player.l.append(x)

    def print_list(self):
        print Player.l

    def pick_another_card(self):
        ans = raw_input("Player1: Do you want to pick one more card? Enter 'y' or 'n'. ")
        if(ans == 'n' or ans == 'no' or ans == 'NO'):
            return
        elif(ans == 'y' or ans == 'yes' or ans == 'YES'):
            p3 = self.pick_card()
            self.track_card(p3)
            self.print_list()

    def sum(self):
        for card in Player.l:
            if(card == "Ace"):
                value1 = input('Found an Ace with Player. Consider as 1 or 11?')
                Player.sump += value1
            elif(card == "Jack" or card == "Queen" or card == "King"):
                Player.sump += 10
            else:
                value2 = int(card)
                Player.sump += value2
        return Player.sump

    
class Dealer(Player):

    #Class Object Attribute

    dl = []
    sumd = 0

    def __init__(self):
        Player.__init__(self)
        
    def track_card(self, x):
        Dealer.dl.append(x)

    def print_list(self):
        print Dealer.dl

    def pick_another_card(self):
        print 'Sum is less than 17. Picking another card for the dealer.'
        d3 = self.pick_card()
        self.track_card(d3)
        print 'Dealer:'
        self.print_list()

    def sum(self):
        Dealer.sumd = 0
        for card in Dealer.dl:
            if(card == "Ace"):
                value1 = input('Found an Ace with Dealer. Consider as 1 or 11?')
                Dealer.sumd += value1
            elif(card == "Jack" or card == "Queen" or card == "King"):
                Dealer.sumd += 10
            else:
                value2 = int(card)
                Dealer.sumd += value2


    def check_sum(self):

        while Dealer.sumd < 17:
            self.pick_another_card()
            self.sum()
        return Dealer.sumd

def result(arg1, arg2):
    if(arg2 > 21):
        print 'Player1 Busted!'
        return
    elif(arg1 > 21):
        print 'Dealer Busted!' 
        return
    elif(arg1 > arg2):
        print 'Dealer wins!'
        return
    elif(arg2 > arg1):
        print 'Player1 wins!'
        return
    else:
        print 'Tie between Player1 and Dealer.'

print 'Player1 vs Dealer'
print 'Distributing Cards:'
player1 = Player()
p1 = player1.pick_card()
player1.track_card(p1)
print 'Player 1: '
player1.print_list()

dealer1 = Dealer()
d1 = dealer1.pick_card()
dealer1.track_card(d1)
print 'Dealer:'
dealer1.print_list()


p2 = player1.pick_card()
player1.track_card(p2)
print 'Player 1: '
player1.print_list()

d2 = dealer1.pick_card()
dealer1.track_card(d2)

player1.pick_another_card()

print 'Dealer:'
dealer1.print_list()
dealer1.sum()
sum_dealer = dealer1.check_sum()
sum_player = player1.sum()

print 'Sum of Player:',sum_player
print 'Sum of Dealer:',sum_dealer
result(sum_dealer, sum_player)
