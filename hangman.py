def get_secret_word():
    """
    Requests the user enter a secret word.
    This function asks for a secret word until gets a valid secret 
    word. A Valid secret word doesn't contain space(s), or ? and is not blank.
    Prints 30 blank lines to hide the inputted word
    @returns: secret word
    
    """
    prompt = input(('Please enter a word to be guessed\n'
                    'that does not contain ? or white space: '))
    while ' ' in prompt or '?' in prompt or prompt =='':
        prompt = input(('Please enter a word to be guessed\n'
                'that does not contain ? or white space: '))
    print('\n'*30)
    return prompt    
    
# end get_secret_word


def get_guess(guesslist):
    """
    Requests user to enter a guess.
    This function continues to ask user for a guess untll it gets a valid
    guess. Valid guess doesnot contain space(s), ?, or more than one letter,
    or any guess which had already been entered.
    @guesslist: a list of all guesses already entered by user.
                This list is modified and newly entered valid guess is 
                added to it.
    @returns: guess list 
                
    """ 
    while True:
        guess = input('Please enter your next guess: ').lower().strip()
        if len(guess) == 0:
            print('You must enter a guess.')
        else:
            if len(guess) == 1:
                if guess != '?' and guess != ' ':
                    if guesslist.count(guess) == 0:
                        break
                    else:
                        print('You already guessed the character:', guess)
            else:
                print('You can only guess a single character.')
    return guess
    
# end get_guess


def match_guess(secretword, hiddenword, guess):
    """ 
    Matches the guess letter in secret word and updates the hidden word
    by replacing ?'s with matched guess
    @secretword: secret word entered by user
    @hiddenword: current hidden word, with ?'s replaced with already matched 
        guesses
    @guess: guess letter entered by user
    @returns: modified hiddenword
    """ 
    newhiddenword = ''
    for i in range(len(secretword)):
        if secretword[i] == guess:
            newhiddenword += guess
        else:
            newhiddenword += hiddenword[i]
    hiddenword = newhiddenword
    return hiddenword

#end match_guess


def display_hangman(attempt):
    """
    Prints the current hangman figure, based on the number of failed attepmts
    @attempts: Failed attenp count
    @returns: None

    """
    if attempt == 0:
        print('')
    elif attempt == 1:
        print('\n |')
    elif attempt == 2:
        print('\n |')
        print(' 0')
    elif attempt == 3:
        print('\n |')
        print(' 0')
        print(' |')
    elif attempt == 4:
        print('\n |')
        print(' 0')
        print('/|')
    elif attempt == 5:
        print('\n |')
        print(' 0')
        print('/|\\')
    elif attempt == 6:
        print('\n |')
        print(' 0')
        print('/|\\')
        print('/')
    elif attempt == 7:
        print('\n |')
        print(' 0')
        print('/|\\')
        print('/ \\')

# end display_hangman


def display_guesses(guesslist):
    """
    Diplays all guesses user had entered in alphabetical order and comma
    separted.
    @guesslist: a list of all guesses already entered by user.
    @returns: None
    """
    guessdisplay = ''
    guessdisplayc = ''
    for i in range(len(guesslist)):
        guessdisplay += guesslist[i]+', '
    if len(guessdisplay) != 0:
        guessdisplayc = guessdisplay[:-2]
    print(guessdisplayc)

# end display_guesses


def is_game_over(hiddenword, secretword, attempt):
    """
    Returns True if the game is over (user guessed the word or did not guess
    in allowed  7 attempts.
    @hiddenword: current hidden word, with ?'s replaced with already matched 
    @secretword: secret word entered by user
    @attempt: Total failed attempts so far.
    @returns: True or False
    """
    if hiddenword == secretword or attempt == 7:
        gameover = True
    else:
        gameover = False
    return gameover

# end is_game_over


def main():
    """
    Mail function call all functions to get secxret words, guesses, keeps
    track of failed attempt count, displays hangman figure, hidden word,
    and check if the game is over
    @returns: None
    """
    secretword = get_secret_word()
    hiddenword = '?'*len(secretword)
    guesslist = []
    attempt = 0
    while attempt != 7:
        display_hangman(attempt)
        print('')
        print(hiddenword)
        print('So far you have guessed: ', end='')
        display_guesses(guesslist)
        guess = get_guess(guesslist)
        guesslist.append(guess)
        guesslist = sorted(guesslist)
        if secretword.count(guess) == 0:
            attempt += 1
        else:
            hiddenword = match_guess(secretword, hiddenword,guess)
        if is_game_over(hiddenword, secretword, attempt) == True:
            if attempt == 7:
                display_hangman(attempt)
                print('\nYou failed to guess the secret word:', secretword)
            elif hiddenword == secretword:
                print('You correctly guessed the secret word:', secretword)
                attempt = 7

# end main


if __name__ == '__main__': #if this is the main program run
  main() #run the main function
