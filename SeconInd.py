def second_index(text: str, symbol: str) -> int | None:
    text = text.replace(symbol, '', 1)
    print(text.index(symbol))
    return text.index(symbol) + 1


text = input()
symbol = ' '
print(second_index(text, symbol))