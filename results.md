Test 1,2,3,4 are all w/CF 12x12, fresh from sheafs (i.e. no re-used sheets)

Test 1 and 2:
1 if success
2 if failure

Test 1
======
Results
-------
[1, 2, 1, 1, 2, 2, 2, 2, 2, 2, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 2, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 2, 1, 2, 2, 1, 1, 1]

Test 2
======
Results
-------
['1', '2', '1', '2', '1', '2', '2', '1', '1', '2', '1', '1', '2', '1', '1', '2', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '2', '1', '2', '1', '1', '1', '2', '1', '1', '2', '2', '1', '2', '1', '1', '1', '1', '2', '1', '2', '1']

Test 3, 4, 5, 6:
1 if success
2 if double pick
3 if mispick
4 if page damaged

Test 3
======
Results
-------
['1', '1', '1', '1', '1', '1', '1', '1', '1', '2', '1', '4', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '2', '1', '1', '1', '1', '1', '1', '1', '2', '1']
Successful picks: 46 (92%)
Multifeeds: 3 (6%)
Misfeeds: 0 (0%)
Damaged sheets: 1 (2%)
Total sheets: 50

Notes
-----
- Nudger stopped working?! After re-powering the arduino, it started working again...

Test 4
======
Results
-------
['1', '1', '1', '1', '2', '1', '1', '1', '1', '1', '4', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '2', '1', '4', '2', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '2', '4', '1', '1', '1', '1', '1', '1', '2', '1']
Successful picks: 42 (84%)
Multifeeds: 5 (10%)
Misfeeds: 0 (0%)
Damaged sheets: 3 (6%)
Total sheets: 50

Notes
-----
- I think that the stack gets easier to feed once it gets towards the bottom

Test 5
======
Results
-------
['1', '1', '1', '1', '1', '1', '1', '1', '1', '2', '1', '3', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '2', '1', '1', '3', '1', '3', '3', '3', '3', '2', '4', '2', '2', '1', '2', '1', '1', '1', '2', '1', '1', '1', '3', '3', '1', '2', '2', '2']

Successful picks: 31 (62%)
Multifeeds: 10 (20%)
Misfeeds: 8 (16%)
Damaged sheets: 1 (2%)
Total sheets: 50

Notes
-----
- This used the really soft bad batch of 8x12 CF that DB gave me on 7/6
- Had to adjust the Z-height midway through the test (right around where all of the 3s are)...I really need a nudger activation sensor
- The double picks might actually just be incorrect programming as I didn't adjust the feed move, which might need to be less for 8x12 sheets...


Test 6
======
Results
-------
['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '3', '1', '4', '1', '1', '3', '1', '1', '1', '1', '1', '1', '1', '3', '3', '3', '3', '1', '3', '3', '1', '4', '1', '4', '3', '1', '4', '2', '2', '1', '4', '3', '3', '3', '3']

Successful picks: 30 (60%)
Multifeeds: 2 (4%)
Misfeeds: 13 (26%)
Damaged sheets: 5 (10%)
Total sheets: 50

Notes
-----
- 12x12 Fiberglass slit cut
- Minor sheet damage occuring on retard roll, likely due to flimsiness of sheet and retard setting
- Static started being an issue where the sheets wouldn't exit the SAR fixture

Test 7
======
Results
-------
['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '2', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '2', '1', '3', '1', '1', '3', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '2', '1', '1', '2', '1']

Successful picks: 44 (88%)
Multifeeds: 4 (8%)
Misfeeds: 2 (4%)
Damaged sheets: 0 (0%)
Total sheets: 50

Notes
-----
- 12x12 CF slit cut (fresh)
- First FAR implementation
- Stack Height: roughly 250-300 sheets
- FAR motor speed: 10RPM
- Some multi-feeds, but no slugs....

Test 8
======
Results
-------
['1', '1', '2', '1', '4', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '2', '1', '1', '1', '2', '1', '2', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '3', '1', '1', '1', '1', '2', '2', '4', '1', '4', '1', '1', '1', '1']

Successful picks: 40 (80%)
Multifeeds: 6 (12%)
Misfeeds: 1 (2%)
Damaged sheets: 3 (6%)
Total sheets: 50

Notes
-----
- Same FAR setup as test #7
- 12x12 CF slit cut, reprocessed (by me) in an oven at 150C for roughly 20min...an attempt to get "worst case" sheets
- Sheets are from Test #7 of the sheet friction tests
- Main goal is to see how FAR works with separating slug heavy groups of sheets
- Did get slugs twice so....Fuck...maybe increase FAR motor speed


Test 9
======
Results
-------
['1', '1', '2', '4', '1', '4', '1', '1', '4', '2', '4', '1', '1', '2', '4', '2', '2', '1', '4', '1', '1', '1', '1', '1', '1', '1', '1', '4', '1', '3', '1', '1', '1', '1', '1', '1', '3', '1', '1', '1', '1', '1', '1', '1', '1', '3', '3', '1', '1', '4']

Successful picks: 33 (66%)
Multifeeds: 5 (10%)
Misfeeds: 4 (8%)
Damaged sheets: 8 (16%)
Total sheets: 50

Notes
-----
- Increased FAR motor speed to 20RPM
- Same "worse case" 12x12 CF slit cut sheets (loaded in rough because they weren't lined up)
- Not a great performance


Test 10
=======
Results
-------
['1', '1', '1', '1', '4', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '3', '3', '3', '1', '3', '3', '3', '3', '3', '3', '3', '1', '3', '3', '3', '1', '3', '1', '1', '3', '1', '1', '4', '3', '3', '3', '1', '1']

Successful picks: 30 (60%)
Multifeeds: 0 (0%)
Misfeeds: 18 (36%)
Damaged sheets: 2 (4%)
Total sheets: 50

Notes
-----
- Removed FAR
- Changed a/L ratio to be closer to the desired 0.5 using the existing setup
- This was sort of hacked and meant that I had to manually perform the takeaway operation
- CF 12x12 slit-cut sheets of unknown origin, I think they were some "worst case" sheets
- Plenty of mis-picks but NOT A SINGLE MULTIFEED!!!!!!

Test 11
=======
Results
-------
['1', '3', '3', '3', '3', '1', '1', '1', '3', '3', '3', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '', '3', '', '3', '3', '3', '3', '3', '3', '1', '1', '1', '1', '1', '1']

Successful picks: 24 (48%)
Multifeeds: 0 (0%)
Misfeeds: 24 (48%)
Damaged sheets: 0 (0%)
Total sheets: 50

Notes
-----
- 8-4-20
- First test with new a/L ratio
- Several set screws fell out of belt pulleys because pulleys are not spaced appropriately, this resulted in losing control of the wheels which caused a lot of misfeeds
- No double feeds
- Before running this test, there was a single large multifeed of a big slug...
- Sheets used in this test were "worse case" sheets
- Torque resistance set at 2.5

Test 12
=======
Results
-------
['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '2', '2', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '3', '1', '1', '1', '3', '1', '1', '1', '3', '1', '1', '1', '1', '1', '1', '3', '3', '1', '1', '1', '1', '3', '3', '3', '1', '1', '1', '1', '1', '1', '3', '1', '3', '3', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '3', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '2', '1', '1', '1', '3', '3', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '3', '3', '3', '1', '1', '1', '1', '1', '1', '1', '1', '1', '2', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '2', '2', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '2', '1', '1', '1', '1', '1', '1']

Successful picks: 176 (88%)
Multifeeds: 7 (4%)
Misfeeds: 17 (8%)
Damaged sheets: 0 (0%)
Total sheets: 200

Notes
-----
- 8/4/20
- Same setup as test 11
- Sheets used were standard CF sheets from the stockpile, 12x12
- Around sheet 100 I moved the Z-stage up a bit
- Some minor motor skipping by the takeaway roller...
- Around sheet 150 I moved the Z-stage up again
- Still got plenty of doubles, and a single triple pick...FUCK

Test 13
=======
Results
-------
['1', '1', '1', '2', '1', '1', '1', '3', '1', '2', '1', '1', '1', '1', '1', '3', '1', '3', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1']

Successful picks: 25 (83%)
Multifeeds: 2 (7%)
Misfeeds: 3 (10%)
Damaged sheets: 0 (0%)
Total sheets: 30

Notes
-----
- 8/4/20
- Same setup as test 12
- Same sheets as test 12
- It seems like all double sheets are separated (i.e. they are not welded together), which indicates that perhaps a FAR would actually work...or maybe just bigger wheels..

Test 14
=======
Results
-------
['1', '1', '1', '1', '1', '1', '1', '1', '1', '3', '1', '1', '3', '1', '1', '3', '3', '1', '1', '1', '1', '1', '4', '1', '1', '1', '1', '1', '1', '1', '1', '3', '1', '1', '1', '4', '1', '4', '1', '4', '3', '2', '2', '2', '4', '2', '1', '4', '1', '4']

Successful picks: 33 (66%)
Multifeeds: 4 (8%)
Misfeeds: 6 (12%)
Damaged sheets: 7 (14%)
Total sheets: 50

Notes
-----
- 8/4/20
- 12x12 Fiberglass slit cut
- The spate of double picks occurred after I over-raised the elevator

Test 15
=======
Results
-------
3 double sheet occurences in 26 feed operations

Notes
-----
- 12x12 Fiberglass (maybe none of them are slit cut?)
- Had to raise the z-bed a little bit between sheet 9 and 10
- Sheet 21 was actually a triple feed, and interestingly there was no sheet stuck in the retard nip when that happened, indicating that the retard roll simply didn't stop any sheets from moving forward
- Sheet 25 was another triple pick, only this time it looks like there are sheets in the retard nip
- Sheet 26 was a big slug of sheets (4 all welded together). This slug was the last of the fiberglass sheets. The fiberglass sheets were sitting on top of some carbon fiber sheets, and it appears a carbon fiber sheet was the "low sheet" in the retard nip and allowed the entire fiberglass slug to move past. Trying to re-feed the slug and all of the sheets separated as expected

Test 16
=======
Results
-------
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,1,1,1,1,3,1,1,1,1,1,3,2,3,1,3,1,1,2,3,3,1,3,1,1,1,1,1,1,3,1,1,3,2,2,3,3]

Successful picks: 62 (79%)
Multifeeds: 4 (5%)
Misfeeds: 12 (15%)
Damaged sheets: 0 (0%)
Total sheets: 78

Notes
-----
- 8/7/20
- 12x12 CF sheets, standard processing
- ~400 CF sheets loaded in the elevator
- Interesting to watch the sheet "ramp" up after the retard roll...likely due to the roll geometry. is this good or bad? Can't say for sure
- Noticeable event for first multifeed: there was no sheet already in the retard nip, the previous pick was a misfeed. Additionally, after this multifeed, there were no remaining sheets in the retard nip, so this shows a failure case where there werent 3+ sheets in the nip, this was an instance where 2 out of 2 sheets made it through the retard nip..the sheets were slightly separated, but otherwise were together
- Same thing happened on next multifeed
- First 3 multifeeds all seem to have the same kind of appearance: 2 sheets that do not appear welded together and in fact have L/E's that are separate by 0.5". But they stay together through the retard nip (see picture on phone)
- Random software failure...
- Double sheets may have been a result of retard clutch slipping because of a loose pulley?....fuck

Test 17
=======
Results
-------
N/A


Notes
-----
- Picking pu where test 16 left off
- Adjusted sheet/sheet elevator raise from 0.04 to 0.041
- Re-raised elevator
- Retard roll stopped functioning

Test 18
=======
Results
-------
 ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '3', '1', '1', '1', '1', '3', '1', '3', '1', '1', '1', '1', '3', '1', '1', '1', '3', '1', '1', '3', '1', '1', '1', '1', '3', '1', '1', '1', '3', '1', '1', '1', '1', '3', '1', '1', '1', '1', '1', '1', '1', '1', '1', '3', '1', '3', '1', '1', '1', '1', '1', '1', '1', '1', '3', '1', '1', '3', '1', '1', '3', '3', '1', '1', '1', '1', '1', '1', '3', '1', '1', '3', '1', '1', '3', '1', '1', '3', '1', '1', '3', '1', '1', '1']

Successful picks: 80 (80%)
Multifeeds: 0 (0%)
Misfeeds: 20 (20%)
Damaged sheets: 0 (0%)
Total sheets: 100

Notes
-----
- Continued from Test 17
- Tightened pulley screws
- Hardcore motor stall on feed #52

Test 19
=======
Results
-------
['3', '1', '1', '1', '1', '3', '1', '1', '3', '1', '1', '3', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '2', '1', '1', '1', '2', '1', '1', '1', '1', '1', '1', '1', '3', '1', '1', '3', '3', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '3', '3', '3', '3', '1', '3', '1', '1', '1', '1', '1', '1', '1', '3', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '3', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1']

Successful picks: 84 (84%)
Multifeeds: 2 (2%)
Misfeeds: 14 (14%)
Damaged sheets: 0 (0%)
Total sheets: 100

Notes
-----
- Continued straight from Test 18
- Adjusted sheet/sheet elevator raise from 0.041 to 0.043
- First double pick occurred and it appears multiple sheets are in the retard nip
