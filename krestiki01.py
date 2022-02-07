def greet():
    print("-------------------")
    print("  Приветсвую Вас  ")
    print("      в игре       ")
    print("  крестики-нолики  ")
    print("-------------------")
    print(" формат ввода от 1 до 9")
board = list(range (1,10))
def board_1 (board):
    print (("_")*11)
    for i in range (3):
        print ("|"f"{board[0+i*3]}""|", "|"f"{board[1+i*3]}""|", "|"f"{board[2+i*3]}""|")
        print (("-")*11)


def ask_users (krestik_nolik):
    valid = False
    while not valid:
        hod = input (f"Игрок {krestik_nolik} выберите клетку : ")
        try:
            hod = int(hod)
        except:
            print ("YOU SHALL NOT PASS!!! Введите число!")
            continue


        if hod >=1 and hod <= 9:
            if (str(board[hod-1]) not in "XO"):
                board[hod-1] = krestik_nolik

            else:
                print  ("Клетка занята!")
                continue
        else:
            print ("Неправильно набран номер, введите число от 1 до 9!!!")
            continue
        return hod

def win_check(board):
    win_res = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
    for w in win_res:
        if board[w[0]] == board [w[1]] == board [w[2]]:
            return board[w[0]]
    return False

def game_run(board):
    greet ()
    count=0
    win=False
    while not win:

        board_1(board)

        if count %2 ==0:
            ask_users("X")
        else:
            ask_users("O")
        count+=1


        if count>4:
            g=win_check(board)
            if g :
                print (f"Выиграл: {g}")
                break
        if count==9:
            print("Ничья!")
            break
    board_1(board)
game_run(board)