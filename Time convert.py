#Validates the user's input
def ValidateInput():
    flag = True

    print("""Welcome to the Time converter 
Please enter the number of minutes you wish to convert
""")
    while flag:
        user_input = input("Enter the number you would like to convert: ")

        if len(user_input) <= 0:
            print("Input cannot be empty, please try again")
            flag = True
        elif not user_input.isdigit():
            print('Input must be a number, please try again')
        elif(int(user_input) < 1):
            print("Input must be more than 1")
            flag = True
        else:
            try:
                int(user_input)
            except ValueError:
                print("Input must be a number, Please try again")
                flag = True
            else:
                return(int(user_input))
            

user_input = int(ValidateInput())
print(user_input)

def time_convert(min):

    Hour = min // 60
    Minutes = min % 60 

    print(f"{Hour}:{Minutes}")

time_convert(user_input)