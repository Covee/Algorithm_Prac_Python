# 백준 / 4344
# 정답 비율: 39.78%

# 문제: 평균은 넘겠지
# 대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다. 당신은 그들에게 슬픈 진실을 알려줘야 한다.ㅋㅋㅋ 잔혹한 현실을 알려주자
# 첫째 줄에는 테스트케이스의 개수 C가 주어진다.
# 둘째 줄부터 각 테스트케이스마다 학생의 수 N(1 ≤ N ≤ 10, N은 정수)이 첫 수로 주어지고, 이어서 N명의 점수가 주어진다.
# 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.
# 각 케이스마다 한 줄씩 평균을 넘는 학생들의 비율을 반올림하여 소수점 셋째자리까지 출력한다.


points = list(map(int, input("(최대 10명)각 학생들의 점수를 띄어쓰기로 구분하여 입력해 주세요: ").split(" ")))
length = len(points)
tot = 0

def higher(points, length, avg):
	high = 0
	for i in range(0, length):
		if points[i] >= avg:
			high += 1

	rate = round(((high / length) * 100), 2)
	print(str(length) + "명의 평균 점수는 " + str(avg) + "점이고, 평균 점수를 넘는 학생의 비율은 " + str(rate) + "% 입니다.")


if length < 1 or length > 10:
	print("학생의 점수 갯수가 충분하지 않거나, 10개 보다 많습니다.")
else:
	for i in range(0, length):
		if points[i] < 0 or points[i] > 100:
			print("범위를 벗어났습니다: (" + str(points[i]) + "점)" + " 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수여야 합니다.")
			exit()
		else:
			tot += points[i]

	avg = round((tot / length), 2)
	higher(points, length, avg)


# comment: 먼저 input의 조건을 걸어 주고, 이후에 함수 실행으로 값을 도출한다.





