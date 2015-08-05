#This program will convert the input into the following format: LLLLLLLLLLFFFFFFFFFFMM/DD/YY
#Asks the user to input the studuent's first name
first_name = input("Please enter the student's first name: ")
#Asks the user to input the students last name
last_name = input("Please enter the student's last name: ")
#Asks the user to input the student's enrollment date
e_date = input("Please enter the student's enrollment date: ")
#The next statement split the enrollment date so that I could assign new variables to it
e_date = e_date.split()
MM = e_date[0]
DD = e_date[1]
DD = DD.replace(',','') #This gets rid of the inputted comma that the user inputs
DD2 = int(DD) #This converts the DD string to an integer for an if statement that comes later on
YYYY = e_date[2]

#the following if statement splits the string, adds '-', then joins the strings. It will then print [0:10]
if len(last_name) <= 9:
    last_name = last_name.split()
    last_name.append('-')
    last_name.append('-')
    last_name.append('-')
    last_name.append('-')
    last_name.append('-')
    last_name.append('-')
    last_name.append('-')
    last_name.append('-')
    last_name.append('-')
    last_name.append('-')
    last_name = ''.join(last_name[0:10])
    ''.join(last_name[0:10])
else:
    last_name[0:10]

if len(first_name) <= 9:
    first_name = first_name.split()
    first_name.append('-')
    first_name.append('-')
    first_name.append('-')
    first_name.append('-')
    first_name.append('-')
    first_name.append('-')
    first_name.append('-')
    first_name.append('-')
    first_name.append('-')
    first_name.append('-')
    first_name = ''.join(first_name[0:10])
    first_name[0:10]
else:
    first_name[0:10]
#the following replace functions searches for the inputted month, then converts it to the appropriate format
MM = MM.replace('January', '01')
MM = MM.replace('February', '02')
MM = MM.replace('March', '03')
MM = MM.replace('April', '04')
MM = MM.replace('May', '05')
MM = MM.replace('June', '06')
MM = MM.replace('July', '07')
MM = MM.replace('August', '08')
MM = MM.replace('September', '09')
MM = MM.replace('October', '10')
MM = MM.replace('November', '11')
MM = MM.replace('December', '12')
MM = MM.replace(' ', '/')

#the following if statement tells the program what to output if the day inputed is single digits
#It will also display the final result

if DD2 < 9:
    print('Storing: '+last_name[0:10]+first_name[0:10]+MM+'/'+'0'+DD+'/'+YYYY[-2:])
else:
    print('Storing: '+last_name[0:10]+first_name[0:10]+MM+'/'+DD+'/'+YYYY[-2:])

