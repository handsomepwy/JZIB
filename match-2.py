import ctypes
from time import sleep
import pyperclip
from PIL import ImageGrab
import pynput


PROCESS_PER_MONITOR_DPI_AWARE = 2
ctypes.windll.shcore.SetProcessDpiAwareness(PROCESS_PER_MONITOR_DPI_AWARE)
mouse_ctr = pynput.mouse.Controller()
keyboard_ctr = pynput.keyboard.Controller()

# https://quizlet.com/841791952/match?funnelUUID=838ce222-9480-4d2d-ba28-71d469d59cd6
word_dict = {"alpha particle": "radioactive",
             "Atomic number": "A number",
             "Cathode-ray": "form o",
             "Compound": "subs",
             "Content": "ideas i",
             "electric field": "the space",
             "Electric plate": "A pair ",
             "Electron": "Negative",
             "Energy level": "3-D",
             "Gold Foil": "tin ",
             "Group (periodic table)": "vertical",
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
             "Period (periodic table)": "hor",
             "Proton": "positive charge ",
             "relative abundance": "The pro",
             "Relative atomic mass": "Mass ",
             "Scientific Method": "A se",
             "spectrum": "band",
             "sphere": "A solid s",
             "subatomic particles": "smaller tha",
             "Tube": "A l",
             "Isoelectronic": "number of e",
             "electron configuration": "the ar",
             "atomic mass": "How h",
             "Atomic model": "A de",
             "Deflected": "Changi",
             "electric charge": "matter"}
# https://quizlet.com/844281707/match?funnelUUID=3313846e-1e68-48fa-8af5-9b57d20017fd
# word_dict = {"Solid": "A state of matter that has a definite shape",
#              "liquid": "A state of matter that has a definite volume but no definite shape.",
#              "Gas": "A state of matter with no definite shape or volume.",
#              "particle": "smallest portion of matter",
#              "Matter": "Anything that has mass and takes up space",
#              "Particle arrangement": "How the particles arrange in space",
#              "intermolecular forces": "attraction forces between molecules. responsible for states of matter.",
#              "Melting": "The change in state from a solid to a liquid",
#              "Freezing": "The change of state from a liquid to a solid",
#              "Boiling": "The change of state from liquid to gas",
#              "Condensation": "The change of state from a gas to a liquid",
#              "Sublimation": "A change directly from the solid to the gas",
#              "Desublimation": "The change of state of water from gas to solid,",
#              "heat curve": "A graph that demonstrates the changing ",
#              "Atom": "Smallest particle of an element",
#              "Element": "pure substance that consists",
#              "Compound": "A substance made up of two or more atoms",
#              "Molecule": "A group of same elements bonded together",
#              "physical change": "A change in a substance that does not ",
#              "chemical change": "A change in matter that produces ",
#              "composition": "the ingredients of something",
#              "reversible": "able to be changed back to an earlier",
#              "irreversible": "not able to change back to",
#              "substance": "matter that has a uniform and definite",
#              "Brownian motion": "random movement of particles",
#              "Diffusion": "Movement of particles from an area of higher",
#              "dissolve": "Movement of particles that is assisted by breaking the intermolecular force",
#              "Temperature": "A measure of how hot (or cold) something",
#              "pressure": "the amount of force exerted",
#              "diffusion rate": "How fast diffusion occurs"}


point_pos = [(399, 370),
             (776, 385),
             (1166, 375),
             (1541, 376),
             (399, 628),
             (787, 636),
             (1153, 633),
             (1534, 635),
             (404, 890),
             (776, 884),
             (1149, 892),
             (1521, 887)]


def run():
    keyboard_ctr.press(pynput.keyboard.Key.ctrl)
    keyboard_ctr.press(pynput.keyboard.KeyCode.from_char("a"))
    keyboard_ctr.release(pynput.keyboard.KeyCode.from_char("a"))
    keyboard_ctr.press(pynput.keyboard.KeyCode.from_char("c"))
    keyboard_ctr.release(pynput.keyboard.KeyCode.from_char("c"))
    keyboard_ctr.release(pynput.keyboard.Key.ctrl)
    text = pyperclip.paste()
    grid_texts = text.split("\r\n")
    grid_texts = grid_texts[8:-1]
    print(grid_texts)
    for key in word_dict:
        for i in range(len(grid_texts)):
            text = grid_texts[i]
            if key == text:
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
