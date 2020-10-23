import matplotlib.pyplot as plt
import csv
import matplotlib.ticker as ticker
from PIL import Image


def make_graph(date, download, upload):
    x = []  #date
    y = []  #download speed
    z = []  #date
    with open(f'{date}_speed.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        next(csvfile)
        for row in plots:
            x.append(str(row[0]))
            y.append(float(row[1]))
            z.append(float(row[2]))
    #find lowest download and upload point based and the times they occured
    lowest_download = sorted(y)[0]
    lowest_download_time = x[y.index(lowest_download)]
    lowest_upload = sorted(z)[0]
    lowest_upload_time = x[z.index(lowest_upload)]
    #create the actual graph
    plt.figure(figsize=(90, 10))
    plt.plot(x, y, label='download', color='r')
    plt.plot(x, z, label='upload', color='b')
    plt.xlabel('time')
    plt.xticks([])
    plt.ylabel('speed in Mb/s')
    plt.title(f"internet speed for {date}")
    #annotate what i am currently paying.
    plt.annotate(
        f"the lowest download speed: {lowest_download} at {lowest_download_time} Mb/s.\nthe lowest upload speed: {lowest_upload} at {lowest_upload_time} Mb/s.\n\nI pay for {download} download.",
        xy=(0.05, 0.88),
        xycoords='axes fraction')
    #showing the level I am paying for.
    plt.axhline(y=int(download), color='r', linestyle='--')
    plt.axhline(y=int(upload), color='b', linestyle='--')
    plt.legend()
    plt.savefig(f'{date}_graph.jpg', bbox_inches='tight')
    Image.open(f'{date}_graph.jpg').show()
