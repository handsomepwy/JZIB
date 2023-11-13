# alright this is the true one
import random
from tqdm import tqdm

won_time = 0
loop_times = 100
for i in tqdm(range(loop_times)):
    doors = [0, 1, 2]
    prize_door = random.choice(doors)
    first_door = random.choice(doors)
    open_door = random.choice(doors)
    while open_door == prize_door or open_door == first_door:
        open_door = random.choice(doors)
    final_door = first_door
    while final_door == first_door or final_door == open_door:
        final_door = random.choice(doors)
    if final_door == prize_door:
        won_time += 1
print(won_time)
