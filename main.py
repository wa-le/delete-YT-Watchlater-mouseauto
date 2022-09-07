import time as t
import pyautogui as pg

try:
  go = int(input("how many YT WatchLater videos are we talking about?: ")) + 1
except ValueError:
  print("Input only positive integers")
else:
  t.sleep(10)
  while go > 1:
    go -= 1
    pg.click()
    pg.moveTo(pg.position().x-100, pg.position().y+170)
    pg.click()
    pg.moveTo(pg.position().x+100, pg.position().y-170)
    t.sleep(5)
  