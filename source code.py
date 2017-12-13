import os
import time
import random
import getpass
import fixpath
from colorama import*
init(autoreset=True)

board = [
'  +---+   \n  |   |   \n      |   \n      |   \n      |   \n      |   \n========= \n',
'  +---+   \n  |   |   \n  0   |   \n      |   \n      |   \n      |   \n========= \n',
'  +---+   \n  |   |   \n  0   |   \n  |   |   \n      |   \n      |   \n========= \n',
'  +---+   \n  |   |   \n  0   |   \n /|   |   \n      |   \n      |   \n========= \n',
'  +---+   \n  |   |   \n  0   |   \n /|\\  |   \n      |   \n      |   \n========= \n',
'  +---+   \n  |   |   \n  0   |   \n /|\\  |   \n /    |   \n      |   \n========= \n',
'  +---+   \n  |   |   \n  0   |   \n /|\\  |   \n / \\  |   \n      |   \n========= \n'
]

class Hangman:
	def __init__(self,word):
		self.word = word
		self.missed_letters = []
		self.guessed_letters = []
		
	def guess(self,letter):
		if letter in self.word and letter not in self.guessed_letters:
			self.guessed_letters.append(letter)
		elif letter not in self.word and letter not in self.missed_letters:
			self.missed_letters.append(letter)
		else:
			return False
		return True
		
	def hangman_over(self):
		return self.hangman_won() or (len(self.missed_letters) == 6)
		
	def hangman_won(self):
		if '-' not in self.hide_word():
			return True
		return False
		
	def hide_word(self):
		rtn = ''
		for letter in self.word:
			if letter not in self.guessed_letters:
				rtn += '-'
			else:
				rtn += letter
		return rtn
		
	def print_game_status(self):
		print board[len(self.missed_letters)]
		print 'Word: ' + self.hide_word()
		print 'Letters Missed: ', 
		for letter in self.missed_letters:
			print letter, 
		print 
		print 'Letters Guessed: ',
		for letter in self.guessed_letters:
			print letter,
		print 

def rand_word():
	
	bank = ['india','australia','africa','japan','malaysia','singapore','oman','pakistan','china','russia','iran','iraq','bangladesh','zimbabwe','italy','ireland','switzerland','germany','canada','spain','italy']
	return bank[random.randint(0,len(bank))]
def rules():
        os.system("cls")
        print
        print
        print"\t\t HOW TO PLAY"
        print
        print(Fore.YELLOW+Style.DIM+"""A PERSON WILL THINK OF
A WORD OR SHORT PHRASE AND MARK OUTBLANKS(SHORT LINES).
FOR EACH LETTER OF EACH WORD. SEPERATE WORD WITH EITHER A SLASH ,
A FAIRLY WIDE GAP, OR PLACE WORD ON SEPERATE LINES.
THEN ANOTHERPLAYER WILL GUESS A LETTER. IF THE LETTER IS IN THE WORD
THEN WRITE THE LETTER IN EVERYWHEREIT WOULD APPEAR,AND CROSS OUT THAT LETTER IN THE ALPHABET.
IF THE LETTER ISN'T IN THE WORDTHEN ADD THE BODY PART TO THE GALLOWS
(HEAD,BODY,LEFTARM,RIGHT ARM,LEFT LEG,RIGHT LEG).
THE PLAYER WILL CONTINUE GUESSING LETTERS UNTIL THEY CAN EITHER SOLVE THE WORD
(OR PHRASE) OR ALL SIX BODY PARTS ARE UNTIL THEY CAN...""")
        print
        print
        time.sleep(10)
        os.system("cls")
               

def play():
	
	game = Hangman(rand_word())
	while not game.hangman_over():
		game.print_game_status()
		user_input = raw_input('\nEnter a letter: ')
		game.guess(user_input)

	game.print_game_status()	
	if game.hangman_won():
		print '\nCongratulations! You are the winner of Hangman!'
	else:
		print '\nSorry, you have lost in the game of Hangman...'
		print 'The word was ' + game.word
		
	print '\nGoodbye!\n'
	time.sleep(10)
	os.system("cls")

turns=1
f=1
while(turns<=3):
        print
        print
        print(Fore.GREEN+Style.BRIGHT+"********************************************************************************")
        print
        print(Fore.RED+Style.BRIGHT+"LOGIN".center(80))
        print
        print(Fore.GREEN+Style.BRIGHT+"********************************************************************************")
        print
        print
        user=raw_input("\t\t USERNAME:::")
        print
        print
        print
        password=getpass.getpass("\t\t PASSWORD::::")
        if user=="python":
                if password=="divesh":
                        print
                        print
                        print(Fore.RED+Style.BRIGHT+"************************************************************************")
                        print
                        print (Fore.WHITE+Style.BRIGHT+"\t\t LOADING....")
                        time.sleep(5)
                        os.system("cls")
                        choice='y'
                        while choice=='y':
                                print (Fore.YELLOW+Style.BRIGHT+"""1.RULES"
2.PLAY
3.EXIT""")
                                ch1=int(raw_input("ENTER YOUR CHOICE::"))
                                time.sleep(5)
                                os.system("cls")
                                if ch1== 1:
                                        rules()
                                if ch1==2:
                                        play()
                                if ch1==3:
                                        break
                                
        
                        break
                else:
                        print
                        print (Fore.YELLOW+Style.BRIGHT+"\t\t\t INVALID PASSWORD")
                        time.sleep(5)
        else:
                print
                print
                print (Fore.RED+Style.BRIGHT+"\t\t\t INVALID PASSWORD")
                time.sleep(5)
        turns+=1
        os.system("cls")
                        

