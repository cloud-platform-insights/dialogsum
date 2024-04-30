import pandas as pd
import sys
import os

jsonl_file = sys.argv[1]
filename = os.path.splitext(jsonl_file)[0]

# Read JSONL file into a DataFrame
df = pd.read_json(jsonl_file, lines=True)

# Write DataFrame to a CSV file
df.to_csv(filename + ".csv", index=False) 
