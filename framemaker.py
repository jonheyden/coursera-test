import numpy as np


class task:
    def __init__(self, name, period, duration, deadline):
        self.name = name
        self.period = period
        self.duration = duration
        self.deadline = deadline


#Takes a list of tasks and returns the LCM of the periods
def get_lcm(tasks):
    lcmarray = []
    for task in tasks:
        lcmarray.append(task.period)
    lcm = np.lcm.reduce(lcmarray)
    return lcm

def get_max_execution_time(tasks):
    max_execution_time = 0
    for task in tasks:
        if task.duration > max_execution_time:
            max_execution_time = task.duration
    return max_execution_time

def get_lowest_period(tasks):
    lowest_period = get_lcm(tasks)
    for task in tasks:
        if task.period < lowest_period:
            lowest_period = task.period
    return lowest_period

def check_frame(task, frame):
     if 2*frame <= task.deadline + np.gcd(int(frame),int(task.period)):
         return True
     else:
         return False

def get_frames(tasks):
      frame_lcm = get_lcm(tasks)
      max_execution_time = get_max_execution_time(tasks)
      lowest_period = get_lowest_period(tasks)
      frames = []
      temp = frame_lcm
      i = 1
      while temp >= max_execution_time:
         frames.append(temp)
         i = i + 1
         temp = frame_lcm/(i)
      rem_arr = []
      for task in tasks:
            for frame in frames:
               if not check_frame(task, frame):
                   rem_arr.append(frame)
            for i in range(len(rem_arr)):
                frames.remove(rem_arr[i])                
            rem_arr = []
      return frames

def get_frames_hyperperiod(frames, hyperperiod):
    x = []
    for frame in frames:
        x.append(hyperperiod/frame)
    
    return x
        
def get_task_amount(task_list, hyperperiod):
    x = []
    for task in task_list:
        x.append(hyperperiod/task.period)
        
    return x
    
    
#Takes a list of tasks and returns a clock driven schedule
def get_schedule(task_list):
    my_hyperperiod = get_lcm(task_list)
    my_frames = get_frames(task_list)
    my_frames_per_period = get_frames_hyperperiod(my_frames, my_hyperperiod)
    my_task_amount = get_task_amount(task_list, my_hyperperiod)
    newline = '\n'
    
    testframeperiodorig = max(my_frames)
    testframeperiod = testframeperiodorig
    testframeamount = my_hyperperiod/testframeperiod
    schedule = []
    
    
    for task in task_list:
        if testframeamount == my_hyperperiod/task.period :
            testframeperiod = testframeperiod - task.duration
            for i in range(int(testframeamount)):
                schedule.append(f'Task {task.name}')
            my_task_amount.remove(my_hyperperiod/task.period)
               
                
    #print(my_frames)           
    print(schedule, testframeperiod, my_task_amount)
    
    #for i in range(testframeamount):
        
        
    
    
    return


task_a = task("A", 3,.5, 3)
task_b = task("B", 5, 0.9, 5)
task_c = task("C", 6, 1.1, 6)
task_d = task("D", 10, 1.4, 5)
task_e = task("E", 15, 1.9, 15)
task_f = task("F", 15, 1.2, 6)

task_list = []
task_list.append(task_a)
task_list.append(task_b)
task_list.append(task_c)
task_list.append(task_d)
task_list.append(task_e)
task_list.append(task_f)


my_hyperperiod = get_lcm(task_list)
my_frames = get_frames(task_list)
my_frames_per_period = get_frames_hyperperiod(my_frames, my_hyperperiod)


get_schedule(task_list)


#print(task_list[0])

#print(np.lc)

