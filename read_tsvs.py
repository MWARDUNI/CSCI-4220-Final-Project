import csv
import pandas as pd


class TSVLoader():
    def __init__(self) -> None:
        self.prop_map = self._read_prop_map()
        self.test = False
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
                reddit[source].append({"target": target, 'post_id': post_id, 'ts': ts, "sentiment": sentiment,
                                       "props": {self.prop_map[i]: x for i, x in enumerate(props.split(","))}})
                if self.test:
                    print(reddit)
                    break
        if self.test:
            print(len(reddit))
        return reddit

    def to_dataframe(self, reddit_data: dict) -> pd.DataFrame:
        rows = []
        for source, posts in reddit_data.items():
            for post in posts:
                # Flatten the props dictionary into the row
                row = {
                    "source": source,
                    "target": post["target"],
                    "post_id": post["post_id"],
                    "timestamp": post["ts"],
                    "sentiment": post["sentiment"],
                }
                row.update(post["props"])  # Add the properties as individual columns
                rows.append(row)
        return pd.DataFrame(rows)


if __name__ == "__main__":
    tsv_reader = TSVLoader()
    
    # Load the data into the nested dictionary format
    reddit_title_data = tsv_reader.main("soc-redditHyperlinks-title.tsv")
    reddit_body_data = tsv_reader.main("soc-redditHyperlinks-body.tsv")
    
    # Convert to pandas DataFrames
    df_title = tsv_reader.to_dataframe(reddit_title_data)
    df_body = tsv_reader.to_dataframe(reddit_body_data)
    
    # Output the DataFrame information
    print(df_title.head(10))
    print(df_body.head(10))

    