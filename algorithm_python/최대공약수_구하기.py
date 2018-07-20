# 모두의 알고리즘(길벗) / 문제 05

# 문제: 두 자연수 a와 b의 최대공약수를 구하는 알고리즘을 만들어 보세요.

def GCD(nums):
	sm = min(nums)
	big = max(nums)

	if big % sm == 0 and sm % sm == 0:
		print("입력하신 " + str(nums) + "의 최대공약수는 " + str(sm) + " 입니다.")
	else:
		for i in range(1, sm):
			if sm % (sm-i) == 0 and big % (sm-i) == 0:
				print("<1번째 함수> 입력하신 " + str(nums) + "의 최대공약수는 " + str(sm-i) + " 입니다.")
				break
			

def GCD_2(nums):
	sm = min(nums)
	big = max(nums)
	v = sm

	while True:
		if big % v == 0 and sm % v == 0:
			print("<2번째 함수> 입력하신 " + str(nums) + "의 최대공약수는 " + str(v) + " 입니다.")
			return v
		v = v-1
		

def GCD_3(nums):	# 유클리드 알고리즘
	sm = min(nums)
	big = max(nums)

	def GCD_4(sm, big):
		if big == 0:
			print("<3번째 함수> 입력하신 " + str(nums) + "의 최대공약수는 " + str(sm) + " 입니다.")
			exit()	# exit는 아예 파이썬 실행 자체를 다 종료함. 그래서 바로 윗줄까지 출력 후, global 명령이라 할지라도 밑에 이어지는 명령은 실행 하지 않고 종료함.
		return GCD_4(big, sm % big)

	GCD_4(sm, big)


typed_in = list(map(int, input("최대공약수를 구할 두 수를 띄어쓰기로 구분하여 입력해 주세요: ").split(" ")))

GCD(typed_in)
GCD_2(typed_in)
GCD_3(typed_in)


# comment: 
# 엄청 많이 헤멨다. 변수를 충분히 많이 만들어도 괜찮다고 생각한다.
# 조건문에서 사칙연산 주의하자.(이거때매 에러 못찾아서 헤맴)
# 재귀함수를 잘 이해하면 정말 간단하게 3번째 함수처럼 구현 가능함.
 