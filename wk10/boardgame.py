from os import system, name 
# define our clear function 
def clear(): 
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 
def user_choice():
    '''
    User inputs a number (0-10) and we return this in integer form.
    No parameter is passed when calling this function.
    '''
    choice = 'wrong'
    while choice.isdigit() == False:
        choice = input("Choose a number: ")
        # Error Message Check
        if choice.isdigit() == False:
            clear()
            print("Sorry, but you did not enter an integer. Please try again.")
    return int(choice)
def display_board(board):
    clear()
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
user_choice()
test_board = ['#','X','O','X','O','X','O','X','O','X']
display_board(test_board)