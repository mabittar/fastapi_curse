from typing import Optional

import requests

from cp_6.env_configuration import settings


def main():
    choice = input("[R]eport weather or [s]ee reports? [exit] to quit!")

    while choice != "exit":
        if choice.lower().strip() == "r":
            post_report()

        elif choice.lower().strip() == "s":
            get_report()

        elif choice.lower() == "exit":
            quit

        else:
            print(f"{choice} not implemented yet!")
            choice = input("\n[R]eport weather or [s]ee reports? [exit] to quit!")


def post_report():
    desc = input("O que você gostaria de reportar?")
    city = input("Em qual cidade está acontecendo?")
    data = dict(
        description=desc,
        location=dict(
            city=city,
        )
    )
    resp = __connector(action="post", data=data)
    resp.raise_for_status()
    result = resp.json()
    print(f"Novo evento reportado: {result.get('id')}")


def get_report():
    resp = __connector(action='get')
    resp.raise_for_status()

    data = resp.json()
    for r in data:
        print(f"{r.get('location').get('city')} has {r.get('description')}")


def __connector(action: str, data: Optional[dict] = None):
    url = settings.url
    endpoint = '/api/reports'
    url = {url} + endpoint
    if action == "post":
        return requests.post(url, json=data)
    elif action == "get":
        return requests.get(url)


if __name__ == '__main__':
    main()
