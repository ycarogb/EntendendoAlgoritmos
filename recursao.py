def regressiva(i):
    if i < 0:
        return
    else:
        print(i)
        regressiva(i-1)

regressiva(5)