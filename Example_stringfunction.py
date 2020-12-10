# word = 'banana'
# print(word)
# count = 0 
# for i in word:
#     if i == 'a':
#         count = count +1
# print(count)

"""Encapsulate the above code in a function named func_count, and generalize it so 
that it accepts the string and the letter as arguments."""

def func_count(word,user_letter):
    # word = 'banana'
    print(word)
    count = 0 
    for i in word:
        if i == user_letter:
            count = count +1
    letter_position = word.find(user_letter)
    letter_list = list()
    letter_list.append(letter_position)
    while letter_position >= 0:
        letter_position = word.find(user_letter, letter_position+1)
        letter_list.append(letter_position)
    letter_list.pop()
    return count,letter_list
ui = input("Enter a string:")
uli = input("Enter which letter to be find from the word: ")
output_count,li = func_count(ui,uli)
print("The letter '" +uli + "' occurred ", output_count, "times and at these positions ",li)