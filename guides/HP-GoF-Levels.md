In ULUS10032 release of the game, in function starting at `0x089F031C`, register `a1` initially corresponds to level ID select. Allowed values:
```
0x00 - Intro sequence (CampsiteWoods)
0x01 - Tutorial indoors
0x02 - Tutorial indoors  (starry, potentially debug)
0x03 - Moody's Challenges (fight: "Dugbog Avifors")
0x04 - Moody's Challenges (boulders: "Leviation Challenge")
0x05 - Moody's Challenges (wall: "Exploding Cauldrons")
0x06 - Moody's Challenges (catapult: "Bubotuber Fling")
0x07 - Moody's Challenges (cubes: "Tower Blocks")
0x08 - Hogwarts Exterior (from menu)
0x09 - Forbidden Forest (first time "Escape" sequence)
0x0A - Forbidden Forest (ReEntrant)
0x0B - Triwizard Task 1: the Dragon (from menu)
0x0C - <<crash/blank screen>> (Originally it was PrefectsBathroom)
0x0D - <<crash/blank screen>> (Originally it was PrefectsBathroom_ReEntrant)
0x0E - Herbology (first time)
0x0F - Herbology (ReEntrant)
0x10 - Triwizard Task 2 - the Lake Underwater (from menu)
0x11 - Triwizard Task 3 - the Maze (from menu)
0x12 - Woldemort (from menu)
0x13 - Card-matching mini-game (against an animation)
0x14 - Card-matching mini-game (Concentration/Pairs)
0x15 - Mini-game - 360-degree defence
0x16 - Mini-game - Run through markers
0x17 - Mini Games Menu (main menu)
Higher values - rebounce to 0x17
```
