import cpuscheduling as cs
data = cs.readdata()
cs.sjfcompletiontime_premptive(data)
cs.turnaroundtime(data)
cs.waitingtime(data)
cs.displaytable(data)




