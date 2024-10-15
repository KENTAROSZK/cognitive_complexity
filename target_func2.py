def func(x: int) -> int:
    total = 0
    for i in range(x):
        if i % 2 == 0:
            for j in range(i):
                if j % 3 == 0:
                    total += j
                else:
                    total -= j
    return total


if __name__ == "__main__": # このifも複雑度としてカウントされてしまう点はオリジナルの複雑度カウントのクラスでの難点
    print(f"{func(x = 6)=}") # 結果は-1になる
    print(f"{func(x = 10)=}") # 結果は-20になる