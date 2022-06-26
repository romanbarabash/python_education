from apps.weather_client import weather_client


def main():
    weather_client.print_the_header()
    code = input('What code do you want the weather for? : ')
    html = weather_client.get_html_from_web(code)
    report = weather_client.get_weather_from_html(html)
    weather_client.print_report(report)


if __name__ == '__main__':
    main()
