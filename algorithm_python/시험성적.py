# 백준/9498
# 정답 비율: 62.78%

# 문제: 시험 점수를 입력받아 90-100점은 A, 80-89점은 B, 70-79점은 C, 60-69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.

# Q: 시험 점수가 주어진다. 점수는 0보다 크거나 같고, 100보다 작거나 같은 자연수이다. 시험 성적을 출력한다.


typed_in = int(input('점수를 입력하세요: '))


if typed_in >= 90 and typed_in <= 100:
	print("A")
elif typed_in >= 80 and typed_in <= 89:
	print("B")
elif typed_in >= 70 and typed_in <= 79:
	print("C")
elif typed_in >= 60 and typed_in <= 69:
	print("D")
elif typed_in >= 0 and typed_in <= 59:
	print("F")




# comment: 문자열, int형 등의 type에서 error를 만났다.