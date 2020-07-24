import requests
from bs4 import BeautifulSoup


def scrap(url):

    # For Download html file of url
    """
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    fp = open("url_rocha.html", "w")
    fp.write(soup.html.prettify())
    fp.close()
    """

    # TO find total land available for search result
    """
    fp = open("url_rocha.html")
    soup = BeautifulSoup(fp, 'html.parser')
    fp.close()
    title = soup.find_all("h4", {"class": "widgettitle"})
    title_split = title[0].get_text().split()
    for x in title_split:
        if x.isnumeric():
            total_land = int(x)
            break
    print(total_land)a
    """

    fp = open("url_rocha.html")
    soup = BeautifulSoup(fp, 'html.parser')
    fp.close()
    lands = soup.find_all("div", {"class": "col-md-12 col-lg-3"})
    print(len(lands))


main_url = "http://www.camposonline.com.uy/campos/index.php"
url_maldonado = "http://www.camposonline.com.uy/campos/resultado-de-busqueda.php?tipo_op=Venta&has=&pais=URUGUAY&depto_URUGUAY=Maldonado&depto_BRASIL=&depto_ARGENTINA=&depto_PARAGUAY=&depto_BOLIVIA=&precio=&preciototal=&explota=&ic=&suelo=&f_ref=&filt=1"
url_rocha = "http://www.camposonline.com.uy/campos/resultado-de-busqueda.php?tipo_op=Venta&has=&pais=URUGUAY&depto_URUGUAY=Rocha&depto_BRASIL=&depto_ARGENTINA=&depto_PARAGUAY=&depto_BOLIVIA=&precio=&preciototal=&explota=&ic=&suelo=&f_ref=&filt=1"


flag = True
while flag:
    for i in range(50):
        base_url = "http://www.camposonline.com.uy/campos/resultado-de-busqueda.php?filt=1&depto={0}&pais=URUGUAY&p={1}"
        url = base_url.format("Maldonado", i)
        print(url)
