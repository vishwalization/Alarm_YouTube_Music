import webbrowser
import schedule
import time

def play_music(url):
    ''' 
    TODO: Opens url in a default browser.

    \param: url Link to YouTube music song/ YouTube video
    ''' 
    webbrowser.open(url)    

# Scheduling (24-hour format)
schedule_time = "12:36:00"
url = "https://music.youtube.com/watch?v=AaxFIY-cWH0"

# Use lambda to delay passing the URL to the function until the scheduled time
schedule.every().day.at(schedule_time).do(lambda: play_music(url))
print(f"Scheduled to play music at {schedule_time} everyday")

# Keeps the script running
while True:
    schedule.run_pending()
    time.sleep(1)