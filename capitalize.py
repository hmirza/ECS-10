#this program will take a user input and convert vowels to uppercase and consonants to lowercase
string = input("Please enter a string: ") 
string = string.lower() #this will make the whole string lower case

string = (string.replace("a", "A")) #this will make all the lower case vowels uppercase
string = (string.replace("e", "E"))
string = (string.replace("i", "I"))
string = (string.replace("o", "O"))
string = (string.replace("u", "U"))

print(string) 







