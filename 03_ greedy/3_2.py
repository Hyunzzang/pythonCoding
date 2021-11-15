# [큰 수의 법칙]
# n는 배열 안의 데이터 총 수, m는 더해야할 개수, k는 가장 큰수 더해야할 수, data는 배열 안의 데이터 수

#n, m, k = map(int, input().split())
#data = list(map(int, input().split()))

m = 8
k = 3
data = [2, 4, 5, 4, 6]
n = len(data)

data.sort()
first = data[n - 1]
second = data[n - 2]

result = 0

# while True:
#     for i in range(k):
#         if m == 0:
#             break
#         result += first
#         m -= 1
#
#     if m == 0:
#         break
# 
#     result += second
#     m -= 1

# 가장 큰 수가 더해지는 횟수 계산
count = int(m / (k + 1)) * k
count += m % (k + 1)

result += count * first
result += (m - count) * second

print("result: ", result)
