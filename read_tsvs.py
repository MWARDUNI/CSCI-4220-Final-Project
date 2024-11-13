import csv

if __name__ == "__main__":
    
    props_map = []
    with open("props_map.csv", "r") as props_file:
        reader = csv.reader(props_file)
        for line in reader:
            props_map = line
    
    
    reddit = {}
    with open("soc-redditHyperlinks-title.tsv", "r") as csv_file:
        reader = csv.reader(csv_file, delimiter="\t")
        for idx, line in enumerate(reader):
            if idx == 0:
                continue
            source = line[0]
            target = line[1]
            post_id = line[2]
            ts = line[3]
            sentiment = line[4]
            props = line[5]
            if source not in reddit.keys():
                reddit[source] = []
            reddit[source].append({"target":target, 'post_id':post_id, 'ts':ts, "sentiment":sentiment,
                                   
                                   "props":{props_map[i]:x for i, x in enumerate(props.split(","))}})
            # print(reddit)
            # break
    print(len(reddit))
            