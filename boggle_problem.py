#create our board with a couple of built in solutions
def createBoard():
	coord = []
	for y in range(4):
		for x in range(4):
			coord.append('('+str(x)+','+str(y)+')')
	board = {coord[0]:'M', coord[1]:'B', coord[2]:'C', coord[3]:'D', coord[4]:'A', coord[5]:'M', coord[6]:'G', coord[7]:'I', coord[8]:'G', coord[9]:'O', coord[10]:'A', coord[11]:'L', coord[12]:'M', coord[13]:'X', coord[14]:'O', coord[15]:'Z'}
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
		print(str(word[currentLetterIt])+" positions: "+str(letPos))
		nextPositions = isNextLetterAdjacent(board, letPos.pop(), word[currentLetterIt+1])
		if len(nextPositions) != 0:
			#is nextLetter the last letter?
			if len(word)-1 == currentLetterIt+1:
				print(str(word[currentLetterIt+1])+" is the next and last letter.")
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

def isNextLetterAdjacent(board, currentLetterPos, nextLetterVal):
	#Return a list of the the adjacent positions
	#that have the matching letter
	adjacentPositions = []
	print("Position we're getting the adjacent positions for: "+currentLetterPos)
	print(currentLetterPos)
	x = int(currentLetterPos[1])
	y = int(currentLetterPos[3])

	#map all 8 positions
	adjacentPositions.append((x-1, y-1))
	adjacentPositions.append((x-1, y))
	adjacentPositions.append((x-1, y+1))
	adjacentPositions.append((x, y-1))
	adjacentPositions.append((x, y+1))
	adjacentPositions.append((x+1, y-1))
	adjacentPositions.append((x+1, y))
	adjacentPositions.append((x+1, y+1))

	#remove illegal positions
	#flags to avoid ValueError
	negXFlag = False
	posXFlag = False
	if x-1 < 0:
		adjacentPositions.remove((x-1, y-1))
		adjacentPositions.remove((x-1, y))
		adjacentPositions.remove((x-1, y+1))
		negXFlag = True
	if x+1 > 3:
		adjacentPositions.remove((x+1, y-1))
		adjacentPositions.remove((x+1, y))
		adjacentPositions.remove((x+1, y+1))
		posXFlag = True
	if y-1 < 0:
		adjacentPositions.remove((x, y-1))
		if not negXFlag:
			adjacentPositions.remove((x-1, y-1))
		if not posXFlag:
			adjacentPositions.remove((x+1, y-1))
	if y+1 > 3:
		adjacentPositions.remove((x, y+1))
		if not negXFlag:
			adjacentPositions.remove((x-1, y+1))
		if not posXFlag:
			adjacentPositions.remove((x+1, y+1))
	
	#check legal positions for nextLetterVal
	print("These are the positions that are adjacent to our current letter: "+str(adjacentPositions))
	adjacentPositionsWithLetterVal = []
	for each in adjacentPositions:
		x, y = each
		if board['('+str(x)+','+str(y)+')'] == nextLetterVal:
			adjacentPositionsWithLetterVal.append('('+str(x)+','+str(y)+')')
	print("These are the positions that are adjacent with the next letter in them: "+str(adjacentPositionsWithLetterVal))
	return adjacentPositionsWithLetterVal

if __name__ == "__main__":
	board, coord = createBoard()
	printBoard(board, coord)
	chosenWord = getWord()
	printAnswer(isWordLegal(board, coord, chosenWord))
