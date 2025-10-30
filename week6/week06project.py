# To avoid division by zero I added an additional qualifier in the average function to make sure it doesn't error out. I also made sure it runs continuously, instead of only once. 

def read_data(data_file):
    with open(data_file) as hr_file:
        next(hr_file)
        output = []
        for line in hr_file:
            parts = line.split(",")
            for item in range(len(parts)):
                parts[item] = parts[item].strip()
            parts[3] = float(parts[3])

            output.append(parts)
        return output

data_list = read_data("testdata.txt")

# print(data_list)
def find_max(data_list, year=False):
    entity = ""
    max_exp = 0
    
    if year == False:
        returned_year = ""
        for item in data_list:
            if item[3] > max_exp:
                max_exp = item[3]
                entity = item[0]
                returned_year = item[2]

        return entity, max_exp, returned_year
    else:
        for item in data_list:
            if item[2] == year:
                if item[3] > max_exp:
                    max_exp = item[3]
                    entity = item[0]
        return entity, max_exp

def find_min(data_list, year=False):
    entity = ""
    min_exp = 120
    if year == False:
        returned_year = ""
        for item in data_list:
            if item[3] < min_exp:
                min_exp = item[3]
                entity = item[0]
                returned_year = item[2]

        return entity, min_exp, returned_year
    else:
        for item in data_list:
            if item[2] == year:
                if item[3] < min_exp:
                    min_exp = item[3]
                    entity = item[0]
        return entity, min_exp

def find_avg(data_list, year):
    total = 0
    count = 0
    for item in data_list:
        if item[2] == year:
            total += item[3]
            count += 1
    if count > 0:
        avg_exp = total/count
        return avg_exp
    else:
        return "0"

def main_loop(ext_list):
    data_file = read_data(ext_list)

    while True:
        year = input("Enter the year of interest: ")
        max_exp = find_max(data_file)
        min_exp = find_min(data_file)
        max_exp_year = find_max(data_file, year)
        min_exp_year = find_min(data_file, year)
        avg_exp = find_avg(data_file, year)
        print()
        print(f"""
The overall max life expectancy is: {float(max_exp[1]):.2f} from {max_exp[0]} in {max_exp[2]}
The overall min life expectancy is: {float(min_exp[1]):.2f} from {min_exp[0]} in {min_exp[2]}

For the year {year}:
The average life expectancy across all countries was {float(avg_exp):.2f}
The max life expectancy was in {max_exp_year[0]} with {float(max_exp_year[1]):.2f}
The min life expectancy was in {min_exp_year[0]} with {float(min_exp_year[1]):.2f}             
""")
        
main_loop("life-expectancy.csv")