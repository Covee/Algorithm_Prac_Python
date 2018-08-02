# 백준 / 9093
# 정답 비율: 45.02%

# 문제: 단어 뒤집기
# 문장이 주어졌을 때, 단어를 모두 뒤집어서 출력하는 프로그램을 작성하시오. 단, 단어의 순서는 바꿀 수 없다. 단어는 영어 알파벳으로만 이루어져 있다.
# 단어의 길이는 최대 20, 문장의 길이는 최대 100이다. 단어와 단어 사이에는 공백이 하나 있다.

import sys


def reversing(sentence, ch):
	for i in range(0, len(ch)):
		dh = list(ch[i])
		dh.reverse()
		for j in range(0, len(dh)):
			print(dh[j], end="")
		print(end=" ")
	print()


sentence = input("뒤집어서 출력할 문장을 입력하세요(단어는 20자 이내, 문장은 최대 100자): ")
ch = list(sentence.split())

if sentence.isdigit() == True:	 # isdigit() 함수는 string이 오직 숫자인지(True) 아닌지(False) 확인해준다. 
	print("숫자만 입력할 수 없습니다.")
elif len(sentence) > 100:
	print("문장의 길이는 0~100자여야 합니다.")
else:
	for i in range(0, len(ch)):
		if len(ch[i]) > 20:
			print("각 단어의 길이는 0~20자여야 합니다.")
			sys.exit()
	reversing(sentence, ch)


# comment: 엄청 간단할 줄 알았는데, 문장과 단어, 즉 2번을 각각 나눴다가 합쳐서 출력해주어야 하고, 여러 조건들도 좀 까다로워서 효율을 잘 생각해서 풀어야 할듯하다.
