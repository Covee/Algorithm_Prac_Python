# 모두의 알고리즘(길벗) / 문제 15

# 문제: 친구의 친구 찾기
# 친구 관계를 이용하여 어떤 한 사람이 직접 또는 간접으로 아는 모든 친구를 출력하는 알고리즘을 만들어 보세요.


def all_friend(db, person):
	waiting = []
	done	= set() 	# 리스트와 달리 집합은 중복을 허용하지 않아 이미 처리한 사람은 여기 넣어서 중복을 방지한다.

	waiting.append(person)
	done.add(person)

	while waiting:
		p = waiting.pop(0)
		# print(p)
		for n in db[p]:
			if n not in done:
				waiting.append(n)
				done.add(n)

	done.remove(person) 	# 자기 자신은 최종 결과에서 지움.

	return done



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

print(str(person) + "는(은) " + str(all_friend(friend_db, person)) + "와 아는사이 입니다.")


# comment: 알고리즘 구현할 때, 일단 쭉 말로 설명 가능하게끔 글로 풀어서 과정을 적어보고 각 과정에 맞는 코드를 생각해보면 좋음.