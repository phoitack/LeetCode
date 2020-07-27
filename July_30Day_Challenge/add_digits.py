def addDigits(num):

	nums = list(str(num))

	while len(nums) > 1:

		total = sum(map(lambda x: int(x), nums))

		nums = list(str(total))

	return(int(nums[0]))


anum = 38

print(addDigits(anum))