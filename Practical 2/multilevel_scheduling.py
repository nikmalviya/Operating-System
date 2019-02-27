import cpuscheduling as cs
data = cs.readdata()
data = cs.multilevelcompletiontime(data)
cs.turnaroundtime(data)
cs.waitingtime(data)
cs.displaytable(data)
