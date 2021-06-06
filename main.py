board = ["" for x in range(8)]

def printboard(board):
    print(board)

def insertletter(pos,t):
    board[pos] = t



def main():
    print("welcome to alternative name generator")
    t = input("what is the first letter of your name??")
    insertletter(1,t)
    printboard(board)
    t = input("what is the second letter of your name??")
    insertletter(6, t)
    printboard(board)
    t = input("what is the third letter of your name??")
    insertletter(2, t)
    printboard(board)
    t = input("what is the fourth letter of your name??")
    insertletter(0, t)
    printboard(board)
    t = input("what is the fifth letter of your name??")
    insertletter(3, t)
    printboard(board)
    t = input("what is the sixth letter of your name??")
    insertletter(7, t)
    printboard(board)
    t = input("what is the seventh letter of your name??")
    insertletter(5, t)
    printboard(board)
    t = input("what is the eight letter of your name??")
    insertletter(4, t)
    printboard(board)

main()





















