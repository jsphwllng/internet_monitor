import matplotlib.pyplot as plt
import csv

def make_graph(date):
  x = [] #date
  y = [] #download speed
  z = [] #date

  with open(f'{date}_speed.csv', 'r') as csvfile:
      plots = csv.reader(csvfile, delimiter=',')
      next(csvfile)
      for row in plots:
          x.append(str(row[0]))
          y.append(float(row[1]))
          z.append(float(row[2]))

  plt.figure(figsize=(90, 10))
  plt.plot(x, y, label='download', color='r')
  plt.plot(x, z, label='upload', color='b')
  plt.xlabel('time')
  plt.xticks(rotation=90)
  plt.ylabel('speed in Mb/s')
  plt.title(f"internet speed for {date}")
  plt.legend()
  plt.savefig(f'{date}_graph.jpg', bbox_inches='tight')