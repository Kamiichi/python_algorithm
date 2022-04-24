seireki = input('西暦年を入力してください：')
seireki = int(seireki)

def seireki2wareki(seireki: int):
    if (1867 > seireki) or (2023 <= seireki):
        print('1868~2022で入力してね')
    else:
        if seireki >= 1868 and seireki < 1912:
            meiji = seireki - 1867
            print('明治{0}年'.format(meiji))
        elif seireki >= 1912 and seireki < 1926:
            taisho = seireki - 1911
            print('大正{0}年'.format(taisho))
        elif seireki >= 1926 and seireki < 1989:
            showa = seireki - 1925
            print('昭和{0}年'.format(showa))
        elif seireki >= 1989 and seireki < 2019:
            heisei = seireki - 1988
            print('平成{0}年'.format(heisei))
        elif seireki >= 2019 and seireki < 2023:
            reiwa = seireki - 2018
            print('令和{0}年'.format(reiwa))

seireki2wareki(seireki)