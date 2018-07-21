# 모두의 알고리즘(길벗) / 문제 12

# 문제: 이분 탐색(binary search)
# 자료가 크기 순서대로 정렬된 리스트에서 특정한 값이 있는지 찾아 그 위치를 돌려주는 알고리즘을 만들어 보세요.
# 리스트에 찾는 값이 없으면 -1을 돌려줍니다.


def b_search(nums, x):
	
	start = 0
	end = len(nums)-1

	while start <= end:
		mid = (start + end) // 2
		if x == nums[mid]:
			return mid
		elif x > nums[mid]:
			start = mid + 1
		else:
			end = mid - 1

	return print("-1") 	# 찾는 값이 없으면 리턴함
	

n_list = list(map(int,input("리스트에 넣을 숫자들을 띄어쓰기로 구분해서 순서대로 입력해 주세요: ").split(" ")))
x = int(input("찾을 숫자를 입력해 주세요: "))

print("찾으시는 숫자 " + str(x) + "는 리스트 " + str(b_search(n_list, x)+1) + "번째에 있습니다.")

# comment: 이분탐색은 정렬이 되어있는 리스트에서 사용하는 방법임.
# 