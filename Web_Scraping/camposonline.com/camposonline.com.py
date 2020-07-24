import requests
from bs4 import BeautifulSoup
from datetime import datetime
import xlsxwriter


BASE_URL = "http://www.camposonline.com.uy"
DOMAIN = "camposonline.com"

RESULT_LIST = [["Ubicación", "N DE REFERENCIA", "HA", "PRECIO/HA", "INVERSION TOTAL", "Link"]]


# Function to scrap data from website
# Function to scrap data from website
# Function to scrap data from website
# Function to scrap data from website
# Function to scrap data from website
# Function to scrap data from website

def scrap(url):

    try:
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')

        lands = soup.find_all('div', {'class': 'col-md-12 col-lg-3'})
        land_count = len(lands)

        if land_count:
            for land in lands:

                sale_type = land.find('div', {'class': 'listing-box-image-label'})
                if sale_type.get_text().strip().lower() == 'venta':

                    sub_link = land.find('span', {'class': 'listing-box-image-links'}).find_all('a')[1]['href']
                    land_link = BASE_URL + sub_link

                    ref_num = land.find('h2').get_text().strip()

                    ha = land.find('h3').get_text().strip()

                    land_details = land.find('div', {'class': 'listing-box-content'}).find_all('dd')
                    land_location = land_details[0].get_text().strip()
                    price_ha = land_details[2].get_text().strip()
                    total_invesment = land_details[4].get_text().strip()

                    lst = [land_location, ref_num, ha, price_ha, total_invesment, land_link]
                    RESULT_LIST.append(lst)

            return land_count

        else:
            return land_count

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

    departments = ["Maldonado", "Rocha"]

    for department in departments:
        flag = True
        page_no = 1

        while flag:
            base_url = "http://www.camposonline.com.uy/campos/resultado-de-busqueda.php?filt=1&depto={0}&pais=URUGUAY&p={1}"
            URL = base_url.format(department, page_no)
            next_page = scrap(URL)

            print("Scraping in Progress Please Wait.... ", end="")
            print(department, next_page, "Lands")

            if not next_page:
                flag = False
            else:
                page_no += 1
        print()
    print()

    print("Scraped Successfully and Results Stored in .... ")
    file_name = save_result()
    print(file_name)
