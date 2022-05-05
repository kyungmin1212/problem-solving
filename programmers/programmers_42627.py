from heapq import heappush, heappop


def solution(jobs):
    n = len(jobs)
    jobs.sort(key=lambda x: (x[0], x[1]))
    start, time = jobs.pop(0)
    now_time = start
    q = []
    heappush(q, (time, start))
    answer = 0
    while q:
        t, s = heappop(q)
        now_time += t
        answer += (now_time - s)
        while True:
            if jobs == [] or jobs[0][0] > now_time:
                break
            s, t = jobs.pop(0)
            heappush(q, (t, s))

        if q == [] and jobs != []:
            start, time = jobs.pop(0)
            now_time = start
            heappush(q, (time, start))

    return int(answer / n)