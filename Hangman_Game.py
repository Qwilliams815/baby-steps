# WELCOME TO HANGMAN

def main():

   import random
   word_list = ['python', 'java', 'kotlin', 'javascript']
   word = list(random.choice(word_list))
   str_word = ''.join(word)
   dash = "-" * (len(word))
   blank_list = list(dash)
   guess_letters = []
   wrong_guesses = []
   win_msg = f"You guessed the word {str_word}!\nYou survived!"



   print()
   print(dash)
   lives = 9
   while lives > 0:

       guess = input("Input a letter: ").strip()

       if guess == str_word:  # WHOLE WORD GUESS CHECKER
           print(win_msg)
           break

       if len(guess) < 2 and guess != '':  # MULTIPLE LETTERS ENTERED CHECKER, EMPTY

           if guess.islower():  # LOWER CASE & ALPHA QUALIFIER

               if guess in word:

                   if guess not in guess_letters:  # DUPLICATE LETTER CHECKER
                       guess_letters.append(guess)

                       if set(guess_letters) == set(word):  # ALL BLANKS FILLED OUT CHECKER
                           print(win_msg)
                           break
                   else:
                       print('You already typed this letter')

                   print()
                   for letter in range(len(word)):  # BLANK REPLACER SEQUENCE
                       if word[letter] == guess:
                           blank_list[letter] = guess
                   letter += 1

               else:
                   if guess not in wrong_guesses:
                       wrong_guesses.append(guess)
                       print("No such letter in the word")
                       lives -= 1
                   else:
                       print('You already typed this letter')
                   if lives == 1:
                       print('You are hanged!')
                       break

                   print()

               print(''.join(blank_list))
           else:
               print('It is not an ASCII lowercase letter\n')
               print(''.join(blank_list))
       else:
           print('You should input a single letter\n')
           print(''.join(blank_list))
   if lives == 0:
       print("You are hanged!")

   restart = input('\nType "play" to play the game, "exit" to quit: ')
   if restart == 'play':
       main()


print("H A N G M A N")
start = input('Type "play" to play the game, "exit" to quit: ')
if start == 'play':
   main()
elif start == 'exit':
   quit()

