import random

def hangman():
    word_list = ['Python', 'Java', 'JavaScript', 'C++', 'HTML']
    random_number = random.randint(0, 4)
    word = word_list[random_number]
    wrong = 0
    stages = ['',
              '               ',
              '_________      ',
              '|              ',
              '|        |     ',
              '|        O     ',
              '|       /|\    ',
              '|       / \    ',
              '|              ',
              ]
    rletters = list(word)
    board = ['_'] * len(word)
    win = False
    print('ハングマンへようこそ！')
    while wrong < len(stages) - 1:
        print('\n')
        guess = input('文字を推測してね')
        if guess in rletters:
            cind = rletters.index(guess)
            board[cind] = guess
            rletters[cind] = '$'
        else:
            wrong += 1
        print(' '.join(board))
        e = wrong + 1
        print('\n'.join(stages[0:e]))
        if '_' not in board:
            print('あなたの勝ち！')
            print(' '.join(board))
            win = True
            break
    if not win:
        print('\n'.join(stages[0:wrong+1]))
        print('あなたの負け！正解は{}'.format(word))

hangman()