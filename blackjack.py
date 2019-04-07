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
