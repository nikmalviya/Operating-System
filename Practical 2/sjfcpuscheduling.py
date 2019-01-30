import cpuscheduling as cs
data = cs.readdata()
data = cs.sjfcompletiontime(data)
cs.turnaroundtime(data)
cs.waitingtime(data)
cs.displaytable(data)
cs.showgraph(data,"SJF Scheduling")

