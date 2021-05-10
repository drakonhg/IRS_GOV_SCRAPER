URL = "https://apps.irs.gov/app/picklist/list/priorFormPublication.html"
HOME_URL = "https://apps.irs.gov"

# for data in total_data:
#     all_data = data.find_all('tr', class_=['even', 'odd'])
#
#     count = 0
#
#     # Looping to check if titles are same and stop where they are, to exclude them
#     for i in range(len(all_data) - 1):
#         current_product_number = all_data[i].find('td', class_='LeftCellSpacer').text
#         next_product_number = all_data[i + 1].find('td', class_='LeftCellSpacer').text
#
#         if current_product_number == next_product_number:
#             count += 1
#
#         else:
#             title = all_data[count].find('td', class_='MiddleCellSpacer').text
#
#             first_year = all_data[count].find('td', class_='EndCellSpacer').text
#             last_year = all_data[count + 1].find('td', class_='EndCellSpacer').text
#
#             data = {
#                 'form_number': current_product_number.strip(),
#                 'form_title': title.strip(),
#                 'min_year': first_year.strip(),
#                 'max_year': last_year.strip(),
#             }
#
#             total_list.append(data)
#
#             count = 0
#
# json_format(total_list)
