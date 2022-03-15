def maxArea(arr):

	area_init = 0

	for i in range(0,len(arr)):
		for j in range(1,len(arr)):

			area = min(arr[i],arr[j]) * abs(i - j)

			if area > area_init:

				area_init = area

	return area_init


def maxArea1(arr):

	area = 0

	for i in range(0, len(arr)):
		for j in range(i+1, len(arr)):

			area = max(area, min(arr[i], arr[j]) * abs(i - j))

			#if area > area_init:

			#	area_init = area

	return area

def maxArea2(arr):

	area = 0

	i = 0
	j = len(arr) - 1

	while i < j:

		print(i,arr[i],j,arr[j],abs(i-j),area)

		area = max(area, min(arr[i], arr[j]) * abs(i - j))

		if arr[i] < arr[j]:
			i = i + 1
		else:
			j = j - 1

		#print(i,j,area)

	return area


if __name__ == '__main__':

	height = [1,8,6,2,5,4,8,3,7]

	print(maxArea(height))
	print(maxArea1(height))
	print(maxArea2(height))
