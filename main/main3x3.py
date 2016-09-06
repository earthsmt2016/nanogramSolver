"""
Main function which is used to output the solution obtained from the nanogram solver.
"""

import sys
sys.path.insert(0, "/home/earthsmt15/Documents/coding/nanogramSolver/solvers/threeByThree")

from threeByThreeSolver import threeByThreeSolver 

#Main function
def main():
	widthCondition = [2,2,3];
	heightCondition = [3,3,1];
	print "Row Condition: "+str(widthCondition);
	print "Height Condition: "+str(heightCondition);
	solver = threeByThreeSolver(widthCondition,heightCondition);
	solver.generatePlausibleSpaces();
	solver.printContentsPlausibleSpaces();
	solver.solverPatternToGrid();

main();
