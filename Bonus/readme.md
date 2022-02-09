#  Credicxo Amazon Scrapper 

A script to bypass Amazon Captcha

## Description
* first fetched the url using `driver.get(url)` & find the captha image src using `driver.find_element(By.XPATH, '//*[@class.="a-row a-text-center"]/img').get_attribute('src')`.
* Load the image in `requests.get(image_path, stream=True).raw` and then passed to `Image.open()` for apply some filter
* Filtered the image using `ImageFilter.GaussianBlur()`.
* Then extracted the text from the filtered image ` pytesseract.image_to_string()`.
* find the input field and filled the extracted text and click the `continue shopping` button. That's it. 
## Getting Started 

### Dependencies

* 
```
import requests

from PIL import Image, ImageFilter
import pytesseract
from selenium import webdriver
from selenium.webdriver.common.by import By
```

## Help

Any advise for common problems or issues.
```
command to run if program contains helper info
```

## Authors

* Name: Bidyut Maji

## Version History

* 0.1
    * Initial Release
