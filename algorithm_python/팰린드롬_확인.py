# 백준/10988
# 정답 비율: 67.67%

# 문제: 
# 알파벳 소문자로만 이루어진 단어가 주어진다. 이 때, 이 단어가 팰린드롬인지 아닌지 확인하는 프로그램을 작성하시오.
# 팰린드롬이란 앞으로 읽을 때와 거꾸로 읽을 때 똑같은 단어를 말한다. 
# level, noon은 팰린드롬이고, baekjoon, online, judge는 팰린드롬이 아니다.

# Q: 첫째 줄에 단어가 주어진다. 단어의 길이는 1보다 크거나 같고, 100보다 작거나 같으며, 알파벳 소문자로만 이루어져 있다.


# 팰린드롬 구별하는 함수 생성
def palindrome(request):
	word = list(request)

	for i in range(0, len(word)//2):
		if word[i] == word[len(word)-1-i]:
			continue
		else:
			return print(request + "는(은) 펠린드롬이 아닙니다.")

	return print(request + "는(은) 펠린드롬 입니다.")


# input 받아서 조건 걸어주고 output 마무리
typed_in = input("단어를 입력하세요.")

if len(typed_in) >= 1 and len(typed_in) <= 100:
	typed_in = typed_in.lower()		# 무조건 소문자로 변경해 준 후 함수에 넣음
	palindrome(typed_in)
else:
	print("warning (단어의 길이가 1보다 크거나 같고, 100보다 작거나 같아야 합니다.)")




# comment: 단어를 input 받아서 list에 넣은 후 비교해야 되는 사고를 해야 빠르게 문제 해결을 할 수 있음.