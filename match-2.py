import pyautogui
import ctypes
from time import sleep
import pyperclip
from PIL import ImageGrab
import pynput


PROCESS_PER_MONITOR_DPI_AWARE = 2
ctypes.windll.shcore.SetProcessDpiAwareness(PROCESS_PER_MONITOR_DPI_AWARE)
mouse_ctr = pynput.mouse.Controller()
keyboard_ctr = pynput.keyboard.Controller()

word_dict = {"alpha": "radioactive",
             "Atomic number": "A number",
             "Cathode-": "form o",
             "Compound": "subs",
             "Content": "ideas i",
             "electric field": "the space",
             "Electric plate": "A pair ",
             "Electron": "Negative",
             "Energy level": "3-D",
             "Gold Foil": "tin ",
             "Group": "vertical",
             "Indivisible": "Cannot",
             "Isotope": "An atom w",
             "location": "particular",
             "metal": "usually a s",
             "Metalloid": "phy",
             "multiple proportions": "Two e",
             "Neutron": "no c",
             "undeflected": "Unchanged",
             "Non-metal": "a gas",
             "Nucleon": "result of r",
             "Nucleus": "heavy,",
             "Observation": "The ac",
             "orbit": "The pa",
             "Period": "hor",
             "Proton": "positive charge ",
             "relative abundance": "The pro",
             "Relative atomic mass": "Mass ",
             "Scientific Method": "A se",
             "spectrum": "band",
             "sphere": "A solid s",
             "subatomic particles": "smaller tha",
             "Tube": "A l",
             "Isoelectronic": "number of e",
             "electronic configuration": "the ar",
             "electron configuration": "the ar",
             "atomic mass": "How h",
             "Atomic model": "A de",
             "Deflected": "Changi",
             "electric charge": "matter"}

area_list = [(223, 251, 566, 476),
             (598, 265, 943, 475),
             (981, 263, 1320, 477),
             (1352, 262, 1700, 479),
             (225, 511, 572, 731),
             (599, 509, 947, 728),
             (973, 505, 1322, 723),
             (1349, 507, 1701, 731),
             (225, 778, 559, 981),
             (602, 770, 941, 984),
             (977, 774, 1312, 990),
             (1358, 776, 1697, 982)]

point_pos = []
for c in area_list:
    point_pos.append(((c[0] + c[2]) / 2, (c[1] + c[3]) / 2))


def run():
    keyboard_ctr.press(pynput.keyboard.Key.ctrl)
    keyboard_ctr.press(pynput.keyboard.KeyCode.from_char("a"))
    keyboard_ctr.release(pynput.keyboard.KeyCode.from_char("a"))
    keyboard_ctr.press(pynput.keyboard.KeyCode.from_char("c"))
    keyboard_ctr.release(pynput.keyboard.KeyCode.from_char("c"))
    keyboard_ctr.release(pynput.keyboard.Key.ctrl)
    pyautogui.hotkey("ctrl", "a")
    pyautogui.hotkey("ctrl", "c")
    text = pyperclip.paste()
    grid_texts = text.split("\r\n")
    grid_texts = grid_texts[8:]
    # for key in word_dict:
    #     try:
    #         first_pos = text.index(key)
    #         pos = area_list[first_pos]
    #         mouse_ctr.position = pos
    #         mouse_ctr.click(pynput.mouse.Button.left, 1)
    #     except ValueError:
    #         continue
    #     for i in range(len(text)):
    #         c = text[i]
    #         if word_dict[key] in c:
    #             pos = area_list[i]
    #             mouse_ctr.position = pos
    #             mouse_ctr.click(pynput.mouse.Button.left, 1)
    #             sleep(0.2)
    #             break
    for key in word_dict:
        for i in range(len(grid_texts)):
            text = grid_texts[i]
            if key in text:
                print(text)
                grid_texts[i] = ""
                mouse_ctr.position = point_pos[i]
                mouse_ctr.click(pynput.mouse.Button.left, 1)
                for j in range(len(grid_texts)):
                    if word_dict[key] in grid_texts[j]:
                        print(grid_texts[j])
                        grid_texts[j] = ""
                        mouse_ctr.position = point_pos[j]
                        mouse_ctr.click(pynput.mouse.Button.left, 1)
                sleep(0.16)
    print(grid_texts)


if __name__ == "__main__":
    sleep(1)
    image_rgb = ImageGrab.grab((0, 0, 1920, 1080)).convert("RGB")
    pixel_rgb = image_rgb.getpixel((745, 818))
    while pixel_rgb == (66, 62, 216) or pixel_rgb == (66, 85, 255):
        image_rgb = ImageGrab.grab((0, 0, 1920, 1080)).convert("RGB")
        pixel_rgb = image_rgb.getpixel((745, 818))
    while image_rgb.getpixel((216, 323)) != (217, 221, 232):
        image_rgb = ImageGrab.grab((0, 0, 1920, 1080)).convert("RGB")
    run()
