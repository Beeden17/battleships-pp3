import random

class BattleshipGame:
    def __init__(self):
        # Set game parameters
        self.grid_size = 5
        self.num_ships = 4
        # Set grid for user and computer
        self.user_grid = [['O' for _ in range(self.grid_size)] for _ in range(self.grid_size)]
        self.computer_grid = [['O' for _ in range(self.grid_size)] for _ in range(self.grid_size)]
        # Generate ships for user and computer
        self.user_ships = self.generate_ships()
        self.computer_ships = self.generate_ships()

    def generate_ships(self):
        # Generate ship locations at random
        ships = []
        for _ in range(self.num_ships):
            ship_row = random.randint(0, self.grid_size - 1)
            ship_col = random.randint(0, self.grid_size - 1)
            # Make sure ships do not overlap
            while (ship_row, ship_col) in ships:
                ship_row = random.randint(0, self.grid_size - 1)
                ship_col = random.randint(0, self.grid_size - 1)
            ships.append((ship_row, ship_col))
        return ships

    def print_grids(self):
        # Print both user's and computer's grids side by side
        print("  Your Grid             Computer's Grid")
        print("  " + " ".join([str(i) for i in range(self.grid_size)]) + "    " + " ".join([str(i) for i in range(self.grid_size)]))
        for i in range(self.grid_size):
            print(i, end=" ")
            for j in range(self.grid_size):
                print(self.user_grid[i][j], end=" ")
            print("  ", end="")
            print(i, end=" ")
            for j in range(self.grid_size):
                print(self.computer_grid[i][j], end=" ")
            print()

    def user_play(self):
        # Function for user's turn
        print("Welcome to Battleships!")
        print("_______________________")
        print("Sink all the computer's ships before yours are found to win!")
        print("____________________________________________________________")
        # Print user's grid
        self.print_grids()
        # Loop until all computer ships are defeated
        while True:
            try:
                # Get the user's guess
                guess_row = int(input("Enter the row to guess (0-4): "))
                guess_col = int(input("Enter the column to guess (0-4): "))
            except ValueError:
                print("Please enter a valid row and column (0-4).")
                continue
            
            # Check if the guess is within parameters
            if guess_row < 0 or guess_row >= self.grid_size or guess_col < 0 or guess_col >= self.grid_size:
                print("Please enter a valid row and column (0-4).")
                continue

            # Check if user hit a ship
            if (guess_row, guess_col) in self.computer_ships:
                print("Congratulations! You hit a ship!")
                self.user_grid[guess_row][guess_col] = 'X'
                self.computer_ships.remove((guess_row, guess_col))
                self.print_grids()
                if len(self.computer_ships) == 0:
                    print("Congratulations! You sunk all the computer's ships!")
                    break
            else:
                print("Sorry, you missed!")
                self.user_grid[guess_row][guess_col] = '-'
                self.print_grids()

    def computer_play(self):
        # Function for computer's turn
        print("Computer's turn...")
        # Loop until all user's ships are defeated
        while True:
            # Generate computer selection
            guess_row = random.randint(0, self.grid_size - 1)
            guess_col = random.randint(0, self.grid_size - 1)

            # Check if computer hit a ship
            if (guess_row, guess_col) in self.user_ships:
                print("Computer hit one of your ships!")
                self.computer_grid[guess_row][guess_col] = 'X'
                self.user_ships.remove((guess_row, guess_col))
                self.print_grids()
                if len(self.user_ships) == 0:
                    print("Oh no! The computer sunk all your ships! You lose!")
                    break
            else:
                print("Computer missed!")
                self.computer_grid[guess_row][guess_col] = '-'
                self.print_grids()
                break

if __name__ == "__main__":
    game = BattleshipGame()
    game.user_play()
    game.computer_play()