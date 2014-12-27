class Card:
	def __init__(self, rank, suit):
		self.suit = suit
		self.rank = rank

	def getSuit(self):
		return self.suit

	def getRank(self):
		return self.rank

	def getValue(self):
		if self.rank.lower() == 'ace':
			return 1
		elif self.rank.lower() in ["jack","queen","king"]:
			return 10
		else:
			return int(self.rank)
