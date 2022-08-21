from matplotlib import pyplot

def checkboundtest(taskset,numberoftasks): # for checking the bound test theorem
     calculate=0
     boundtestconst=numberoftasks*((2**(1/numberoftasks))-1)
     tasktimeexec=[taskset[i][1] for i in range(numberoftasks)]
     taskperiodtime=[taskset[j][0] for j in range(numberoftasks)]
     for var in range(numberoftasks):
        calculate+=(tasktimeexec[var]/taskperiodtime[var])
     if calculate<=boundtestconst:
        return calculate
     else:
        return 0
def taskcalculations(taskset,numberoftasks):
    periodlist=[]
    minimumperiodindex=[]
    exectimelist=[]
    periodtemplist=[] #just for copying the periodlist in it
    for i in range(numberoftasks): #get the value of each task period
        periodlist.append(taskset[i][0])
    periodtemplist=periodlist.copy()
    periodtemplist.sort() # after sorting we could know which task has the smaalest period
    for periodindex in range(numberoftasks):
        minimumperiodindex.append(periodlist.index(periodtemplist[periodindex])) # we now saving the index of each task from smaallest to highest period time
    for extime in minimumperiodindex: # now we got the execution time of each task in assending sort
        exectimelist.append(taskset[extime][1])
    maxtimeofinterval = max(periodtemplist) # this is the time in one interval of execution
    countsofeach_task=[]
    for count in range(numberoftasks): # we calculate the occurence of each task
        var=maxtimeofinterval/periodtemplist[count]
        var2=str(var)
        if (len(var2)>4)and (periodtemplist[count]+exectimelist[count]<=maxtimeofinterval):
            indexoffloatingpoint=var2.index('.')
            var3=var2[:indexoffloatingpoint]
            countsofeach_task.append(int(var3)+1)
            var3=''
        elif (var2.endswith('.0')):
            indexoffloatingpoint = var2.index('.')
            var3=var2[:indexoffloatingpoint]
            countsofeach_task.append(int(var3))
            var3=''
        var2=''
    return exectimelist,periodtemplist,countsofeach_task
def checkingandcomparingtasks(taskset_,tasksnumber_):
          ex,P,occurence=taskcalculations(taskset_,tasksnumber_)
          tobeexecuted=[]
          tobeexecutedexactly = []
          timeinterval=[i for i in range(max(P))]
          timeinterval.append(max(P))
          c=0
          for counter in range(tasknumber):
           for i in range(0,P[counter]):
               if occurence[c%tasksnumber_]>=1:
                   tobeexecuted.append(ex[c%tasksnumber_])
                   occurence[c%tasksnumber_]-=1
                   c+=1
           tobeexecutedexactly=[i for i in tobeexecuted for j in range(i)] # sequence of occurence over the interval we need to customize with time
          return tobeexecuted,tobeexecutedexactly
def Drawing(taskksett,exsched,numberoftasks):
        exx,per,occ=taskcalculations(taskksett,numberoftasks)
        colors=['b','r','g']
        figure,axes = pyplot.subplots()
        axes.set_title('RMA algorithm')
        axes.set_ylim(0, 50);axes.set_xlim(0, 50)
        axes.set_xlabel('interval time for one time')
        axes.broken_barh([(0,exx[0]),(per[0],exx[0])],(20,7),facecolors=(colors[0]))
        axes.broken_barh([(exx[0],exx[1]), (per[1],exx[1])], (19,7), facecolors=(colors[1]))
        axes.broken_barh([(exx[0]+exx[1],exx[2])], (18, 7), facecolors=(colors[2]))
        pyplot.show()
tasknumber=eval(input('enter number of tasks\t'))
Taskset=[]
for i in range(tasknumber):
   temp=((eval(input(f'enter period of task {i+1} \t'))),(eval(input(f'enter exectime of task {i+1} \t'))))
   Taskset.append(temp)
check_value=checkboundtest(Taskset,tasknumber)
executiontimelist,periodtimelist,Occurenceeachtask=taskcalculations(Taskset,tasknumber)
schedule,exactschedue=checkingandcomparingtasks(Taskset, tasknumber)
if check_value!=0:
   print(check_value,'is sufficient for scheduling')
   print(executiontimelist, periodtimelist, Occurenceeachtask)
   print(schedule,exactschedue)
   print(len(exactschedue))
   Drawing(Taskset,exactschedue,tasknumber)
else:
    print('cant be scheduled')


