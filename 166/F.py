from functools import reduce

class ABC:
    def __init__(self, A,B,C, cmds):
        self.current = dict(A=A,B=B,C=C)
        self.selected = []
        self.cmds = cmds
        self.answer = None

    def inc(self, X):
        self.current[X] += 1
    
    def dec(self, X):
        self.current[X] -= 1
    
    def select(self, X, Y):
        self.inc(X)
        self.dec(Y)
        self.selected.append(X)
        #print("select", X, "current", self.current)
    
    def get(self, X):
        return self.current[X]
    
    def abc(self):
        return sum(self.current.values())

    def run_commands(self):
        cmds = self.cmds
        for i, cmd in enumerate(cmds):
            if sum([self.get(c) for c in cmd]) == 0:
                self.answer = "No"
                return
            
            elif self.get(cmd[0]) ==  self.get(cmd[1]) == 1:
                another = (set("ABC") - set(cmd)).pop()
                if self.get(another) == 0 and i < len(cmds) -1:
                    next_cmds = cmd[i+1:]
                    for j, next_cmd in enumerate(next_cmds):
                        if next_cmd == cmd:
                            continue
                        else:
                            X = (set(cmd) & set(next_cmd)).pop()
                            XX = (set(cmd) - set([X])).pop()
                            if j % 2 == 0:
                                self.select(X, XX)
                            else:
                                self.select(XX, X)

                else:
                    self.select(cmd[0], cmd[1])
            else:
                small, big = sorted(cmd, key=lambda key: self.get(key))
                self.select(small, big)

            if list(map(lambda x: x < 0, self.current.values())).count(True) > 0:
                self.answer = "No"
                return
                
        self.answer = "Yes"

    def print_answer(self):
        print(self.answer)
        if self.answer == 'Yes':
            print("\n".join(self.selected))

def test():
    A,B,C = 2, 3, 4
    import numpy as np
    XX = ["AB", "BC", "CA"]
    cmds = [XX[i] for i in np.random.randint(0,3, [10])]

    resolver = ABC(A,B,C, cmds)
    resolver.run_commands()
    print(resolver.selected)
    print(resolver.current)
    resolver.print_answer()

    A,B,C = 1, 1, 0
    cmds = ["AB", "AB", "AB", "BC"]
    resolver = ABC(A,B,C, cmds)
    resolver.run_commands()
    print(resolver.selected)
    print(resolver.current)
    resolver.print_answer()

    A,B,C = 1, 1, 0
    cmds = ["AB", "AB", "BC"]
    resolver = ABC(A,B,C, cmds)
    resolver.run_commands()
    print(resolver.selected)
    print(resolver.current)
    resolver.print_answer()

    A,B,C = 1, 0, 0
    cmds = ["AB", "AB", "BC"]
    resolver = ABC(A,B,C, cmds)
    resolver.run_commands()
    print(resolver.selected)
    print(resolver.current)
    resolver.print_answer()

def main():

    test()

    N, A ,B, C = map(int, input().split())
    S = [input() for i in range(N)]
    
    resolver = ABC(A,B,C, S)
    resolver.run_commands()
    resolver.print_answer()



if __name__ == '__main__':
    main()