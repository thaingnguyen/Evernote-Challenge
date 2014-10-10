This problem seems easy at the beginning but it's tricky to handle number zero

First we need to calculate the product of all non-zero value in the list
Then, there are 3 possible cases:
	- The list has 0 zeros: for each element k, we print out product/k which is the product of all elements but k
	- The list has exactly 1 zeros:
		+ If that number is 0, we print out k
		+ If that number is not 0, we print out 0
	- The list has > 1 zeros, no matter what other elements are, the product of all elements but k will be 0


