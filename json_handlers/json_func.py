import json


# Creates json data to FORM/data.json
def create_json_data(data):
    with open('FORMS/data.json', 'w') as file:
        json.dump(data, file)

# Reads json data from FORMS/data.json


def read_data_json():
    with open(f'FORMS/data.json', 'r+') as file:
        data = json.load(file)
    return data

# Dumps all needed data and returns it as a json + creates a data.json
# where the same information is stored for download uses


def json_response_data(
        td_form_name: list,
        td_form_title: list,
        td_form_rev_year: list):

    pdf_links = []

    # Storing all available form names
    names = [name.text.strip() for name in td_form_name]
    # Storing all available titles
    titles = [title.text.strip() for title in td_form_title]
    # Storing all available links for fututre use ( to download them )
    links = [link.find('a', href=True)['href'] for link in td_form_name]
    # converting to int because will then compare variables
    years = [int(year.text.strip()) for year in td_form_rev_year]

    set_names = set(names)
    final_dict = []

    for name in set_names:
        last_year = 0
        # Because it is sorted by product names the first year is current year
        # or the latest
        first_year = max(years)
        json_dict = {'form_number': name}
        for index, product_number in enumerate(names):
            if product_number == name:
                pdf_links.append(links[index])

                # Preventing errors, thats why there is a need to compare and
                # get right data
                if years[index] > last_year:
                    last_year = years[index]
                elif years[index] < first_year:
                    first_year = years[index]

                json_dict = {
                    'form_number': name,
                    'form_title': titles[index],
                    'max_year': last_year,
                    'min_year': first_year,
                    'pdf_links': pdf_links
                }

        final_dict.append(json_dict)
        pdf_links = []   # Resets all links back to empty list. It is needed, so that when a new form_number is used the links that are related to it were added
    create_json_data(final_dict)

    print(json.dumps(final_dict, indent=4))  # Prints a json data
