import csv


time_data = []

with open('data.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        time_data.append(row)
        
column_data = [["Test name", "Diff"]]
table_data = [["Test name", "Run time"]]

for row in time_data[1:]:
    test_name = row[0]
    run_time = float(row[1])
    avg_time = float(row[2])
    diff_avg = avg_time - run_time
    column_data.append([test_name, diff_avg])
    table_data.append([test_name, run_time])
