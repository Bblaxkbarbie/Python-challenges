#List containing the conversion rates
roman_numerals_list = {
    1 : "I",
    4: "IV",
    5: "V",
    9: "IX",
    10: "X",
    40 : "XL",
    50: "L",
    90: "XC",
    100: "C",
    400: "CD",
    500 : "D",
    900: "CM",
    1000: "M",
    4000: "MV̅",
    5000: "V̅",
    9000 : "MX̅",
    10000: "X̅"
}

#Validates the user's input
def validateInput():
    flag = True

    print("""Welcome to the Roman Numeral Converter
The number entered must be between 1 - 10000""")
    while flag:
        user_input = input("Enter the number you would like to convert: ")

        #Validating empty user input
        if len(user_input) <= 0:
            print("Input cannot be empty, please try again")
            flag = True
        #Validating to check if user input is a number
        elif not user_input.isdigit():
            print('Input must be a number, please try again')
            flag = True
        #Validaing to check if the number is not a negative number
        elif(int(user_input) < 1):
            print("Input must be more than 0")
            flag = True
        #Validating to check if the number is more than 10000
        elif int(user_input) > 10000 :
            print("Input must be less than 10000")
            flag = True
        else:
            try:
                int(user_input)
            except ValueError:
                print("Input must be a number, Please try again")
                flag = True
            else:
                return(int(user_input))
            

#Converts user input into roman numerals 
def convertToRomanNumerals(num):
    #Dividing the number
    ten_thousands = num//10000
    thousands = (num % 10000) // 1000
    hundreds = (num % 1000) // 100
    tens = (num % 100) // 10
    units = (num % 10)

    #Variable to contain roman numerals
    roman_numerals =""

    #ten-thousands
    if(ten_thousands > 0):
        roman_numerals += roman_numerals_list.get(10000) * ten_thousands
    
    #thousands
    if(thousands == 9):
        roman_numerals += roman_numerals_list.get(9000)
    elif(thousands >= 5):
        roman_numerals += roman_numerals_list.get(5000)
        roman_numerals += roman_numerals_list.get(1000) *(thousands - 5)
    elif(thousands == 4):
        roman_numerals += roman_numerals_list.get(4000)
    elif(thousands >= 1):
        roman_numerals += roman_numerals_list.get(1000) * thousands
    
        #hundreds
    if(hundreds == 9):
        roman_numerals += roman_numerals_list.get(900)
    elif(hundreds >= 5):
        roman_numerals += roman_numerals_list.get(500)
        roman_numerals += roman_numerals_list.get(100) *(hundreds - 5)
    elif(hundreds == 4):
        roman_numerals += roman_numerals_list.get(400)
    elif(hundreds >= 1):
        roman_numerals += roman_numerals_list.get(100) * hundreds
    
        #tens
    if(tens == 9):
        roman_numerals += roman_numerals_list.get(90)
    elif(tens >= 5):
        roman_numerals += roman_numerals_list.get(50)
        roman_numerals += roman_numerals_list.get(10) *(tens - 5)
    elif(tens == 4):
        roman_numerals += roman_numerals_list.get(40)
    elif(tens >= 1):
        roman_numerals += roman_numerals_list.get(10) * tens

    #unit
    if(units == 9):
        roman_numerals += roman_numerals_list.get(9)
    elif(units >= 5):
        roman_numerals += roman_numerals_list.get(5)
        roman_numerals += roman_numerals_list.get(1) *(units - 5)
    elif(units == 4):
        roman_numerals += roman_numerals_list.get(4)
    elif(units >= 1):
        roman_numerals += roman_numerals_list.get(1) * units

    print(num, "in roman numerals is:", roman_numerals)
      
#Funtion to enable users to continue their conversion
def continueConversion():
    flag = True

    while flag:
        user_input = input("Press enter to continue....")
        
        if(user_input == ""):
            flag = False
            input_num = validateInput()
            convertToRomanNumerals(input_num)
        else:
            flag = True



#Calling the functions 
input_num = validateInput()
convertToRomanNumerals(input_num)
continueConversion()


