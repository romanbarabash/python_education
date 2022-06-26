import bs4
import requests
import collections

WeatherReport = collections.namedtuple('WeatherReport', 'condition, temp, scale, loc')


def print_the_header():
    print('-----------------------------------------------------')
    print('                    WEATHER APP')
    print('-----------------------------------------------------')
    print()


def get_html_from_web(code):
    url = 'https://www.wunderground.com/weather-forecast/{}'.format(code)
    response = requests.get(url)
    return response.text


def get_weather_from_html(html):
    soup = bs4.BeautifulSoup(html, 'html.parser')
    loc = soup.find(class_='columns small-12').find('h1').get_text()
    condition = soup.find(class_='condition-icon').find('p').get_text()
    temp = soup.find(class_='test-false wu-unit wu-unit-temperature').find(class_='wu-value wu-value-to').get_text()
    scale = soup.find(class_='test-false wu-unit wu-unit-temperature').find(class_='wu-label').get_text()

    clean_loc = cleanup_text(loc)
    location = find_city_and_state_from_location(clean_loc)
    condition = cleanup_text(condition)
    temp = cleanup_text(temp)
    scale = cleanup_text(scale)

    return WeatherReport(condition=condition, temp=temp, scale=scale, loc=location )


def find_city_and_state_from_location(loc: str):
    parts = loc.split('\n')
    return parts[0].strip()


def cleanup_text(text: str):
    if not text:
        return text

    text = text.strip()
    return text


def print_report(report):
    print('The temp in {} is {} {} and {}'.format(report.loc, report.temp, report.scale, report.condition))
