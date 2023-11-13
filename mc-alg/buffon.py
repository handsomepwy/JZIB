# Buffon's needle problem (min ver.)
import math
import random
from tqdm import tqdm

in_point = 0
loop_times = 10000000
for i in tqdm(range(loop_times)):
    x = random.random() / 2
    theta = random.uniform(0, math.pi)
    if x < math.sin(theta)/2:
        in_point += 1
print("in point: "+str(in_point))
result_pi = loop_times / in_point * 2
print("result pi: "+str(result_pi))
