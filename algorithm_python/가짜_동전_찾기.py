# 모두의 알고리즘(길벗) / 문제 15-2

# 문제: 가짜 동전 찾기
# 겉보기에는 똑같은 동전이 n개 있습니다. 이 중에서 한 개는 싸고 가벼운 재료로 만들어진 가짜 동전입니다.
# 좌우 무게를 비교할 수 있는 양팔 저울을 이용해서 다른 동전보다 가벼운 가짜  동전을 찾아내는 알고리즘을 만들어 보세요.

import random


def weigh(a,b,c,d):
	if fake >= a and fake <= b:
		return -1
	if fake >= c and fake <= d:
		return 1
	
	return 0


def find_fakecoin(left, right):
	if left == right:	# 동전이 1개뿐이면 그게 가짜 동전이니 비교할 필요가 없다.
		return left

	half = (right - left + 1) // 2

	left_s1 = left
	right_s1 = left + half -1
	left_s2 = left + half
	right_s2 = left_s2 + right

	result = weigh(left_s1, right_s1, left_s2, right_s2)

	if result == -1:
		return find_fakecoin(left_s1, right_s1)
	elif result == 1:
		return find_fakecoin(left_s2, right_s2)
	else:
		return right


n = int(input("전체 동전 갯수를 입력하시오: "))

fake = random.randint(0, n) 	# 가짜 동전의 위치 임의로 설정

print("가짜 동전은 " + str(find_fakecoin(0, n-1)) + " 번째 동전이다.")


# comment: 