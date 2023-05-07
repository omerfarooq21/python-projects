import os
from time import sleep
def sum(a,b,c) -> int: 
    return a+b+c

def m(x,y,v) -> str:
    return '❌' if Xstate[v]==1 else ('⚽️' if Zstate[v] == 1 else v)

def print_board(x,y):
    print(f"| {m(x,y,0)} | {m(x,y,1)} | {m(x,y,2)}|")
    print(f"|__|__|__|")
    print(f"| {m(x,y,3)} | {m(x,y,4)} | {m(x,y,5)}|")
    print(f"|__|__|__|")
    print(f"| {m(x,y,6)} | {m(x,y,7)} | {m(x,y,8)}| \n\n")

def checkwin(x,y):
    wins =[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[6,4,2]]
    
    for win in wins:
        if(sum(x[win[0]],x[win[1]],x[win[2]])==3):
            print("🎉 ❌ Won the match 🎉")
            return 1
        if(sum(y[win[0]],y[win[1]],y[win[2]])==3):
            print("🎉 ⚽️ Won the match 🎉")
            return 0
        if((x[0]+x[1]+x[2]+x[3]+x[4]+x[5]+x[6]+x[7]+x[8]+y[0]+y[1]+y[2]+y[3]+y[4]+y[5]+y[6]+y[7]+y[8])==9):
            print("Match Tie 😜")
    return -1


    
if __name__ == "__main__":
    games = ['Tic','   Tac','\tToe']
    os.system('clear')

    for game in games:
        print(game)
        sleep(1)

    Xstate = [0,0,0,0,0,0,0,0,0]
    Zstate = [0,0,0,0,0,0,0,0,0]
    turn = 1
    while(True):
        print_board(Xstate, Zstate)
        if(turn==1):
            print("❌ turn")
            value = int(input("enter a value : "))
            Xstate[value] = 1 
        if(turn == 0):
            print("⚽️ turn")
            value = int(input("enter a value : "))
            Zstate[value] = 1
        cwin = checkwin(Xstate,Zstate)
        turn = 1 - turn
        if(cwin != -1):
            print("Match over 😜")
            print_board(Xstate, Zstate)
            break
          
        os.system('clear')