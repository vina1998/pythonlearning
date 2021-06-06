
n=[1,2,3,4]

def askforguess():
    t=input("I am thinking of a number between 1 to 4. Take a guess!")
    return int(t)


def thinkingofanumber():
    import random
    s=random.choice(n)
    return s

def main():
    while True:
        n=askforguess()
        t=thinkingofanumber()
        if n == t:
            print("nice job!")
        else:
            print("too bad!")
        play_again = input("play again? (y/n): ")
        if play_again.lower() != "y":
            break

main()