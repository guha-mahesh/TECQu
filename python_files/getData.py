import requests
from datetime import datetime
import json


def get_streak(username):
    url = f"https://alfa-leetcode-api.onrender.com/{username}/calendar"

    # Fetch data from the API
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Error: {response.status_code}")
        return None

    data = response.json()

    # Check the raw response data structure to debug
    print("Raw data from API:", data)

    # Extract submissionCalendar and parse it
    submission_calendar_str = data.get("submissionCalendar", "{}")

    try:
        # Convert the stringified JSON to a dictionary
        submission_calendar = json.loads(submission_calendar_str)
    except json.JSONDecodeError:
        print("Error: Failed to decode the submission calendar data.")
        return None

    # Extract the timestamps of the submissions (keys from the dictionary)
    submission_dates = [datetime.utcfromtimestamp(int(timestamp)).strftime("%Y-%m-%d")
                        for timestamp in submission_calendar.keys()]

    if not submission_dates:
        print("No submissions found for this user.")
        return 0

    # Sort dates in descending order (from most recent to oldest)
    submission_dates = sorted(submission_dates, reverse=True)

    # Calculate the streak
    streak = 1
    current_date = datetime.strptime(submission_dates[0], "%Y-%m-%d")

    for i in range(1, len(submission_dates)):
        previous_date = datetime.strptime(submission_dates[i], "%Y-%m-%d")
        # Check if the previous date is exactly one day before the current date
        if (current_date - previous_date).days == 1:
            streak += 1
            current_date = previous_date
        else:
            break  # Break the streak if there's a gap in consecutive days

    return streak


# Example usage
username = "guhamahesh"  # Replace with the actual username
streak = get_streak(username)
if streak is not None:
    print(f"{username}'s streak: {streak} consecutive days of submission.")
