#  Credicxo Amazon Scrapper 

A script to bypass Amazon Captcha

## Description
* First fetched the url using `driver.get()` & find the captha image src using `driver.find_element(By.XPATH, '//*[@class.="a-row a-text-center"]/img').get_attribute('src')`.
* Load the image in `requests.get(image_path, stream=True).raw` and then passed to `Image.open()`.
* Filtered the image using `ImageFilter.GaussianBlur()`.
* Then extract the text from the filtered image ` pytesseract.image_to_string()`.
* Find the input field and filled the extracted text
* Click the `continue shopping` button. That's it. 

## Getting Started 

### Installation 

* For Windows only
 *[https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-v5.0.1.20220118.exe]

### Dependencies
 
```
import requests

from PIL import Image, ImageFilter
import pytesseract
from selenium import webdriver
from selenium.webdriver.common.by import By
```

## Help

Any advise for common problems or issues.

## Authors

* Name: Bidyut Maji

## Version History

* 0.1
    * Initial Release

## Thanks!
