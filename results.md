Test 1,2,3,4 are all w/CF 12x12, fresh from sheafs (i.e. no re-used sheets)

Test 1 and 2:
1 if success
2 if failure

Test 1:
[1, 2, 1, 1, 2, 2, 2, 2, 2, 2, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 2, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 2, 1, 2, 2, 1, 1, 1]

Test 2
['1', '2', '1', '2', '1', '2', '2', '1', '1', '2', '1', '1', '2', '1', '1', '2', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '2', '1', '2', '1', '1', '1', '2', '1', '1', '2', '2', '1', '2', '1', '1', '1', '1', '2', '1', '2', '1']

Test 3, 4, 5, 6:
1 if success
2 if double pick
3 if mispick
4 if page damaged

Test 3
Results
['1', '1', '1', '1', '1', '1', '1', '1', '1', '2', '1', '4', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '2', '1', '1', '1', '1', '1', '1', '1', '2', '1']
Notes
- Nudger stopped working?! After re-powering the arduino, it started working again...

Test 4
Results
['1', '1', '1', '1', '2', '1', '1', '1', '1', '1', '4', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '2', '1', '4', '2', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '2', '4', '1', '1', '1', '1', '1', '1', '2', '1']
Notes
- I think that the stack gets easier to feed once it gets towards the bottom

Test 5
Results
['1', '1', '1', '1', '1', '1', '1', '1', '1', '2', '1', '3', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '2', '1', '1', '3', '1', '3', '3', '3', '3', '2', '4', '2', '2', '1', '2', '1', '1', '1', '2', '1', '1', '1', '3', '3', '1', '2', '2', '2']

Notes
- This used the really soft bad batch of 8x12 CF that DB gave me on 7/6
- Had to adjust the Z-height midway through the test (right around where all of the 3s are)...I really need a nudger activation sensor
- The double picks might actually just be incorrect programming as I didn't adjust the feed move, which might need to be less for 8x12 sheets...


Test 6
Results
['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '3', '1', '4', '1', '1', '3', '1', '1', '1', '1', '1', '1', '1', '3', '3', '3', '3', '1', '3', '3', '1', '4', '1', '4', '3', '1', '4', '2', '2', '1', '4', '3', '3', '3', '3']

Notes
- 12x12 Fiberglass slit cut
- Minor sheet damage occuring on retard roll, likely due to flimsiness of sheet and retard setting
- Static started being an issue where the sheets wouldn't exit the SAR fixture

Test 7

Results
['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '2', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '2', '1', '3', '1', '1', '3', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '2', '1', '1', '2', '1']

Notes
- 12x12 CF slit cut (fresh)
- Stack Height: roughly 250-300 sheets
- FAR motor speed: 10RPM
- First FAR implementation
- Some multi-feeds, but no slugs....

Test 8

Results
['1', '1', '2', '1', '4', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '2', '1', '1', '1', '2', '1', '2', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '3', '1', '1', '1', '1', '2', '2', '4', '1', '4', '1', '1', '1', '1']

Notes
- Same FAR setup as test #7
- 12x12 CF slit cut, reprocessed (by me) in an oven at 150C for roughly 20min...an attempt to get "worst case" sheets
- Sheets are from Test #7 of the sheet friction tests
- Main goal is to see how FAR works with separating slug heavy groups of sheets
- Did get slugs twice so....Fuck...maybe increase FAR motor speed


Test 9
Results
['1', '1', '2', '4', '1', '4', '1', '1', '4', '2', '4', '1', '1', '2', '4', '2', '2', '1', '4', '1', '1', '1', '1', '1', '1', '1', '1', '4', '1', '3', '1', '1', '1', '1', '1', '1', '3', '1', '1', '1', '1', '1', '1', '1', '1', '3', '3', '1', '1', '4']

Notes
- Increased FAR motor speed to 20RPM
- Same "worse case" 12x12 CF slit cut sheets (loaded in rough because they weren't lined up)
- Not a great performance


Test 10
Results
['1', '1', '1', '1', '4', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '3', '3', '3', '1', '3', '3', '3', '3', '3', '3', '3', '1', '3', '3', '3', '1', '3', '1', '1', '3', '1', '1', '4', '3', '3', '3', '1', '1']

Notes
- Removed FAR
- Changed a/L ratio to be closer to the desired 0.5 using the existing setup
- This was sort of hacked and meant that I had to manually perform the takeaway operation
- CF 12x12 slit-cut sheets of unknown origin, I think they were some "worst case" sheets
- Plenty of mis-picks but NOT A SINGLE MULTIFEED!!!!!!

Test 11

Results
['1', '3', '3', '3', '3', '1', '1', '1', '3', '3', '3', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '', '3', '', '3', '3', '3', '3', '3', '3', '1', '1', '1', '1', '1', '1']

Notes:
- 8-4-20
- First test with new a/L ratio
- Several set screws fell out of belt pulleys because pulleys are not spaced appropriately, this resulted in losing control of the wheels which caused a lot of misfeeds
- No double feeds
- Before running this test, there was a single large multifeed of a big slug...
- Sheets used in this test were "worse case" sheets
- Torque resistance set at 2.5

Test 12

Results
['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '2', '2', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '3', '1', '1', '1', '3', '1', '1', '1', '3', '1', '1', '1', '1', '1', '1', '3', '3', '1', '1', '1', '1', '3', '3', '3', '1', '1', '1', '1', '1', '1', '3', '1', '3', '3', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '3', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '2', '1', '1', '1', '3', '3', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '3', '3', '3', '1', '1', '1', '1', '1', '1', '1', '1', '1', '2', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '2', '2', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '2', '1', '1', '1', '1', '1', '1']

Notes
- 8/4/20
- Same setup as test 11
- Sheets used were standard CF sheets from the stockpile, 12x12
- Around sheet 100 I moved the Z-stage up a bit
- Some minor motor skipping by the takeaway roller...
- Around sheet 150 I moved the Z-stage up again
- Still got plenty of doubles, and a single triple pick...FUCK

Test 13
Results
['1', '1', '1', '2', '1', '1', '1', '3', '1', '2', '1', '1', '1', '1', '1', '3', '1', '3', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1']

Notes
- 8/4/20
- Same setup as test 12
- Same sheets as test 12
- It seems like all double sheets are separated (i.e. they are not welded together), which indicates that perhaps a FAR would actually work...or maybe just bigger wheels..

Test 14
Results
['1', '1', '1', '1', '1', '1', '1', '1', '1', '3', '1', '1', '3', '1', '1', '3', '3', '1', '1', '1', '1', '1', '4', '1', '1', '1', '1', '1', '1', '1', '1', '3', '1', '1', '1', '4', '1', '4', '1', '4', '3', '2', '2', '2', '4', '2', '1', '4', '1', '4']

Notes
- 8/4/20
- 12x12 Fiberglass slit cut
- The spate of double picks occurred after I over-raised the elevator

Test 15
Results
3 double sheet occurences in 26 feed operations

Notes
- 12x12 Fiberglass (maybe none of them are slit cut?)
- Had to raise the z-bed a little bit between sheet 9 and 10
- Sheet 21 was actually a triple feed, and interestingly there was no sheet stuck in the retard nip when that happened, indicating that the retard roll simply didn't stop any sheets from moving forward
- Sheet 25 was another triple pick, only this time it looks like there are sheets in the retard nip
- Sheet 26 was a big slug of sheets (4 all welded together). This slug was the last of the fiberglass sheets. The fiberglass sheets were sitting on top of some carbon fiber sheets, and it appears a carbon fiber sheet was the "low sheet" in the retard nip and allowed the entire fiberglass slug to move past. Trying to re-feed the slug and all of the sheets separated as expected



