nilai = 55
# bisa mengunakan == or is
# bisa mengunakan != or is not
# di python 3.8 sudah tidak bisa mengunakan is
if nilai == 75:
    print('nilai anda adalah: ', nilai)

if nilai != 60:
    print('nilai anda adalah: ', nilai)

# tanda { } di ganti menjadi : hanya di python

print(100*"~")
nilai = 90
if 80 <= nilai <= 100:
    print('nilai anda adalah A')
elif 70 <= nilai <= 100:
    print('nilai anda adalah B')
elif 60 <= nilai <= 100:
    print('nilai anda adalah C')
elif 50 <= nilai <= 100:
    print('nilai anda adalah E')
else:
    print('anda tidak lulus, silakan mengulang matakuliah tersebut!')

print(100*'=')

data = 'viky ganteng' .split()
print(data)

viky = [1,2,3,4,5]
print(viky())