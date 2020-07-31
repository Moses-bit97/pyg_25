import datetime as dt
import csv
import os.path


print(
    '''
    ###############################
            Time Tracker
    ###############################\n
    ''')


task_name = input('Enter the name of the task: \n')
input('Press Enter to Start the tracker...\n')


start_datetime = dt.datetime.now()
start_date = start_datetime.strftime("%b %d %Y")
start = start_datetime.strftime('%H:%M')
print(f"You started working at: {start}")


input('Press Enter to Stop the tracker When done...')


end_datetime = dt.datetime.now()
end_date = end_datetime.strftime("%b %d %Y")
end = end_datetime.strftime('%H:%M')
print(f"You completed your task at: {end}")


duration = end_datetime - start_datetime
earning = round((duration.total_seconds()/3600)*5, 2)
