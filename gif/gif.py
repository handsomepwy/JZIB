import imageio
from PIL import Image

# pic src:lab.nulla.top/ba-logo


def compose_gif(pics_list):
    for c in pics_list:
        pics_list[pics_list.index(c)] = Image.open(c)
    imageio.mimsave("result.gif", pics_list, fps=5)


def convert(pics_list):
    for c in pics_list:
        img = Image.open(c)
        img = img.resize((1800, 500))
        img.save(""+c)


compose_gif(["1.png", "2.png", "3.png", "4.png", "5.png", "6.png", "7.png"])
# convert(["1.png", "2.png", "3.png", "4.png", "5.png", "6.png", "7.png"])
