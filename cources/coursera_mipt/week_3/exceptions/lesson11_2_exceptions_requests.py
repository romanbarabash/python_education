import requests

url = "https://github.com/not_found"

try:
    response = requests.get(url, timeout=30)
    response.raise_for_status()
except requests.Timeout:
    print("timeout error, url:", url)
except requests.HTTPError as err:
    code = err.response.status_code
    print("error in url: {0}, code: {1}".format(url, code))
except requests.RequestException:
    print("error in url downloading: ", url)
else:
    print(response.content)

