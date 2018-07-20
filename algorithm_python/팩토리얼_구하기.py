# 모두의 알고리즘(길벗) / 문제 04

# 문제: 1부터 n까지 연속한 정수의 곱을 구하시오.(팩토리얼 만들기, 재귀)

def factorial(n):
	result = 1
	for i in range(1, n+1):
		result = i*result

	print("입력하신 " + str(n) + "의 팩토리얼은 " + str(result) + " 입니다.")


def factorial_2(n):
	if n <= 1:
		return 1
	return n * factorial_2(n-1)		# 재귀 함수를 씀.


n = int(input("팩토리얼 값을 구할 숫자를 입력하세요: "))

factorial(n)
print("2번째 팩토리얼 함수 값은 " + str(factorial_2(n)) + " 입니다.")


# comment: 재귀 함수의 기본 이해가 필요해 보인다. 1번 함수와 2번 함수 같은 기능을 한다.
# 