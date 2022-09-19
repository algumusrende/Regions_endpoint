from urllib import response
import requests

city_url = f"https://algogso.pythonanywhere.com/?input={input('İl İsmi Yazınız: ')}"

response_township = requests.get(city_url)

result = response_township.json()

print(result)