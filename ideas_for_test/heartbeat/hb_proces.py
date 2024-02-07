import logging
import re
from datetime import datetime
from pathlib import Path

logging.basicConfig(filename="hb.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
filename = Path(__file__).parent / "hblog"

pattern = re.compile(r"Timestamp (\d+:\d+:\d+) Key (\S+)")
heartbit_dict = {}

with open(filename, mode="r") as f:
    for line in f:
        match = pattern.search(line)
        if match:
            timestamp = datetime.strptime(match.group(1), "%H:%M:%S")
            key = match.group(2)

            if key not in heartbit_dict:
                heartbit_dict[key] = []
            heartbit_dict[key].append(timestamp)

for key, timestamps in heartbit_dict.items():
    intervals = []
    for i in range(len(timestamps) - 1):
        intervals.append((timestamps[i] - timestamps[i + 1]).total_seconds())

    for interval in intervals:
        if 30 < interval <= 32:
            logging.warning(f"Heartbeat more than 30 seconds but less than 32 - Key: {key}")
        elif interval > 32:
            logging.error(f"Heartbeat exactly 32 seconds - Key: {key}")
