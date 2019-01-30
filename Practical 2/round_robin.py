import cpuscheduling as cs
data = cs.readdata()
tq = int(input('Enter Time Quantum : '))
cs.roundrobincompletiontime(data,tq)
cs.turnaroundtime(data)
cs.waitingtime(data)
cs.displaytable(data)
cs.showgraph(data,'Round Robin Scheduling')
