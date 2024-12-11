import os
import json
from datetime import datetime, timedelta
from load_config import load_config

def get_last_run_date():
    """
    Checks if last_run.json exists. If it does, return the stored date.
    If not, return the default date from config.
    """
    config = load_config()
    default_date_str = config.get("default_last_run_date", "2024-01-01")
    last_run_path = os.path.join(os.path.dirname(__file__), '..', 'last_run.json')
    
    if os.path.exists(last_run_path):
        # Read the last_run.json file
        with open(last_run_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            last_run_str = data.get("last_run_date", default_date_str)
    else:
        # Use the default date from config if file does not exist
        last_run_str = default_date_str

    # Convert string to a date object for easier manipulation
    last_run_date = datetime.strptime(last_run_str, "%Y-%m-%d")
    return last_run_date

def update_last_run_date(new_date):
    """
    After a successful fetch, update last_run.json with the new date.
    new_date should be a datetime object.
    """
    last_run_path = os.path.join(os.path.dirname(__file__), '..', 'last_run.json')
    data = {
        "last_run_date": new_date.strftime("%Y-%m-%d")
    }
    with open(last_run_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)

def get_date_range_for_fetch():
    """
    Determine the current date and set the query to fetch papers from
    the day after last_run_date up to today.
    
    Returns:
      (start_date_str, end_date_str) in 'YYYYMMDD' format.
    """
    # Get the last run date
    last_run_date = get_last_run_date()

    # The new start date is one day after the last run date
    start_date = last_run_date + timedelta(days=1)

    # Today’s date
    today = datetime.utcnow()  # using UTC time for consistency
    end_date = today

    # Convert these to 'YYYYMMDD' strings
    start_date_str = start_date.strftime("%Y%m%d")
    end_date_str = end_date.strftime("%Y%m%d")

    return start_date_str, end_date_str

# Optional test
if __name__ == "__main__":
    start_str, end_str = get_date_range_for_fetch()
    print("Start:", start_str, "End:", end_str)

