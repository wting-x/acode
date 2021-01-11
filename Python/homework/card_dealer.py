# This program uses a dictionary as a deck of cards.
from random import shuffle

def main():
    # Create a deck of cards.
    deck = create_deck()

    # Deal the cards.
    deal_cards(deck)

# The create_deck function returns a dictionary
# representing a deck of cards.
def create_deck():
    # Create a dictionary with each card and its value
    # stored as key-value pairs.
    deck = {'Ace of Spades':11, '2 of Spades':2, '3 of Spades':3,
            '4 of Spades':4, '5 of Spades':5, '6 of Spades':6,
            '7 of Spades':7, '8 of Spades':8, '9 of Spades':9,
            '10 of Spades':10, 'Jack of Spades':10,
            'Queen of Spades':10, 'King of Spades': 10,

            'Ace of Hearts':11, '2 of Hearts':2, '3 of Hearts':3,
            '4 of Hearts':4, '5 of Hearts':5, '6 of Hearts':6,
            '7 of Hearts':7, '8 of Hearts':8, '9 of Hearts':9,
            '10 of Hearts':10, 'Jack of Hearts':10,
            'Queen of Hearts':10, 'King of Hearts': 10,

            'Ace of Clubs':11, '2 of Clubs':2, '3 of Clubs':3,
            '4 of Clubs':4, '5 of Clubs':5, '6 of Clubs':6,
            '7 of Clubs':7, '8 of Clubs':8, '9 of Clubs':9,
            '10 of Clubs':10, 'Jack of Clubs':10,
            'Queen of Clubs':10, 'King of Clubs': 10,

            'Ace of Diamonds':11, '2 of Diamonds':2, '3 of Diamonds':3,
            '4 of Diamonds':4, '5 of Diamonds':5, '6 of Diamonds':6,
            '7 of Diamonds':7, '8 of Diamonds':8, '9 of Diamonds':9,
            '10 of Diamonds':10, 'Jack of Diamonds':10,
            'Queen of Diamonds':10, 'King of Diamonds': 10}
    #Randomly disrupt the cards
    dict = {}
    key_list = list(deck.keys())
    shuffle(key_list)
    for x in key_list:
        dict[x] = deck[x]

    # Return the deck.
    return dict

# The deal_cards function deals a specified number of cards
# from the deck.

def deal_cards(deck):
    # Initialize an accumulator for the hand value.
    hand_value1 = 0
    card_list1 = []
    copy_list1 = []
    hand_value2 = 0
    card_list2 = []
    copy_list2 = []

    # Deal the cards and accumulate their values.
    #当所抽到的牌为A时，若A的值看作11时手中全部牌之和大于21，则将A的值看作1
    for count in range(int(len(deck)/2)):
        card1, value1 = deck.popitem()
        card2, value2 = deck.popitem()
        if hand_value1 > 21 and 'Ace' in card1:
            value1 = 1
        if hand_value2 > 21 and 'Ace' in card2:
            value2 = 1
        card_list1.append(card1)
        copy_list1.append(card1)
        hand_value1 += value1
        card_list2.append(card2)
        copy_list2.append(card2)
        hand_value2 += value2


        if hand_value1>21 or hand_value2>21:
            break

    # Display the value of the hand and show the winner
    print('Value of hand1:', hand_value1)
    print('Cards of hand1\t', copy_list1)
    print('Value of hand2:', hand_value2)
    print('Cards of hand2\t', copy_list2)
    if hand_value1 > 21 and hand_value2 > 21:
        print('No players wins!')
    elif hand_value1 > 21:
        print('Winner is hand2!')
    else:
        print('Winner is hand1!')

# Call the main function.
main()
