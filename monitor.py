import speedtest, csv
import datetime
s = speedtest.Speedtest()

def record():
  with open(f'{datetime.date.today()}_speed.csv', mode='w') as speedcsv:
    fieldnames = ['time', 'speed']
    csv_writer = csv.DictWriter(speedcsv, fieldnames=fieldnames)
    csv_writer.writeheader()
    start_day = datetime.date.today()
    while True:
      time = datetime.datetime.now().strftime("%H:%M:%S")
      print(time)
      speed = round((round(s.download()) / 1048576), 2)
      print(speed, "Mb/s")
      csv_writer.writerow({'time': time, 'speed': speed})
      if datetime.date.today() != start_day:
        record()

record()
