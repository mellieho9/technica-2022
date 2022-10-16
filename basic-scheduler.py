from z3 import *

'''
Number of time slots in the day. 
0 => 08:00-09:00
1 => 09:00-10:00
2 => 10:00-11:00
3 => 11:00-12:00
4 => 12:00-13:00
5 => 13:00-14:00
6 => 14:00-15:00
7 => 15:00-16:00
'''
TIME_SLOTS = 8

'''
Class object. Stores (at least) class name and size. 
e.g., Class("A", 30)
'''
class Class:
    def __init__(self, name, size):
        self.name = name
        self.size = size

'''
Room object. Stores (at least) room name and size.
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
    room_names = [ r.name for r in rooms ]

    # Create three variables for every class.
    # The first variable describes the (index of the) assigned room, the second
    # describes the time slot, and the third describes the size of the assigned room.
    vars = []
    for c in classes:
        c_vars = [ Int(c.name + "_room"), Int("%s_time" % c.name), Int("%s_size" % c.name) ] 
        vars.append(c_vars)

    # Every class must be assigned a valid room
    for i in range(len(classes)):
        room = vars[i][0]
        s.add(And(0 <= room, room < len(rooms)))

    # Every class must be assigned a valid time slot
    for i in range(len(classes)):
        time = vars[i][1]
        s.add(And(0 <= time, time < TIME_SLOTS))

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
            s.add(Not(And(room_i == room_j, time_i == time_j)))
    
    # The size of the class must be at most the capacity of the room
    for i in range(len(classes)):
        size = vars[i][2]
        s.add(class_sizes[i] <= size)
        # Example addition: the class should not be too small for the room
        # s.add(size - class_sizes[i] <= 15)

    # Check if a solution exists
    if s.check() == unsat:
        raise(Exception("No valid schedule"))

    # Print the schedule
    m = s.model()
    for i in range(len(classes)):
        room = m[vars[i][0]].as_long()
        time = m[vars[i][1]].as_long()
        print("Class %s is in room %s at " % (class_names[i], room_names[room]), end="")
        print_time(time)
        print()

def print_time(t):
    if t == 0:
        print("08:00-09:00", end="")
    elif t == 1:
        print("09:00-10:00", end="")
    elif t == 2:
        print("10:00-11:00", end="")
    elif t == 3:
        print("11:00-12:00", end="")
    elif t == 4:
        print("12:00-13:00", end="")
    elif t == 5:
        print("13:00-14:00", end="")
    elif t == 6:
        print("14:00-15:00", end="")
    elif t == 7:
        print("15:00-16:00", end="")
    else:
        raise(Exception("Invalid time slot: %d" % t))

# Run a small instance of the scheduling problem
classes = [Class("A", 20), 
           Class("B", 15), 
           Class("C", 30), 
           Class("D", 40),
           Class("E", 10),
           Class("F", 50),
           Class("G", 45),
           Class("H", 35),
           Class("I", 30),
           Class("J", 20),
           Class("K", 10),
           Class("L", 20)]
rooms = [Room("X", 50), 
         Room("Y", 20), 
         Room("Z", 35)]
schedule(classes, rooms)
