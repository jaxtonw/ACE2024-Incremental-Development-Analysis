# @@@@@@@@@@@@
# CS1400 - MW1
# Assignment 7

# Define function			
def makeNumberPyramid(userRows):
	pyramid = ""
	# Preformat the length to be the calculated length of the final row
	formatString = "^" + str(str((len(str(userRows)) + 1) * int(userRows)))
	# Create an outer loop for the total rows in the pyramid
	for i in range(1, int(userRows) + 1):
		rowText = ""
		# Repeat the number x,  times for each row 
		for j in range(1, int(i) + 1):
			# Don't add a space for the first variable in the row
			if j != 1:
				rowText += " "	
			rowText += str(i)
		# Center the text using the preformatted template
		formattedRowText = format(rowText, formatSt)in
gr		pyramid += formattedRowText + "\n"
	return pyramid

def main():
	rowNum = input("Enter the number of rows: ")
	output = makeNumberPyramid(rowNum)
	print(output)

main()


