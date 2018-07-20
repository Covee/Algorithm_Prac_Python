# 모두의 알고리즘(길벗) / 문제 08

# 문제: 선택 정렬(selection sort)
# 주어진 리스트 안의 자료를 작은 수부터 큰 수 순서로 배열하는 정렬 알고리즘을 만들어 보세요.


def s_sort(nums):
	for i in range(0, len(nums)-1):
		for j in range(i+1, len(nums)):
			if nums[i] > nums[j]:
				nums[i], nums[j] = nums[j], nums[i] 	# 이렇게 하면 두 리스트 안의 값이 뒤바뀐다.

	print("작은 수 순서대로: " + str(nums))


n_list = list(map(int,input("리스트에 넣을 숫자들을 띄어쓰기로 구분해서 입력해 주세요: ").split(" ")))

s_sort(n_list)

# comment:
# 시간 복잡도가 n제곱2 라서 크기가 커질수록 시간이 오래걸린다. 
# 