#Asks the user how much money they wish to withdraw
#and outputs the types of bills they will recieve.

Money_Left = int(input("Please enter the amount of money you wish to withdraw: "))


print("You received:")
Hundreds = (Money_Left//100)
print(Hundreds, "Hundreds.") #Outputs 100's recieved

Money_Left = Money_Left - Hundreds *100
Fiftys = (Money_Left//50)
print(Fiftys, "fifties.") #Outputs 50's recieved

Money_Left = Money_Left - Fiftys *50
Twenties = (Money_Left//20)
print(Twenties, "twenties.") #Outputs 20's received

Money_Left = Money_Left - Twenties *20
Tens = (Money_Left//10)
print(Tens, "tens.") #Outputs 10's received

Money_Left = Money_Left - Tens *10
Fives = (Money_Left//5)
print(Fives, "fives.") #Outputs 5's recieved

Money_Left = Money_Left - Fives *5
Ones = (Money_Left//1)
print(Ones, "ones.") #Outputs 1's received




                                                      




