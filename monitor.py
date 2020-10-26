import speedtest, csv
import datetime
import time as t
from graph_maker import make_graph
from drive_uploader import upload_to_drive
import time

s = speedtest.Speedtest()

def record(length, download, upload):
    #create csv file with headers time and speed
    with open(f'{datetime.date.today()}_speed.csv',
              mode='w',
              newline='',
              encoding='utf-8') as speedcsv:
        csv_writer = csv.DictWriter(speedcsv, fieldnames=['time', 'downspeed', 'upspeed'])
        csv_writer.writeheader()
        start_day = datetime.datetime.today()
        start_time = datetime.datetime.now()
        completed_time = start_day + datetime.timedelta(minutes = length)
        print(f"it is now {start_time} and i will stop recording at {completed_time}")
        while True:
            #writes into the CSV file until the time is completed changes
            if datetime.datetime.now() < completed_time:
                time = datetime.datetime.now().strftime("%H:%M:%S")
                downspeed = round((round(s.download()) / 1048576), 2)
                upspeed = round((round(s.upload()) / 1048576), 2)
                csv_writer.writerow({'time': time, 'downspeed': downspeed, "upspeed": upspeed})
                print(f"time: {time}, downspeed: {downspeed} Mb/s, upspeed: {upspeed} Mb/s")
                # t.sleep(60)
            else:
                #when time is over stop writing, generate a graph, upload that graph to google drive and start again
                speedcsv.close()
                print("\nnow generating graph...")
                make_graph(str(start_day)[:10], download, upload)
                try:
                    upload_to_drive(f"{start_day}" + "_graph.jpg")
                    print("now uploaded to drive")
                except:
                    print("API keys not correct - now saving to local device")
                    pass
                print("now you can check out your graph :)")
                break
