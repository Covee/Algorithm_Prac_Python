# 모두의 알고리즘(길벗) / 문제 07

# 문제: 순차 탐색 (linear search)
# 주어진 리스트에 특정한 값이 있는지 찾아 그 위치를 돌려주는 알고리즘을 만들어 보세요.
# 리스트에 찾는 값이 없다면 -1을 돌려줍니다.

def find(nums, pick):
	for i in range(0, len(nums)):
		if nums[i] == pick:
			print(str(pick) + "의 위치는 " + str(i+1) + "번째 자리에 있습니다.")


n_list = list(map(int,input("리스트에 넣을 숫자들을 띄어쓰기로 구분해서 입력해 주세요: ").split(" ")))
pick = int(input("찾을 숫자를 입력해 주세요: "))

find(n_list, pick)



# comment: 리스트에 5개 자료가 있으면 최대 5번을 돌아서 찾는 방식. 100만개 있으면... 엄청 비효율적이라는것을 알 수 있다.
# 