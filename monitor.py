import speedtest, csv
import datetime
from graph_maker import make_graph
s = speedtest.Speedtest()

def record():
  #create csv file with headers time and speed
  with open(f'{datetime.date.today()}_speed.csv', mode='w') as speedcsv:
    fieldnames = ['time', 'speed']
    csv_writer = csv.DictWriter(speedcsv, fieldnames=fieldnames)
    csv_writer.writeheader()
    start_day = datetime.date.today()
    while True:
      hours = datetime.datetime.now().strftime("%H")
      minutes = datetime.datetime.now().strftime("%M")
      print(time)
      speed = round((round(s.download()) / 1048576), 2)
      print(speed, "Mb/s")
      if minutes == "30" or minutes == "00":
        csv_writer.writerow({'time': f"{hours}:{minutes}", 'speed': speed})
      else:
        csv_writer.writerow({'time': f"{hours}", 'speed': speed})
      #if day has changed, i.e past midnight, new csv file begins
      #? maybe update this with generating graph then re-write?
      if datetime.date.today() != start_day:
        speedcsv.close()
        make_graph(start_day)
        record()

record()
