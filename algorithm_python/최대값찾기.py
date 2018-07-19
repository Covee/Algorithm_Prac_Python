# 모두의 알고리즘(길벗) / 문제 02

# 문제: 
# 주어진 숫자 중 가장 큰 숫자를 찾는 알고리즘을 만들어 보세요. (최대값 찾기)


n = list(map(int,input("비교할 숫자들을 띄어쓰기로 구분해서 입력해 주세요: ").split(" ")))

def compare(n):
	keep = n[0]
	for i in range(len(n)):
		if n[i] > keep:
			keep = n[i]

	print("입력한 숫자들 중 최대값은 " + str(keep) + "입니다.")

compare(n)


# comment: for문의 범위와 input을 여러개 받는 map함수를 잘 기억하고 있어야 한다.
# 