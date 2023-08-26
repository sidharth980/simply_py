
class xno:
    win = [
        [0,4,8],
        [2,4,6]]
    def __init__(self) -> None:
        self.bord = [x for x in range(9)]
        for x in range(3):
            win1 = []
            win2 = []
            for y in range(3):
                win1.append(x*3+y)
                win2.append(y*3+x)
            self.win.append(win1)
            self.win.append(win2)

    def play(self):
        plyr = "O"
        while not self.check_win():
            self.show()
            pos = int(input(f"Player {plyr} : "))
            if self.change(pos,plyr):
                if plyr == "O":
                    plyr = "X"
                else:
                    plyr = "O"
        self.show()

    
    def change(self,pos,plyr):
        if isinstance(pos,int):
            if pos <=8:
                if isinstance(self.bord[pos],int):
                    self.bord[pos] = str(plyr)
                    return True   
        return False
    
    def check_win(self):
        for x,y,z in self.win:
            if self.bord[x] == self.bord[y] == self.bord[z]:
                print(f"{self.bord[x]} Wins")
                return True
        for x in self.bord:
            if isinstance(x,int):
                return False
        print("Game Tie")
        return True
    
    def show(self):
        print("\n -------")
        for x in range(3):
            print(" ",end = "|")
            for y in range(3):
                if isinstance(self.bord[x*3+y],int):
                    print(" ",end = "|")
                else:
                    print(self.bord[x*3+y],end="|")
            print("\n -------")
    


gam = xno()
gam.play()
