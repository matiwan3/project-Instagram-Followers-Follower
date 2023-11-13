import instaloader
import os
import json
from datetime import datetime

# Load Instagram credentials from credentials.py
from credentials import USERNAME, PASSWORD

# Create an instance of Instaloader
L = instaloader.Instaloader()

# Login to Instagram
L.load_session_from_file(USERNAME)

# Create a database file to store followers
db_file = 'followers_db.json'

# Check if the database file exists
if not os.path.exists(db_file):
    # If the file doesn't exist, create an empty database
    with open(db_file, 'w') as f:
        json.dump({}, f)

# Load previous followers data
with open(db_file, 'r') as f:
    try:
        previous_followers = json.load(f)
    except json.decoder.JSONDecodeError:
        previous_followers = {}

# Get the current followers
profile = instaloader.Profile.from_username(L.context, USERNAME)
current_followers = set(profile.get_followers())

# Compare current followers with previous followers
new_followers = current_followers - set(previous_followers.keys())
unfollowers = set(previous_followers.keys()) - current_followers

# Update the database with the current followers
current_followers_data = {str(follower.username): follower.full_name for follower in current_followers}
with open(db_file, 'w') as f:
    json.dump(current_followers_data, f, indent=2)

# Print the results
print(f"Total followers: {len(current_followers)}")

# Filter out followers that already exist in the previous data
new_followers = [follower for follower in new_followers if str(follower.username) not in previous_followers]

print(f"New followers: {len(new_followers)}")
for follower in new_followers:
    print(f"  - {follower.username} ({follower.full_name})")

# Filter out unfollowers that still exist in the current data
unfollowers = [unfollower for unfollower in unfollowers if str(unfollower) not in current_followers_data]

print(f"Unfollowers: {len(unfollowers)}")
for unfollower in unfollowers:
    print(f"  - {unfollower} ({previous_followers[unfollower]})")

