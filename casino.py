import random, time, sys
def flip_coin(guess, bet):
    guess.lower()
    if 'head' not in guess.lower() and 'tail' not in guess.lower():
        print('You have to choose heads or tails.\n')
        return(0)

    # Give result and compare the the pick
    result = random.randint(0,1)
    # 0 is Tails
    if result == 0:
        result = 'tails'
        print('The coin landed on tails.')
        if result == guess:
            print('You have won!\n+' + str(bet) + ' chips\n')
            return(bet)
        else:
            print('You have lost.\n-' + str(bet)+ ' chips\n')
            return(-bet)
    # 1 is Heads        
    else:
        result = 'heads'
        print('The coin landed on heads.')
        if result == guess:
            print('You have won!\n+' + str(bet)+ ' chips\n')
            return(bet)
        else:
            print('You have lost.\n-' + str(bet)+ ' chips\n')
            return(-bet)

def cho_han(guess, bet):
    if 'even' not in guess.lower() and 'odd' not in guess.lower():
        print('You have to choose even or odd.\n')
        return(0)
    # Generate two random dice and add them
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    sum_ = dice1 + dice2
    print('The sum of the two dice is ' + str(sum_) + ': ', end='')
    # Check if sm is even or odd
    if sum_ % 2 == 0:
        sum_ = 'even'
    else:
        sum_ = 'odd'
    print(sum_ + '!')
    # Compare guess to sum
    if sum_ == guess:
        print('You have won!\n+' + str(bet)+ ' chips\n')
        return(bet)
    else:
        print('You have lost.\n-' + str(bet)+ ' chips\n')
        return(-bet)

def pick_a_card(bet):
    deck = [1,2,3,4,5,6,7,8,9,'Jack','Queen','King']
    deck *= 4
    player_card = random.choice(deck)
    deck.remove(player_card)    # Remove the card from deck
    computer_card = random.choice(deck)
    print('You picked ' + str(player_card) + '.' + '\nThe computer picked ' + str(computer_card) + '.')
    # Convert names to numbers
    if player_card == 'Jack':
        player_card = 10
    elif player_card == 'Queen':
        player_card = 11
    elif player_card == 'King':
        player_card = 12
    if computer_card == 'Jack':
        computer_card = 10
    elif computer_card == 'Queen':
        computer_card = 11
    elif computer_card == 'King':
        computer_card = 12
    
    if player_card > computer_card:
        print('You have won!\n+' + str(bet)+ ' chips\n')
        return(bet)
    elif player_card < computer_card:
        print('You have lost.\n-' + str(bet)+ ' chips\n')
        return(-bet)
    else:
        print('It is a tie.'+ ' chips\n')
        return(0)

def roulette(bet):
    print('This is a game of Python Roulette')
    chosen_nums = []
    while True:
        print('Place an [I]nside or [O]utside bet.')
        bet_type = input()
        if 'i' in bet_type.lower() or 'inside' in bet_type.lower(): 
            print('Place a [Si]ngle, [Sp]lit, [St]reet, [DS]Double Street, [Tri]o, or [B]sket bet.')
            inside_bet = input()
            if 'si' in inside_bet.lower():
                bet_type = 'single'
                while True:
                    try:
                        print('Bet on a single number (0-36,00).')
                        num = input()
                        if num == '00':
                            chosen_nums.append(num)
                            break
                        num = int(num)
                        if num not in range(37):
                            print('That is not a valid number.')
                            continue
                        chosen_nums.append(num)
                        break
                    except ValueError:
                        print('That is not a valid number.')
                        continue
                break
            elif 'sp' in inside_bet.lower():
                bet_type = 'split'
                while True:
                    try:
                        # 00 is treated as 0 in this bet
                        print('One at a time, bet on two numbers that are one or three away (e.g. 10,11 or 2,5).')
                        num1 = int(input())
                        if num1 not in range(37):
                            print('That is not a valid number.')
                            continue
                        num2 = int(input())
                        if num2 not in range(37):
                            print('That is not a valid number.')
                            continue
                        if abs(num1 - num2) != 3 and abs(num1 - num2) != 1:
                            print('The two numbers were not one or three away.')
                            continue
                        chosen_nums.extend([num1,num2])
                        break
                    except ValueError:
                        print('That is not a valid number.')
                        continue
                break
            elif 'ds' in inside_bet.lower() or 'do' in inside_bet.lower():
                bet_type = 'double street'
                while True:
                    try:
                        print('Give only one number (1-31) to bet on it and the next consecutive five\n(e.g. 1: 1,2,3,4,5,6).')
                        num = int(input())
                        if num not in range(1,32):
                            print('That is not a valid number.')
                            continue
                        message = 'You have bet on '
                        for i in range(num, num + 5):
                            message = message + str(i) + ', '
                            chosen_nums.append(i)
                        message = message + 'and ' + str(num + 5)
                        chosen_nums.append(num + 5)
                        print(message)
                        break
                    except ValueError:
                        print('That is not a valid number.')
                        continue
                break
            elif 'st' in inside_bet.lower():
                bet_type = 'street'
                while True:
                    try:
                        print('Give only one number (1-34) to bet on it and the next consecutive three\n(e.g. 1: 1,2,3).')
                        num = int(input())
                        if num not in range(1,35):
                            print('That is not a valid number.')
                            continue
                        message = 'You have bet on '
                        for i in range(num, num + 2):
                            message = message + str(i) + ', '
                            chosen_nums.append(i)
                        message = message + 'and ' + str(num + 2)
                        chosen_nums.append(num + 2)
                        print(message)
                        break
                    except ValueError:
                        print('That is not a valid number.')
                        continue
                break
            elif 'tri' in inside_bet.lower():
                bet_type = 'trio'
                while True:
                    print('A three number bet that is either [0],1,2 or [00],2,3')
                    num = input()
                    if num == '0':
                        print('You have chosen 0, 1, and 2.')
                        chosen_nums.extend([0,1,2])
                        break
                    elif num == '00':
                        print('You have chosen 00, 2, and 3')
                        chosen_nums.extend(['00',2,3])
                        break
                    else:
                        print('That is not a valid number.')
                        continue
                break
            elif 'b' in inside_bet.lower():
                bet_type = 'basket'
                print('You have bet on 0, 00, 1, 2, and 3')
                chosen_nums.extend(['00',0,1,2,3])
                break
            else:
                print('That is not a valid bet.')
                continue
        elif 'o' in bet_type.lower() or 'outside' in bet_type.lower():
            print('Place a High, Low, Even, Odd, or Dozen bet.')
            outside_bet = input()
            if 'high' in outside_bet.lower() or '19' in outside_bet:
                bet_type = 'high'
                print('You have bet on numbers nineteen to thirty six.')
                chosen_nums.extend([i for i in range(19,37)])
                break
            elif 'low' in outside_bet.lower() or '1' in outside_bet:
                bet_type = 'low'
                print('You have bet on numbers one to eighteen.')
                chosen_nums.extend([i for i in range(1,19)])
                break
            elif 'even' in outside_bet.lower():
                bet_type = 'even'
                # Both 0 and 00 don't count as even or odd
                print('You have bet on all even numbers.')
                chosen_nums.extend([num for num in range(1,37) if num % 2 == 0])
                break
            elif 'odd' in outside_bet.lower():
                bet_type = 'odd'
                print('You have bet on all odd numbers.')
                chosen_nums.extend([num for num in range(1,37) if num % 2 != 0])
                break
            elif 'doz' in outside_bet.lower():
                bet_type = 'dozen'
                print('Choose a dozen to bet on: [F]first (1-12), [S]econd (13-24), [T]hird (25-36).')
                choice = input()
                if choice.lower() == 'f':
                    print('You have chosen the first dozen (1-12).')
                    chosen_nums.extend([i for i in range(1,13)])
                    break
                elif choice.lower() == 's':
                    print('You have chosen the second dozen (13-24).')
                    chosen_nums.extend([i for i in range(13,25)])
                    break
                elif choice.lower() == 't':
                    print('You have chosen the third dozen (25-36).')
                    chosen_nums.extend([i for i in range(25,37)])
                    break
                else:
                    print('That is not a valid bet.')
            else:
                print('That is not a valid bet.')         
        else:
            print('That is not a valid bet.')
            continue
    #print(chosen_nums)
    #print(bet_type)
    wheel = ['00']
    wheel.extend(range(0,37))
    ball = random.choice(wheel)
    # Where the ball lands
    print('The ball has landed on...')
    print('. ')
    time.sleep(1)
    print('. ')
    time.sleep(1)
    print('. ')
    time.sleep(1)
    print(str(ball))
    # Rewards based on what bet_type you choose
    if ball in chosen_nums:
        if bet_type == 'single':
            print('You have won!\n+' + str(35 * bet) + ' chips\n')
            return(35*bet)
        elif bet_type == 'split':
            print('You have won!\n+' + str(17 * bet) + ' chips\n')
            return(17*bet)
        elif bet_type == 'street':
            print('You have won!\n+' + str(11 * bet) + ' chips\n')
            return(11*bet)
        elif bet_type == 'double street':
            print('You have won!\n+' + str(5 * bet) + ' chips\n')
            return(5*bet)
        elif bet_type == 'trio':
            print('You have won!\n+' + str(11 * bet) + ' chips\n')
            return(11*bet)
        elif bet_type == 'basket':
            print('You have won!\n+' + str(6 * bet) + ' chips\n')
            return(6*bet)
        elif bet_type == 'high':
            print('You have won!\n+' + str(1 * bet) + ' chips\n')
            return(1*bet)
        elif bet_type == 'low':
            print('You have won!\n+' + str(1 * bet) + ' chips\n')
            return(1*bet)
        elif bet_type == 'even':
            print('You have won!\n+' + str(1 * bet) + ' chips\n')
            return(1*bet)
        elif bet_type == 'odd':
            print('You have won!\n+' + str(1 * bet) + ' chips\n')
            return(1*bet)
        elif bet_type == 'dozen':
            print('You have won!\n+' + str(2 * bet) + ' chips\n')
            return(2*bet)
    else:
        print('None of your numbers were landed on.\nYou have lost\n-' + str(bet)+ ' chips\n')
        return(-bet)

def casino(starting_bet):
    global money
    money = starting_bet
    print('')
    while True:
        print('You have ' + str(money) +' chips.')
        if money <= 0:
            print('You can no longer bet and are being kicked out.\nRestart? [R]')
            restart = input()
            if restart.lower() == 'r':
                casino(starting_bet)
            else:
                sys.exit('You have been kicked out.')
        print('What game would you like to play?')
        print('[FC]Flip a Coin, [CH]Cho Han, [PC]Pick a Card, [RL]roulette, [EXIT]')
        chosen_game = input()
        if 'fc' in chosen_game.lower() or chosen_game.lower() == 'flip a coin':
            print('How much would you like to bet?')
            given_bet = input()
            while True:
                try:
                    given_bet = int(given_bet)
                    if given_bet > money:
                        print('You have bet more than you have.')
                        casino(money)
                    if given_bet < 0:
                        print('You cannot bet negative chips')
                        casino(money)
                    break
                except ValueError:
                    print('That is not a valid bet.')
                    casino(money)
            print('Heads or tails?')
            guess = input()
            money += flip_coin(guess, given_bet)
            continue
        elif 'ch' in chosen_game.lower() or  chosen_game.lower() == 'cho han':
            print('How much would you like to bet?')
            given_bet = input()
            while True:
                try:
                    given_bet = int(given_bet)
                    if given_bet > money:
                        print('You have bet more than you have.')
                        casino(money)
                    if given_bet < 0:
                        print('You cannot bet negative chips')
                        casino(money)
                    break
                except ValueError:
                    print('That is not a valid bet.')
                    casino(money)
            print('Even or odd?')
            guess = input()
            money += cho_han(guess, given_bet)
            continue
        elif 'pc' in chosen_game.lower() or chosen_game.lower() == 'pick a card':
            print('How much would you like to bet?')
            given_bet = input()
            while True:
                try:
                    given_bet = int(given_bet)
                    if given_bet > money:
                        print('You have bet more than you have.')
                        casino(money)
                    break
                except ValueError:
                    print('That is not a valid bet.')
                    casino(money)
            money += pick_a_card(given_bet)
            continue
        elif 'rl' in chosen_game.lower() or chosen_game.lower() == 'roulette':
            print('How much would you like to bet?')
            given_bet = input()
            while True:
                try:
                    given_bet = int(given_bet)
                    if given_bet > money:
                        print('You have bet more than you have.')
                        casino(money)
                    if given_bet < 0:
                        print('You cannot bet negative chips')
                        casino(money)
                    break
                except ValueError:
                    print('That is not a valid bet.')
                    casino(money)
            money += roulette(given_bet)
            continue
        elif chosen_game.lower() == 'exit':
            print('Thank you for playing!')
            print('You have left with ' + str(money) + ' chips.')
            sys.exit('')
        else:
            print('That is a not a valid game.')
            continue

print('\nHow many chips do you have? ',end='')
while True:
    try:
        
        starting_bet = int(input())
        if starting_bet <= 0:
            print('You\'re too poor to be gambling in a casino.\n')
            print('How many chips do you have? ', end='')
            continue
        break
    except ValueError:
        print('\nI asked how many chips do you have? ', end='')

casino(starting_bet)