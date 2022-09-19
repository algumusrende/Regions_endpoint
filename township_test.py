from urllib import response
import requests

township_url = f"https://algogso.pythonanywhere.com/township/?input={input('İlçe İsmi Yazınız: ')}"

response_township = requests.get(township_url)

result = response_township.json()

print(result)
