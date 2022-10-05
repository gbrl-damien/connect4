from .game import Grid, Player, Cell


class CheaterB(Player):
    """This IA cheats and modify the grid to ensure player B wins."""

    def play(self, grid: Grid) -> int:
        #on remplace la grille actuelle par un grille gagnante pour B 
        
        for j in range(1,grid.columns-1) : #remplace les colones de la premiere ligne
            grid.place(j,Cell.B) #le joueur B joue 'O'          
        
        return 6
