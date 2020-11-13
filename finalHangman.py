import tkinter as tk
import random



word_file = open("words.txt", 'a')
#Student should add a couple words of their choice here
#and here
word_file.close

mywords = []
word_file = open("words.txt", 'r')

for line in word_file:
        word = line.replace('\n', '')
        mywords.append(word.strip())
word_file.close()

#Function to create a frame which contains a listbox with different difficulty levels
def difficulty_select():
	
	global settings 

	settings = tk.Frame(window, relief = 'groove', bd = 5)
	settings.grid(row = 1, pady = 5)
	difficulty = tk.Label(settings, text  = "Please select a difficulty level:")
	difficulty.grid(row = 0)
	levels = tk.Listbox(settings, relief = 'sunken', height = 3)
	levels.grid(row = 1, pady = 5)
	levels.insert(0, 'Easy') 
	levels.insert(1, 'Intermediate')
	levels.insert(2, 'Expert')
	lets_play = tk.Button(settings, text = "Let's play!", command = lambda: reset(False, levels.curselection()[0]))
	lets_play.grid(row = 2)


def clicked():

        letter_guess = (guess_input.get()).lower()

        if ((letter_guess not in guessed_letters) and (len(letter_guess) == 1)):

                guessed_letters.append(letter_guess)
                updateAlphabet(letter_guess)
                
                if (letter_guess in word):
                        correct = 0
                        
                        #Replaces the '_' with the correctly guessed letter and then updates the frame
                        for i in range(len(word)):
                                if (word[i] == letter_guess):
                                        correct += 1
                                        hidden_word[i] = letter_guess
                        new_word = tk.Label(game_frame, text = hidden_word)
                        new_word.grid(row =2)
                        
                        """Checks to see if there are any more letters to be guessed, 
                        if there aren't it creates a pop up window with the choice to play again or quit"""
                        if ('_' not in hidden_word):
                                global end_frame
                                game_frame.destroy()
                                end_frame = tk.Frame(window, relief = 'groove', bd = 5)
                                end_frame.grid(row = 1, pady = 5)
                                congrats = tk.Label(end_frame, text = 'CONGRATULATIONS!')
                                congrats.grid(row = 0)
                                correct = tk.Label(end_frame, text = 'You\'ve guessed the word correctly, it was:')
                                correct.grid(row = 1)
                                current_word = tk.Label(end_frame, text = hidden_word)
                                current_word.grid(row =2)
                                button_frame = tk.Frame(end_frame)
                                button_frame.grid(row = 3)
                                play_button = tk.Button(button_frame, text = "Play Again!", command = lambda:reset(True, difficulty_level))
                                play_button.pack(side = 'left')
                                quit_button = tk.Button(button_frame, text ="Quit", command = quit)
                                quit_button.pack(side = 'right')
                                add()

                else:
                	global wrong_guesses
                	wrong_guesses += 1
                	drawMan(wrong_guesses)

#Function that draws a new body part in the canvas when the user guessed the wrong letter
def drawMan(bodypart):
        if (bodypart ==1):
                hangman.create_line(50, 280, 250, 280, width= 2)
        elif (bodypart ==2):
                hangman.create_line(50, 280, 50, 50, width = 2)
        elif (bodypart==3):
                hangman.create_line(50, 50, 150, 50, width = 2)
        elif (bodypart ==4):
                hangman.create_line(150, 100, 150, 50, width = 2)      
        elif (bodypart ==5):
                hangman.create_oval(125,100,175,150, width = 2)
        elif (bodypart ==6):
                hangman.create_line(150,150,150,210,width=2)
        elif (bodypart==7):
                hangman.create_line(150,170,120,170,width =2)
        elif (bodypart==8):
                hangman.create_line(150,170,180,170,width =2)
        elif (bodypart==9):
                hangman.create_line(150, 210, 130, 250, width = 2)
        else:
                hangman.create_line(150, 210, 170, 250, width = 2)

                """If the hangman is completed then the a pop up window is created with an option to
                play again or quit the game"""
                global end_frame
                game_frame.destroy()
                end_frame = tk.Frame(window, relief = 'groove', bd = 5)
                end_frame.grid(row = 1, pady = 5)
                unlucky = tk.Label(end_frame, text = 'UNLUCKY!')
                unlucky.grid(row = 0)
                incorrect = tk.Label(end_frame, text = 'The correct word was:')
                incorrect.grid(row = 1)
                current_word = tk.Label(end_frame, text = word)
                current_word.grid(row =2)
                button_frame = tk.Frame(end_frame)
                button_frame.grid(row = 3)
                play_button = tk.Button(button_frame, text = "Play Again!", command = lambda:reset(True, difficulty_level))
                play_button.pack(side = 'left')
                quit_button = tk.Button(button_frame, text ="Quit", command = quit)
                quit_button.pack(side = 'right')

#Function to strike out the letter that the user guesses        
def updateAlphabet(letter):
        index = alphabet_letters.index(letter)
        alphabet_letters.remove(letter)
        alphabet_letters.insert(index, letter + '\u0336')
        new_alphabet = tk.Label(game_frame, text = alphabet_letters)
        new_alphabet.grid(row = 3)

def quit():
        window.destroy()

def center(win):
    """
    centers a tkinter window
    :param win: the root or Toplevel window to center
    """
    window_height = 700
    window_width = 350

    screen_width =  win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()

    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))

    win.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))


"""Function to reset the game if the play again button is clicked, 
also called just before the mainloop() to set the 1st game up"""
def reset(restart, level):

        global game_frame
        global guessed_letters
        global alphabet_letters
        global word
        global hidden_word
        global guess_input
        global difficulty_level
        global wrong_guesses

        difficulty_level = level
        settings.destroy()

        #When the game is first started, the stopwatch begins to update
        if not (restart):
        	update_stopwatch()

        if (restart):
        	end_frame.destroy()
        	hangman.delete("all")

        word = random.choice(mywords)

        hidden_word = []
        for i in range(len(word)):
                hidden_word.append("_")

        #Creates the base for the hangman
        if (level == 1):
        	hangman.create_line(50, 280, 250, 280, width= 2)
        	hangman.create_line(50, 280, 50, 50, width = 2)
        	wrong_guesses = 2

        elif (level == 2):
        	hangman.create_line(50, 280, 250, 280, width= 2)
        	hangman.create_line(50, 280, 50, 50, width = 2)
        	hangman.create_line(50, 50, 150, 50, width = 2)
        	hangman.create_line(150, 100, 150, 50, width = 2)
        	wrong_guesses = 4

        else:
        	wrong_guesses = 0 

        guessed_letters = []
        alphabet_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', \
        'u', 'v', 'w', 'x', 'y', 'z']

        #Frame below the canvas, with the alphabet, the word to be guessed and the widget to take input
        game_frame = tk.Frame(window, relief = 'groove', bd = 5)
        game_frame.grid(row = 1, pady = 5)

        current_word = tk.Label(game_frame, text = hidden_word)
        current_word.grid(row =2)
        alphabet = tk.Label(game_frame, text = alphabet_letters)
        alphabet.grid(row = 3)
        welcome = tk.Label(game_frame, text = 'LET\'S PLAY HANGMAN!')
        welcome.grid(row = 0)
        intro = tk.Label(game_frame, text = 'Try guess the following word:')
        intro.grid(row = 1)
        
                
        guess_frame = tk.Frame(game_frame)
        guess_label = tk.Label(guess_frame, text = "Guess a letter: ").grid(row = 0, column = 0)
        guess_input = tk.Entry(guess_frame)
        guess_input.grid(row = 0, column = 1)
        guess_button = tk.Button(guess_frame, text = "Submit", command=lambda *args:[clicked(),clear_text(guess_input)]).grid(row = 1, column = 1)
        guess_frame.grid(row = 4, pady = 10)
        
        def clear_text(guess_input):
            guess_input.delete(0, 'end') 
        
                
        guess_input.bind('<Return>', lambda *args:[clicked(),clear_text(guess_input)])


counter = 0

def counter_label(label):
    label.config(text="Wins: " + str(counter))
    #label.after(1000,count)

def add():
    global counter
    counter += 1
    label.config(text="Wins: " + str(counter))
    
window = tk.Tk()
window.title("Hangman Game")


hangman = tk.Canvas(window, height=300, width=300, relief = 'ridge', bd = 10)
hangman.grid(padx = 10, pady  = 15, row = 0)

wins = tk.Frame(window, height=100, width=300, relief = 'ridge', bd = 10)
wins.grid(padx = 10, pady  = 10, row = 2)

label = tk.Label(wins, fg= "dark green", height=5, width=30)
label.grid()

counter_label(label)

center(window)

# Stopwatch label
stopwatch = tk.Label(wins, text="")
stopwatch.grid()

minutes = 0
seconds = 0

def update_stopwatch():
    global minutes
    global seconds

    if seconds < 59:
        seconds += 1
    elif seconds == 59:
        seconds = 0
        minutes +=1

    # Update Label.
    time_string = "{:02d}:{:02d}".format(minutes, seconds)
    stopwatch.config(text=time_string)

    wins.after(1000, update_stopwatch)  # Call again in 1000 millisecs.


difficulty_select()

window.mainloop()
