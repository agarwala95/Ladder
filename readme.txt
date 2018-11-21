Problem 1.1 Ladders

I used Python 3.5.4 for the assignment. My solution is breadth first search. This method searches for the goal word at every level of the tree
and then returns the previous nodes till the start word.

To easily traverse through the word file, I have used a hashing function where I denote each word with a hash value. This reduces the time to search
for a word. Also, only those words with the same letters/characters but with different order of characters have the same hash value.
I find the connecting nodes for a word using the function children() function. This connects each word to all words that can be obtained by adding a letter
or subtracting a letter.

I have used the following packages:
string
collections : defaultdict
queue : Queue
sys



