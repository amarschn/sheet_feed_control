def collate(results):
	success = 0
	multifeed = 0
	misfeed = 0
	damage = 0
	total = len(results)
	for i in results:
		if i == 1 or i is '1':
			success+=1
		elif i == 2 or i is '2':
			multifeed +=1
		elif i == 3 or i is '3':
			misfeed += 1
		elif i == 4 or i is '4':
			damage += 1

	print("Successful picks: {} ({:.0f}%)".format(success, success/total * 100))
	print("Multifeeds: {} ({:.0f}%)".format(multifeed, multifeed/total * 100))
	print("Misfeeds: {} ({:.0f}%)".format(misfeed, misfeed/total * 100))
	print("Damaged sheets: {} ({:.0f}%)".format(damage, damage/total * 100))
	print("Total sheets: {}".format(len(results)))

collate(['3', '1', '1', '1', '1', '3', '1', '1', '3', '1', '1', '3', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '2', '1', '1', '1', '2', '1', '1', '1', '1', '1', '1', '1', '3', '1', '1', '3', '3', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '3', '3', '3', '3', '1', '3', '1', '1', '1', '1', '1', '1', '1', '3', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '3', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'])