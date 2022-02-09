import requests

from PIL import Image, ImageFilter
import pytesseract
from selenium import webdriver
from selenium.webdriver.common.by import By

#amazon captha url
url = "https://www.amazon.com/errors/validateCaptcha"

#driver excutable path
driver = webdriver.Chrome(executable_path=r"C:\Program Files\Google\Chrome\Application\chromedriver.exe")

driver.get(url)  # fetch url

#find the image src
image_path = driver.find_element(By.XPATH, '//*[@class="a-row a-text-center"]/img').get_attribute('src')

#load the url in Image
image = Image.open(requests.get(image_path, stream=True).raw)

#apply GaussianBlur with radius 1
image = image.filter(ImageFilter.GaussianBlur(1))

#extracting the text from image
valid_str = pytesseract.image_to_string(image)

#input the valid str
driver.find_element(By.XPATH, '//*[@name="field-keywords"]').send_keys(valid_str)
driver.find_element(By.XPATH, '//*[@class="a-button-text"]').click() # click the buuton

#closing the driver
driver.close()
