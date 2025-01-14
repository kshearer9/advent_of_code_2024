# Read data and split each line into a list of numbers
with open('day2_pt1_input.txt') as day2_pt1_input:
	data = day2_pt1_input.read()
	list_data = []
	for line in data.split('\n'):
		list_data.append(line.split(' '))
	# Change strings into integers
	list_data = [list(map(int, line)) for line in list_data]

# Create function which checks if numbers are ascending or descending
def ascending_or_descending(report):
	# Check if numbers are ascending, continue until it reaches the end of the list
	for i in range(1, len(report)):
		if report[i] > report[i-1]:
			if i == len(report)-1:
				return True
		# If list stops ascending at any point skip to check descending
		else:
			break
	# Same for descending, but return false if it stops descending
	for j in range(1, len(report)):
		if report[j] < report[j-1]:
			if j == len(report)-1:
				return True
		else:
			return False

# Create function to check if levels differ between 1-3
def safe_distance(report):
	for i in range(1, len(report)):
		if abs(report[i] - report[i-1]) >=1 and abs(report[i] - report[i-1]) <=3:
			continue
		else:
			return False
	return True

# Check how many are safe
safe_reports = 0
for report in list_data:
	if ascending_or_descending(report) and safe_distance(report):
		safe_reports += 1

print(safe_reports)