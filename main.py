from selenium import webdriver
from bs4 import BeautifulSoup


url = "https://clutch.co/directory/mobile-application-developers"

driver = webdriver.Chrome()
driver.get(url) 
html_source = driver.page_source
# print(res)
soup = BeautifulSoup(html_source, 'html.parser')
# print(soup.prettify())
companies = [company.text.strip() for company in soup.find_all('a', attrs={"class":"company_title directory_profile"})]
website = [web.get('href') for web in soup.find_all('a', attrs={"class":"website-link__item"})]

print(companies)
print(website)
