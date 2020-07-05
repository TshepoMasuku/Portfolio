import random


def hangman():
    words = ["ace", "bat", "cat", "dot", "ear", "forty", "goat", "hi", "ink",
             "juice", "kitchen", "lamp", "mouse", "no", "orange", "purse",
             "question", "rest", "sound", "talk", "unicorn", "vest",
             "water", "x-rays", "yams", "zebra"]
    print('Welcome to Hang Man.')
    stages = [
        '   +------+     ',
        '   |      |     ',
        '   |      |     ',
        '   |      O     ',
        '   |     /|\    ',
        '   |      |     ',
        '   |     / \    ',
        '   |            ',
        '___|____________',
        '   Hanged Man   '
    ]

    random_number = random.randint(0, 25)
    random_word = words[random_number]

    word_length = len(random_word)
    score_board = ['_']*word_length
    print(''.join(score_board))

    word_letters = []
    for letter in random_word:
        word_letters.append(letter)

    win = False
    wrong_guesses = 0
    while wrong_guesses < len(stages)-1:
        guess = input('Guess a letter contained in the secret word with {} letters.  ->  '.format(word_length))
        if guess in word_letters:
            print('Your guess is correct.')
            guess_index = random_word.index(guess)
            score_board[guess_index] = guess
            word_letters[guess_index] = '$'
            print(''.join(score_board))
        else:
            print('Your guess is incorrect.')
            print("\n".join(stages[0:wrong_guesses+1]))
            wrong_guesses += 1

        if '_' not in score_board:
            win = True
            print('You win, you guessed {} correctly.'.format(random_word.upper()))
            break

    # when wrong_guesses == len(stages)-1:
    if not win:
        print('You lost, the secret word was {}.'.format(random_word.upper()))
        print("\n".join(stages[0:wrong_guesses + 1]))


hangman()
