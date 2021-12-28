class Game:
    def __init__(self, id) -> None:
        # did players make theirs moves?
        self.p1Move = False 
        self.p2Move = False

        self.ready = False
        self.id = id # Game id / Room Id to connect players within a same game/room
        self.moves = [None, None] # store players' moves/choices

        self.wins = [0,0]
        self.ties = 0

    # param int p : 0, 1
    # return player's move
    def get_player_move(self, p):
        return self.moves[p]

    # update player status after player makes a move
    def play(self, player, move):
        self.moves[player] = move
        if player == 0:
            self.p1Move = True
        else:
            self.p2Move = True

    # check if both players are connected
    def connected(self):
        return self.ready

    # check if both players have made their moves
    def allMoved(self):
        return self.p1Move and self.p2Move

    # check players' moves to see who won
    def winner(self):
        # get first letter of 'Rock', 'Paper', 'Scissor'
        p1 = self.moves[0].upper() [0]
        p2 = self.moves[1].upper() [0]

        winner = -1
        if p1 == p2:
            pass
        elif p1 == "R" and p2 == "S":
            winner = 0
        elif p1 == "R" and p2 == "P":
            winner = 1
        elif p1 == "P" and p2 == "R":
            winner = 0
        elif p1 == "P" and p2 == "S":
            winner = 1
        elif p1 == "S" and p2 == "P":
            winner = 0
        elif p1 == "S" and p2 == "R":
            winner = 1

        return winner

    def reset(self):
        self.p1Move = False
        self.p2Move = False