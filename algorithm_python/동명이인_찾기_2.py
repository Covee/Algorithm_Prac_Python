# 모두의 알고리즘(길벗) / 문제 14

# 문제: 동명이인 찾기(dictionary 이용)
# n명의 사람 이름 중에 같은 이름을 찾아 집합으로 만들어 돌려주는 알고리즘을 만들어 보세요.


def same_name(names):
	box = {}

	for name in names:
		if name in box:
			box[name] += 1
		else:
			box[name] = 1

	result = set()
	for name in box:
		if box[name] >= 2:
			result.add(name)

	return result
	

names = list(map(str,input("리스트에 넣을 이름들을 띄어쓰기로 구분해서 순서대로 입력해 주세요: ").split(" ")))
# print(same_name(names))

print("같은 이름은 " + str(same_name(names)) + " 입니다.")

# comment: 
# 