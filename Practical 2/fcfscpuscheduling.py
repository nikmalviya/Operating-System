import cpuscheduling as cs
data = cs.readdata()
data = cs.fcfscompletiontime(data)
cs.turnaroundtime(data)
cs.waitingtime(data)
cs.displaytable(data)
cs.showgraph(data,'FCFS Scheduling')


