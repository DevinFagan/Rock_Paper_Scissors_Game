import random


class RockPaperScissorsGame:
    def __init__(self):
        self.username = ''
        self.playlist = ''
        self.scoreboard = {}
        self.win_conditions = {}
        self.user_input = ''
        self.computer_choice = ''

# Create a dictionary using the input in txt file and if it's a new player give them a 0 score
    def score_tracking(self):
        with open("rating.txt") as f:
            for line in f:
                (key, val) = line.split()
                self.scoreboard[key] = int(val)

        self.username = input("Enter your name:")
        print(f"Hello, {self.username}")

        if self.username not in self.scoreboard:
            self.scoreboard[self.username] = 0

# Allow customers to add their own game values. If left empty playlist = rock,paper,scissors
    def playlist_creation(self):
        self.playlist = input("Please choose the items you plan to play the game with (separate with commas)").split(
            ',')
        if self.playlist == ['']:
            self.playlist = ['rock', 'paper', 'scissors']

        print("Okay, let's start")

# Rotates the list and creates a win dictionary for the computer
    def list_convertor(self):
        the_playlist = self.playlist[self.playlist.index(self.computer_choice) + 1:] + \
                       self.playlist[:self.playlist.index(self.computer_choice)]
        strength = the_playlist[:(len(the_playlist) // 2)]
        self.win_conditions[self.computer_choice] = strength

# Takes user and computer input. Creates the win_conditions dictionary and awards points to the winner
    def game_creation(self):
        while True:
            self.user_input = input()
            self.computer_choice = random.choice(self.playlist)
            self.list_convertor()

            if self.user_input in self.playlist + ['!exit', '!rating']:

                if self.user_input in self.win_conditions[self.computer_choice]:
                    print(f"Well done. The computer chose {self.computer_choice} and failed")
                    self.scoreboard[self.username] += 100
                elif self.user_input in self.computer_choice:
                    print(f"There is a draw ({self.computer_choice})")
                    self.scoreboard[self.username] += 50
                elif self.user_input in '!rating':
                    print(f"Your rating: {self.scoreboard[self.username]}")
                elif self.user_input in '!exit':
                    print('Bye!')
                    break
                else:
                    print(f"Sorry, but the computer chose {self.computer_choice}")
            else:
                print("Invalid input")

    def main(self):
        self.score_tracking()
        self.playlist_creation()
        self.game_creation()


test = RockPaperScissorsGame()
test.main()
