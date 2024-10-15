def func(x: int) -> str:
    if x > 0:
        if x < 10:
            if x % 2 == 0:
                if x == 4:
                    return "x is 4"
                else:
                    return "x is even"
            else:
                return "x is odd"
    return "x is negative or zero"


if __name__ == "__main__": # このifも複雑度としてカウントされてしまう点はオリジナルの複雑度カウントのクラスでの難点
    print(f"{func(x = 3)=}") # 奇数の時
    print(f"{func(x = 4)=}") # 4の時
    print(f"{func(x = 6)=}") # 偶数の時
