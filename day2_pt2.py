from day2_pt1 import list_data, ascending_or_descending, safe_distance

safe_reports = 0

# Loop through each report
for report in list_data:
	# Check which ones are safe without removing anything
	if ascending_or_descending(report) and safe_distance(report):
		safe_reports += 1
	else:
		for i in range(0, len(report)):
			# Remove each number and check if the report is safe without it
			number_deleted = report.pop(i)
			if ascending_or_descending(report) and safe_distance(report):
				safe_reports += 1
				break
			# If not, add the number back in and check the next
			else:
				report.insert(i, number_deleted)

print(safe_reports)