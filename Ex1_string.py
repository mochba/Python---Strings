"""Read a string from a user and check if it is sring or not"""
str = input("\nEnter a string: ")

if str.isalpha():
    
    print("\nEntered string is :", str)
    lenght_ofstr = len(str) # length of a string 
    print("\nLenth of the entered string is ",lenght_ofstr )
    last_letter_position = lenght_ofstr - 1 # last position of the string 
    print(last_letter_position)
    # printing the entered string in reverse order 

    index = 0 
    while index <=  last_letter_position:
        last_letter = str[last_letter_position]
        last_letter_position = last_letter_position-1
        print("string backward letter",last_letter)
        
    # printing the entered string in same order 
        
    for str_letter in str: 
        print("Letter in the entered strings are ",str_letter)
    print("sliced string is ",str[:5])
else:
    print("Enter a valid string")
    quit