import random
def RPS():
    r = "rock"
    p = "paper"
    s = "scissor"
    all_choices = (r,p,s)
    i = input (f"enter a choice: {r},{p},{s}:")
    c = random.choice(all_choices)
    print(c)
    if((i==r and c== s)or(i==p and c==r) or(i==s and c==p)):
        print("you win wow fantastic")
    elif(i==c):
         print("tie")
    else:
        print("you loose OHH! better luck next time")
if __name__ == "__main__":
    print("let's play rock paper scissor \n")
    RPS()   


