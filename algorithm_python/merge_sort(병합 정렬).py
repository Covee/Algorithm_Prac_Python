# 모두의 알고리즘(길벗) / 문제 10

# 문제: 병합 정렬(merge sort)
# 주어진 리스트 안의 자료를 작은 수부터 큰 수 순서로 배열하는 정렬 알고리즘을 만들어 보세요.


def m_sort(nums):
	if len(nums) <= 1: 			# 종료 조건: 리스트에 1개 이하의 수가 있을 경우, sorting이 필요 없다.
		return nums

	mid = len(nums) // 2			# 주어진 리스트의 중간 index를 찾음
	line_1 = m_sort(nums[:mid]) 	# 재귀호출!!! 반 나눈 리스트를 계속 반씩 나누어서, 결국 정렬이 됨
	line_2 = m_sort(nums[mid:])
	result = []

	while line_1 and line_2:
		if line_1[0] >= line_2[0]:
			result.append(line_2.pop(0))
		else:
			result.append(line_1.pop(0))

	while line_1: 								# 두 라인을 비교하다가 한 라인이 먼저 다 사라지면, 나머지 라인이 사라질때 까지 다 result에 넣음
		result.append(line_1.pop(0))
	while line_2:
		result.append(line_2.pop(0))
	return result


n_list = list(map(int,input("리스트에 넣을 숫자들을 띄어쓰기로 구분해서 입력해 주세요: ").split(" ")))

print("정렬을 마쳤습니다! " + str(m_sort(n_list)))


# comment: 재귀함수를 제대로 이해해야 recursion error 안만난다...ㅠㅠ 꼭 탈출조건 정확해야함.
# 