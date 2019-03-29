def first_fit(memory, process):
    for space in memory:
        if memory[space] is None and process <= space:
            memory[space] = process
            return True
    else:
        return False

def best_fit(memory, process):
    for space in sorted(memory):
        if memory[space] is None and process <= space:
            memory[space] = process
            return True
    else:
        return False

def worst_fit(memory,process):
    for space in sorted(memory, reverse=True):
        if memory[space] is None and process <= space:
            memory[space] = process
            return True
    else:
        return False
def display_memory(memory):
    print('Partition\t', 'Value')
    for space, value in memory.items():
        print(space, '\t', value)
file = open('in_for_mem', 'r')
partitions = eval(file.readline())
memory = dict.fromkeys(partitions, None)
process_sizes = eval(file.readline())
print(process_sizes)
for process in process_sizes:
    if not best_fit(  memory, process):
        print('Process with size : ', process, 'cannot be allocated in memory ')
    else:
        print('Process with size', process, ' is placed in memory')
display_memory(memory)






