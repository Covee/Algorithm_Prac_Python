# 백준 / 1929
# 정답 비율: 29.64%

# 문제: 소수 구하기
# 첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 100,000)
# M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.

# (1번째 방식)
# def prime_number(num):
# 	count = 0
# 	for i in range (2, num):
# 		if num % i == 0:
# 			count += 1

# 	if count == 0:
# 		return num


# def result(m, n):
# 	plist = []

# 	for i in range(m, n+1):
# 		if prime_number(i) == None:
# 			pass
# 		else:
# 			plist.append(prime_number(i))

# 	print(str(m) + ", " + str(n) + " 사이의 소수는 " + str(plist) + " 입니다.")


# (2번째 방식)
def result(m, n):
	plist = list(range(2, n+1))

	for i in range(2, n+1):
		# if i == 1:
		# 	plist.remove(1)
		# 	i += 1

		j = 2
		while i*j <= n:
			if i*j in plist:
				plist.remove(i*j)
			j += 1

	while m not in plist:
		m += 1
	order = plist.index(m)
	mlist = plist[order:]
	

	print(len(mlist)) 	# 숫자가 커질수록 모든 소수를 프린트해내서 어지러워서... len 함수로 몇개인지만 프린트 되게끔 함
	# print(len(plist))







m = int(input("<< 작은수 m과 큰수 n 사이의 숫자들이 소수인지 판별하겠습니다 >>\n먼저 m을 입력하세요: "))
while m < 1 or m > 100000:
	print("m은 0보다 크고 100,000보다 작아야 합니다.")
	m = int(input("<< 작은수 m과 큰수 n 사이의 숫자들이 소수인지 판별하겠습니다 >>\n먼저 m을 입력하세요: "))

n = int(input("n을 입력하세요: "))
while n <= m or n > 100000:
	print("n은 처음 입력한 m보다 크고 100,000보다 같거나 작아야 합니다.")
	n = int(input("n을 입력하세요: "))

result(m, n)



# comment: 처음 했던 방식은 시간 복잡도가 너무 좋지 않음.. 따라서 2번째는 '에라스토테네스의 체' 라는 방식을 이용해서 만들어봄.
# 그 결과, 더 빠르긴 한데 여전히 10000개가 넘어가는 순간부터 느리고, 100000개 단위부터는 아예 거의 멈춤.
# 효율적인 방법을 더 연구해 봐야 할 것 같다.

