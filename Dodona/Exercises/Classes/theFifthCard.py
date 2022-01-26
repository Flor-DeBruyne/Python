class Card:

    data_suit = ["clubs", "diamonds", "hearts", "spades"]
    data_rank = {"ace":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "knight":11, "queen":12, "king":13}

    def __init__(self, rank, suit):
        if rank in self.data_rank and suit in self.data_suit:
            self.rank = rank
            self.suit = suit
            self.rank_int = list(self.data_rank.values())[list(self.data_rank).index(rank)]
        else:
            raise AssertionError('invalid card')
    
    def __str__(self):
        return f"{self.rank} of {self.suit}"

    def __repr__(self):
        return f"Card(rank='{self.rank}', color='{self.suit}')"

    def __eq__(self, other):
        if isinstance(other, Card):
            if self.suit == other.suit:
                return self.rank_int == other.rank_int , self.rank_int
            return self.rank_int == other.rank_int if self.suit == other.suit else False  

    def __lt__(self, other):
        if isinstance(other, Card):
            if self.suit == other.suit:
                return self.rank_int < other.rank_int 
            return self.rank_int < other.rank_int if self.suit < other.suit else False  

    def __ne__(self, other):
        if isinstance(other, Card):
            if self.suit == other.suit:
                return self.rank_int != other.rank_int
            return self.rank_int != other.rank_int if self.suit != other.suit else False  

    def __le__(self, other):
        if isinstance(other, Card):
            if self.suit == other.suit:
                return self.rank_int <= other.rank_int
            return self.rank_int <= other.rank_int if self.suit <= other.suit else False  

    def __gt__(self,other):
        if isinstance(other, Card):
            if self.suit == other.suit:
                return self.rank_int > other.rank_int
            return self.rank_int > other.rank_int if self.suit > other.suit else False  
    
    def __ge__(self, other):
        if isinstance(other, Card):
            if self.suit == other.suit:
              return self.rank_int >= other.rank_int
            return self.rank_int >= other.rank_int if self.suit >= other.suit else False  

    # def fifthCard(self, list_card):
    
        