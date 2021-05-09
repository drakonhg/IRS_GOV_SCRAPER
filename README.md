# IRS GOVERNMENT SCRAPER

## Main Task
This is a scraper for https://apps.irs.gov/app/picklist/list/priorFormPublication.html. It's job to scrape and return data in json format. This data can be downloaded to pdf file.

## Libraries

* os
* sys
* json
* requests
* BeautifulSoup4


## No selenium
I did not use selenium because it consumes more cpu and ram, than requests and bs4. It is also a faster way to scrape data. As there is no need to render JavaScript scirpts and bypass security (e.g akamai, etc), it is a best option to use.

## Usage

There are two main files: parse_data.py and download_pdf.py. Each run by command line argument


To get json_data of specified forms
```shell script
python parse_data.py Form W-2, Form 1095-C, Publ 3

```
All of the forms should be listed with comma, else it would not work

Additionally, it stores all data that was parse in FORMS directory by data.json

You can use this data, to fetch required links and download needed pdf.

#### Note
Download part only works after parse_data stored some data.

To download pdf file within specified range
```shell script
python download_pdf.py Form W-2 P 1988-1990

``` 

#### Note
 You can use any range


## Requirements

If you woud like to git clone it or copy the code, there is a requirements.txt that stores all libraries that are needed for script to work.



