#Script to automate the deletion of videos in youtube WatchLater

import time as t
import pyautogui as pg


#take amount of videos to delete from user
try:
  go = int(input("how many YT WatchLater videos are we talking about?: ")) + 1
except ValueError:
  print("Input only positive integers")
else:
  # script waits 10secs so you have the time to put your mouse at the initial position
  t.sleep(10)
  while go > 1:
    go -= 1
    pg.click()
    # move mouse below current position
    pg.moveTo(pg.position().x-100, pg.position().y+170)
    pg.click()
    # move mouse back to initial position
    pg.moveTo(pg.position().x+100, pg.position().y-170)
    t.sleep(5)
  
"""
    script can be used for other tasks asides deleting YT WatchLater by
    changing the positions or defining new mousse activities
"""