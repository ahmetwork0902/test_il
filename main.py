f = open('test_dir/24.txt')
s = f.readline()
l = 0
maxi = 0
pos = []
for i in range(len(s)):
    if s[i] == 'T':
        pos.append(i)
for i in range(101, len(pos)):
    l = pos[i] - pos[i-101] - 1
    maxi = max(maxi, l)
print(maxi)
