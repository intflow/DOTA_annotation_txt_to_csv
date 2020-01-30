import os
import csv

## txt to csv
path_list = []
for (Par, Subs, Files) in os.walk('/home/gbkim/gb_dev/RetinaNet_Tensorflow_Rotation/data/io/DOTA/'):
    for each_file in Files:
        ext = os.path.splitext(each_file)[-1]
        if ext == '.txt':
            file_path = os.path.join(Par, each_file)
            path_list.append(file_path)            
print(len(path_list))

for each_txt in path_list:
    #Open txt file
    with open(each_txt, 'r') as f:
        stripped = (line.strip() for line in f)
        lines = (line.split(' ') for line in stripped if line)
        
        csv_file_path = os.path.splitext(each_txt)[0]+'.csv'
        with open(csv_file_path, 'w') as out_file:
            writer = csv.writer(out_file)
            writer.writerows(lines)
