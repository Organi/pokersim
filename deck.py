import random
from card import Card

class Deck:
	deck = []

	def __init__(self):
		for suit in ['Clubs', 'Diamonds', 'Hearts', 'Spades']:
			for rank in ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']:
				self.deck.append(Card(rank, suit))
		#self.shuffle()

	def shuffle(self):
		random.shuffle(self.deck)

	def draw(self):
		return self.deck.pop()
