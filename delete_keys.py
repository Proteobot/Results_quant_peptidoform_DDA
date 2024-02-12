"""Delete entries in results.json using pandas."""
import argparse
import json
import logging

import pandas as pd

logging.basicConfig(level=logging.INFO,
                    filename='delete_log.txt',
                    format='%(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %H:%M:%S')
logging.getLogger().addHandler(logging.StreamHandler())

parser = argparse.ArgumentParser(description='Delete keys from a JSON file')
parser.add_argument('--json_file', '-f',
                    default='results.json',
                    # type=str,
                    # required=False,
                    help='The JSON file to modify')
parser.add_argument('--keys', '-k',
                    nargs='+',
                    required=True,
                    help='The keys to delete')

# %%
args = parser.parse_args()

with open(args.json_file) as f:
    all_datapoints = pd.read_json(args.json_file).set_index('id')

to_keep = list()
deleted = list()
for idx in all_datapoints.index:
    # keep original order:
    if idx not in args.keys:
        to_keep.append(idx)
    else:
        deleted.append(idx)

for key in args.keys:
    if key in deleted:
        logging.warning(f'Deleting information: {key}')
    else:
        logging.warning(f'Key not found: {key}')

all_datapoints.loc[to_keep].reset_index().to_json(
    args.json_file, orient="records", indent=2)
