#The following program allows the user to essentially choose their own destiny
#
print("Your alarm starts going off. What do you do?")
print("1. Wake up")
print('2. Hit the snooze button')
print("3. Sleep through it")

Choice_1 = int(input("Your choice: "))#This assigns a variable to the user input


if Choice_1 == 1:# if you choose 1 you get the following options
    print('You wake up groggily and stumble into the shower.'
              'The hot water refreshes you and you feel much better.'
              'You finish showering and get changed. What do you do?\n'
              '1. Head to class\n'
              '2. Skip class and catch up on homework\n'
              '3. Skip class and head to a party')
    Choice_2 = int(input("Your choice: "))
 
    if Choice_2 ==1: #if you choose 1 and choose 1, 2, or 3, you will have the following options
        print('You head to class and while it is not very fun you laern quite a bit.\n'
                  'You feel more prepared for your midterm as result.')

    elif Choice_2 ==2:#these elif statements make sure that the program doesn't run anything below a statement that is valid
        print('You have been falling behind on your homework and so stay home to play catch up.\n'
                  'You manage to finish it all but you are too brain tired to do anything else that day.')
        
    elif Choice_2 ==3:
        print('College is a time for living it up.\n'
                  'You skip class, head to a part, and have a great time.\n'
                  'Or at least you think you had a great time because you cannot remember any of it.\n'
                  'Hopefully no one took any embarrassing pictures of you.')
    else:
        print("You entered an invalid choice and so spontaneously combusted.")#will recieve this error message if you choose an option that is not given
elif Choice_1 == 2:
    print('You hit the snooze button and go back to sleep but soon again it is going off. What do you do?\n'
              '1. Find a more permanent solution to silence the clock.\n'
              '2. Wake up and rush to class.')
    Choice_3 = int(input("Your choice: "))

    if Choice_3 == 1:
        print('You chuck your alarm out of your 4th story dorm window and hear a satisfying crack when it lands.\n'
                  'You go back to sleep but have weird dreams about running around the face of a clock.')
    elif Choice_3 == 2:
        print('You wake up but having overslept you only have time to throw on some clothes and head to class.\n'
                  'Everyone in class keeps giving you funny looks because you are a little stinky and your stomach keeps making noises but at least you made it to class on time.')
    else:
        print("You entered an invalid choice and so spontaneously combusted.")

elif Choice_1 == 3:
    print('You must have had a crazy night last night as you sleep through your screaming alarm clock.\n'
              'Eventually it goes silent and you sleep through the morning missing all your classes.\n'
              'Hopefully you did not miss anything important.')
else:
    print("You entered an invalid choice and so spontaneously combusted.")














