Problem 1: Word Occurrence Tracker
Input Processing:

#First, we take the total number of words as input.
Then, we read each word for the given number of lines.
Tracking Word Occurrences:

#We use a dictionary to keep track of how many times each word appears.
We also use a list to remember the order in which each unique word first appears.
Output:

The first line of output should show how many distinct words were entered.
The second line should display how many times each word appeared, in the order of their first appearance.

Problem 2: Credit Card Number Validator
#Check the Format:

The card number should either have 16 digits or be written as 4 groups of 4 digits, separated by hyphens. A regular expression pattern can be used to check this.
If the card number uses hyphens, they should only appear after every group of 4 digits.
#Check for  Repeated Digits:

There should be no sequence of 4 or more repeated digits in a row.
Output:

For each credit card number, if it follows these rules, print "Valid". Otherwise, print "Invalid".
