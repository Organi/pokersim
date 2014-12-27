import random
from card import Card

class Deck:
	deck = []

	def __init__(self):
		for suit in ['Clubs', 'Diamonds', 'Hearts', 'Spades']:
			for rank in ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10']:
				deck.append(Card(rank, suit))
		Deck.shuffle()

	def shuffle:
		random.shuffle(deck)
