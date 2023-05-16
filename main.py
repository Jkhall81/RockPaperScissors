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


class HumanPlayer(Player):
    def move(self):
        while True:
            player_move = input('Rock, Paper, or Scissors? ').lower()
            if player_move in moves:
                return player_move
            else:
                print("You fucked something up!! Try again!")


class ReflectPlayer(Player):
    def __init__(self):
        super().__init__()
        self.opponent_move = None

    def move(self):
        if self.opponent_move is None:
            return random.choice(moves)
        return self.opponent_move

    def learn(self, my_move, their_move):
        self.opponent_move = their_move


class CyclePlayer(Player):
    def __init__(self):
        super().__init__()
        self.last_move = None

    def move(self):
        if self.last_move is None:
            return random.choice(moves)
        index = moves.index(self.last_move)
        return moves[(index + 1) % len(moves)]

    def learn(self, my_move, their_move):
        self.last_move = my_move


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
            print('Player 1 wins!\n')
            self.p1.increase_score()
        elif beats(move2, move1):
            print('Player 2 wins!\n')
            self.p2.increase_score()
        else:
            print("It's a tie!\n")

        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def score(self):
        score1 = self.p1.get_score()
        score2 = self.p2.get_score()
        print(f'Player 1 score: {score1}')
        print(f'Player 2 score: {score2}')
        if score1 > score2:
            print('Player 1 wins!!\n')
        elif score2 > score1:
            print('Player 2 wins!!\n')
        else:
            print('We have a tie!!\n')

    def play_game(self):
        print("Game start!")
        for game_round in range(3):
            print(f"Round {game_round + 1}:\n")
            self.play_round()
        self.score()
        print("Game over!")


if __name__ == '__main__':
    game = Game(HumanPlayer(), CyclePlayer())
    game.play_game()
