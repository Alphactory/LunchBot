import requests
import datetime
import time

link = "http://<link goes here>"
webhook = "<webhook goes here>"

def get_orders(link):
    return requests.get(f"{link}/orders").text.replace("<br>", "\n")


def main():
    while True:
        now = datetime.datetime.now()
        current_time = now.strftime("%H%M")
        print(current_time)
        if current_time == "1200":
            data = {"content": f"lunch orders for {datetime.date.today()}: ```{get_orders(link)}```"}
            requests.post(webhook, json=data)
            requests.get(f"{link}/clear")
        time.sleep(60)


main()
