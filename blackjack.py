from random import shuffle


def points(hand):
    ''' ([int]) -> int
    Returns the points of the cards you have in your hand

    >>> points([5,10,4])
     19 points
    '''
    if sum(hand) == 21:
        print('you have blackjack!')
        print(sum(hand))
        return sum(hand)

    elif sum(hand) > 21:
        print('you have busted!')
        print(sum(hand))
        return sum(hand)
    elif sum(hand) < 21:
        print(sum(hand))
        return sum(hand)


def blackjack():
    Ace = 11
    K = 10
    Q = 10
    J = 10
    cards = [
        Ace, Ace, Ace, Ace, K, K, K, K, Q, Q, Q, Q, J, J, J, J, 10, 10, 10, 10,
        9, 9, 9, 9, 8, 8, 8, 8, 7, 7, 7, 7, 6, 6, 6, 6, 5, 5, 5, 5, 4, 4, 4, 4,
        3, 3, 3, 3, 2, 2, 2, 2
    ]
    shuffle(cards)
    player_hand = [cards.pop(), cards.pop()]
    dealer_hand = [cards.pop(), cards.pop()]
    while True:
        print('Player\'s Turn')
        print(player_hand)
        response = input('Do wanna hit or stay:')
        if response == 'hit':
            player_hand.append(cards.pop())
        if points(player_hand) > 21:
            break
        elif points(player_hand) == 21:
            break
        elif response == 'stay':
            break
        else:
            print('please choose a valid option!')
            break
    while True:
        print('Dealer\'s Turn')
        if points(dealer_hand) < 17:
            print(dealer_hand)
            cards.pop()
            response = input('Do wanna hit or stay:')
        if response == 'hit':
            dealer_hand.append(cards.pop())
            print(dealer_hand)
            points(dealer_hand)
            break
        elif response == 'stay':
            pass


def main():
    blackjack()


if __name__ == '__main__':
    main()
