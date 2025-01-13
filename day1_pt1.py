with open('Day1_Input', 'r') as day1_input:
	lines = day1_input.readlines()

ls1 = []
ls2 = []

for l in lines:
	line_split = l.split("   ")
	ls1.append(int(line_split[0]))
	ls2.append(int(line_split[1]))


ls1.sort()
ls2.sort()
joined_list = list(zip(ls1, ls2))

total = 0
for i in joined_list:
	total += abs(i[1]- i[0])

print(total)