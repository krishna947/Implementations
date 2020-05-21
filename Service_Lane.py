n,t = map(int, input().split())
arr = list(map(int, input().split()))
for _ in range(t):
    i,j = map(int, input().split())
    large_vehicle = min(arr[i:j+1])
    print(large_vehicle)
