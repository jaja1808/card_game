class Card:
    colour = ("spades", "hearts", "diamonds", "clubs")
    card_name = ("7", "8", "9", "10", "ace", "jack", "king", "queen")

    def __init__(self, card_name, colour):
        if card_name not in self.card_name:
            raise ValueError(f"Invalid card name: {card_name}. Allowed values are {self.card_name}")
        if colour not in self.colour:
            raise ValueError(f"Invalid card colour: {colour}. Allowed values are {self.colour}")

        self._card_name = card_name
        self._colour = colour
        self._asset_card = 0
        self._visible = 0

    def get_card_name(self):
        return self._card_name

    def get_colour(self):
        return self._colour

    def get_card_colour(self):
        return f"{self._card_name} of {self._colour} and {self._asset_card}"
    
    def set_card_name(self, card_name):
        if card_name not in self.card_name:
            raise ValueError(f"Invalid card name: {card_name}. Allowed values are {self.card_name}")
        self._card_name = card_name

    def set_colour(self, colour):
        if colour not in self.colour:
            raise ValueError(f"Invalid card colour: {colour}. Allowed values are {self.colour}")
        self._colour = colour
    def set_asset_card(self,colour):
        if colour not in self.colour:
            raise ValueError(f"Invalid card colour: {colour}. Allowed values are {self.colour}")
        if colour == self._colour:
            self._asset_card = 1
    def set_card_visible(self):
        self._asset_card = 1

class Game :
    jeu = []
    def create_game (self,jeu):
        for card_name in Card.card_name:
            for colour in Card.colour:
                card = Card(card_name, colour)
                jeu.append(card)

    def asset_colour (self,jeu,colour):
        [i.set_asset_card(colour) for i in jeu]


