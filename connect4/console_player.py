from .game import Grid, Player


class ConsolePlayer(Player):
    """Allow a human to see the grid in its shell, and input a column from the
    keyboard."""

    def play(self, grid: Grid) -> int:
        print(grid) #affiche la grille grâce au dunder __str__
        c=int(input("Please input the columns's number : ")) #demande a l utilisateur de saisir une valeur et la typecast
        return c #retourne la valeur saisie
