import speedtest, csv
import datetime
from graph_maker import make_graph
from drive_uploader import upload_to_drive

s = speedtest.Speedtest()

def record():
  #create csv file with headers time and speed
  with open(f'{datetime.date.today()}_speed.csv', mode='w') as speedcsv:
    csv_writer = csv.DictWriter(speedcsv, fieldnames=['time', 'speed'])
    csv_writer.writeheader()
    start_day = datetime.date.today()
    count = 0
    while True:
      #writes into the CSV file until the date changes
      time = datetime.datetime.now().strftime("%H:%M")
      speed = round((round(s.download()) / 1048576), 2)
      csv_writer.writerow({'time': time, 'speed': speed})
      print({'time': time, 'speed': speed}, "Mb/s")
      if datetime.date.today() == start_day:
      #when day changes stop writing, generate a graph, upload that graph to google drive and start again
        speedcsv.close()
        make_graph(start_day)
        upload_to_drive(f"{start_day}" + "_graph.jpg")
        record()

record()
