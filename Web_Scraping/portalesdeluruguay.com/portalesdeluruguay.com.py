import requests
from bs4 import BeautifulSoup
from datetime import datetime
import xlsxwriter


BASE_URL = "https://www.portalesdeluruguay.com.uy"
DOMAIN = "portalesdeluruguay.com"

ALLOWED_CITIES = ['Barra de Valizas', 'Cabo Polonio', 'Garzon', 'Jose Ignacio', 'La Barra', 'La Paloma', 'La Pedrera',
                  'Manantiales', 'Punta de este', 'Punta del Diablo']

SCRAPED_URLS = []

RESULT_LIST = [["Ubicación", "Metraje Terren", "Precio Venta", "Link"]]


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

        lands = soup.find_all('div', {'class': 'strip_all_tour_list wow fadeIn'})
        land_count = len(lands)

        if land_count:
            for land in lands:

                land_details = land.find('div', {'class': 'col-lg-6 col-md-6 col-sm-6'})

                location = ''.join(land_details.find('span').get_text().lower().split())

                for city in ALLOWED_CITIES:
                    city = ''.join(city.lower().split())
                    if city in location:
                        link = land_details.find('a')['href']
                        SCRAPED_URLS.append(link)
                        break

            return land_count

        else:
            return land_count

    except Exception as e:
        print(e)
        exit(0)


# Function to scrap data from website
# Function to scrap data from website
# Function to scrap data from website
# Function to scrap data from website
# Function to scrap data from website
# Function to scrap data from website

def scrap_data(url):

    try:
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')

        location = soup.find('div', {'class': 'alojOtros'}).get_text().strip()

        land_size = "Not Available"
        land_details = soup.find('div', {'class': 'all_facility_list'})
        land_details = land_details.find_all('span', {'class': 'carNum'})
        for detail in land_details:
            full_detail = detail.parent.get_text()
            joined_detail = ''.join(full_detail.lower().split())
            required_name = ''.join("Metraje Terreno".lower().split())

            if required_name in joined_detail:
                land_size = full_detail

        land_price = ' '.join(soup.find('div', {'class': 'infoButton'}).get_text().strip().split())

        lst = [location, land_size, land_price, url]
        RESULT_LIST.append(lst)

    except Exception as e:
        print(e)
        exit(0)


# To Save the Result
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
# Driver Code

if __name__ == "__main__":

    print("Scraping started .... ")

    flag = True
    page_no = 1

    while flag:
        base_url = "https://www.portalesdeluruguay.com.uy/es/terrenos/page_{0}"
        URL = base_url.format(page_no)
        next_page = scrap_url(URL)

        print("Scraping URLS in Progress Please Wait.... ", end="")
        print(next_page, "Properties")

        if not next_page:
            flag = False
        else:
            page_no += 1
    print()

    count = 1
    len_ = len(SCRAPED_URLS)
    for URL in SCRAPED_URLS:
        scrap_data(URL)
        print("Scraping Data in Progress({0}/{1}) Please Wait.... from {2}".format(count, len_, URL))
        count += 1
    print()

    print("Scraped Successfully and Results Stored in .... ")
    file_name = save_result()
    print(file_name)
