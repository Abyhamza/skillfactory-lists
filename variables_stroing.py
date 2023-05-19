def encode(in_str):
    # Создаем переменную result чтобы сахранять в нее наш конечный результат
    result = ""
    # Создаем переменную LastChar чтобы хранить последний символ
    lastChar = None
    # Создаем переменную counter чтобы считать количество поторений символа
    counter = 0
    # Создаем цикл for который включает символ (char) в строке (in_str)
    for char in in_str:
        # Если последний символ(LastСhar) не равен нынешней(char) и последний символ(LastChar) не равен None
        if lastChar != char and lastChar != None:
            # В результат (result) предыдущего символа (LestChar)добавляем счетчик(counter)
            result += f"{lastChar}{counter}"
            # В счетчик (counter) присваиваем значение один
            counter = 1
            # В предыдущий символ(LestChar) присваиваем значение нынешего символа (char)
            lastChar = char
        else:
            # В счетчик (counter) добавляем значение при каждом цикле
            counter += 1
            # В предыдущий символ(LestChar) присваиваем значение нынешего символа (char)
            lastChar = char
    return result


test_in_1 =  "aaabbbbaaabbcccddddd"
test_out_1 = "a3b4a3b2c3d5"
test_result_1 = encode(test_in_1)
print(f"{test_in_1} => {test_out_1} == {test_result_1} is {test_out_1 is test_result_1}")

test_in_2 =  "jjjjkkkkaaaaasss"
test_out_2 = "j4k4a5s3"
test_result_2 = encode(test_in_2)
print(f"{test_in_2} => {test_out_2} == {test_result_2} is {test_out_2 is test_result_2}")
