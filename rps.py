import random

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:

    # Instance initializer
    def __init__(self):
        # Score of the player
        self.score = 0
        # Move of the player
        self.mov = ''

    # Function to choose a move
    def move(self):
        # Always return "rock"
        self.mov = 'rock'
        return self.mov

    # Function to learn the move of opponent player
    def learn(self, player_one_move):
        pass

    # Function to check if user move beat opponent's move
    def beats(self, opp_move):
        return ((self.mov == 'rock' and opp_move == 'scissors') or
                (self.mov == 'scissors' and opp_move == 'paper') or
                (self.mov == 'paper' and opp_move == 'rock'))


class RandomPlayer(Player):

    # Instance initializer
    def __init__(self):
        # Call the super class initializer
        super().__init__()

    # Function to choose a move
    def move(self):
        # Select a move at random and return it
        self.mov = random.choice(moves)
        return self.mov

    # Function to learn the move of opponent player
    def learn(self, player_one_move):
        pass

    # Function to check if user move beat opponent's move
    def beats(self, opp_move):
        return ((self.mov == 'rock' and opp_move == 'scissors') or
                (self.mov == 'scissors' and opp_move == 'paper') or
                (self.mov == 'paper' and opp_move == 'rock'))


class ReflectPlayer(Player):

    # Instance initializer
    def __init__(self):
        # Call the super class initializer
        super().__init__()
        # Variable used for learning opponent's move
        self.reflect_move = ''

    # Function to choose a move
    def move(self):
        # Select a move if self.reflect_move is empty
        # and return it
        if self.reflect_move == '':
            self.mov = random.choice(moves)
            return self.mov
        else:
            # Let self.move equal self.reflect_move
            # and return it
            self.mov = self.reflect_move
            return self.mov

    # Function to learn the move of opponent player
    def learn(self, player_one_move):
        self.reflect_move = player_one_move

    # Function to check if user move beat opponent's move
    def beats(self, opp_move):
        return ((self.mov == 'rock' and opp_move == 'scissors') or
                (self.mov == 'scissors' and opp_move == 'paper') or
                (self.mov == 'paper' and opp_move == 'rock'))


class CyclePlayer(Player):

    # Instance initializer
    def __init__(self):
        # Call the super class initializer
        super().__init__()

    # Function to choose a move
    def move(self):
        if self.mov == '':
            self.mov = 'rock'
            return self.mov
        if self.mov == 'rock':
            self.mov = 'paper'
            return self.mov
        if self.mov == 'paper':
            self.mov = 'scissors'
            return self.mov
        if self.mov == 'scissors':
            self.mov = 'rock'
            return self.mov

    # Function to learn the move of opponent player
    def learn(self, player_one_move):
        pass

    # Function to check if user move beat opponent's move
    def beats(self, opp_move):
        return ((self.mov == 'rock' and opp_move == 'scissors') or
                (self.mov == 'scissors' and opp_move == 'paper') or
                (self.mov == 'paper' and opp_move == 'rock'))


class HumanPlayer(Player):

    # Instance initializer
    def __init__(self):
        # Call the super class initializer
        super().__init__()

    # Function to choose a move
    def move(self):
        while True:
            # Get mov from user
            self.mov = input("Rock, paper, scissors? > ").lower()
            # Check if mov is in moves list
            if self.mov in moves:
                return self.mov
                break

    # Function to learn the move of opponent player
    def learn(self, my_move, their_move):
        pass

    # Function to check if user move beat opponent's move
    def beats(self, opp_move):
        return ((self.mov == 'rock' and opp_move == 'scissors') or
                (self.mov == 'scissors' and opp_move == 'paper') or
                (self.mov == 'paper' and opp_move == 'rock'))


class Game:

    # Instance initializer
    def __init__(self, p1, p2):
        # Initialize the two player objects
        self.p1 = p1
        self.p2 = p2

    # Show winner to the console after game ends
    def displayWinner(self):
        print("*** TOTAL SCORE ***")
        print(f"PLAYER ONE: {self.p1.score}\nPLAYER TWO: {self.p2.score}")
        if self.p1.score > self.p2.score:
            print("PLAYER ONE WINS!")
        elif self.p1.score < self.p2.score:
            print("PLAYER TWO WINS")
        else:
            print("THE GAME ENDED IN A DRAW")

    # Check and print the winner to the console
    # at the end of each round
    def checkWinner(self, val1, val2):
        if val1 == val2:
            print("** TIE **")
            print(f"""Score: Player One {self.p1.score}, """ +
                  f"""Player Two {self.p2.score}""")
        elif val1:
            print("** PLAYER ONE WINS **")
            self.p1.score += 1
            print(f"""Score: Player One {self.p1.score}, """ +
                  f"""Player Two {self.p2.score}""")
        elif val2:
            print("** PLAYER TWO WINS **")
            self.p2.score += 1
            print(f"""Score: Player One {self.p1.score}, """ +
                  f"""Player Two {self.p2.score}""")

    # Play each round of game
    def play_round(self):
        # Player one to play
        player_one_move = self.p1.move()
        # Show to the console player one move
        print(f"You played {self.p1.mov}.")
        # Player two to play
        player_two_move = self.p2.move()
        # Learn the move of player one
        self.p2.learn(player_one_move)
        # Show to the console player two move
        print(f"Opponent played {self.p2.mov}.")
        # Check if player 1 beats player 2
        bool1 = self.p1.beats(self.p2.mov)
        # Check if player 2 beats player 1
        bool2 = self.p2.beats(self.p1.mov)
        # Check for winner
        self.checkWinner(bool1, bool2)

    # Function to print game status
    def game_start_end(self, game_status):
        print("====================")
        print("GAME " + game_status + "!")
        print("====================")

    # Play game based on number of rounds
    def play_game(self, numberOfRounds):
        self.game_start_end('START')
        # Play the game in numberOfRounds times
        for round in range(numberOfRounds):
            print(f"Round {round + 1} --:")
            self.play_round()
        # Print game status
        self.game_start_end('ENDS')
        # Display the winner
        self.displayWinner()


if __name__ == '__main__':
    # An empty list of opponent objects
    opponentObj = []
    # Append all opponent player object to the list
    opponentObj.append(Player())
    opponentObj.append(RandomPlayer())
    opponentObj.append(ReflectPlayer())
    opponentObj.append(CyclePlayer())
    # Ask user for the number of rounds to play the game
    while True:
        try:
            # ASk for the number of rounds
            numberOfRounds = input("How many rounds do you want to play? ")
            # Convert numberOfRounds to an int
            convertNum = int(numberOfRounds)
            if isinstance(convertNum, int):
                # Randomly choose an opponent player
                randomNumber = random.randint(0, 3)
                # Create a game object based on HumanPlayer and
                # randomly choosen object
                game = Game(HumanPlayer(), opponentObj[randomNumber])
                # Start the game
                game.play_game(convertNum)
                break
        except ValueError:
            # Let the user choose the right data type value
            print("Please enter the right number of rounds!")
            continue
