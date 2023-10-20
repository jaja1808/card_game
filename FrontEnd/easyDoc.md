Key classes for a Belote game with Pygame

Game:

- Initializes pygame, creates window, loads assets
- Manages various game states like bidding, playing, scoring
- Tracks global game logic like current trick, lead suit
- Contains Player objects and Deck
- Handles events like clicks, keypresses
- Updates graphics each frame in game loop

Player:

- Attributes like name, team, points, AI or human
- Keeps track of hand using Hand object
- Makes bids and plays cards
- AI players have logic to choose bids and card plays
- Human players read inputs to get moves

Deck:

- Initializes full deck of Card objects
- Shuffle() method mixes up order
- Deal() method deals cards to players
- Keep track of cards remaining

Card:

- Suit, rank, and image attributes
- Method to draw itself on screen
- Knows point value for scoring
- Trump cards have override logic

Hand:

- Group of cards belonging to a Player
- Update as cards played, new cards drawn
- Logic to pick valid plays for turn

Trick:

- Stores cards played in current trick
- Evaluates winner based on suit leads and follows
- Awards trick points once complete

BidBox:

- Displays bid selection options
- Reads player's bid choice as input
- Communicates bid to Game class

InfoPanel:

- UI element that displays scores and game status
- Text updated as game state changes
