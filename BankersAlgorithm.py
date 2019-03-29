import numpy as np

total_available = []
data = []
current_available = []
safe_order = []


def readData():
    with open('input_for_bankers_algo') as file:
        global total_available
        total_available = np.array(eval(file.readline().split('=')[1].replace('\n','')))
        file.readline()
        for line in file:
            rdata = line.replace('\n','').split()
            data.append(
                dict(PID=rdata[0], AVAIL=np.array(eval(rdata[1])), MAX=np.array(eval(rdata[2])),DONE=False)


            )


def calculate_resources_needed():
    avails = np.array([d['AVAIL'] for d in data])
    global current_available
    current_available = total_available - np.sum(avails,axis=0)
    for d in data: d['NEED'] = d['MAX'] - d['AVAIL']


def process_order_for_safe_state():
    global current_available, safe_order
    while not all([d['DONE'] for d in data]):
        at_least_one_is_allocated = False
        for d in data:
            if not d['DONE']:
                if all(current_available - d['NEED'] >=0 ):
                    at_least_one_is_allocated = True
                    safe_order.append(d['PID'])
                    d['DONE'] = True
                    current_available+=d['AVAIL']
        if not at_least_one_is_allocated:
            print('Resource Allocation not Safe..')
            exit(-1)


def display():
    print('PID\t','  ALLOCATION\t',' MAX\t\t',' NEED')
    for d in data:
        print('{PID}\t\t{AVAIL}\t\t{MAX}\t\t{NEED}'.format(**d))
    print('\nSafe Order : ', ' -> '.join(safe_order))

readData()
calculate_resources_needed()
process_order_for_safe_state()
display()
