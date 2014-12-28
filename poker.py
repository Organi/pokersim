from card import Card
from deck import Deck

class Poker:
	def __init__(self):
		self.deck = Deck()

	





poker = Poker()

for i in range(0,52):
	print poker.deck.draw().toString()
