We can easily see that this buffer is actually a modified bounded circular queue when you can add as many variables as you want and newest elements will override oldest one if neccesary.

In order to solve this problem, we have to keep track of three variables:
begin_queue : index of first element in queue
end_queue : index of first element in queue
current_size : number of element in queue

Note: 
For circular queue, when current index > size, we have to go back to index 0 and continue to enqueue or dequeue. Instead of having a conditional statement to handle this situation, we just need to assign begin_queue/end_queue = (begin_queue/end_queue + 1) % size

For "A" command:
	- Check whether the "override" thing happens or current_size + k > queue_size with k is the number of entries add. 
		+ If it happens, increase begin_queue to the correct position (begin_queue + (current_size-size)) % size and set current_size 			to queue_size
		+ If it doesn't, simply update current_size by k
	- Enqueue k elements as usual
For "R" command:
	- Since we can assume we never remove more than the number of entries in the queue, we just need to increase begin_queue to the 	correct position and decrease current_size
For "L" command:
	- Have a temporary variable go from index begin_queue to index end_queue and print it out
For "Q" command:
	- Stop

Analysis:
"A" command: O(k) with k is the number of entries added
"R" command: O(1)
"L" command: O(n) with n is the size of the buffer
"Q" command: O(1)
Space	   : O(n) with n is the size of the buffer
