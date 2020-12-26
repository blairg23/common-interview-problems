# Part 2
# We are writing a tool to help users manage their calendars. Given an unordered list of times of day when people are busy, write a function that tells us the intervals during the day when ALL of them are available.

# Each time is expressed as an integer using 24-hour notation, such as 1200 (12:00), 1530 (15:30), or 800 (8:00).

# Sample input:

# p1_meetings = [
#   (1230, 1300),
#   ( 845, 900),
#   (1300, 1500),
# ]

# p2_meetings = [
#   ( 0, 844),
#   ( 930, 1200),
#   (1515, 1546),
#   (1600, 2400),
# ]

# p3_meetings = [
#   ( 845, 915),
#   (1515, 1545),
#   (1235, 1245),
# ]

# p4_meetings = [
#   ( 1, 5),
#   (844, 900),
#   (1515, 1600)
# ]

# schedules1 = [p1_meetings, p2_meetings, p3_meetings]
# schedules2 = [p1_meetings, p3_meetings]
# schedules3 = [p2_meetings, p4_meetings]

# Expected output:

# findAvailableTimes(schedules1)
#  => [  844,  845 ],
#     [  915,  930 ],
#     [ 1200, 1230 ],
#     [ 1500, 1515 ],
#     [ 1546, 1600 ]

# findAvailableTimes(schedules2)
#  => [    0,  845 ],
#     [  915, 1230 ],
#     [ 1500, 1515 ],
#     [ 1545, 2400 ]

# findAvailableTimes(schedules3)
#     [  900, 930],
#     [ 1200, 1515 ]

# n = number of meetings
# s = number of schedules


p1_meetings = [
  (1230, 1300),
  ( 845, 900),
  (1300, 1500),
]

p2_meetings = [
  ( 0, 844),
  ( 930, 1200),
  (1515, 1546),
  (1600, 2400),
]

p3_meetings = [
  ( 845, 915),
  (1515, 1545),
  (1235, 1245),
]

p4_meetings = [
  (   1, 5),
  ( 844, 900),
  (1515, 1600)
]

schedules1 = [p1_meetings, p2_meetings, p3_meetings]
schedules2 = [p1_meetings, p3_meetings]
schedules3 = [p2_meetings, p4_meetings]

"""
Solution taken from: https://stackoverflow.com/a/63769599/1224827
"""

minutesInDay = 60 * 24

def minuteToString(time):
    hour = str(int(time / 60))
    minute = str(int(time % 60))

    if len(hour) == 1:
        hour = '0' + hour
    if len(minute) == 1:
        minute = '0' + minute

    return hour + ':' + minute


def stringToMinute(time):
    hour, minute = time.split(':')
    return 60 * int(hour) + int(minute)


def availableTimeSlots(meetings, k):
    freeTime = [True] * k
    step = int(minutesInDay / k)

    for meet in meetings:
        for i in range(int(meet[0] / step), int(meet[1] / step)):
            freeTime[i] = False

    result = list()
    openInterval = False
    beg, end = 0, 0
    for i, slot in enumerate(freeTime):
        if not openInterval and slot:
            openInterval = True
            beg = i
        elif openInterval and not slot:
            openInterval = False
            end = i
            beg = minuteToString(beg * step)
            end = minuteToString(end * step)
            result.append((beg, end))

    return result


def main():
    p1_meetings = [
        ('12:30', '13:00'),
        ( '8:45', '9:00'),
        ('13:00', '15:00'),
    ]

    p2_meetings = [
        ( '00:00', '8:44'),
        ( '9:30', '12:00'),
        ('15:15', '15:46'),
        ('16:00', '24:00'),
    ]

    p3_meetings = [
        ( '8:45', '9:15'),
        ('15:15', '15:45'),
        ('12:35', '12:45'),
    ]

    p4_meetings = [
        ('00:01', '00:05'),
        ( '8:44', '9:00'),
        ('15:15', '16:00')
    ]

    meetings = [
        list(map(stringToMinute, meeting)) for p in [p1_meetings, p2_meetings, p3_meetings, p4_meetings]
        for meeting in p
    ]
    print(meetings)
    print(availableTimeSlots(meetings, 48))


if __name__ == '__main__':
    main()