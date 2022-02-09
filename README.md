#  Credicxo Amazon Scrapper  [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1MPAmJaJLXxE_iDLdDVdJoGu6NZ8xthZR?usp=sharing)

scrap basic deatils from the amazon product pages

## Description
* First created Asin number and Country two list from the `Amazon Scraping - Sheet1.csv` file.
* Created list of all urls using  Asin number and Country lists.
* Maked a `product_row` of  each scraped product the `Product Title`, `Product Image URL`, `Price of the Product` and `Product Details` from pages using ` concurrent.futures.ThreadPoolExecutor()`.
*  Create  `amazon_data` list and append all  `product_row` dicts.
*  Using `json.dump()` function created a `Amazon_Products.json` file.
*  Optional: after connecting to local database and used ` cursor.executemany()` to dump the data.

## Getting Started

### Dependencies

```
import json
import os
import requests
import time

from bs4 import BeautifulSoup as soup
import mysql.connector
import pandas as pd
```

## Help

Any advise for common problems or issues.

## Authors

* Name: Bidyut Maji

## Version History

* 0.1
    * Initial Release

## Thanks!
