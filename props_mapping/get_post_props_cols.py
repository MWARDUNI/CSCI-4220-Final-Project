
import csv


if __name__ == "__main__":
    columns = []
    with open("post_props.csv", "r") as csv_file:
        reader = csv.reader(csv_file, delimiter=".")
        for line in reader:
            columns.append(line[1].strip())
    
    with open("props_map.csv", "w") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(columns)
        
    
    