import functions

winnettable = functions.getwinner()
char = '14325234' #current char the player is on
tries = 0 #just tries...
myIndex = 0 #index of the char
txt_path = r'C:\Users\guy11\Desktop\devops\text.txt'

functions.rstFile(txt_path)
myfile = open(txt_path,'r')
file_len = len(myfile.read()) #gets length of the file
while char not in "TREASURE": #runs until the player lands on a letter
    movedir = input("where do you want to move 1 for Forward 0 for Backwards ") #player choose driction
    if (movedir == '0' and myIndex==0): #prevent moving backwards when in start of file
        print("cant move backwards! move direction auto-changed to forward")
        movedir = '1'
    while (movedir not in ['0','1']): #input check 0/1 only
        print("wrong input")
        movedir = input("where do you want to move 1 for Forward 0 for Backwards ")

    moveAmount= input("how much do you wnat to move?")
    while functions.moveInputCheck(moveAmount,movedir,myIndex, file_len)==False: #input check for text limits and invalid input
        moveAmount = input("please enter a valid move ammount (you entered a big number or even not a number at all)")

    moveAmount = int(moveAmount)
    if int(movedir) == 1: #moves in the file -1 to read the landed char
        myIndex += moveAmount
        myfile.seek(myIndex-1)
    elif int(movedir) == 0:
        myIndex -= moveAmount
        myfile.seek(myIndex-1)
    char = str(myfile.read(1)) #prints the landed char
    print(f"you landed on {char}")
    tries += 1
    myfile.seek(myIndex)
print(f"nice! it took you {tries} tries")
functions.setwinner(winnettable, tries)
functions.printwinner(winnettable)