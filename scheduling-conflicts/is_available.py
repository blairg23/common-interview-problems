# Part 1
# We are writing a tool to help users manage their calendars. Given an unordered list of times of day when a person is busy and a start time and end time, 
# write a function that tells us whether that person is available or not.

# Sample input:

# meetings = [
#   (1230, 1300),
#   ( 845, 900),
#   (1300, 1500),
# ]

# Expected output:

# isAvailable(meetings, 900, 1230) # => True
# isAvailable(meetings, 815, 945) # => False
# isAvailable(meetings, 945, 1200) # => True
# isAvailable(meetings, 1300, 1430) # => False
# isAvailable(meetings, 1315, 1500) # => False
# isAvailable(meetings, 900, 1015) # => True
# isAvailable(meetings, 1500, 1530) # => True
# isAvailable(meetings, 900, 1245) # => False
# isAvailable(meetings, 845, 1015) # => False
# isAvailable(meetings, 1245, 1330) # => False

# n = number of meetings
# s = number of schedules

def isAvailable(meetings, start_time, end_time):
    # iAmAvailable = True
    for meeting in meetings:
        # Meeting lands to the left (earlier) than the unavailable times
        if start_time < meeting[0] and end_time < meeting[0]:
            pass
        # Meeting lands to the right (later) than the unavailable times:
        elif start_time > meeting[1]:
            pass
        # Meeting starts at the same time another meeting is in progress:
        elif start_time == meeting[0]:
            return False
        # Meeting lands in the middle of an unavailable time
        elif (start_time < meeting[0] and end_time > meeting[0]):
            # iAmAvailable = False
            return False
        # Meeting lands in the middle of an unavailable time
        elif start_time > meeting[0] and end_time <= meeting[1]:
            return False
        # Meeting lands in the middle of an unavailable time
        elif start_time > meeting[0] and start_time < meeting[1]:
            return False
            
    return True


meetings = [
  (1230, 1300),
  ( 845, 900),
  (1300, 1500),
]

assert isAvailable(meetings, 900, 1230) ==  True
assert isAvailable(meetings, 815, 945) == False
assert isAvailable(meetings, 945, 1200) == True
assert isAvailable(meetings, 1300, 1430) == False
assert isAvailable(meetings, 1315, 1500) == False
assert isAvailable(meetings, 900, 1015) == True
assert isAvailable(meetings, 1500, 1530) == True
assert isAvailable(meetings, 900, 1245) == False
assert isAvailable(meetings, 845, 1015) == False
assert isAvailable(meetings, 1245, 1330) == False