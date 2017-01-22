#!venv/bin/python

import time


def main():
    max_n = 0
    max_repeat = 0
    for i in range(1, 1000):
        mods = []
        if i < 10:
            j = 10
            while j % i not in mods:
                if j % i == 0: break
                if j < i:
                    j *= 10
                    continue
                mods.append(j%i)
                j = (j - i*(j/i))*10
            if mods and (j%i in mods):
                repeat = len(mods) - mods.index(j%i)
                if repeat > max_repeat:
                    max_repeat = repeat
                    max_n = i
        if i >= 10 and i < 100:
            j = 100
            while j % i not in mods:
                if j % i == 0: break
                if j < i:
                    j *= 10
                    continue
                mods.append(j%i)
                j = (j - i*(j/i))*10
            if mods and (j%i in mods):
                repeat = len(mods) - mods.index(j%i)
                if repeat > max_repeat:
                    max_repeat = repeat
                    max_n = i
        if i >= 100 and i < 1000:
            j = 1000
            while j % i not in mods:
                if j % i == 0: break
                if j < i:
                    j *= 10
                    continue
                mods.append(j%i)
                j = (j - i*(j/i))*10
            if mods and (j%i in mods):
                repeat = len(mods) - mods.index(j%i)
                if repeat > max_repeat:
                    max_repeat = repeat
                    max_n = i
    print max_n

if __name__ == '__main__':
	start = time.time()
	main()
	print 'Program runtime: {0:.3f}s'.format(time.time() - start)
