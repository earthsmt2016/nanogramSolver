"""
Class which is used to access the properties of a given 3 by 3 grid.
"""

import sys
sys.path.insert(0, "/home/earthsmt15/Documents/Coding/nanogramSolver2016/basicFunctions")

import useful_functions

class gridProperties:

	def __init__(self,width,height,grid,solutionGrid):
		self.width = width;
		self.height = height;
		self.plausibleGrid = grid;
		self.solutionGrid = solutionGrid;
		self.plausibleGridExpanded = [];
		self.uniqueCombinations = [];

	def convertGridAndSort(self):
		for indRow in self.plausibleGrid:
			self.plausibleGridExpanded.extend(indRow);
		self.uniqueCombinations = sorted(set(self.plausibleGridExpanded),reverse=True);

	def analyzeNanogramGrid(self):
		self.convertGridAndSort();
		if(self.width == self.height[::-1] and max(self.width)!=3 and max(self.height)!=3):
			for indexRow,indRow in enumerate(self.plausibleGrid):
				for indexElement,indElement in enumerate(indRow):
					if indElement==max(self.uniqueCombinations):
						self.solutionGrid[indexRow][indexElement]=1;
					if indElement==min(self.uniqueCombinations):
						self.solutionGrid[indexRow][indexElement]=1;
		else:
			for indexRow,indRow in enumerate(self.plausibleGrid):
				for indexElement,indElement in enumerate(indRow):
					if (indElement!=min(self.uniqueCombinations)):
						self.solutionGrid[indexRow][indexElement]=1;
					if (len(self.uniqueCombinations)==1):
						self.solutionGrid[indexRow][indexElement]=1;

		
			
			
		
		

