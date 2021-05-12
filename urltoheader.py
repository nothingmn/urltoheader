import os
import uuid
from imgconvert import convert
from argparse import ArgumentParser
from chromedriver_py import binary_path # this will get you the path variable

parser = ArgumentParser()
parser.add_argument('-u', action="store", dest="url")
parser.add_argument('-n', action="store", dest="name")
args = parser.parse_args()

from selenium import webdriver
driver = webdriver.Chrome(executable_path=binary_path)

pngFile = args.name + ".png"
driver.get(args.url)
driver.save_screenshot(pngFile)

driver.close()

convert(pngFile, args.name)
