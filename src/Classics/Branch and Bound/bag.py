class Table:
    def __init__(self, n: int, M: int, v: list, w: list):
        self.n = n
        self.M = M
        self.v = v
        self.w = w
        self.cs = self.calc_cs()
        self.ci = self.calc_ci()

    def calc_cs(self, ignore: int = -1) -> int:
        cs: int = 0
        w_total: int = 0
        for i in range(self.n):
            if i == ignore:
                continue
            w_total += self.w[i]
            if w_total <= self.M:
                cs += self.v[i]
        return -(cs)

    def calc_ci(self, ignore: int = -1) -> int:
        ci: int = 0
        w_total: int = 0
        for i in range(self.n):
            if i == ignore:
                continue
            ci += self.v[i]
            w_total += self.w[i]
            if w_total > self.M:
                return -int(ci - (w_total - self.M) * self.v[i] / self.w[i])
        return -(ci)

n = 4
M = 15
v = [10, 10, 12, 18]
w = [2, 4, 6, 9]

table = Table(n, M, v, w)

ans:list = []
def find_node(i):
    x1 = table.cs - table.ci
    x0 = table.calc_cs(i) - table.calc_ci(i)
    print(x1,x0)
    if x1 < x0 or x1 == x0: return True
    else:
        table.cs = table.calc_cs(i)
        table.ci = table.calc_ci(i)
        return False

for i in range (n):
    is_max = find_node(i)
    ans.append(is_max)

filtered_list = [i for (i, e) in zip(v, ans) if e]
print(filtered_list)