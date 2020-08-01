# Time-tracking Programme - Group PYG-25
A programme that tracks the time taken to complete a task.

## Requirements
This programme uses in-built modules from `Python3` so there is no need to set up
a virtual environment or have a `requirement.txt` file.

## Running the Programme
1. Clone the repository
2. Navigate into project directory
   ```bash
   cd pyg_25
   ```
3. Execute the programme.
   ```bash
   python3 time_tracker.py
   ```

## Contributors
- [Naa Norley Wayoe](https://github.com/naa-norley)
- [Moses Fetuah](https://github.com/Moses-bit97)
- [Kofi Ocran](https://github.com/mupati)


## Implementation Process
This program makes use of the `datetime`, `csv` and `os.path` modules.
The current date and time is recorded immediately a user start the program. 
A function is created to format the computed duration.
In the duration function, the time recorded by the tracker will be converted to seconds.
Using the divmod() function the dividend being the duration a user spent on a task (start time-end time)
is divided by the divisor thus hours(3600) and minutes(60).
This is to give the duration in seconds which will be multiplied by $5 to give the amounts earned by the user.
In order to know the particular project the user is working on and how much he earned on the project.

 
The program is designed to be an interactive one. User input is required and it is done by asking the user to enter the name of the task,
After which a message is displayed indicating that if the user presses the enter key the tracker will start.
This records the exact time a user starts working on a task.
A message is displayed telling the user to press the enter key to stop the tracker.
A user gets a message showing the time the project was complete and a
summary of the time and earnings made on the project in a table format.

 
Storing time and information from the program in a csv file, the csv module was imported and given a file name with headers. 
The csv.DctWriter class maps dictionaries onto output rows. This csv file contains the records of the program.