print(r"""


 _       _                       _                           _ _
(_)_ __ | |_ ___ _ __ _ __   ___| |_   _ __ ___   ___  _ __ (_) |_ ___  _ __
| | '_ \| __/ _ \ '__| '_ \ / _ \ __| | '_ ` _ \ / _ \| '_ \| | __/ _ \| '__|
| | | | | ||  __/ |  | | | |  __/ |_  | | | | | | (_) | | | | | || (_) | |
|_|_| |_|\__\___|_|  |_| |_|\___|\__| |_| |_| |_|\___/|_| |_|_|\__\___/|_|



""")


def ask_for(thing):
    correct_input = False
    while correct_input != True:
        answer = input(f"{thing}\n> ")
        try:
            int(answer)
            correct_input = True
            return answer
        except ValueError:
            print(f"{answer} is not a number")


length = int(ask_for("how many minutes should we monitor your internet for?"))
download = int(ask_for("what is your expected download speed in Mb/s?"))
upload = int(ask_for("what is your expected upload speed in Mb/s?"))

print("if you have imported your google drive API key you will now be asked to log into your google drive account\n")

from monitor import record

print("now monitoring your internet speed...")

record(length, download, upload)

print(r"""


                       _ _                  _
  __ _  ___   ___   __| | |__  _   _  ___  / \
 / _` |/ _ \ / _ \ / _` | '_ \| | | |/ _ \/  /
| (_| | (_) | (_) | (_| | |_) | |_| |  __/\_/
 \__, |\___/ \___/ \__,_|_.__/ \__, |\___\/
 |___/                         |___/


""")
