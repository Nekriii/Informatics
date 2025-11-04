numb = input("Введите набор из 7 цифр '0' и '1' ")
bits = [int(bit) for bit in numb]
r1, r2, i1, r3, i2, i3, i4 = bits
s1 = r1 ^ i1 ^ i2 ^ i4
s2 = r2 ^ i1 ^ i3 ^ i4
s3 = r3 ^ i2 ^ i3 ^ i4
error = s1 + s2*2 + s3*4
if error > 0:
    bits[error - 1] = 1 - bits[error - 1]
    inf = bits[2], bits[4], bits[5], bits[6]
    print('Информационные биты:', inf)
    print('Ошибка в позиции:', error)
else:
    inf1 = bits[2], bits[4], bits[5], bits[6]
    print('Информационные биты:', inf1)

