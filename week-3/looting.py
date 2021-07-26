n, W = map(int, input().split())
w = []
vpw = []
mxv = 0
for _ in range(n):
    vx, wx = map(int, input().split())
    w.append(wx)
    vpw.append(vx/wx)

for _ in range(n):
    mx = 0
    if W > 0:
        for i in range(1, n):
            if vpw[i] > vpw[mx]:
                mx = i
        if W >= w[mx]:
            W -= w[mx]
            mxv += w[mx] * vpw[mx]
            vpw[mx] = 0
        else:
            mxv += W * vpw[mx]
            W = 0
            break
print("{:.4f}".format(round(mxv, 4)))
