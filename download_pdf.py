import os
import sys
import json

import requests

# Downloads pdf that we wanted and place in folder DOWNLOADS


def download_exact_links(links: list):
    with open('FORMS/data.json', 'r+') as file:
        data = json.load(file)

    for i, name in enumerate(data):
        for j, link in enumerate(links):
            if link['link'] in name['pdf_links']:
                pdf_file = requests.get(link['link'], allow_redirects=True)

                download_link_pdf_file(
                    pdf_file.content, name['form_number'], link['year'])


# Getting exact links from range of years and fetching them
def get_exact_links(form_number: str, year_range: list) -> list:
    exact_links = []

    updated_year_range = range(int(year_range[0]), int(year_range[-1]) + 1)

    with open('FORMS/data.json', 'r+') as file:
        data = json.load(file)

    for i, name in enumerate(data):
        if form_number == name['form_number']:

            for index in range(len(updated_year_range)):
                print(updated_year_range[index])
                link = format_string(name['form_number'])
                link += f'--{updated_year_range[index]}.pdf'

                data = {
                    'link': link,
                    'year': updated_year_range[index]
                }

                exact_links.append(data)

    return exact_links  # Returns links that we are needed

# Downloads pdf to our folder with right format


def download_link_pdf_file(link: str, form_number: str, year):
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, f'DOWNLOADS/{form_number}-{year}.pdf')
    with open(my_file, 'wb') as file:
        file.write(link)

# This was invented to create a right link which will append to our
# exact_links array.


def format_string(string: str) -> str:
    link = 'https://www.irs.gov/pub/irs-prior/'
    total = ""
    fn = string.lower().split(' ')
    try:
        fn.remove('and')

    except ValueError:
        pass

    finally:
        total += fn[0][0]
        for i in range(len(fn) - 1):
            total += ''.join(fn[i + 1].split('-'))

        link += total

    return link

# Main function that executes


def main(form_number):
    print(form_number)

    year_range = sys.argv[-1].split('-')

    links = get_exact_links(form_number=product_number,
                            year_range=year_range)

    download_exact_links(links)


if __name__ == '__main__':
    # Executes a function main()

    product_number = f"{sys.argv[1]} {' '.join(sys.argv[2: -1])}"

    main(product_number)  # Same login as in parse_data.py
