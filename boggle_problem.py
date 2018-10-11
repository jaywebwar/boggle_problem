#create our board with a couple of built in solutions
def createBoard():
	coord = []
	for i in range(4):
		for j in range(4):
			coord.append("("+str(i)+","+str(j)+")")
	board = {coord[0]:'A', coord[1]:'B', coord[2]:'C', coord[3]:'D', coord[4]:'E', coord[5]:'F', coord[6]:'G', coord[7]:'H', coord[8]:'I', coord[9]:'J', coord[10]:'K', coord[11]:'L', coord[12]:'M', coord[13]:'N', coord[14]:'O', coord[15]:'P'}
	print(board)
	return board

#print the board to the user
def printBoard(board):
	return None

#choose a word
def getWord():
	return None

#check the board against our chosen word
def isWordLegal(board, word):
	return None

#print whether the word is legal or not
def printAnswer(isLegal):
	return None

if __name__ == "__main__":
	board = createBoard()
	#printBoard(board)
	#chosenWord = getWord()
	#printAnswer(isWordLegal(board, chosenWord))
