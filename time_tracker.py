import datetime as dt
import csv
import os.path


# Prompt to Show application start
print(
    '''
    ###############################
            Time Tracker
    ###############################\n
    ''')

# Prompt user to enter the name of the task
task_name = input('Enter the name of the task: \n')

# Prompt user to [press enter] to start tracking the task duration
input('Press Enter to Start the tracker...\n')

# Get the date and time after [starting] the tracker
start_datetime = dt.datetime.now()
start_date = start_datetime.strftime("%b %d %Y")
start = start_datetime.strftime('%H:%M')
print(f"You started working at: {start}")

# Notify the user that they can [press enter] to stop the tracker
input('Press Enter to Stop the tracker When done...')

# Get the date and time after [stopping] the tracker
end_datetime = dt.datetime.now()
end_date = end_datetime.strftime("%b %d %Y")
end = end_datetime.strftime('%H:%M')
print(f"You completed your task at: {end}")

# Compute the duration for the task
duration = end_datetime - start_datetime

# Compute the amount earned for the duration
# compared with what 1 hr or 3600 seconds is worth
earning = round((duration.total_seconds()/3600)*5, 2)


# Define a function that formats duration into hours, minutes and seconds
def format_duration(duration):
    """
    Params:
    duration (timedelta): The difference between 2 datetimes

    Returns:
    A String of the formatted timedelta as nHrs:nminutes:nsecs
    """
    total_seconds = duration.seconds
    hours = divmod(total_seconds, 3600)[0]
    minutes = divmod(total_seconds, 60)
    return f"{hours}Hrs:{minutes[0]}mins:{minutes[1]}secs"


# Get the formatted duration with format_duration function
formatted_duration = format_duration(duration)

# Print the summary of the time-tracked
print(
    f'''
    | Task | Start Date | Start Time | Completion Date | Completion Time | Duration (Hrs) | Earnings($) |
    -----------------------------------------------------------------------------------------------------
    | {task_name} | {start_date}| {start} | {end_date}  | {end} | | {formatted_duration} | ${earning} |
    '''
)

# Write Time tracker summary into csv file
filename = 'tracker_summary.csv'
file_exists = os.path.isfile(filename)
with open(filename, 'a') as write_obj:
    headers = ['Task', 'Start_Date', 'Start_Time', 'Completion_Date',
               'Completion_Time', 'Duration(Hrs)', 'Earnings($)']
    writer = csv.DictWriter(write_obj, delimiter=',',
                            lineterminator='\n', fieldnames=headers)
    if not file_exists:
        writer.writeheader()
    writer.writerow(
        {'Task': task_name, 'Start_Date': start_date, 'Start_Time': start,
         'Completion_Date': end_date,
         'Completion_Time': end, 'Duration(Hrs)': duration, 'Earnings($)': earning
         })
