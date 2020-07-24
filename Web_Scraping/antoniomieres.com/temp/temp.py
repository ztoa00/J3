from bs4 import BeautifulSoup


def get_id():

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
                                return id
                            except:
                                pass
    return None


print(get_id())