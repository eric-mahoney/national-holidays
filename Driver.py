from bs4 import BeautifulSoup
import requests
import emoji
import pyperclip

# the url to fetch the national holidays from
URL = 'https://nationaldaycalendar.com/what-day-is-it/'
# the HTML class name for each of the events we're interested in
SEARCH_STRING = 'evcal_event_title'

class Driver:
    def __init__(self):
        self.browser = None
        self.text = ''
    
    # fetch the data and build the driver
    def build(self):
        request = requests.get(URL)
        self.browser = BeautifulSoup(request.content, "html.parser")
    
    # uses the emoji library to check each word in the holiday and return the emoji for it
    # (param) holiday: str - the current holiday (ex: 'National Pizza Day')
    def get_emojis(self, holiday):
        emojis = ''
        for word in holiday.split(' '):
            lowercase = word.lower()
            word_to_emoji = emoji.emojize(f':{lowercase}:', language='alias')
            if emoji.is_emoji(word_to_emoji):
                emojis += word_to_emoji
        return emojis
    
    # trims the raw html down to just the text of each holiday
    # (param) holidays: str[] - a formatted list of all of today's national holidays
    def trim_holiday_html(self, holidays):
        formatted = []
        for holiday in holidays:
            formatted.append(holiday.text)
        return sorted(formatted, key=len)
    
    # formats the holidays by length into a line separated text string
    # (param) holidays: str[] - a list of all of today's national holidays
    def format_holiday_text(self, holidays):
        text = ''
        formatted_holidays = self.trim_holiday_html(holidays)
        for index, holiday in enumerate(formatted_holidays):
            emojis = self.get_emojis(holiday)
            if index != len(holidays) - 1:
                text += f'- {holiday} {emojis}\n'
            else:
                text += f'- {holiday} {emojis}'
        return text
    
    # searches the html request for the search string we specified 
    # (ex: the class that each holiday has)
    def get_holidays(self):
        data = self.browser.find_all("span", class_=SEARCH_STRING)
        self.text = self.format_holiday_text(data)
        return self.text
    
    # copies the contents of the events to the clipboard
    def copy_to_clipboard(self):
        pyperclip.copy(self.text)
        return self.text
