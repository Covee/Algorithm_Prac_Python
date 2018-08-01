# 백준 / 10947
# 정답 비율: 3.83%

# 문제: 로또 만들기
# 1보다 크거나 같고, 45보다 작거나 같은 수 6개를 출력한다. 채점 프로그램은 랜덤으로 이용해서 '수 6개와, 보너스 숫자 하나'를 구한다.
# 채점 프로그램이 구한 숫자와 6개와 번호가 모두 일치하면 100점을 받는다.
# 5개의 번호가 일치하고, 일치하지 않는 숫자가 보너스 숫자와 일치하면 80점을 받는다.
# 5개의 번호가 일치하면 60점을 받는다. 4개의 번호가 일치하면 40점을 받는다. 3개의 번호가 일치하면 20점을 받는다.
# 그 외의 경우에는 틀렸습니다를 받는다.

import random


def lotto(my_pick, bonus):
	lottolist = []
	lottobonus = []
	
	for i in range(0, 6):
		pick = random.randint(1, 45)
		while pick in lottolist:		# 리스트 안에 중복되는 수가 존재하면 다시 랜덤 돌려서, 중복 없을때까지 돌린 후 빠져나오는 조건.
			pick = random.randint(1, 45)
		lottolist.append(pick)

	pick = random.randint(1, 45)	# 다시 보너스 숫자 한개 추첨(역시 중복 방지)
	while pick in lottobonus:
		pick = random.randint(1, 45)
	lottobonus.append(pick)

	lottolist.sort()
	my_pick.sort()

	# 프로그램이 잘 돌아가는지 체크해 볼 예제 (왜냐하면 로또 1등 당첨이 잘 돌아가는지 확인하려면 1등 당첨이 되야하니까...)
	# lottolist = [1, 2, 3, 4, 5, 30]
	# lottobonus = [7]

	print("추첨 번호: " + str(lottolist) + " / 보너스 번호" + str(lottobonus))
	print("입력 번호: " + str(my_pick) + " / 보너스 번호" + str(bonus))

	if my_pick == lottolist:
		print("숫자 6개가 모두 일치하여 100점 입니다.")
	else:
		count = 0
		for i in range(0, 6):
			for j in range(0, 6):
				if my_pick[i] == lottolist[j]:
					count += 1			
		if count == 5:
			if bonus == lottobonus:
				print("숫자 5개가 일치하고 보너스 숫자가 일치하여 80점 입니다.")
			else:
				print("숫자 5개가 일치하여 60점 입니다.")
		elif count == 4:
			print("숫자 4개가 일치하여 40점 입니다.")
		elif count == 3:
			print("숫자 3개가 일치하여 30점 입니다.")
		elif count == 2:
			print("숫자 2개가 일치하여 20점 입니다.")
		elif count <= 1:
			print("'도박하시면 망할 팔자시네여!'")


my_pick = list(map(int, input("숫자 1-45 사이의 6개 로또 번호를 띄어쓰기로 구분해서 입력해 주세요(아니면 오류 잘남): ").split(" ")))
bonus = list(map(int, input("보너스 번호를 입력해 주세요: ")))
lotto(my_pick, bonus)


# comment: 
# 간단할 줄 알았는데 생각보다 손이 많이가고, while문으로 중복되는 수를 거르고 돌리는 개념 자체를 이해하는데 헤맬 수 있는 문제였다.
# 그리고 입력에 제한을 두는 것(6개 로또번호 입력해야데 7개 혹은 5개 입력한다던지, 번호가 1-45 사이가 아닌 수가 입력되었다던지)은 코딩하지 않았다. 넘 귀찮..
# 다음에 기회되면 그건 넣겠다. if문으로 조건만 걸어주고 똑같이 my_pick 안에 같은수가 입력되면 오류를 뱉는 것만 써주면 되서 어렵지 않을거다.
# 로또를 해본 적이 없어서 약간 헷갈렸다. 그럴 수 있당

