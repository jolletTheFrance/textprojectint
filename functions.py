import random

winners_path=r'C:\Users\guy11\Desktop\devops\winners.txt'

def rstFile(txt_path):
    '''
    create the treasure map
    :param txt_path: path to the text file
    :return:
    '''
    with open(txt_path, 'w+') as file:
        for num in range(10):
            rndnum = random.randint(1,20)
            for singelNum in range(rndnum):
                file.write(str(num))
        file.write("TREASURE")
        for num in range(9,-1,-1):
            rndnum = random.randint(1,20)
            for singelNum in range(rndnum):
                file.write(str(num))
def moveInputCheck(moveAmount, moveDir, myIndex, fileLen):
    """
    checks that the player doent move from text limits
    :param moveAmount: how much the player wants to move
    :param moveDir: in what direction they want to move
    :param myIndex: what index is the file at now
    :param fileLen: how muvh chars are in the file
    :return: true if move is possiable false if not
    """
    try:
        moveAmount = int(moveAmount)
    except:
        return False
    if int(moveDir) == 1 and (myIndex+moveAmount < fileLen):
        return True
    elif int(moveDir) == 0 and (myIndex-moveAmount > 0):
        return True
    else:
        return False

def getwinner():
    """
    opens a file if one doesnt exist then copy each line without the /n
    creates winnertable!
    :return: list of winners and the score
    """
    winnertable = []
    try:
        winners_path = open("winner_table.txt", 'r')

    except:
        winners_path = open("winner_table.txt", 'w')
        winners_path.close()
        winners_path = open("winner_table.txt", 'r')

    for line in winners_path:
        winnertable.append(line.split(" "))
        winnertable[len(winnertable)-1][1] = winnertable[len(winnertable)-1][1].replace("\n", "")
    return winnertable


def setwinner(winnertable,score):
    """
    checks if a players is at top ten if yes calls savewinner function
    :param winnertable: list of winners and scores
    :param score: current score
    :return:
    """
    if len(winnertable) < 10:
        winnertable.append([input("you are at top 10!!! enter your nickname: "), score])
        savewinner(winnertable)
    if int(winnertable[len(winnertable)-1][1]) > score:
        winnertable[len(winnertable)-1][1] = score
        winnertable[len(winnertable) - 1][0] = input("you are at top 10!!! enter your nickname: ")
        savewinner(winnertable)

def savewinner(winnertable):
    """
    sorts the 2D table by the second cell in each bigger cell and saves the winners table again line by line
    :param winnertable: list of winners and scores
    :return:
    """
    if len(winnertable) != 2:
        winnertable.sort(key=lambda x: int(x[1]))
    winners_path = open("winner_table.txt","w")
    for cell in winnertable:
        winners_path.write(str(cell[0]))
        winners_path.write(" ")
        winners_path.write(str(cell[1])+"\n")

def printwinner(winnertable):
    """
    just prints the top 10
    :param winnertable: list of winners and scores
    :return:
    """
    print("\n\n\ntop scores:")
    for cell in winnertable:
        print(cell)