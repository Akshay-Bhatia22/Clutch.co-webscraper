from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from math import ceil
import xlsx_writer
MAX_PAGES = 5
MAX_DOMAINS = 5
BASE_URL = "https://clutch.co/directory/mobile-application-developers?related_services="
DOMAIN_LIST = [
                "field_pp_sl_mobile_app_dev", "field_pp_sl_web_programming", "field_pp_sl_application_dev", "field_pp_sl_web_design",\
                "field_pp_sl_ecommerce", "field_pp_sl_app_interface_design", "field_pp_sl_seo", "field_pp_sl_smm", "https://clutch.co/directory/mobile-application-developers",\
                "field_pp_sl_graphic_design", "field_pp_sl_it_strategy2", "field_pp_sl_branding", "field_pp_sl_iot_dev"
                ]

# Calculating total no of pages as per total firms per domain
def calc_total_pages(soup, const_results_pp = 40):
    firms = soup.find('div', attrs={"class":"tabs-info"}).text   
    pages = ceil(int(firms.split()[0].replace(',',''))/const_results_pp)
    # print(pages)
    return pages

def create_url(domain, page_no=1):
    return BASE_URL+f"{domain}&page={page_no}"

def pack(**kwargs):
    min_project_size = list()
    hourly_rate = list()
    employee = list()
    location = list()
    for module in kwargs.get('module_list'):
        min_project_size.append(module[0])
        hourly_rate.append(module[1])
        employee.append(module[2])
        location.append(module[3])
    kwargs["min_project_size"]=min_project_size
    kwargs["hourly_rate"]=hourly_rate
    kwargs["employee"]=employee
    kwargs["location"]=location

    # print(kwargs.keys())
    # print(kwargs)
    del kwargs["module_list"]

    return kwargs 



# scraping required data from each list item
def get_data(soup):
    pre_process = lambda text : text.split('\n\n\n\n\n\n')
    companies = [company.text.strip() for company in soup.find_all('a', attrs={"class":"company_title directory_profile"})]
    website = [web.get('href') for web in soup.find_all('a', attrs={"class":"website-link__item"})]
    module_list = [pre_process(company.text.strip()) for company in soup.find_all('div', attrs={"class":"module-list"})]
    ratings = [rating.text.strip() for rating in soup.find_all('span', attrs={"class":"rating sg-rating__number"})]

    return pack(companies=companies, website=website, module_list=module_list, ratings=ratings)
    
    
def loop(domain, page_no=1, data=True):
    options = Options()
    # options.headless = True
    driver = webdriver.Chrome(options=options)
    driver.get(create_url(domain, page_no)) 
    html_source = driver.page_source
    soup = BeautifulSoup(html_source, 'html.parser')
    driver.quit()
    if data:
        return get_data(soup)
        
    return soup

def driver_code():
    MAX_PAGES = int(input("Enter max page limit : "))
    MAX_DOMAINS = int(input("Enter max domains limit : "))
    
    # Check if valid url is created and get no Of pages
    for domain in DOMAIN_LIST[:MAX_DOMAINS]:
        # try:
        #     loop(domain)
        # except:
        #     # Not found exception
        #     print("Not found")
        #     break

        # looping upto max pages
        total_pages = calc_total_pages(loop(domain,1, data=False))
        sheet_name_domain = " ".join(domain.split('_')[3:])
        for i in range(1,total_pages):
            # print(i)
            if i>MAX_PAGES:
                break
            xlsx_writer.run((loop(domain,i)), sheet_name_domain, counter=i)

driver_code()