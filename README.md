#  An Automated Assistant for Course Management
A Python algorithm that utilizes Z3-Solver to automatically assign the appropriate time slot and location for a given course

## Background

Course scheduling is a real problem at many universities, as it is difficult to account for multiple factors like instructor availability, room sizes, etc., while making sure that all classes are eventually scheduled. Since much of this process is still done manually for departments at UMD, we wanted to come up with an automated solution to satisfy scheduling requirements with less intensive manual effort. 

## Current progress  🏃
- [x] Add in code to read input from a file instead of editing the program
- [x] Add in code to schedule classes in different days (MWF or TT) and durations (50-minute intervals on MWF or 75-minute intervals in TT)
- [x] Increase the parameters to include professor who will teach the course
- [x] Add in code to make separate schedules for lectures and discussions
- [x] Visualize results onto Google Calendar

## What's next  🧩
- Add in code to schedule time slots for longer courses (i.e. labs that are over 75 minutes long)
- Add in code to schedule other day patterns (i.e. Monday and Wednesday, any other day)
- Add in code to prevent putting small classes in big lecture halls
- Add in code to allow multiple lectures and multiple discussions for one class to happen at different classes and buildings
- Add in a Professor class to account for professor's time and location preferences

## Technologies used so far  🛠️
- Google Colab
- Python
- SAT Modulo Theories
- Z3-Solver
- Pandas
- Javascript
- Google App Script
- Google Calendar


