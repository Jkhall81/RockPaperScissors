import random
"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def __init__(self):
        self.score = 0

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass

    def increase_score(self):
        self.score += 1

    def get_score(self):
        return self.score


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")

        if beats(move1, move2):
            print('Player 1 wins!')
            self.p1.increase_score()
        elif beats(move2, move1):
            print('Player 2 wins!')
            self.p2.increase_score()
        else:
            print("It's a tie!")

        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def score(self):
        score1 = self.p1.get_score()
        score2 = self.p2.get_score()
        print(f'Player 1 score: {score1}')
        print(f'Player 2 score: {score2}')

    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"Round {round + 1}:")
            self.play_round()
        self.score()
        print("Game over!")


if __name__ == '__main__':
    game = Game(RandomPlayer(), RandomPlayer())
    game.play_game()
