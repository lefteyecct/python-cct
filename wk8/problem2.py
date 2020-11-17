try:
    x = 5
    y = 0
    z = x/y
except EOFError:
    print("error occurs!")
finally:
    print("it ends here regardless")