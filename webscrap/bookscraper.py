# -*- coding: utf-8 -*-
# Indentation: Visual Studio

'''
Scrap data from below webpage
https://www.pastemagazine.com/books/fantasy-books/the-50-best-fantasy-novels-of-the-21st-century/

'''

__version__ = 1.0
__author__ = "Sourav Raj"
__author_email__ = "souravraj.iitbbs@gmail.com"


# import sys
# sys.path.append(r'G:\PythonProjects\python\classes\classAndObjectBasics')

from bs4 import BeautifulSoup
import requests
import csv
# csv_file=open('data.csv')
source = requests.get('https://aconitecafe.com/top-100-fantasy-novels-of-all-time-1-20/').text
soup=BeautifulSoup(source, 'lxml')

# csv_writer=csv.writer(csv_file)
# csv_writer.writerow(soup.prettify)
# csv_file.close()

# print(soup.prettify)
article=soup.find('div', class_='elementor-column elementor-col-66 elementor-top-column elementor-element elementor-element-3c7939b1')
print(article)

# file1 = open("webscrap/data.txt","w")
# x=str(soup.prettify)
# file1.writelines(x)
# file1.close()

# print('dfd')