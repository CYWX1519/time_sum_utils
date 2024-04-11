

using_time = [
    "20:37", "48:57", "15:17", "13:43",
]

def calcul_time(time_array):
    if len(time_array) == 0:
        return 0
    
    days = 0
    hours = 0
    minute = 0
    second = 0
    
    def add_time(second, minute, hours, days):
        if(second >= 60):
            second -= 60
            minute += 1
        if(minute >= 60):
            minute -= 60
            hours += 1
        if hours >= 24:
            hours -= 24
            days += 1
        return days, hours, minute, second
            
    for time in time_array:
        time_list = time.split(":")
        if(len(time_list) == 0):
            continue
        for index in range(len(time_list)):
            if index == 0:
                second += (int)(time_list[len(time_list) - index - 1])
            elif index == 1:
                minute += (int)(time_list[len(time_list) - index - 1])
            else:
                hours += (int)(time_list[len(time_list) - index - 1])
            days, hours, minute, second = add_time(second, minute, hours, days)
                
    return "{0:0>2d}:{1:0>2d}:{2:0>2d}:{3:0>2d}".format(days, hours, minute, second)
                
print(calcul_time(using_time))