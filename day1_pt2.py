# Get both lists from pt 1 file
from day1_pt1 import ls1, ls2

# Set similarity score to zero
sim_score = 0

# For each item in list 1, check how many times it is in list 2, multiply it by this count and add to similarity score
for i in ls1:
	sim_score += i * ls2.count(i)

print(sim_score)