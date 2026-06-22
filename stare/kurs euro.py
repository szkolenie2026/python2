import urllib.request
import json

def get_eur_rate():
	url = "http://api.nbp.pl/api/exchangerates/rates/A/EUR/?format=json"
	try:
		with urllib.request.urlopen(url, timeout=10) as resp:
			data = json.load(resp)
		rate = data["rates"][0]["mid"]
		date = data["rates"][0]["effectiveDate"]
		print(f"EUR: {rate} (date: {date})")
	except Exception as e:
		print("Błąd pobierania kursu EUR:", e)

if __name__ == "__main__":
	get_eur_rate()
