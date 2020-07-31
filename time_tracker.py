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

def format_duration(duration):
    total_seconds = duration.seconds
    hours = divmod(total_seconds, 3600)[0]
    minutes = divmod(total_seconds, 60)
    return f"{hours}Hrs:{minutes[0]}mins:{minutes[1]}sec"

 


formatted_duration = format_duration(duration)

 

print(
    f'''
    | Task | Start Date | Start Time | Completion Date | Completion Time | Duration (Hrs) | Earnings($) |
    -----------------------------------------------------------------------------------------------------
    | {task_name} | {start_date}| {start} | {end_date}  | {end} | | {formatted_duration} | ${earning} |
    '''
)

