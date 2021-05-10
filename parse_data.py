import sys
from request_handlers import request_func as req_fn
from json_handlers import json_func

# Main function that executes


def main(form_number):
    data = req_fn.create_requests(form_number)

    form_number_data, form_title_data, form_year_data = req_fn.get_souped_data(
        data)

    json_func.json_response_data(
        form_number_data,
        form_title_data,
        form_year_data)


if __name__ == '__main__':
    # Getting correct form_number list
    product_number = [x.lstrip() for x in ' '.join(sys.argv[1:]).split(',')]

    main(form_number=product_number)
