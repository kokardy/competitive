import heapq 
def resolve(N,A,B,C,D):
    heap = [(0, N)]
    heapq.heapify(heap)

    footprint = set()

    while True: 
        cost, n = heapq.heappop(heap)
        if n == 0:
            return cost
        if n in footprint:
            continue
        footprint.add(n)

        h = (cost + D*n, 0)
        heapq.heappush(heap, h)

        two1 = n % 2
        two2 = 2 - two1
        h = (cost + D*two1 + A, (n -  two1) // 2)
        heapq.heappush(heap, h)
        if two1 != 0:
            h = (cost + D*two2 + A, (n +  two2) // 2)
            heapq.heappush(heap, h)

        three1 = n % 3
        three2 = 3 - three1
        h = (cost + D*three1 + B, (n - three1) // 3)
        heapq.heappush(heap, h)
        if three1 != 0:
            h = (cost + D*three2 + B, (n + three2) // 3)
            heapq.heappush(heap, h)

        five1 = n % 5
        five2 = 5 - five1
        h = (cost + D*five1 + C, (n - five1) // 5)
        heapq.heappush(heap, h)
        if five1 != 0:
            h = (cost + D*five2 + C, (n + five2) // 5)
            heapq.heappush(heap, h)

        



def main():
    T = int(input())
    for _ in range(T):
        NABCD = list(map(int, input().split()))
        ans = resolve(*NABCD)
        print(ans)
    pass

if __name__ == '__main__':
    main()