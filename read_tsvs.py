import csv

class TSVLoader():
    def __init__(self) -> None:
        self.prop_map = self._read_prop_map()
        self.test = False
        self.use_props = False
        return None

    def _read_prop_map(self) -> list:
        props_map = []
        with open("props_mapping/props_map.csv", "r") as props_file:
            reader = csv.reader(props_file)
            for line in reader:
                props_map = line
        return props_map


    def main(self, filename) -> dict:
        if ".tsv" not in filename:
            raise RuntimeError("File must be tab separated!")
        
        reddit = {}
        with open(filename, "r") as csv_file:
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
                if self.use_props:
                    reddit[source].append({target: 
                                            {"post_id": post_id, 
                                            "ts": ts, 
                                            "sentiment": sentiment,
                                            "props": {self.prop_map[i]:x for i, x in enumerate(props.split(","))}}})
                else:
                        reddit[source].append({target: 
                                            {"post_id": post_id, 
                                            "ts": ts, 
                                            "sentiment": sentiment}})
                        
                if self.test:
                    print(reddit)
                    break
        if self.test:
            print(len(reddit))
        return reddit


if __name__ == "__main__":
    
    tsv_reader = TSVLoader()
    graphable_object = tsv_reader.main("soc-redditHyperlinks-title.tsv")
    print(len(graphable_object))
            