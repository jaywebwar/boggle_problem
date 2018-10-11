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
	word = input()
	return word

#check the board against our chosen word
def isWordLegal(board, coord, word, currentLetterIt = None, letPos = None):
	if currentLetterIt == None:
		currentLetterIt = 0
		#where is currentLetter
		letPos = findLetterPos(board, coord, word[currentLetterIt])
	if len(letPos) == 0:
		#there are no positions
		return False
	for number in range(len(letPos)):
		#check if nextLetter is adjacent to currentLetter
		isIt, nextPositions = isNextLetterAdjacent(board, coord, letPos.pop(), word[currentLetterIt+1])
		if isIt:
			#is nextLetter the last letter?
			if len(word)-1 == currentLetterIt+1:
				return True
			#advance letterIt and check if legal
			currentLetterIt = currentLetterIt +1
			if isWordLegal(board, coord, word, currentLetterIt, nextPositions):
				return True
	#None of the positions had the next letter
	return False

#print whether the word is legal or not
def printAnswer(isLegal):
	if isLegal:
		print("Good answer")
	else:
		print("Bad answer")

#helper functions for isWordLegal
def findLetterPos(board, coord, letter):
	positions = []
	#return all  positions on the board that match letter
	for each in coord:
		if board[each] == letter:
			positions.append(each)
	return positions

def isNextLetterAdjacent(board, coord, currentLetterPos, nextLetterVal):
	#This function needs to return bool for whether or not the next
	#letter is adjacent and return a list of the the adjacent positions
	#that have the matching letter
	return None, None

if __name__ == "__main__":
	board, coord = createBoard()
	printBoard(board, coord)
	chosenWord = getWord()
	printAnswer(isWordLegal(board, coord, chosenWord))
