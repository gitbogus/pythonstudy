# aabcccccaaa 를 a2b1c5a3형식으로 만들기
def  str_compression(s):
    count, last = 1, ""
    list_aux = []
    for i, c in enumerate(s):
        if last == c:
            count += 1
        else:
            if i != 0:
                list_aux.append(str(count))
            list_aux.append(c)
            count = 1
            last = c
        list_aux.append(str(count))
        return "".join(list_aux)

if __name__ == "__main__":3
    result = str_compression("aabccccaaa")
    print(result)