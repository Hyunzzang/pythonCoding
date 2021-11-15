# [거스름돈] 거슬러 줘야 할 동전의 최소 개수 구하기

# 거스름돈
n = 1260
# 거스름돈 개수
count = 0

coin_type_list = [500, 100, 50, 10]

for coin in coin_type_list:
    count += n // coin
    n %= coin


print("답: ", count)