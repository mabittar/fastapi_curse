from ..env_configuration import Settings
import requests

def main():
    Settings()
    choice = input("[R]eport weather or [s]ee reports? [exit] to quit!")

    while choice != "exit":
        if choice.lower().strip() == "r":
            pass

        elif choice.lower().strip() == "s":
            pass
        
        else:
            print(f"{choice} not implemented yet!")
            choice = input("\n[R]eport weather or [s]ee reports? [exit] to quit!")


def post_report():
    pass


def get_report():
    url = Settings.url
    endpoint = '/api/reports'
    url = {url} + endpoint
    resp = requests.get(url)
    resp.raise_for_status()