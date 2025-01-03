import requests

class coinGeckoAPI:
    def __init__(self, key: str):
        self.url = "https://api.coingecko.com/api/v3"
        self.session = requests.Session()
        self.session.headers.update(
            {
                "accept": "application/json",
                "x-cg-demo-api-key": key
            }
        )

    def get_price(self, coin: str):
        response = self.session.get(f"{self.url}/simple/price?ids={coin}&vs_currencies=eur&include_last_updated_at=true")
        response.raise_for_status()
        return response.json()
