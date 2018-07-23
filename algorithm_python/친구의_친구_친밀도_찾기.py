# 모두의 알고리즘(길벗) / 문제 15-2

# 문제: 친구의 친구를 찾고 친밀도 찾기(응용)
# 친구 관계를 이용하여 어떤 한 사람이 직접 또는 간접으로 아는 모든 친구를 출력하는 알고리즘을 만들어 보세요.
# 관계간 친밀도도 같이 표시합니다.(가까울수록 1, 2, 3, n... 이런식으로)


def all_friend(db, person):
	waiting = [] 		# 이제 처리할 사람들 리스트
	done	= set() 	# 리스트와 달리 집합은 중복을 허용하지 않아 이미 처리한 사람은 여기 넣어서 중복을 방지한다.
	
	waiting.append((person, 0))
	done.add(person)

	print(str(person) + "의 친구들은, \n-------------------")

	while waiting:
		(p, luv) = waiting.pop(0) 	# 처리할 리스트의 첫번째 친구와 친밀도를 꺼냄.
		if not (p, luv) == (person, 0): 	# 자기 자신은 최종 결과에서 지움.
			print(str(p)+ " ("+ str(luv) + "촌)")
		# result.add((p, luv)) 		# print할 최종 결과를 튜플로 저장한다.
		for n in db[p]:
			if n not in done:
				waiting.append((n, luv+1))
				done.add(n)

	print("-------------------\n입니다.")



friend_db = {
	"spring": ['winter','top'],
	"summer": ['top', 'cobee', 'fall'],
	"fall": ['summer', 'cobee'],
	"winter": ['spring',],
	"cobee": ['summer','fall'],
	"top": ['spring','summer',],
	"trash": ['yeah'],
	"yeah": ['trash'],
}

person = input("누구의 모든 친구를 알고싶나요? ")
all_friend(friend_db, person)


# comment: 알고리즘 구현할 때, 일단 쭉 말로 설명 가능하게끔 글로 풀어서 과정을 적어보고 각 과정에 맞는 코드를 생각해보면 좋음.