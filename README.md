![a robot with two wifi bars coming out of its antenna](https://raw.githubusercontent.com/jsphwllng/internet_monitor/master/image/internet_monitor.png "roboto")
# A tool to monitor internet speeds and record them

## to do
* <strike>monitor internet speed and write to a csv fille</strike>
* write some analytics to return highest, average and lowest speeds
* <strike> write a way to turn this into a graph</strike>
* <strike> automate an upload of these files daily to a cloud storage system</strike>


## key learning points
1. use of matplotlib
2. environments and environment variables
3. pydrive and automated file uploads
4. benefits of a simple CSV over a database
5. my internet is pretty inconsistent
6. error handling

## installing and running
* optional:
  * [generate your API key from here first](https://developers.google.com/drive/api/v3/quickstart/python#step_1_turn_on_the)

```bash
cd ~
git clone git@github.com:jsphwllng/internet_monitor.git
pip3 install -r requirements.txt
*touch client_secrets.json (and add the contents from the credentials.json)
python3 monitor.py
```
*if you don't want to upload your files to google drive then skip this step

🤖📶 please let me know if this was useful for you
