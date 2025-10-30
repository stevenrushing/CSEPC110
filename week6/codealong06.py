# expected output
# Alexia (ID: 1913), Engineer - $84000.00
# Herman (ID: 4266), Manager - $106000.00
# Jay (ID: 5849), Engineer - $93000.00
# Ahmad (ID: 1326), Tester - $85000.00

with open("hr_system.txt") as hr_file:
    next(hr_file)
    for line in hr_file:
        parts = line.split(" ")
        name = parts[0]
        job_id = parts[1]
        job_title = parts[2]
        salary = parts[3]

        print(f"{name} (ID: {job_id})")