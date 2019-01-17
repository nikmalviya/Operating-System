processes = list(map(int, input('Enter Process Arrival Times : ').split()))
burst_times = list(map(int, input('Enter Burst Times : ').split()))


def findcompletiontime(processes, brust_times):
    num = 0
    ct = []
    for x in brust_times:
        num += x
        ct.append(num)
    return ct


def findturnaroundtime(comp_time, arrival_times):
    tat = []
    for c,a in zip(comp_time, arrival_times):
        tat.append(c-a)
    return tat


def findwaitingtime(tat, bt):
    wt = []
    for t,b in zip(tat,bt):
        wt.append(t- b)
    return wt

def printgantchart(at, bt, ct, tat, wt):
    print('PID\t\t AT\t\tCT\t\tTAT\t\tWT')
    for n, a, c, t, w in zip(range(1,len(at)+1), at, ct, tat, wt):
        print(n, '\t\t', a, '\t\t', c, '\t', t, '\t\t', w)


ct = findcompletiontime(processes, burst_times)
tat = findturnaroundtime(ct, processes)
wt = findwaitingtime(tat, burst_times)
printgantchart(processes,burst_times, ct, tat, wt)




