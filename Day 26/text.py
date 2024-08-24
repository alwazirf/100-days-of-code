data1 = []
data2 = []
with open("file1.txt") as file_1:
    data_1 = file_1.readlines()
    for dat in data_1:
        data1.append(int(dat.strip()))
with open("file2.txt") as file_2:
    data_2 = file_2.readlines()
    for dat in data_2:
        data2.append(int(dat.strip()))
result = [dat for dat in data2 if dat in data1]

print(result)