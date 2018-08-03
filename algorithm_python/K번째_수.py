# 백준 / 11004
# 정답 비율: 29.41%

# 문제: K번째 수
# 수 N개 A1, A2, ..., AN이 주어진다. A를 오름차순 정렬했을 때, 앞에서부터 K번째 있는 수를 구하는 프로그램을 작성하시오.
# 첫째 줄에 N(1 ≤ N ≤ 5,000,000)과 K (1 ≤ K ≤ N)이 주어진다.
# 둘째에는 A1, A2, ..., AN이 주어진다. (-109 ≤ Ai ≤ 109)
# A를 정렬했을 때, 앞에서부터 K번째 있는 수를 출력한다.


def sorting(out, num_list):
	num_list.sort()
	print(num_list[out-1])


num = int(input("총 몇 개의 수를 정렬하시겠습니까?: "))
out = int(input("몇 번째 수를 출력하시겠습니까?: "))
num_list = list(map(int, input(str(num) + "개의 수를 띄어쓰기로 구분하여 차례로 입력해 주세요: ").split(" ")))

while len(num_list) != num:
	print("정확히 " + str(num) + "개를 입력해 주세요.")
	num_list = list(map(int, input(str(num) + "개의 수를 띄어쓰기로 구분하여 차례로 입력해 주세요: ").split(" ")))

sorting(out, num_list)


# comment: 정답 비율 낮은거 실화야..?
