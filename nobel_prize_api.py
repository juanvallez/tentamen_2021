import requests


def get_nobel_prize_data(prize_category, year):
    api_parameters = {"nobelPrizeYear": int(year), "nobelPrizeCategory": prize_category}
    nobel_prize_data = requests.get("http://api.nobelprize.org/2.1/nobelPrizes", params=api_parameters).json()
    return nobel_prize_data