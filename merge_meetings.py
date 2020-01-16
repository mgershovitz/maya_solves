# Related blog post - https://algoritmim.co.il/2019/07/06/merge-meetings/

class Meeting(object):
    def __init__(self, start, end):
        self.start_time = start
        self.end_time = end

    def __lt__(self, other):
        return self.start_time < other.start_time

    def __eq__(self, other):
        return self.start_time == other.start_time and self.end_time == other.end_time

    def __repr__(self):
        return "(%d,%d)" % (self.start_time, self.end_time)


def merge_meetings(arr):
    if len(arr) <= 1:
        return arr

    arr.sort()
    res = [arr[0]]
    previous_meeting = arr[0]
    for i in range(1, len(arr)):
        new_meeting = arr[i]
        if new_meeting.start_time <= previous_meeting.end_time:
            previous_meeting.end_time = new_meeting.end_time
        else:
            res.append(new_meeting)
            previous_meeting = new_meeting

    return res


def run_tests():
    arr = [Meeting(3, 4), Meeting(0, 2)]
    assert merge_meetings(arr) == [Meeting(0, 2), Meeting(3, 4)]

    arr = [Meeting(3, 4), Meeting(0, 2), Meeting(1, 3)]
    assert merge_meetings(arr) == [Meeting(0, 4)]

    arr = [Meeting(0, 1), Meeting(3, 5), Meeting(4, 8), Meeting(10, 12), Meeting(9, 10)]
    assert merge_meetings(arr) == [Meeting(0, 1), Meeting(3, 8), Meeting(9, 12)]


if __name__ == '__main__':
    run_tests()
