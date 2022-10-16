# Mel, Suruchi, Erin, Akshitha, Maria
# Making code account for different durations and days

from z3 import *

'''
Number of time slots in the day for MWF: 
0 => 08:00-08:50
1 => 09:00-09:50
2 => 10:00-10:50
3 => 11:00-11:50
4 => 12:00-12:50
5 => 13:00-13:50
6 => 14:00-14:50
7 => 15:00-15:50
8 => 16:00-16:50

Number of time slots in the day for TTh: 
0 => 08:00-9:15
1 => 09:30-10:45
2 => 11:00-12:15
3 => 12:30-13:45
4 => 14:00-15:15
5 => 15:30-16:45
'''
TIME_SLOTS_A = 9
TIME_SLOTS_B = 6

DAYS = 2

'''
Class object. Stores class name, size, professor, and identifier to group lectures/discussions

e.g., Class("A", 30)
'''
class Class:
    def __init__(self, name, size, professor, identifier):
        self.name = name
        self.size = size
        self.number = identifier
        self.professor = professor
'''
Room object. Stores room name and size.

e.g., Room("X", 45)
'''
class Room:
    def __init__(self, name, size):
        self.name = name
        self.size = size

'''
Input: List of Classes
Input: List of Rooms
Output: Prints Schedule
'''
def schedule(classes, rooms):

    s = Solver()

    # Put input data in a more convenient format
    class_names = [ c.name for c in classes ]
    class_sizes = [ c.size for c in classes ]
    class_professor = [c.professor for c in classes ]
    room_names = [ r.name for r in rooms ]

    # Create five variables for every class.
    # The first variable describes the (index of the) assigned room, the second
    # describes the time slot, and the third describes the size of the assigned room.
    vars = []
    for c in classes:
        c_vars = [Int("%s_room" % c.name), Int("%s_time" % c.name), Int("%s_size" % c.name), Int("%s_days" % c.name), Int("%s_professor" % c.name)] 
        vars.append(c_vars)

    # Every class must be assigned a valid room
    for i in range(len(classes)):
        room = vars[i][0]
        s.add(And(0 <= room, room < len(rooms)))

    # Every class must be assigned a valid time slot
    for i in range(len(classes)):
        time = vars[i][1]
        days = vars[i][3]
        s.add(Implies(days == 0, And(0 <= time, time < TIME_SLOTS_A)))
        s.add(Implies(days == 1, And(0 <= time, time < TIME_SLOTS_B)))

    # Every class must be assigned a pattern of days
    for i in range(len(classes)):
        days = vars[i][3]
        s.add(And(0 <= days, days < DAYS))

    # The assigned room determines the assigned room size
    for i in range(len(classes)):
        for j in range(len(rooms)):
            room = vars[i][0]
            size = vars[i][2]
            s.add(Implies(room == j, size == rooms[j].size))

    # No two classes can be assigned to the same room during the same time slot
    for i in range(len(classes)):
        for j in range(i+1, len(classes)):
            room_i = vars[i][0]
            room_j = vars[j][0]
            time_i = vars[i][1]
            time_j = vars[j][1]
            days_i = vars[i][3]
            days_j = vars[j][3]
            s.add(Not(And(room_i == room_j, time_i == time_j, days_i == days_j)))

            if classes[i].number == classes[j].number:
                s.add(Not(And(time_i == time_j, days_i == days_j)))

    #AKSHITHA: No two classes can have the same professor during the same time slot
    for i in range(len(classes)):
        for j in range(i+1, len(classes)):
            professor_i = vars[i][4]
            professor_j = vars[j][4]
            time_i = vars[i][1]
            time_j = vars[j][1]
            days_i = vars[i][3]
            days_j = vars[j][3]
            s.add(Not(And(professor_i == professor_j, time_i == time_j, days_i == days_j)))
    
    # The size of the class must be at most the capacity of the room
    for i in range(len(classes)):
        size = vars[i][2]
        s.add(class_sizes[i] <= size)

    # Check if a solution exists
    if s.check() == unsat:
        raise(Exception("No valid schedule"))

    # Print the schedule
    m = s.model()
    for i in range(len(classes)):
        room = m[vars[i][0]].as_long()
        time = m[vars[i][1]].as_long()
        days = m[vars[i][3]].as_long()
        print("Class %s is with %s in room %s at " % (class_names[i], class_professor[i], room_names[room]), end="")
        if days == 0:
            print_timeA(time)
        elif days == 1:
            print_timeB(time)
        print_days(days)
        print()

def print_timeA(t):
    if t == 0:
        print("08:00-08:50", end="")
    elif t == 1:
        print("09:00-09:50", end="")
    elif t == 2:
        print("10:00-10:50", end="")
    elif t == 3:
        print("11:00-11:50", end="")
    elif t == 4:
        print("12:00-12:50", end="")
    elif t == 5:
        print("13:00-13:50", end="")
    elif t == 6:
        print("14:00-14:50", end="")
    elif t == 7:
        print("15:00-15:50", end="")
    elif t == 8:
        print("16:00-16:50", end="")
    else:
        raise(Exception("Invalid time slot: %d" % t))

def print_timeB(t):
    if t == 0:
        print("08:00-09:15", end="")
    elif t == 1:
        print("09:30-10:45", end="")
    elif t == 2:
        print("11:00-12:15", end="")
    elif t == 3:
        print("12:30-13:45", end="")
    elif t == 4:
        print("14:00-15:15", end="")
    elif t == 5:
        print("15:30-16:45", end="")
    else:
        raise(Exception("Invalid time slot: %d" % t))

def print_days(t):
    if t == 0:
        print(" on Monday, Wednesday, and Friday")
    elif t == 1:
        print(" on Tuesday, Thursday")
    else:
        raise(Exception("Invalid days: %d" % t))

# Run a small instance of the scheduling problem

infilename = "technica-2022/testcase2.txt"

infile = open(infilename,'r')

nums = []

classesDone = False

classes = []
rooms = []
while True:
    line = infile.readline()
    if not line:
        break
    if line[:7].lower() == "classes" or line == "\n":
        pass
    elif line[:5].lower() == "rooms":
        classesDone = True
    elif not classesDone:
		    #append a new class instance to the classes list
        split1 = line.find(" ")
        split2 = line[split1+1:].find(" ") + split1 + 1
        split3 = line[split2+1:].find(" ") + split2 + 1
        classes.append(Class(line[:split1], int(line[split1:split2]), line[split2+1:split3], line[split3+1:len(line)-1]))
    else:
        #append a new room to the rooms instance
        split = line.find(" ")
        rooms.append(Room(line[:split], int(line[split:len(line)-1])))

infile.close()
schedule(classes, rooms)
