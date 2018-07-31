# 백준 / 11721
# 정답 비율: 51.61%

# 문제: 5개씩 끊어서 출력
# 알파벳 소문자와 대문자로만 이루어진 길이가 N인 단어가 주어진다.
# 한 줄에 5글자씩 끊어서 출력하는 프로그램을 작성하시오.

word = list(input("출력할 문장을 입력하세요: "))

for i in range(0, len(word)):
	if i % 5 == 4:
		print(word[i])
	else:
		print(word[i], end="")
print("")


# comment: 고정관념에 갇혀있으면 풀기 힘든 문제.
