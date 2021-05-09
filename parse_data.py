import sys
from request_handlers import request_func as req_fn
from json_handlers import json_func

# Main function that executes
def main(product_number):
    data = req_fn.create_requests(product_number)

    form_number_data, form_title_data, form_year_data = req_fn.get_souped_data(data)

    json_func.json_response_data(form_number_data, form_title_data, form_year_data)

if __name__ == '__main__':
    product_number = [x.lstrip()  for x in ' '.join(sys.argv[1:]).split(',')]   # Getting correct form_number list

    main(product_number)





