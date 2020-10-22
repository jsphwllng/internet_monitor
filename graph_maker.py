import matplotlib.pyplot as plt
import csv
import matplotlib.ticker as ticker


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
    #find lowest download and upload point based and the times they occured
    lowest_download = sorted(y)[0]
    lowest_download_time = x[y.index(lowest_download)]
    lowest_upload = sorted(z)[0]
    lowest_upload_time = x[z.index(lowest_upload)]
    plt.figure(figsize=(90, 10))
    plt.plot(x, y, label='download', color='r')
    plt.plot(x, z, label='upload', color='b')
    plt.xlabel('time')
    plt.xticks(rotation=90)
    plt.ylabel('speed in Mb/s')
    plt.title(f"internet speed for {date}")
    plt.annotate(f" the lowest download speed: {lowest_download} ast {lowest_download_time}.\nthe lowest upload speed: {lowest_upload} at {lowest_upload_time}\n\nI pay for 100 down and 40 up.",
                 xy=(0.05, 0.95),
                 xycoords='axes fraction')
    plt.legend()
    plt.savefig(f'{date}_graph.jpg', bbox_inches='tight')


make_graph("2020-10-22")
