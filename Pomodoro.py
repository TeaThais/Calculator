tm = input('How much time? ').split('.')
#print(tm)
time_h = int(tm[0])
time_m = int(tm[1])
minutes = time_h * 60 + time_m
print(minutes)
pomo = minutes // 25
half_pomo = minutes % 25
print(f'{pomo}' + ' pomodoros and ' f'{half_pomo}' ' minutes')
print()
tm = input('How much time? ').split('.')

