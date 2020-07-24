from bs4 import BeautifulSoup
import json
import urllib.request


def get_api_id():
    fp = open("1.html")
    soup = BeautifulSoup(fp, 'html.parser')
    fp.close()
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
                                id = int(cl)
                                print(id)
                                return id
                            except:
                                pass
    return None


def get_data(url):
    response = urllib.request.urlopen(url)

    j = json.load(response)
    """
    with open('j.json', 'w') as outfile:
        json.dump(j, outfile, sort_keys=True, indent=4)
    """

    print(j['resultado']['ficha'][0]['in_tip'])
    print(j['resultado']['ficha'][0]['in_loc'])
    print(j['resultado']['ficha'][0]['in_bar'])
    print(j['resultado']['ficha'][0]['in_cal'])
    print(j['resultado']['ficha'][0]['precio'])
    print(j['resultado']['superficie']['dato'][3])


api_id = get_api_id()

URL = "https://xintel.com.ar/api/?cache=08072020&json=fichas.propiedades&amaira=false&suc=ATM&global=LU3AIKPR4F6ZSUY8GQODKWRO8&emprendimiento=True&oppel=&esweb=&apiK=4m17zq256jvsm24wOnqbev43y&id={0}"
URL = URL.format(api_id)
get_data(URL)
