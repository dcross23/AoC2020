#For fast solution, just need tileId, finalDrawing, getId(), matchesBelow() and matchedRight()
#The rest are created for slow solution
class Tile():
    def __init__(self, tileID, drawing): 
        self.tileID = tileID 
        self.originalDrawing = drawing 
        self.finalDrawing = drawing 
        self.visited = False 
        
    def isVisited(self):
    	return self.visited

    def setVisited(self, value):
    	self.visited = value

    def getID(self):
    	return self.tileID

    def getFinalDrawing(self):
    	return self.finalDrawing

    def resetFinalDrawing(self):
    	self.finalDrawing = self.originalDrawing.copy()

    def rotate(self):
    	newTile = []
    	for i in range(0,len(self.finalDrawing[0])):
    		s = ''
    		for t in reversed(self.finalDrawing):
    			s += t[i]
    		newTile.append(s);
    	self.finalDrawing = newTile

    def flip(self):
    	newTile = []
    	for t in reversed(self.finalDrawing):
    		newTile.append(t)
    	self.finalDrawing = newTile

    def matchesPossibilitiesBelow(self, tile):
    	for _ in range(2):
    		for _ in range(4):
    			if(self.finalDrawing[0] == tile[len(tile)-1]):
    				return True
    			else:
    				self.rotate()
    		self.resetFinalDrawing()
    		self.flip()
    	return False

    def matchesPossibilitiesRight(self, tile):
    	for _ in range(2):
    		for _ in range(4):
    			matches = True
    			for i,elem in enumerate(self.finalDrawing):
    				if(elem[0] != tile[i][len(tile)-1]):
    					matches = False
    					break

    			if(matches):
    				return True
    			else:
    				self.rotate()
    		self.resetFinalDrawing()
    		self.flip()
    	return False


    def matchesBelow(self, tile):
    	if(self.finalDrawing[0] == tile[len(tile)-1]):
    		return True
    	else:
    		return False

    def matchesRight(self, tile):
    	matches = True
    	for i,elem in enumerate(self.finalDrawing):
    		if(elem[0] != tile[i][len(tile)-1]):
    			matches = False
    			break

    	if(matches):
    		return True
    	else:
    		return False

    def removeBorders(self):
   		newTile = []
   		for i,l in enumerate(self.finalDrawing):
   			if(i>0 and i<len(self.finalDrawing)-1):
   				newTile.append(l[1:-1])
   		self.finalDrawing = newTile