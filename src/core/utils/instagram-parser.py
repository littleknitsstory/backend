from urllib import request
import urllib
import requests
import datetime
from bs4 import BeautifulSoup
import re
import json


USER_NAME = ""  # add instagram username
COUNT_PICTURES = 5  # number of pictures


# TODO: rewrite this place
def download_file(url):
    print("Downloading image...")
    f = urllib.request.urlopen(url)
    htmlSource = f.read()
    soup = BeautifulSoup(htmlSource, "html.parser")
    metaTag = soup.find_all("meta", {"property": "og:image"})
    imgURL = metaTag[0]["content"]
    fileName = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S") + ".jpg"
    urllib.request.urlretrieve(imgURL, fileName)
    print("Done. Image saved to disk as " + fileName)


soup = BeautifulSoup(
    request.urlopen("https://www.instagram.com/" + USER_NAME), "html.parser"
)
metaTag = soup.find_all("script", type="text/javascript")
pattern = "window._sharedData = {.+};</script>"
parse_text = re.findall(pattern, str(metaTag))
parse_text = parse_text[0].replace(";</script>", "")
parse_text = parse_text.replace("window._sharedData = ", "")

json_dict = json.loads(parse_text)

short_adress = []
# shortcode - code picture
for number in range(
    len(
        json_dict["entry_data"]["ProfilePage"][0]["graphql"]["user"][
            "edge_owner_to_timeline_media"
        ]["edges"]
    )
):
    short_adress.append(
        json_dict["entry_data"]["ProfilePage"][0]["graphql"]["user"][
            "edge_owner_to_timeline_media"
        ]["edges"][number]["node"]["shortcode"]
    )

temp_url = "https://www.instagram.com/p/"

for item in range(COUNT_PICTURES):
    download_file(temp_url + short_adress[item])

print("All pictures are downloaded!")
