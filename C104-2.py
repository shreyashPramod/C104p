from collections import Counter
import csv


with open('SOCR-HeightWeight.csv',newline='')as f:
    reader=csv.reader(f)
    file_data=list(reader)
file_data.pop(0)

#sourting data to get the height of people
new_data=[]
for i in range(len(file_data)):
    n_num=file_data[i][1]
    new_data.append(n_num)

#calculating mode
data=Counter(new_data)
mode_data_for_range={
    "60-70":0,
    "70-80":0,
    "80-90":0
}

for height,occurence in data.items():
    if 60 < float(height) < 70:
        mode_data_for_range["60-70"] += occurence 
    elif 70 < float(height) < 80: 
        mode_data_for_range["70-80"] += occurence 
    elif 80 < float(height) < 90: 
        mode_data_for_range["80-90"] += occurence

mode_range,mode_occurence=0,0
for range, occurence in mode_data_for_range.items(): 
    if occurence > mode_occurence: 
        mode_range, mode_occurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurence 
mode = float((mode_range[0] + mode_range[1]) / 1) 
print(f"Mode is -> {mode:2f}")
