from .game import Grid, Player
from .game import Cell #Ajout de la classe Cell

class DumbIA(Player):
    def play(self, grid: Grid) -> int:
        i=0 # indice de boucle
        j=0 #indice de boucle
        # parcours de la grille
        for i in range(grid.lines) :
            for j in range(grid.columns) :
                if grid.grid[i][j]==Cell.EMPTY : #Test de case vide
                    return j #retourne l indice la colonne ou le jeton a ete place et quitte




