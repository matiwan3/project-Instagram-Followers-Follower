# Instagram Follower Tracker

## Introduction

This Python script is designed to track changes in your Instagram followers, providing information on new followers and unfollowers since the last script run. The script uses the `instaloader` library for interacting with Instagram.

## Features

- Logs in to Instagram using provided credentials.
- Fetches current followers and compares them with the previous run.
- Prints total followers, new followers, and unfollowers since the last run.
- Stores follower data in a JSON file for future comparisons.

## Prerequisites

- Python 3.x
- Required Python packages: `instaloader`

## Installation

1. **Clone the repository, install the required packages, and create a `credentials.py` file:**

   ```bash
   git clone https://github.com/yourusername/instagram-follower-tracker.git
   cd instagram-follower-tracker
   pip install instaloader
   ```
2. Create a credentials.py file
   ```bash
    USERNAME = 'your_instagram_username'
    PASSWORD = 'your_instagram_password'
   ```
3. Run the script:
   ```bash
     python instagram_follower_tracker.py
   ```
<b>The script will output the following information:</b>
<li> Total followers. </li>
<li> New followers (excluding those already in the previous data). </li>
<li> Unfollowers (excluding those still present in the current data). </li>

## Important Note
Please be aware that web scraping Instagram data may violate Instagram's terms of service. Ensure you comply with their policies and use the script responsibly.

## License
This project is licensed under the MIT License - see the [LICENSE](https://chat.openai.com/c/LICENSE) file for details.
