import cpuscheduling as cs
data = cs.readdata_with_priority()
data = cs.prioritycompletiontime(data)
cs.turnaroundtime(data)
cs.waitingtime(data)
cs.display_with_priority(data)
cs.showgraph(data,'Priority Scheduling')

