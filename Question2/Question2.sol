For this problem, Hash Table (or Dictionary in Python) is a perfect data structure.

Algorithms
1. Iterate through all the words, add it to the hash table with key is that word and value is the frequency.
2. Get the list of all tuple(value,key) which is (freq,word) from the hash table
3. Sort it with increasing word
4. Sort it again with decreasing freq (The sort algorithm is stable)
5. Print out first k elements

Analysis
Run time : O(n)
Space	 : O(n) 
