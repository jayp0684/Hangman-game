import random  # import random function

def get_word():   #get word is a function that have list of words
	words = ['Fire',
		'Laugh',
		'Falling',
		'Star',
		'Elephant',
		'Basketball',
		'Computer',
		'Danger',
		'Apple',
		'Party',
		'Random',
		'Highland',
		'Lion',
		'Mouse',
		'Cat',
		'Apple',
		'Grape',
		'Orange',
		'Whale',
		'Dolphine',
		'Grandfather',
		'Grandmother',
		'Flag',
		'Running',
		'Volleyball',
		'Baseball',
		'Warning',
		'Important',
		'Open',
		'Stop',
		'Hat',
		'Bat',
		'Blind',
		'Boy',
		'Girl',
		'Hammer',
		'Monkey',
		'Voltage',
		'Electric',
		'Gamer',
		'Quitter',
		'Blind',
		] 
	return random.choice(words).upper() #uppercase the words or letters
	#random words picks an element within sequence 
	
def check(word,guesses,guess):#the first thing we do in our check function is 
	status = ''#set up status to the empty string.
	matches = 0#<----
	for letter in word:#loop through the letters in our word
		if letter in guesses:
			status  += letter#using the status variable to create the word going to return to user. either going to be a bunch of *, * with letters in them, or the full word
		else:#can put * in our status string
			status += '*'
			
		if letter == guess:#if guess letter matches
			matches =+ 1
			
	if matches > 1:
		print('Yes! The word contains',matches,'"' + '"' + 's')#if guess matches for example 2 A's
	elif matches == 1:
		print('Yes! The word contains the letter "' + guess + '"')#if guess match 1 letter
	else:
		print('Sorry. The word does not contain the letter "' + guess + '"')#if guessed wrong
			
	return status#return the words with some of the letters that cover up with *
		
def main():
	word = get_word() #call first function
	guesses = []  #guesses gets an empty list,that's going to keep track of the users guesses in this list 
	guessed = False # have not yet guessed the word incorrectly
	print('The word contains', len(word),'letter.')# len = count the letter of the word 
	while not guessed: #while loop when guessed is false then we assign text =
		text = 'Please enter one letter or a {}-letter word. '.format(len(word))#the len(word) will replace the {} will assign that to the variable text.
		guess = input(text)#will output the text message and will get input from the user and assign that input to the variable guess
		guess = guess.upper()#uppercase guess letters
		if guess in guesses:#if false
			print('You already guessed "' + guess + '"')#you already guess certain letters
		elif len(guess) ==len(word):#if enter a word that have same number of character as the answer word
			guesses.append(guess)#then will append their guess to the guesses list
			if guess == word:#if guess the right word exist
				guessed = True#will set guessed to true
			else:
				print('Sorry, that is incorrect.')#if not true will print
		elif len(guess) == 1:#if they guess a 1 letter character
			guesses.append(guess)#will append that guess to guesses
			result = check(word,guesses,guess)#then will result to check arguments. lets check out our check function
			if result == word:
				guessed = True
			else:
				print(result)#thats the word mix with *
		elif len(guess) == 1:
			guesses.append(guess)
			result = check(word,guesses,guess)#checked the value arguments
			if result == word:#if guess is correct
				guessed = True
				
			else:
				print(result)
		else:
			print('Invalit entry.')#user didn't enter 1 letter or any letters that is contain in the word.
			
	print('Yes, the word is',  word + '! You got it in', len(guesses), 'tries.')#if user guessed the words or letters

main()

			
		
			