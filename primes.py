#calculate the primes from 2 to N inclusive
max_prime_search = input('Please enter an integer >= 2: ')
#print(prime)
if max_prime_search.isdigit():#if the input is a digit then it will execute the nested while loop below
    while int(max_prime_search) < 2 or max_prime_search.isalpha():#this loop makes sure that the number inputted is greater than or equal to 2
        max_prime_search = input('Please enter an integer >= 2: ')
else:   #if the input is not a number, it will execute the below while loop until a valid number is inputted
    while not max_prime_search.isdigit() or int(max_prime_search) <2:
        max_prime_search = input('Please enter an integer >= 2: ')


user_number = int(max_prime_search)#converts the user input into an integer

for a in range(2, user_number+1):
    if a > 1:# if the number is greater than 1
        for i in range(2, a):#all the numbers from 2 and the input
            if(a % i) == 0:#if divisible by itself
                break
        else:
            print(a)

        
     
