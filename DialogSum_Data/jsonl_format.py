import pandas as pd
import sys
import os

jsonl_file = sys.argv[1]
filename = os.path.splitext(jsonl_file)[0]

# Read JSONL file into a DataFrame
original_dataset = pd.read_json(jsonl_file, lines=True)
# Create a new DataFrame to store transformed data
transformed_df = pd.DataFrame(columns=["messages"])

# each entry should be:
#  {"messages": [{"role": "user", "content": "DIALOGUE"}, {"role": "model", "content": "SUMMARY"}]}
for _, row in original_dataset.iterrows():
    dialogue = row['dialogue']
    summary = row['summary']
    messages = [{"role": "user", "content": dialogue},
                {"role": "model", "content": summary}]
    transformed_df.loc[len(transformed_df)] = [messages]


# Write DataFrame to a new JSONL file
transformed_df.to_json(filename + ".transformed.jsonl", orient="records", lines=True)
