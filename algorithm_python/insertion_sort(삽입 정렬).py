# 모두의 알고리즘(길벗) / 문제 09

# 문제: 삽입 정렬(insertion sort)
# 주어진 리스트 안의 자료를 작은 수부터 큰 수 순서로 배열하는 정렬 알고리즘을 만들어 보세요.


def i_sort(nums):
	for i in range(1, len(nums)):
		val = nums[i]
		j = i-1
		while j >= 0 and nums[j] > val:
			nums[j+1] = nums[j]
			nums[j] = val
			j = j-1

	print("정렬을 마쳤습니다! " + str(nums))


n_list = list(map(int,input("리스트에 넣을 숫자들을 띄어쓰기로 구분해서 입력해 주세요: ").split(" ")))

i_sort(n_list)


# comment: 처음 구현 해봐서 엄청 많이 헤맸다. 예를 들어 놓고 하나씩 맞춰가면서 코드 작성을 하면 좀 도움이 되는 것 같다.
# 