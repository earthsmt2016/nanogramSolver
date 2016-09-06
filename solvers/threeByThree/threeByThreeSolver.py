"""
Class which is used to solve 3x3 nanogram solver puzzles.
"""

import sys
sys.path.insert(0, "/home/earthsmt15/Documents/coding/nanogramSolver/basicFunctions")

import useful_functions
from gridProperties import gridProperties

class threeByThreeSolver(object):
	
	grid_size = 3;

	def __init__(self,widthConditions,heightConditions):
		self.plausibleSolution = [];
		self.solutionToGrid = [];
		self.widthConditions = widthConditions;
		self.heightConditions = heightConditions;

	def generatePlausibleSpaces(self):
		for heightElement in self.heightConditions:
			perHeightScore = [];
			perSolutionScore = [];
			for widthElement in self.widthConditions:
				indScore = heightElement*widthElement;
				perHeightScore.append(indScore);
				perSolutionScore.append(0);
			self.plausibleSolution.append(perHeightScore);
			self.solutionToGrid.append(perSolutionScore);

	def printContentsPlausibleSpaces(self):
		useful_functions.printList(self.plausibleSolution);

	def solverPatternToGrid(self):
		gridPropertiesAnalyzer = gridProperties(self.widthConditions,self.heightConditions,self.plausibleSolution,self.solutionToGrid);
		gridPropertiesAnalyzer.analyzeNanogramGrid();
		print "\n";
		useful_functions.printList(gridPropertiesAnalyzer.solutionGrid);

				
				
		
