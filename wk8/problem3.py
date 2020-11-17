def ask():
    while True:
        try:
            num = int(input("provide an integer: "))
            print (num*num)
        except:
            print("it's not an integer!")
        # else:
        #     print("yay!")
            
            break
        finally:
            print("it always comes here")

ask()