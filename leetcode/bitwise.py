bin_format = "{0:032b}"

start = 21
end = 24


#   start by converting the beginning into binary
start_bin = bin_format.format(start)
start_bin_array = [int(i) for i in start_bin]

#   select the lowest 1 bit as the step size
step_size = 0
left_1 = 32
right_1 = 32
for i in range(len(start_bin_array)):
    if start_bin_array[i] == 1:
        left_1 = i
        break
s = bin_format.format(end)
for i in range(len(s)):
    if s[i] == '1':
        right_1 = i
        break

if right_1 < left_1:
    # return 0
    pass

#   run a while till we pass the ending point
while (start <= end) and sum(start_bin_array) != 0:
    #   in each step, check if you the lowest 1 bit has changed, and update the step size
    bin = int(''.join(str(i) for i in start_bin_array), 2)
    bin = start & bin
    bin = bin_format.format(bin)
    start_bin_array = [int(i) for i in bin]
    for i in range(len(start_bin_array)):
        index = -1 + (-i)
        if start_bin_array[index] == 1:
            step_size = 2 ** i
            break
    start = int(''.join(str(i) for i in start_bin_array), 2) + step_size
    # start = start + step_size
#   in the end return the lowest bit selector
print(int(''.join(str(i) for i in start_bin_array), 2))