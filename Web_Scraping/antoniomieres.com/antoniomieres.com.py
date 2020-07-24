import json
import urllib.request
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import xlsxwriter


BASE_URL = "http://www.antoniomieres.com.uy/"
DOMAIN = "antoniomieres.com"


SEARCH_URL = "http://www.antoniomieres.com.uy/propiedades?p={0}&tipo={1}&ope=V&loc={2}&par=All&b=All&a1=All&cod="
BASE_API_URL = "https://xintel.com.ar/api/?cache=08072020&json=fichas.propiedades&amaira=false&suc=ATM&global=LU3AIKPR4F6ZSUY8GQODKWRO8&emprendimiento=True&oppel=&esweb=&apiK=4m17zq256jvsm24wOnqbev43y&id={0}"


SCRAPED_URLS = []
SCRAPED_API_ID = {}


RESULT_LIST = [["LAND TYPE", "Ubicación", "Banner1", "Banner2", "PRECIO", "PRECIO", "LAND SIZE", "LINK"]]


# Function to scrap url from website
# Function to scrap url from website
# Function to scrap url from website
# Function to scrap url from website
# Function to scrap url from website
# Function to scrap url from website


def scrap_url(url):

    try:
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')
        lands = soup.find_all('div', {'class': 'shop-item course-v2'})
        land_count = len(lands)
        if land_count:
            for land in lands:
                land_details = land.find('div', {'class': 'shop-desc'})
                sub_url = land_details.find('a')['href']
                land_url = BASE_URL + sub_url
                SCRAPED_URLS.append(land_url)
            return land_count
        else:
            return land_count

    except Exception as e:
        print("Error at scrap_url function : ", e)
        exit(0)


# Function to scrap api_id from website
# Function to scrap api_id from website
# Function to scrap api_id from website
# Function to scrap api_id from website
# Function to scrap api_id from website
# Function to scrap api_id from website


def scrap_api_id(url):
    try:
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')
        tags = soup.find_all("script", {"type": "text/javascript"})
        for tag in tags:
            tag_str = str(tag)
            if "<script t" in tag_str and "$.ajax" in tag_str:
                for line in tag_str.split():
                    if "'id':" in line:
                        cleaned_line = line.split("'id':")
                        cleaned_line = cleaned_line[1].split("'")
                        for cl in cleaned_line:
                            if cl:
                                try:
                                    a_id = int(cl)
                                    return a_id
                                except:
                                    pass
        return None

    except Exception as e:
        print("Error at scrap_api_id function : ", e)
        exit(0)


# Function to scrap Data from website
# Function to scrap Data from website
# Function to scrap Data from website
# Function to scrap Data from website
# Function to scrap Data from website
# Function to scrap Data from website


def scrap_data(api_url,url):

    try:
        response = urllib.request.urlopen(api_url)
        j = json.load(response)

        lst = [j['resultado']['ficha'][0]['in_tip'],
               j['resultado']['ficha'][0]['in_loc'],
               j['resultado']['ficha'][0]['in_bar'],
               j['resultado']['ficha'][0]['in_cal'],
               j['resultado']['ficha'][0]['in_val'],
               j['resultado']['ficha'][0]['precio'],
               j['resultado']['superficie']['dato'][3],
	       url]
        RESULT_LIST.append(lst)

    except Exception as e:
        print("Error at scrap_data function : ", e)
        exit(0)


# To Save the Result
# To Save the Result
# To Save the Result
# To Save the Result
# To Save the Result
# To Save the Result


def save_result():

    now = datetime.now().strftime("%Y_%m_%d_%H%M%S")
    fname = DOMAIN + "_" + str(now) + ".xlsx"
    workbook = xlsxwriter.Workbook(fname)
    worksheet = workbook.add_worksheet()
    for row in range(len(RESULT_LIST)):
        for column in range(len(RESULT_LIST[row])):
            worksheet.write(row, column, RESULT_LIST[row][column])
    workbook.close()
    return fname


# Driver Code
# Driver Code
# Driver Code
# Driver Code
# Driver Code
# Driver Code


if __name__ == "__main__":

    print("Scraping started .... ")
    print("Take a rest and sit back, it takes time to scrap all those data..")

    # Phase 1

    # Scraping the BASE URL(Main Website) for all available land in Main website

    departments = ["maldonado", "rocha"]
    land_types = {"Campo": 'P', "Chacra": 'Q', "Terreno": 'T'}
    for department in departments:
        for land_type in land_types:
            flag = True
            page_no = 0
            while flag:
                URL = SEARCH_URL.format(page_no, land_types[land_type], department)
                next_page = scrap_url(URL)
                print("Scraping URLS in Progress Please Wait.... ", end="")
                print(department, land_type, next_page, "Lands")
                if not next_page:
                    flag = False
                else:
                    page_no += 1
            print()
        print()
    print()
    print()

    # Phase 2

    # Scraping each scraped land url from Phase 1 to get the api id

    count = 1
    len_ = len(SCRAPED_URLS)
    for URL in SCRAPED_URLS:
        api_id = scrap_api_id(URL)
        if api_id:
            SCRAPED_API_ID[URL] = api_id
        print("Scraping API_ID in Progress({0}/{1}) Please Wait.... from {2}".format(count, len_, URL))
        count += 1
    print()
    print()

    # Phase 3

    # Scraping each api from Phase 2 to get the data of each land

    count = 1
    len_ = len(SCRAPED_API_ID)
    for URL in SCRAPED_API_ID:
        API_URL = BASE_API_URL.format(SCRAPED_API_ID[URL])
        scrap_data(API_URL, URL)
        print("Scraping Data in Progress({0}/{1}) Please Wait.... from {2}".format(count, len_, URL))
        count += 1
    print()

    # Phase4

    # Storing the result

    print("Scraped Successfully and Results Stored in .... ")
    file_name = save_result()
    print(file_name)
