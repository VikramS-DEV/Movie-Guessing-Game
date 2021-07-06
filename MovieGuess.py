import random

# Initial movie list
movie_list = ['The Godfather', 'The Wizard of Oz', 'Citizen Kane', 'The Shawshank Redemption', 'Pulp Fiction','Spy next door','Eat Pray Love']


# Hide movie name with _ except vowels and space
def Hide_Name(mname):
    vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U', ' ')
    hiddenword = ""

    for c in mname:
        if c not in vowels:
            hiddenword += "_"
        else:
            hiddenword += c
    return hiddenword

#Check the guessed letter
def Check_Guess(mname, gl):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U', ' ']
    hiddenword = ""

    for c in mname:
        if c not in vowels and c.lower() not in gl:
            hiddenword += "_"
        else:
            hiddenword += c
    return hiddenword


ans = "y"

guesslist = []

while ans != 'y' or ans != 'Y':
    print("Press 'Y' to guess the movie")
    ans = input()
    if ans == 'y' or ans == 'Y':
        movie_name = random.choice(movie_list)  #Select Movie
        hidden_name = Hide_Name(movie_name)    #Hide movie name bu Displaying olny vowels
        guess_word = ""
        live = 6        #lives
        print(hidden_name)
        print("Lives: 6")

        while movie_name.lower() != guess_word.lower():
            print("Guess letter")
            char = input()
            guesslist.append(char.lower())

            if char.lower() not in movie_name.lower():   #Life loss
             live = live - 1

            guess_word = Check_Guess(movie_name, guesslist)
            print(guess_word)
            print("Lives: ", live)

            if live == 0:
             print("You are out of lives!")
             guesslist.clear()
             break

            if movie_name == guess_word:
             print("Correct Guess!!")
             guesslist.clear()
    else:
        print("Game is Stopped")
        break