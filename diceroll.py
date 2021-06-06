
n= [1,2,3,4,5,6]

def roll():
    import random
    f= random.choice(n)
    print(f)

def main():
    while True:
        roll()
        play_again = input("roll again? (y/n): ")
        if play_again.lower() != "y":
            break

main()


