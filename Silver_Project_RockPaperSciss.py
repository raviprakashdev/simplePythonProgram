import random


def getUserInput():
    player = 'blank'
    while player.lower() != 'r' and player.lower() != 'p' and player.lower() != 's':
        player = input("\n\nEnter your valid choice from R,P or S: ").lower()
    return player


def getSystemInput():
    lst = ['r', 'p', 's']
    bot = random.choice(lst)
    return bot


def checkWinner(player, bot):
    if player == bot:  # If both player and bot choose the same
        return 'draw'
    elif player == 'r' and bot == 'p':
        return 'bot'
    elif player == 'r' and bot == 's':
        return 'player'
    elif player == 'p' and bot == 'r':
        return 'player'
    elif player == 'p' and bot == 's':
        return 'bot'
    elif player == 's' and bot == 'r':
        return 'bot'
    elif player == 's' and bot == 'p':
        return 'player'


def rockPaperScissor():
    resume = 'y'
    player_score = 0
    bot_score = 0
    while resume.lower() == 'y':
        ply = getUserInput()
        bt = getSystemInput()
        print('Bot Entered - ', bt)
        print('You Entered - ', ply)
        winner = checkWinner(ply, bt)
        print('Winner is - ', winner)
        if winner == 'player':
            player_score += 1
        elif winner == 'bot':
            bot_score += 1
        print("\n\n------ScoreCard------")
        print("Player:", player_score)
        print("Bot:", bot_score)
        resume = input("\n\nDO YOU WANT TO CONTINUE THE GAME!? Press y : ")


rockPaperScissor()
