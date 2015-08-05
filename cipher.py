string_input = input('Please enter a string to be ciphered: ') #asks user to input the string that they want to be ciphered
shift_amt = input('Please enter a shift amount between 0 and 25: ')#asks the user to enter amount that they want shifted

if shift_amt.isdigit():

    while not int(shift_amt) in range(0,26): #when the input is a digit and not within the given range, it will keep asking the user to input a valid number until valid number is recieved
        shift_amt = (input('Please enter a shift amount between 0 and 25: '))
else:
    while not shift_amt.isdigit() or not int(shift_amt) in range(0,26): #when the input is not a digit or not in the given range, this while loop will keep asking the user to input a valid input until a number is recieived
        shift_amt = (input('Please enter a shift amount between 0 and 25: '))
string_list = list(string_input)

#print('string_list:', string_list)

for alpha in string_list: #Loops the input
    if alpha.isdigit() is True:#if it's a digit, it will print the same thing
        print(alpha, end='')
    elif alpha.isalnum() is False:#if not's a number or letter, it will print the same thing
        print(alpha,end='')
    elif (alpha.isupper() is True) and ((ord(alpha) + int(shift_amt)) > ord('Z')):#for all uppercase letters, checks if it goes passed it and then wraps around
        print(chr(ord(alpha) + int(shift_amt) - ord('Z') + ord('A') - 1),end='')
    elif (alpha.islower() is True) and ((ord(alpha) + int(shift_amt)) > ord('z')):#for all lowercase letters, checks if it goes passed it and then wraps around 
       print(chr(ord(alpha) + int(shift_amt) - ord('z') + ord('a') - 1) ,end='')
    else:
        print(chr(ord(alpha) + int(shift_amt)),end='')#when wrap around is not needed, it adds shift amount



