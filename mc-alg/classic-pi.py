# classic version of using Monte-Carlo to get pi
import math
from random import random
from tqdm import tqdm

in_point = 0
loop_times = 10000000
for i in tqdm(range(loop_times)):
    x, y = random(), random()
    if math.sqrt(x**2+y**2) <= 1:
        in_point += 1
print("in point: "+str(in_point))
result_pi = in_point / loop_times * 4
print("result pi: "+str(result_pi))
