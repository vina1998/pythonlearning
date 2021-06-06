
def jumbler(n):
    import random
    s= random.sample(n, len(n))
    return s

def main():
    while True:
        n = input("What is your name?")
        t=jumbler(n)
        print("your nickname is:", t)
        play_again = input("play again? (y/n): ")
        if play_again.lower() != "y":
            break


main()


