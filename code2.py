#code 2

# this is test for commit
# this is test for commit


def defmasraf(roz,masraf):
    masraf30roz = (masraf*30)//roz

    if masraf30roz >= 0:
        if masraf30roz <= 100:
            mab1 = 600 * masraf30roz
        else:
            mab1 = 100 * 600
    else:mab1 = 0

    if masraf30roz > 100:
        if masraf30roz <= 200:
            mab2 = 700 * (masraf30roz-100)
        else:
            mab2 = 100 * 700
    else:mab2 = 0

    if masraf30roz > 200:
        if masraf30roz <= 300:
            mab3 = 1500 * (masraf30roz-200)
        else:
            mab3 = 100 * 1500
    else:mab3 = 0

    mabkol = mab1+mab2+mab3
    mabkol = (mabkol/30)*roz
    return mabkol
    

def defend(mabkol):
    abonman = 22755
    avarez = 14867
    takhfif = 99568
    bime = 1933
    mab = mabkol+abonman+avarez+bime-takhfif
    return mab

roz = int(input("tedad rozhay masrafi: "))
masraf = int(input("masraf be KWH: "))

mabkol = defmasraf(roz,masraf)

mabpardakhti = defend(mabkol)

print("Mablagh pardakhti = ",int(mabpardakhti),"riyal")