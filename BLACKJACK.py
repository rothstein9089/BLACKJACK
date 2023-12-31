import random

print('Welcome to BLACKJACK. Play againts the computer!\n')

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
random.shuffle(cards)


class Players:
    def __init__(self):
        self.user_hand = random.sample(cards, 2)
        self.comp_hand = random.choice(cards)

    def draw_card(self):
        card = random.choice(cards)
        return card


players = Players()


class Game:

    def player_turn(self):
        while True:
            if sum(players.user_hand) == 21:
                break
            else:
                pass

            if sum(players.user_hand) < 21:
                choice = input("would you like another card? ").lower()
                if choice == 'y':
                    add = int(players.draw_card())
                    players.user_hand.append(add)
                    print(f"You have {players.user_hand}")
                else:
                    break
            elif sum(players.user_hand) > 21:
                break
            else:
                pass

    def comp_turn(self):
        while True:
            draw = players.draw_card()
            players.comp_hand += draw

            if players.comp_hand == 21:
                break
            elif players.comp_hand > 21:
                break
            elif players.comp_hand in [17, 18, 19, 20]:
                break
            else:
                continue

    def tally_total(self):
        print(f'Your hand is {players.user_hand}')
        print(f'The computer has {players.comp_hand}\n')

        game.player_turn()
        game.comp_turn()

        total_user_hand = sum(players.user_hand)

        if players.comp_hand == 21:
            print(f'Comp won! with a {players.comp_hand}')
        elif total_user_hand == 21:  # Compare the total hand value with 21
            print(f'User won! with a {players.user_hand}')
        elif total_user_hand > 21:  # Compare the total hand value with 21
            print(f'Comp won! with a {players.comp_hand}. You had {players.user_hand}')
        elif players.comp_hand > 21:
            print(f'User won! with a {players.user_hand}. The computer had {players.comp_hand}')
        elif total_user_hand > players.comp_hand:
            print(f'User won with a {players.user_hand}. Comp had {players.comp_hand}')
        else:
            print(f'Comp won with a {players.comp_hand}. User had {[players.user_hand]}')


game = Game()
game.tally_total()


