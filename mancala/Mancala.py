from random import random


class Mancala:
    def __init__(self):
        self.p1_pits = [4, 4, 4, 4, 4, 4]
        self.p2_pits = [4, 4, 4, 4, 4, 4]
        self.p1_store = 0
        self.p2_store = 0
        self.labels = ["A", "B", "C", "D", "E", "F"]
        self.turn = self.first_turn_random() #1 for p1, 2 for p2

    def first_turn_random(self):
        return 2
        return round(random()) + 1

    def start(self):
        selection = self.get_input()
        if self.turn == 1:
            current_index = self.labels[::-1].index(selection)
            current_value = self.p1_pits[current_index]
            self.p1_pits[current_index] = 0 # we have removed all marbles from the current spot
            order = self.increment_board(current_index, current_value)
            self.decon_super_board(order, current_index)

        if self.turn == 2:
            current_index = self.labels.index(selection)
            current_value = self.p2_pits[current_index]
            self.p2_pits[current_index] = 0 # we have removed all marbles from the current spot
            order = self.increment_board(current_index, current_value)
            self.decon_super_board(order, current_index)


    def increment_board(self, current_index, current_value):
        order = self.make_super_board(current_index)
        counter = 0
        while current_value > 0:
            #print(order)
            if counter >= len(order):
                counter = 0
            order[counter] += 1
            current_value -= 1
            counter += 1
        return order

    def make_super_board(self, current_index):
        if self.turn == 1:
            return self.p1_pits[current_index + 1: len(self.p1_pits)] + [self.p1_store] + self.p2_pits[::-1] + \
                   [self.p2_store] + self.p1_pits[0:current_index + 1]
        if self.turn == 2:
            temp = self.p2_pits[current_index + 1: len(self.p2_pits)] + [self.p2_store] + self.p1_pits[::-1] + \
                   [self.p1_store] + self.p2_pits[0:current_index + 1]
            temp_last = [temp.pop(-1)]
            return temp[::-1] + temp_last

    def decon_super_board(self, new_board, current_index):
        print(new_board, current_index)
        if self.turn == 1:
            self.p1_pits = new_board[len(new_board) - current_index - 1:] + new_board[0:len(self.p1_pits) - current_index - 1]
            self.p1_store = new_board[len(self.p1_pits) - current_index - 1]
            self.p2_pits = new_board[len(self.p1_pits) - current_index: len(self.p1_pits) - current_index + len(self.p2_pits)][::-1]
            self.p2_store = new_board[len(new_board) - current_index - 2]
            self.toString()
        if self.turn == 2:

            ########## THE PROBELM IS HERE

            self.p2_pits = new_board[:current_index][::-1] + new_board[-1 * (len(self.p2_pits) - current_index):][::-1]
            self.p2_store = new_board[current_index]
            self.p1_pits = new_board[current_index + 1: len(self.p2_pits) + current_index + 1]
            self.p1_store = new_board[-1 * (len(self.p1_pits) - current_index + 1)]
            self.toString()

    def get_input(self):
        correct_input = False
        while not correct_input:
            selection = str(input("Player " + str(self.turn) + " enter the corresponding"
                                                               " letter you'd like to select: ")).upper()
            print("You selected: " + selection)

            if selection in self.labels:
                correct_input = True
            else:
                print("Invalid input. Please enter a valid character.")
        return selection

    def check_turn(self, old_board):
        pass

    def toString(self):
        print("---- Board ----")
        print("  " + str(self.labels).replace(",", "").replace("'", "")[1:-1])
        print("  " + str(self.p2_pits).replace(",", "")[1:-1])
        print(str(self.p2_store) + " " * 13 + str(self.p1_store))
        print("  " + str(self.p1_pits).replace(",", "")[1:-1])
        print("  " + str(self.labels[::-1]).replace(",", "").replace("'", "")[1:-1])
        print("---------------")
        print("Player {}'s turn.".format(self.turn))