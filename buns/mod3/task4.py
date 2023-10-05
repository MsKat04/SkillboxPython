n = int(input("input number"))
if n <= 0:
    print("Неверный ввод")

hexs = "0123456789ABCDEF"
strbin, srtfol, mol = '', '', ''
n1,n2 = n,n

while n > 0:
    strbin = str(n % 2) + strbin
    n //= 2
while n1 > 0:
    srtfol = str(n1 % 8) + srtfol
    n1 //= 8
while n2 > 0:
    mol = hexs[n2 % 16] + mol
    n2 //= 16
print(strbin, srtfol, mol)

