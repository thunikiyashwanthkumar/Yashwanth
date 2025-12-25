import datetime

def update_log():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("activity_log.txt", "a") as f:
        f.write(f"AI Update at: {timestamp}\n")
    print(f"Log updated at {timestamp}")

if __name__ == "__main__":
    update_log()
