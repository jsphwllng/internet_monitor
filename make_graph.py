import matplotlib.pyplot as plt
import csv
import matplotlib.ticker as ticker
times = []
download = []
upload = []
with open(
        'test.csv',
        'r',
        newline='',
) as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    next(csvfile)
    for row in plots:
        times.append(str(row[0]))
        download.append(float(row[1]))
        upload.append(float(row[2]))

print(times, "\n", download, "\n", upload)

plt.figure(figsize=(20, 10))
plt.plot(times, download, label='download', color='r')
plt.plot(times, upload, label='upload', color='b')
plt.xlabel('time')
plt.ylabel('speed in Mb/s')
plt.title(f"internet speed")
plt.legend()
plt.savefig(f'test_graph.jpg', bbox_inches='tight')
