"""
The Ancient Game of Nimm
"""



def main():
    stones = 20
    players = 2
    print("There are " + str(stones) + " stones left")
    while stones > 0:
        players = decide_player(players)
        amount = int(input("Player " + str(players) + " would you like to remove 1 or 2 stones? "))
        if amount == 1 or amount == 2:
            stones -= amount
            print("")
        else:
            amount = int(input("Please enter 1 or 2: "))
            stones -= amount
            print("")
        if stones > 0:
            print("There are " + str(stones) + " stones left")
    if players == 2:
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")
        
def decide_player(players):
    if players == 2:
        players -= 1
        return players
    else:
        players += 1
        return players




if __name__ == '__main__':
    main()
