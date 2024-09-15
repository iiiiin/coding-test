# 1928
# Base64 Decoder

T = int(input())
for test_case in range(1,T+1):
    encoded = input()
    decoded = ""
    for s in range(len(encoded)):
        if encoded[s].isupper():
            decoded += str(format((ord(encoded[s]) - 65), '06b'))
        elif encoded[s].islower():
            decoded +=  str(format((ord(encoded[s]) - 71), '06b'))
        elif encoded[s].isdigit():
            decoded +=  str(format((ord(encoded[s]) + 4), '06b'))
        elif encoded[s] == "+":
            decoded +=  str(format(62, '06b'))
        elif encoded[s] == "/":
            decoded +=  str(format(63, '06b'))
    result = []
    for j in range(0,len(decoded),8):
        result.append(chr(int(decoded[j:j+8], 2)))

    print("#"+str(test_case)+" "+"".join(result))