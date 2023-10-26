from PIL import ImageGrab
import pytesseract
import pynput.mouse
import ctypes
from time import sleep
import threading
from multiprocessing import Process, Manager

PROCESS_PER_MONITOR_DPI_AWARE = 2
ctypes.windll.shcore.SetProcessDpiAwareness(PROCESS_PER_MONITOR_DPI_AWARE)
mouse_ctr = pynput.mouse.Controller()

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


def four_ocr_process(image, row_number, grid_texts_list):
    image_row = (image.crop(area_list[4 * row_number + 0]),
                 image.crop(area_list[4 * row_number + 1]),
                 image.crop(area_list[4 * row_number + 2]),
                 image.crop(area_list[4 * row_number + 3]))
    text1 = pytesseract.image_to_string(image_row[0], lang='eng')
    text1 = text1.replace("\n", " ")
    text2 = pytesseract.image_to_string(image_row[1], lang='eng')
    text2 = text2.replace("\n", " ")
    text3 = pytesseract.image_to_string(image_row[2], lang='eng')
    text3 = text3.replace("\n", " ")
    text4 = pytesseract.image_to_string(image_row[3], lang='eng')
    text4 = text4.replace("\n", " ")
    grid_texts_list.extend((text1, text2, text3, text4))


def ocr_process(image, sector_number, grid_texts_list):
    image_sector = image.crop(area_list[sector_number])
    text = pytesseract.image_to_string(image_sector, lang='eng')
    text = text.replace("\n", " ")
    grid_texts_list.append(text)


ThreadLock = threading.Lock()
processes = []


def run():
    image = ImageGrab.grab((0, 0, 1920, 1080))
    manager = Manager()
    grid_texts = manager.list([])
    for i in range(3):
        ocr_proc = Process(target=four_ocr_process, args=(image, i, grid_texts))
        ocr_proc.start()
        processes.append(ocr_proc)
    for c in processes:
        c.join()
    print(grid_texts)
    for key in word_dict:
        for i in range(len(grid_texts)):
            text = grid_texts[i]
            if key in text:
                print(text)
                grid_texts[i] = ""
                mouse_ctr.position = point_pos[i]
                mouse_ctr.press(pynput.mouse.Button.left)
                mouse_ctr.release(pynput.mouse.Button.left)
                for j in range(len(grid_texts)):
                    if word_dict[key] in grid_texts[j]:
                        print(grid_texts[j])
                        grid_texts[j] = ""
                        mouse_ctr.position = point_pos[j]
                        mouse_ctr.press(pynput.mouse.Button.left)
                        mouse_ctr.release(pynput.mouse.Button.left)
                sleep(0.17)
    print(grid_texts)


if __name__ == "__main__":
    sleep(1)
    point_pos = []
    for c in area_list:
        point_pos.append(((c[0] + c[2]) / 2, (c[1] + c[3]) / 2))
    print(point_pos)
    image_rgb = ImageGrab.grab((0, 0, 1920, 1080)).convert("RGB")
    pixel_rgb = image_rgb.getpixel((745, 818))
    while pixel_rgb == (66, 62, 216) or pixel_rgb == (66, 85, 255):
        image_rgb = ImageGrab.grab((0, 0, 1920, 1080)).convert("RGB")
        pixel_rgb = image_rgb.getpixel((745, 818))
    while image_rgb.getpixel((216, 323)) != (217, 221, 232):
        image_rgb = ImageGrab.grab((0, 0, 1920, 1080)).convert("RGB")
    run()
