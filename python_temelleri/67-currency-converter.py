import requests
bozulan_doviz = input("bozulan döviz türü: ")
alinan_doviz = input("alınan döviz türü: ")
miktar = int(input(f"Ne kadar {bozulan_doviz} bozdurmak istiyorsunuz:"))
url = f"https://api.apilayer.com/exchangerates_data/convert?to={alinan_doviz}&from={bozulan_doviz}&amount={miktar}"

payload = {}
headers= {
  "apikey": "your-api-key"
}

response = requests.request("GET", url, headers=headers, data = payload)

status_code = response.status_code
result = response.text

print(result)
