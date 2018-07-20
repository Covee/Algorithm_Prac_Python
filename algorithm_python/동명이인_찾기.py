# 모두의 알고리즘(길벗) / 문제 03

# 문제: 
# n명의 사람 이름 중에서 같은 이름을 찾아 집합으로 만들어 돌려주는 알고리즘을 만들어 보세요.

names = list(map(str, input("사람 이름을 콤마로 구분하여 적어 주세요: ").split(",")))

def same_name(names):
	same = set()
	for i in range(0, len(names)):
		for j in range(i+1, len(names)):
			if names[i] == names[j]:
				same.add(names[j])

	print("같은 이름은 " + str(same) + " 입니다.")

same_name(names)


# comment: 집합 자료형의 특징을 잘 이해해야 한다. 집합 자료형은 중복을 허용하지 않는다. 순서도 없다.
# 