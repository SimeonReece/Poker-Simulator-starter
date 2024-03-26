import itertools, secrets
def create_deck():
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    # Use itertools.product to generate all possible combinations of ranks and suits
    deck = [{'rank': rank, 'suit': suit} for rank, suit in itertools.product(ranks, suits)]
    return deck
# Example usage:
deck_of_cards = create_deck()

def secure_shuffle_deck(deck):
    secrets.SystemRandom().shuffle(deck)

# Example usage:
my_deck = create_deck()
secure_shuffle_deck(my_deck)
print("\nSecurely shuffled deck:")
print(my_deck)

class GameFactory:
    def __init__(self, players):
        self.players = iter(players)
        self.current_player = next(self.players)
        self.community_cards = []

    def switch_player(self):
        self.current_player = next(self.players)

    def deal_community_cards(self, num_cards):
        for _ in range(num_cards):
            card = my_deck.pop()
            self.community_cards.append(card)

def deal_holdem_game(players, community_cards):
    for player in players:
        player['hand'] = [my_deck.pop(), my_deck.pop()]

    # This is where we will create wholecard function 
    print("\nInitial Hands:")
    for i, player in enumerate(players, start=1):
        print(f"Player {i} Hand: {player['hand']}")

# Example usage:
num_players = 9
# for now its just text. this will become an object for the game factory to use
players_list = [{'name': f'Player {i+1}'} for i in range(num_players)]

holdem_game = GameFactory(players_list)
community_cards = []

# Deal starting hands
deal_holdem_game(players_list, community_cards)

# Flop (deal 3 community cards)
print("\nCommunity Cards:")
holdem_game.deal_community_cards(5)
board = []
for i, card in enumerate(holdem_game.community_cards):
    board.append({'rank': card['rank'], 'suit': card['suit']})
    if i < 3:
        print(f"card {i+1}: {board[i]}")
    if i == 3: # the turn card should be separated for app needs
        print(f"card {i+1}: {board[i]}")
    if i == 4: # the river card should be separated for app needs
        print(f"card {i+1}: {board[i]}")
