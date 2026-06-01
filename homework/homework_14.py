import requests
import json

pdf_url = "https://github.com/progit/progit2/releases/download/2.1.449/progit.pdf"
response = requests.get(pdf_url)

with open("progit.pdf", mode="bw") as file:
    file.write(response.content)

json_url = "http://api.open-notify.org/astros.json"

json_response = requests.get(json_url)

data = json_response.json()

with open("astros.json", mode="w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=4)
