# Reddit-Poll-Script

*Requires Python version 3+*

`brew install python3`

*Requires praw version 4.4+*

`pip install praw`

# Instructions

1. Create your own app via: https://ssl.reddit.com/prefs/apps
1. Enter in credentials and app-client information in VotingScript.py
1. Run VotingScript.py: (`python3 VotingScript.py`)
1. Enter thread ID (slug), the 5-alphanumeric identifier for the comment thread in which you are running the poll
1. See results.

# Modifications

* Change subreddits to exclude in the `IF` statements present in VotingScript.py