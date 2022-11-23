## About

Python program that fetches today's holidays from [nationaldaycalendar](https://nationaldaycalendar.com/) and formats into a text message to send to friends.

### Tech

- Python

  - [BeautifulSoup](https://pypi.org/project/beautifulsoup4/): used to parse html retrieved from the website.

  - [Emoji](https://pypi.org/project/emoji/): used to convert text to emojis for the text message.

  - [Pyperclip](https://pypi.org/project/pyperclip/): used for copying to clipboard for each operating system.

## Setup

1. `git clone https://github.com/eric-mahoney/national-holidays.git`.

1. Navigate to the directory that this repo was cloned to.

1. Install pipenv if you haven't already: `pip install pipenv` (or `pip3 install pipenv` if using python3 alias in cli).

1. Install all dependencies for the project: `pipenv install`.

## Use

1. Make sure you're in the directory that this was repo was cloned to.

1. Run the script by running `py Main.py` or `py3 Main.py` depending on your alias.

1. The script should run and copy the contents of the holidays to your clipboard.

1. Paste this anywhere you'd like to share it with people: text, email, social media, etc.
