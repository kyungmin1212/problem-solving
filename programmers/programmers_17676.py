def make_second(time):
    d, t, s = time.split()
    s = float(s[:-1])
    hour, minute, second = t.split(":")
    total_second = int(hour) * 3600 + int(minute) * 60 + float(second)

    start_time = round(total_second - s, 3)
    end_time = total_second

    return round(start_time + 0.001, 3), end_time


def solution(lines):
    start_end_time_list = []
    for time in lines:
        s, e = make_second(time)
        start_end_time_list.append([s, e])

    answer = 0

    for start, end in start_end_time_list:
        count = 0
        for s, e in start_end_time_list:
            if (start <= s < start + 1) or (start <= e < start + 1) or (s <= start and e >= start + 1):
                count += 1
        if answer < count:
            answer = count

        count = 0
        for s, e in start_end_time_list:
            if (end <= s < end + 1) or (end <= e < end + 1) or (s <= end and e >= end + 1):
                count += 1
        if answer < count:
            answer = count

    return answer