class chessboard:
	def __init__(self,N=4):
		self.N=N5
		self.column=[]

	def safe(self,column):
		row = len(self.column)
		for q_column in self.column:
			if column==q_column:
				return False
		for q_row,q_column in enumerate(self.column):
			if q_column-q_row==column-row:
				return False
		for q_row, q_column in enumerate(self.column):
		    if ((self.N - q_column) - q_row == (self.N - column) - row):
		        return False
		return True
	def display(self):
	    for row in range(self.N):
	        for column in range(self.N):
	            if column == self.column[row]:
	                print("Q",end=' ')
	            else:
	                print("*",end=' ')
	        print()

def print_solutions_start(size):
    board = chessboard(size)
    number_sols = print_solutions(board)
    return number_sols

def print_solutions(board):
	size = board.N
	if size == len(board.column):
		board.display()
		print()
		return 1
	solutions=0
	for column in range(size):
		if board.safe(column):
			board.column.append(column)
			solutions+=print_solutions(board)
			board.column.pop()
	return solutions

n = int(input("Enter N:"))
num = print_solutions_start(n)
print("Number of solutions:",num)