alphabet = [
    ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')'],
    ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
    ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ':'],
    ['Z', 'X', 'C', 'V', 'B', 'N', 'M', '<', '>', '?'],
]

def getResult(symbol, k):
    # 查找符號 S 在 alphabet 中的位置
    for row in range(len(alphabet)):
        for col in range(len(alphabet[row])):
            if alphabet[row][col] == symbol:
                # 根據 k 的值決定輸出的方向
                if k == 1 and row > 0:  # 向上
                    return alphabet[row - 1][col]
                elif k == 2 and row < len(alphabet) - 1:
                    return alphabet[row + 1][col]
                elif k == 3 and col < len(alphabet[row]) - 1:
                    return alphabet[row][col + 1]
                elif k == 4 and col > 0:
                    return alphabet[row][col - 1]
                else:
                    return "" 
    return None

N = int(input("次數: "))
for _ in range(N):
    S = input("符號: ")
    K = int(input("方向: "))

    result = getResult(S, K)
    print({result})
    print()