def read_int():
    return int(input())

def read_ints():
    return map(int, input().split())

def read_lines(N):
    return [input() for i in range(N)]

def main():
    N, K = read_ints()
    towns = [int(t) -1  for t in input().split() ]
    #print(N, K , towns)

    loop = []
    loop_set = set()
    next_town = towns[0]
    while next_town not in loop_set:
        #print(f"next_t={next_town}")
        loop.append(next_town)
        loop_set.add(next_town)
        next_town = towns[next_town]

    i = loop.index(next_town)
    all_loop = loop
    pre_loop = loop[:i]
    loop = loop[i:]
    pre_length = len(pre_loop)
    loop_length = len(loop)

    """
    for k in range(1, 10):
        if k - 1  < len(all_loop):
            print(f"k={k}", all_loop[k-1] + 1)
        else:
            i = ((k -1 - len(pre_loop)) % loop_length)
            print(i, pre_loop, loop)
            print(f"k={k}", loop[i]+1)
    """

    #print(pre_loop, loop)
    if K - 1  < len(all_loop):
        print(all_loop[K-1] + 1)
    else:
        i = ((K -1 - pre_length) % loop_length)
        #print(i, pre_loop, loop)
        print(loop[i]+1)

if __name__ == '__main__':
    main()