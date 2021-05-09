import settings
import requests
from bs4 import BeautifulSoup as bs


"""
The longest function in this project, had only this choice at the programming time. 
It gets all requests.content and then loop through pages, because data is coming in old fashion way.
Therefore it was used to collect all contents and store them in an array
"""
def create_requests(product_number: list) -> list:
    row_count = 0

    soup_list = []

    for i in product_number:

        print(i.strip())

        UNIQUE_URL = f"?sortColumn=sortOrder&indexOfFirstRow=0&value={i.strip()}&criteria=formNumber&resultsPerPage=200&isDescending=false"

        URL = settings.URL + UNIQUE_URL

        req = requests.get(URL)

        pages = get_total_pages(req.content)    # Getting total pages of a form_number

        # Looping through pages to collect all content
        for _ in range(0, pages):
            UNIQUE_URL = f"?sortColumn=sortOrder&indexOfFirstRow={row_count}&value={i.strip()}&criteria=formNumber&resultsPerPage=200&isDescending=false"

            URL = settings.URL + UNIQUE_URL

            next_req = requests.get(URL)

            soup = bs(next_req.content, 'html.parser')

            soup_list.append(soup)

            row_count += 200

        row_count = 0

    return soup_list    #Returning list of contents, which will then iterate to load json data

# Simple function, return how many pages are there per form_number
def get_total_pages(r: requests.Request) -> int:
    soup = bs(r, 'html.parser')

    pages = soup.find('th', class_='NumPageViewed')

    try:
        formatted_total_pages = pages.find_all('a')[-2]

        return int(formatted_total_pages.text)

    except IndexError:
        solo_page = 1
        return solo_page

# After getting all content needed, looping to get souped_data. This is for scraping useful for us data.
def get_souped_data(data: list):
    td_form_name, td_form_title, td_form_rev_year = [], [], []

    # Iterates over data and finds useful data
    for soup in data:
        td_name = soup.find_all('td', {'class': 'LeftCellSpacer'})
        td_title = soup.find_all('td', {'class': 'MiddleCellSpacer'})
        td_rev_year = soup.find_all('td', {'class': 'EndCellSpacer'})
        td_form_name.extend(td_name)
        td_form_title.extend(td_title)
        td_form_rev_year.extend(td_rev_year)

    return td_form_name, td_form_title, td_form_rev_year    # Returns three lists for showing right data