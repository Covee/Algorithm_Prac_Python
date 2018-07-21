# 모두의 알고리즘(길벗) / 문제 11

# 문제: 퀵 정렬(quicksort)
# 주어진 리스트 안의 자료를 작은 수부터 큰 수 순서로 배열하는 정렬 알고리즘을 만들어 보세요.


def q_sort_sub(nums, start, end):
	if end - start <= 0: return nums

	base = nums[end]
	i = start

	for j in range(start, end):
		if nums[j] <= base:
			nums[i], nums[j] = nums[j], nums[i]
			i += 1

	nums[i], nums[end] = nums[end], nums[i]

	q_sort_sub(nums, start, i-1)
	q_sort_sub(nums, i+1, end)

def q_sort(nums):
	q_sort_sub(nums, 0, len(nums)-1)


n_list = list(map(int,input("리스트에 넣을 숫자들을 띄어쓰기로 구분해서 입력해 주세요: ").split(" ")))
q_sort(n_list)
print("퀵정렬을 마쳤습니다! " + str(n_list))

# comment: 정말 정말 헷갈림... 잘 확인하고 또 확인하자....ㅠㅠ 헷갈려...
# 