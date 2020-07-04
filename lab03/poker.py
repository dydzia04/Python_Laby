import random

class Karta:
    def __init__(self, figura, kolor):
        self.figura =figura
        self.kolor =kolor
        
    def show(self):
        print("('"+self.figura+"', '"+self.kolor+"')")
        
class Gracz:
    def __init__(self):
        self.cards = []
    
    def  __str__(self):
        karty = "["
        for k in self.cards:
            karty+="('"+k.figura+"', '"+k.kolor+"'),"
        karty = karty[:-1]
        karty+="]"
        return karty
        
    def show(self):
        for card in self.cards:
            card.show()
            
def Deck():
    talia =[]
    for kolor in ['Pik', 'Karo', 'Kier', 'Trefl']:
            for figura in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'D', 'K', 'A']:
                talia.append(Karta(figura,kolor))      
    return talia;

def show(deck):
    print("Talia :")
    for card in deck:
        card.show()

def shuffle_deck(deck):
    random.shuffle(deck)

def deal(deck,n):
    players = [Gracz() for i in range(n)]
        
    for i in range(5):
        for player in players:
            player.cards.append(deck.pop())
            
    return players

def histogram(tekst):
    dictionary = {}
    
    for character in tekst:
        if character != " ":
            if character in dictionary:
                dictionary[character] += 1
            else:
                dictionary[character] = 1
            
    return dictionary

def is_figura_sequence(hand):
    
    #order = ['2','3','4','5','6','7','8','9','10','J','D','K','A']
    order = ['A','K','D','J','10','9','8','7','6','5','4','3','2']
    
    cardIterator = order.index(hand[0].figura)#getting index of card in order[] of first card in hand
    
    inOrder=1#we take that order is correct at start
    #if there isn't 4 more cards after iterator its it not possible
    if cardIterator>len(order)-len(hand):
        cardIterator=0
        inOrder=0
        return inOrder
        
    for card in hand:#iterating thru whole cards
        #checking if card figura matches order[]
        if card.figura!=order[cardIterator]:
            inOrder=0
            
        cardIterator+=1
    
    return inOrder
    
    
#    print(set(kolejnosc).issubset())
    
def hand_figura(hand):
    
    hand_figura_list = []  # TODO: pobierz liste rang kart gracza. Uzyj listy skladanej.
    hand_kolor_list = [] # TODO: pobierz liste kolorow kart gracza. Uzyj listy skladanej.

    print("Cards:")
    for card in hand:
        hand_figura_list.append(card.figura)
        hand_kolor_list.append(card.kolor)
        print(card.figura+" "+card.kolor)
    
    print("---------DATA-----------")
    
    # histogramy rang kart graczy  okresla ile razy wystapila karta o tej samej randze,
    # potrzebne do ustalenia ukladu kart
    # TODO: uzyj funkcji 'histogram' z poprzedniego laboratorium!
    
    hand_figura_histogram = histogram(hand_figura_list)
    print("histogram figura: "+str(hand_figura_histogram.items()))
    print("histogram figura list: "+str(list(hand_figura_histogram.values())))
    
    # histogramy kolorow kart graczy, jesli 5 in hand_kolor_histogram.values() == True
    # to wszystkie karty sa jednego koloru
    
    hand_kolor_histogram = histogram(hand_kolor_list)
    print("histogram kolors: "+str(hand_kolor_histogram.items()))
    print("histogram kolors list: "+str(list(hand_kolor_histogram.items())))
    
    # czy karty sa "po kolei" (konieczne w: poker krolewski, pokerze, strit)
    # TODO: zaimplementuj funkcje is_figura_sequence(hand) ktora zwraca True jesli karty sa po kolei
    #       w przeciwnym razie zwraca false. Pobiera liste kart jako parametr
    
    is_hand_figura_sequence = is_figura_sequence(hand)
    print("is in order: "+str(is_hand_figura_sequence))

    hand_strength = 0 # zwracana zmienna, ja trzeba ustawic
    # ------ sprawdzamy uklad gracza 1:
    
    # --- sprawdzamy poker krolewski: 5 kart w tym samym kolorze, po kolei, najwyzsza to as
    #poker krolewski (Royal flush)
    if( (5 in hand_kolor_histogram.values()) and ( 'A' in hand_figura_list ) and is_hand_figura_sequence):
        hand_strength = 10
        
    # --- sprawdzamy poker: 5 kart w tym samym kolorze, po kolei
    #poker (Straight flush)
    elif( ( 5 in hand_kolor_histogram.values()) and is_hand_figura_sequence):
        hand_strength =  9
        
    # --- sprawdzamy kareta: 4 karty z tą samą wartościa
    #Kareta (Four of a kind)
    elif(4 == list(hand_figura_histogram.values())[0]):
        hand_strength =  8
        
    # --- sprawdzamy ful: 3 karty z tą samą wartościa, 2 karty z tą samą wartościa
    #ful (Full house)
    elif(3 == list(hand_figura_histogram.values())[0] and 2 == list(hand_figura_histogram.values())[1] or 3 == list(hand_figura_histogram.values())[1] and 2 == list(hand_figura_histogram.values())[0]):
        hand_strength =  7
        
    # --- sprawdzamy kolor: 5 kart z tym samym kolorem
    #kolor (flush)
    elif(5 in hand_kolor_histogram.values()):
        hand_strength =  6
        
    # --- sprawdzamy strit: 5 kart po sobie, conajmniej jedna w innym kolorze, dozwolone ('5','4','3','2','A')
    #strit (Straight)
    elif((is_hand_figura_sequence or hand[0].figura=='5' and hand[1].figura=='4' and hand[2].figura=='3' and hand[3].figura=='2' and hand[4].figura=='A') and 5 not in hand_kolor_histogram.values()):
        hand_strength = 5
    
    # --- sprawdzamy trojka: 3 karty z tą samą wartościa
    #trojka (Three of a kind)
    elif(3 in list(hand_figura_histogram.values())):
        hand_strength = 4
    
    # --- sprawdzamy dwie pary:2 x 2 karty z tą samą wartościa
    #dwie pary (Two pair)
    elif(2 == list(hand_figura_histogram.values())[0] and 2 == list(hand_figura_histogram.values())[1] or 2 == list(hand_figura_histogram.values())[1] and 2 == list(hand_figura_histogram.values())[2] or 2 == list(hand_figura_histogram.values())[0] and 2 == list(hand_figura_histogram.values())[2]):
        hand_strength = 3
    
    # --- sprawdzamy jedna pare: 2 karty z tą samą wartościa
    #jedna pare (One pair)
    
    
    elif(2 in hand_figura_histogram.values()):
        hand_strength = 2    
    
    # --- sprawdzamy wysoka karta: 2 karty z tą samą wartościa, 2 karty z tą samą wartościa
    #wysoka karta (High card)
    else:
        hand_strength = 1
        
    # TODO: za pomoca instrukcji elif oraz else sprawdz ponizsze warunki i ustaw
    #       wartosc zmiennej hand_strength:
    #        - sprawdzamy karete: 4 karty tej samej rangi
    #        - sprawdzamy full house: 3 karty tej samej rangi i 2 karty tej samej rangi
    #        - sprawdzamy kolor
    #        - sprawdzamy strit
    #        - sprawdzamy trojke 
    #        - sprawdzamy wysoka karte
    #        - sprawdzamy dwie pary
    #        - sprawdzamy jedna pare
    return(hand_strength)
    



talia = Deck()

shuffle_deck(talia)
show(talia)
players = deal(talia,2)
    
print()
for player in players:
    print("--------------------")
    print("Hand str: "+str(hand_figura(player.cards)))
    print("--------------------")
    