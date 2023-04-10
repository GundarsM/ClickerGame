import pyautogui
import time
import keyboard
import cv2
import numpy
import pytesseract

#while 1:
    #position = pyautogui.position()
    #print(position)
def print_position():
    position = pyautogui.position()
    print(position)

def click(point):
    time.sleep(0.05)
    pyautogui.click(point[0],point[1])

def money_level():
    my_screenshot = pyautogui.screenshot(region=(1102,55,250,40))
    my_image = numpy.array(my_screenshot)
    my_image = cv2.cvtColor(my_image, cv2.COLOR_BGR2GRAY)

    #cv2.imshow("bilde", my_image)
    #cv2.waitKey(0)
    pytesseract.pytesseract.tesseract_cmd = "C:\Program Files\Tesseract-OCR\\tesseract.exe"
    text = pytesseract.image_to_string(my_image)
    text = text.replace("K","000")
    text = text.replace("M", "000000")
    text = text.replace("@", "")
    text = text.replace(",", "")
    text = text.replace("®", "")
    print(text)
    try:
        number = int(text)
    except:
        number = 0

def main():
    clicker_points = {"monster":[1697,305],
                      "upgrade":[[1054,510],
                                 [1054,420],
                                 [1054,333],
                                 [1054,246]],
                      "next":[1836,86],
                      "next_l":[1737,86],
                      "upgrade_hero":[[1134,261],[1160,258],[1190,261],[1220,261]]}

    upgrade_time = time.time()
    next_level_upgrade_time = time.time()
    while not keyboard.is_pressed('q'):
        money_level()
        #print_position()
        #print([clicker_points["upgrade"][0][0],clicker_points["upgrade_hero"][0][1]])
        click(clicker_points["monster"])

        #img = pyautogui.screenshot(region=(973,0,1919,600))
        #img.getpixel((1134,261))

        #imm = pyautogui.screenshot() #nolasa screenshoutu un izdrukaa
        #ime = numpy.array(imm)
        #cv2.imshow("bilde",ime)
        #cv2.waitKey(0)

        #print(pyautogui.pixel(1134,249))
        #cv2.imshow(img)
        #cv2.waitKey(0)
        current_time = time.time()

        if current_time-upgrade_time>100:
            print("Upgrade")
            pyautogui.scroll(-400) #400 būs viena hero scrollam
            pyautogui.scroll(-400)
            pyautogui.scroll(-400)
            pyautogui.scroll(-400)
            for i in range(2):
                for upgrades in clicker_points["upgrade"]:
                    click(upgrades)
                    #print(upgrades[0])
                    for vieta in clicker_points["upgrade_hero"]:
                        #print(pyautogui.pixel(vieta[0],upgrades[1]))
                        if not (pyautogui.pixel(vieta[0],upgrades[1]-20)) == (57,216,14):
                            click([vieta[0],upgrades[1]+10])
                            #print("NAV")
                        else:
                            print("IR")

                pyautogui.scroll(400)  # 400 būs viena hero scrollam
                pyautogui.scroll(400)
                pyautogui.scroll(400)
                pyautogui.scroll(400)

            upgrade_time = time.time()

        if current_time-next_level_upgrade_time>10:
            print("next level")
            click(clicker_points["next_l"])
            next_level_upgrade_time = time.time()


main()