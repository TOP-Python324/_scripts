from time import perf_counter as pc, perf_counter_ns as pc_ns, sleep


start = pc_ns()
list(range(10000))
end = pc_ns()

print(end - start, 'нс\n')


start = pc()
sleep(2.5)
end = pc()

print(end - start, 'с\n')
