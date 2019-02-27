def readdata():
    file = open('data', 'r')
    data = []
    for line in file.read().split('\n'):
        l = line.split(' ')
        dict =  {
                'PID': l[0].strip(),
                'AT': int(l[1].strip()),
                'BT': int(l[2].strip()),
                'CT': 0,
                'TAT': 0,
                'WT': 0,
                }
        data.append(dict)
    return data
def readdata_with_priority():
    file = open('data_with_priority', 'r')
    data = []
    for line in file.read().split('\n'):
        l = line.split(' ')
        dict = {
            'PID': l[0].strip(),
            'AT': int(l[1].strip()),
            'BT': int(l[2].strip()),
            'CT': 0,
            'TAT': 0,
            'WT': 0,
            'PRIORITY': int(l[3].strip())
        }
        data.append(dict)
    return data

def fcfscompletiontime(data):
    data = sorted(data, key=lambda x: x['AT'])
    lastct = min([x['AT'] for x in data])
    for d in data:
        lastct = lastct + d['BT']
        d['CT'] = lastct
    return data
def multilevelcompletiontime(data):
    data = sorted(data, key=lambda x: x['AT'])
    sys_queue = []
    user_queue = []

    pcounter = 0
    completed = []
    time = 0
    totalp = len(data)
    while pcounter != totalp:
        for x in data.copy():
            if x['AT'] <= time:
                if x['PID'][-1] == 'S':
                    sys_queue.append(x)
                else:
                    user_queue.append(x)
                data.remove(x)
        if len(sys_queue):
            d = sys_queue.pop(0)
            time = time + d['BT']
            d['CT'] = time
            completed.append(d)
            pcounter += 1
        elif len(user_queue):
            d = user_queue.pop(0)
            time = time+ d['BT']
            d['CT'] = time
            completed.append(d)
            pcounter += 1
        else:
            time+=1
    return completed
def sjfcompletiontime(data):
    queue = []
    data = sorted(data, key=lambda x: (x['AT'], x['BT']))
    loopend = sum([x['BT'] for x in data]) + min([x['AT'] for x in data])
    completed = []
    time = 0
    while time != loopend + 1:
        for x in data.copy():
            if x['AT'] <= time:
                queue.append(x)
                data.remove(x)
        queue = sorted(queue, key=lambda x: x['BT'])
        if len(queue) != 0:
            d = queue.pop(0)
            time = time + d['BT']
            d['CT'] = time
            completed.append(d)
        else:
            time = time + 1
    return completed


def sjfcompletiontime_premptive(data):
    queue = []
    data = sorted(data, key=lambda x: (x['AT'], x['BT']))
    completed = []
    time = 0
    for d in data: d['RT'] = d['BT']
    n = len(data)
    pcounter = 0
    while pcounter != n:
        for x in data.copy():
            if x['AT'] <= time:
                queue.append(x)
                data.remove(x)
        queue = sorted(queue, key=lambda x: x['RT'])
        if len(queue) != 0:
            d = queue.pop(0)
            d['RT'] = d['RT'] - 1
            if(d['RT'] == 0):
                completed.append(d)
                d['CT'] = time+1
                pcounter+=1
            else:
                queue.append(d)
            time = time + 1
        else:
            time = time + 1
    for d in completed: del d['RT']
    return completed

def roundrobincompletiontime(data,tq):
    data = sorted(data, key=lambda x: x['AT'])
    queue = []
    completed = []
    time = 0    
    n = len(data)
    temp = {}
    flag = False
    pcounter = 0
    for d in data: d['RT'] = d['BT']
    while (n != pcounter):
        for x in data.copy():
            if x['AT'] <= time:
                queue.append(x)
                data.remove(x)
        if flag:
            queue.append(temp)
            flag = False
        if len(queue) != 0:
            d = queue.pop(0)
            if d['RT'] <= tq:
                time += d['RT']
                d['CT'] = time
                d['RT'] = 0
                completed.append(d)
                pcounter += 1
            else:
                time += tq
                d['RT'] -= tq
                temp = d
                flag = True
            # print(d)
        else:
            time += 1

    for d in completed: del d['RT']
    return completed
def prioritycompletiontime(data):
    queue = []
    data = sorted(data, key=lambda x: (x['PRIORITY'], x['AT'], x['PID']))
    completed = []
    time = 0
    n = len(data)
    pcounter = 0
    while pcounter != n:
        for x in data.copy():
            if x['AT'] <= time:
                queue.append(x)
                data.remove(x)
        queue = sorted(queue, key=lambda x: (x['PRIORITY'], x['AT'], x['PID']))
        if len(queue) != 0:
            d = queue.pop(0)
            time += d['BT']
            d['CT'] = time
            completed.append(d)
            pcounter+=1
        else:
            time = time + 1
    return sorted(completed,key= lambda x: x['PID'])

def turnaroundtime(data):
    for d in data:
        d['TAT'] = d['CT'] - d['AT']


def waitingtime(data):
    for d in data:
        d['WT'] = d['TAT'] - d['BT']

def displaytable(data):
    print('PID \t','AT \t','BT \t','CT \t','TAT \t','WT')
    wt = 0
    tat = 0
    for d in data:
        print(' %s  \t %2d  \t %2d  \t %2d  \t %2d  \t %2d' % tuple(d.values()))
        wt = wt + d['WT']
        tat = tat + d['TAT']
    wt = wt / len(data)
    tat = tat / len(data)
    print()
    print('Average Waiting Time : {:.2f}'.format(wt))
    print('Average Turn Around Time : {:.2f} '.format(tat))

def display_with_priority(data):
    print('PID \t', 'AT \t', 'BT \t', 'CT \t', 'TAT \t', 'WT \t', 'PRTY')
    wt = 0
    tat = 0
    for d in data:
        print(' %s  \t %2d  \t %2d  \t %2d  \t %2d  \t %2d  \t %2d' % tuple(d.values()))
        wt = wt + d['WT']
        tat = tat + d['TAT']
    wt = wt / len(data)
    tat = tat / len(data)
    print()
    print('Average Waiting Time : {:.2f}'.format(wt))
    print('Average Turn Around Time : {:.2f} '.format(tat))
def showgraph(data,title):
    import numpy as np
    import matplotlib.pyplot as plt
    avgwt = 0
    for d in data: avgwt+=d['WT']
    avgct = 0
    for d in data: avgct += d['CT']
    avgtat = 0
    for d in data: avgtat += d['TAT']
    height = [round(avgwt/len(data),2),round(avgtat/len(data),2),round(avgct/len(data),2)]
    print(height)
    bars = ('WT', 'TAT', 'CT')
    y_pos = np.arange(len(bars))
    plt.bar(y_pos, height)
    plt.title(title)
    plt.xticks(y_pos, bars)
    plt.show()


