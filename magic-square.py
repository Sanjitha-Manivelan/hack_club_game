def board_layout():
    print("-------")
    print("|" + board[0][0] + "|" + board[0][1] + "|" + board[0][2] + "|")
    print("-------")
    print("|" + board[1][0] + "|" + board[1][1] + "|" + board[1][2] + "|")
    print("-------")
    print("|" + board[2][0] + "|" + board[2][1] + "|" + board[2][2] + "|")
    print("-------")

def number_input():
    input_numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    number = input("\nEnter the number that you want to put (1, 2, 3, 4, 5, 6, 7, 8, or 9): ")
    while number not in input_numbers or number in numbers_entered:
        print("\nWhat you inputed is incorrect please try again!\n")
        print("These could be the errors you did:\n1.Number already chosen\n")
        print("2.You did not enter a number")
        print("\n3.You did not enter 1, 2, 3, 4, 5, 6, 7, 8, or 9\n")
        number = input("Enter the number that you want to put (1, 2, 3, 4, 5, 6, 7, 8, or 9): ")
        continue
    return number

def user_output(number):
    row_column_input = ["1","2","3"]
    row = input("\nEnter the row number(1, 2, or 3) that you want to place your number: ")
    column = input("\nEnter the column number(1, 2, or 3) that you want to place your number: ")
    
    while row not in row_column_input or column not in row_column_input:
        print("\nWhat you inputed is incorrect please try again!\n")
        print("These could be the errors you did:\n1.You did not enter a number")
        print("\n2.You did not enter 1, 2, or 3 for rows or columns or both\n")
        row = input("\nEnter the row number(1, 2, or 3) that you want to place your number: ")
        column = input("\nEnter the column number(1, 2, or 3) that you want to place your number: ")
        continue

    if int(row) <= 0 or int(column) <= 0 or board[int(row)-1][int(column)-1] != " ":
        print("\nThat space is already full or invalid number please try again!\n")
    else:
        board[int(row)-1][int(column)-1] = number
        numbers_entered.append(number)
        
def game_over():
    count_diagonal_1 = 0
    count_diagonal_2 = 0
    count_row = 0
    count_column = 0
    for row in range(len(board)):
        for column in range(len(board)):
            count_row += int(board[row][column])
            count_column += int(board[column][row])
        
        if count_row != 15 or count_column != 15:
            return False
        count_row = 0
        count_column = 0
    length_board = len(board) - 1
    for row in range(len(board)):
        count_diagonal_1 += int(board[row][row])
        count_diagonal_2 += int(board[length_board-row][row])
   
    if count_diagonal_1 != 15 or count_diagonal_2 != 15:
        return False
    
    return True
    
board = [[" "," "," "],[" "," "," "],[" "," "," "]]
numbers_entered = []
def game():
    while True:
        if (board[0][0] != " " and board[0][1] != " " and board[0][2] != " " 
        and board[1][0] != " " and board[1][1] != " " and board[1][2] != " " 
        and board[2][0] != " " and board[2][1] != " " and board[2][2] != " "):
            board_layout()
            if game_over() == True:
                print("Congratulations, you won!!! :)")
                break
            else:
                print("You lost :(")
                break
        else:
            board_layout()
            user_output(number_input())
game()
