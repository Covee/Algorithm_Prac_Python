# 모두의 알고리즘(길벗) / 문제 01

# 문제: 
# 1부터 n까지 연속된 정수의 합을 구하는 알고리즘을 만들어 보세요.


def nsum(n):
	total = 0
	for i in range(0, n+1):
		total = i + total

	print("1부터 n까지의 합은 " + str(total) + "입니다.")


def nsum_2(n):
	total = n * (n + 1) // 2

	print("(2번째 방법)1부터 n까지의 합은 " + str(total) + "입니다.")


typed_in = int(input("n값을 입력하세요: "))

nsum(typed_in)
nsum_2(typed_in)


# comment:
# n까지의 합을 구하는 방법은 크게 두가지다. 두 번째 방법이 좀 더 나은 알고리즘이라고 할 수 있다.
# 첫 번째 방법은 시간복잡도 O(n)이고, 두 번째 방법은 O(1)이므로 무조건 2번째 방법을 써야 효율적이다.