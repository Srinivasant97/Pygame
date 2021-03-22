

import sys
from game import Game
def main():
    g= Game()
    g.run()
    sys.exit()
if __name__ == "__main__":
    main()
# clear the screen
# update the game
# draw the game

# 1) Behavior
# 2) constants
# 3) Data Definitions
# 4) functions

#
# """
#   Behaviors:
#     Game Over:
#       - snake hits the edge of the screen
#       - snake touches itself
#     Snake Movement:
#       - body trails its head
#     Snake:
#       - Eats an apple, grows by open
#     Score:
#       - How much food has been eaten
#     Menu Screen:
#       - Shows one time at the beginning
#       - disappears on any key press
#     Game over:
#       - Displays when snake hits wall or eats itself
#       - will go back a new game on any keypress
#     key input:
#       - arrow keys and wasd change snake direction
# """
#
# """
# Constants:
#   - Colors
#   - Window dimensions
#   - size of cells
#   - frame rate
#   - Cell width and cell height
# """

#
# def main():
#   game = Game()
#   game.run()
#   sys.exit()
#
# if __name__ == '__main__':
#     main()