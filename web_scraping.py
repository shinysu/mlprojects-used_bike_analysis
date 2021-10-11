#extract bike details from website
import requests
from bs4 import BeautifulSoup
import re
from cleanup import cleanup_record
from file_ops import write_csv_file


def get_html(url):
    try:
        response = requests.get(url)
        return response.content
    except requests.ConnectionError as e:
        print("Connection Error. Make sure you are connected to Internet.\n")
        print(str(e))
    except requests.Timeout as e:
        print("Timeout Error")
        print(str(e))


def remove_spaces(words):
    return [word.strip() for word in words if word.strip()]


def split_elements(line):
    return re.split('\n|\t', line)


def get_all_items(html):
    soup = BeautifulSoup(html, 'lxml')
    all_bikes = soup.find("div", {"id": "usedbike_filter_list"}).find_all("div", {"class": "card-box-shadow"})
    bike_details = []
    for bike in all_bikes:
        bikename = bike.find('a').text
        bike_divs = bike.find_all("div", {"class": "col-6"})
        data = remove_spaces(split_elements(bike_divs[0].text))
        location = data[0]
        kilometers = data[1]
        model = data[2]
        engine = remove_spaces(bike_divs[1].text.split('\n'))[1]
        price = split_elements(remove_spaces(bike_divs[2].text.split('₹'))[0])[0]
        bike_details.append([bikename, model, engine, price, kilometers, location])
    return bike_details


if __name__ == '__main__':
    url = 'http://www.vicky.in/bike/second-hand-bikes-in-chennai/page/'
    html = get_html(url)
    bike_details = get_all_items(html)
    cleaned_rows = [cleanup_record(row) for row in bike_details]
    write_csv_file('bike_details_cleaned.csv', cleaned_rows)