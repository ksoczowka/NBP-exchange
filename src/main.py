import requests

code = input('Podaj kod waluty: ').lower()

date = input("Podaj datę (RRRR-MM-DD) albo \'today\': ")
if date == "":
    date = 'today'

result = requests.get(f'http://api.nbp.pl/api/exchangerates/rates/a/{code}/{date}/').json()

currency_value = result['rates'][0]['mid']

print(f"1 {code.upper()} = {currency_value} PLN\nData: {date}")