from user_input import UserInput

def main():
    usr_inpt = UserInput()
    while True:
        option = usr_inpt.select_option()
        if option == 5:
            break
        else:
            usr_inpt.match_option(option)
    

if __name__ == "__main__":
    main()