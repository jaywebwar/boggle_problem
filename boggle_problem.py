#create our board with a couple of built in solutions
def createBoard():
	coord = []
	for i in range(4):
		for j in range(4):
			coord.append("("+str(i)+","+str(j)+")")
	board = {coord[0]:'A', coord[1]:'B', coord[2]:'C', coord[3]:'D', coord[4]:'E', coord[5]:'M', coord[6]:'G', coord[7]:'I', coord[8]:'I', coord[9]:'O', coord[10]:'A', coord[11]:'L', coord[12]:'C', coord[13]:'X', coord[14]:'O', coord[15]:'Z'}
	return board, coord

#print the board to the user
def printBoard(board, coord, it = None):
	if it == None:
		it = 0
	print(board[coord[it]]+', '+board[coord[it+1]]+', '+board[coord[it+2]]+', '+board[coord[it+3]])
	it = it + 4
	if it == 16:
		return None
	else:
		printBoard(board, coord, it)

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
	board, coord = createBoard()
	printBoard(board, coord)
	#chosenWord = getWord()
	#printAnswer(isWordLegal(board, chosenWord))
