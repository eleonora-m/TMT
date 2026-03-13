import os
import time
import logging
from nyct_gtfs import NYCTFeed

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Get subway line from environment variable, default to 'L'
subway_line = os.getenv('SUBWAY_LINE', 'L')

logging.info(f"Monitoring subway line: {subway_line}")

# Initialize the feed
feed = NYCTFeed(subway_line)

while True:
    try:
        # Refresh the feed data
        feed.refresh()

        # Filter for active trains on the specified line
        active_trains = feed.filter_trips(line_id=subway_line, underway=True)

        num_active = len(active_trains)

        # Log the number of active trains
        logging.info(f"Number of active {subway_line} trains: {num_active}")

    except Exception as e:
        logging.error(f"Error fetching data: {e}")

    # Wait 30 seconds before next check
    time.sleep(30)