import numpy as np
import cv2
from PIL import ImageGrab
import pyautogui
import time
import pynput
from pynput.keyboard import Key, Controller
# from finder import boostposition



def boostposition(rocketleague):
  keyboard = Controller()
  carxpos = 960
  carypos = 700
  boostimg = cv2.imread('Boost1.jpg', cv2.IMREAD_UNCHANGED)
  
  boostImgGray = cv2.cvtColor(boostimg, cv2.COLOR_BGR2HSV)
  
  result  = cv2.matchTemplate(rocketleague, boostImgGray, cv2.TM_CCOEFF_NORMED)
  threshold = 0.1
  locations = np.where(result >= threshold)
  newlocations = list(zip(*locations[::-1]))
  firstboost = newlocations[0:1]
  lastboost = newlocations[-2:-1]
 
  firstxcord = []
  firstycord = []
  lastxcord = []
  lastycord = []

  # Puts x and y cords in a seperate list
  for i in firstboost:
    firstxcord.append(i[0])
    firstycord.append(i[1])
  for i in lastboost:
    lastxcord.append(i[0])
    lastycord.append(i[1])

  boost_w = boostimg.shape[1]
  boost_h = boostimg.shape[0]
  line_color = (0,255,0)
  line_type = cv2.LINE_4
  
  for i in firstboost:
    topleft = i
    bottom_right = (firstxcord[0] + boost_w, firstycord[0] + boost_h)
    cv2.rectangle(rocketleague,topleft, bottom_right,line_color, 2)
  for i in lastboost:
    topleft = i 
    bottom_right = (lastxcord[0] + boost_w, lastycord[0] + boost_h)
    cv2.rectangle(rocketleague,topleft, bottom_right,line_color, 2)
  try:
    if carxpos > firstxcord[0]:
      pyautogui.keyDown('a')
      pyautogui.keyUp('a')
    if carxpos < firstxcord[0]:
      pyautogui.keyDown('d')
      pyautogui.keyUp('d')
  except:
    print("no boost")

  pyautogui.keyDown('w')

  cv2.rectangle(rocketleague,(900,700),(1025,850), line_color,2 )
  cv2.imshow('Matches', rocketleague)

def get_screenshot():
  line_color = (0,255,0)
  img = ImageGrab.grab(bbox=(0, 0, 1920, 1080)) #x, y, w, h #1617, 640

  screenshot = np.array(img)

  lowerLimit=np.array([255,255,116])
  upperLimit=np.array([255,255,160])
  mask = cv2.inRange(screenshot,lowerLimit,upperLimit)

  res = cv2.bitwise_and(screenshot,screenshot,mask = mask)
  
  return res
  
while(True):
  boostposition(get_screenshot())
  if cv2.waitKey(1) == ord('q'):
    cv2.destroyAllWindows()
    break




  













            




























