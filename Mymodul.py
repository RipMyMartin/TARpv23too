def Summa(arv1:int,arv2:int,arv3=0) -> int:
    """ Funktsioon tagastab kolme arvu summa
        Summa(arv1,arv2,arv3)
    :param int arv1: Arv1 Sisestab kasutaja
    :param int arv2: Arv2 Sisestab kasutaja
    :param int arv3: Vaikimisi arv3 võrdub nulliga
    :rtype: int
    """

    s=arv1+arv2+arv3
    return s
def IntKontroll():

    def arithmetic(x: int, y: int, op:str) -> float:
        """ Funktsioon tagastab kolme arvu summa
            arithmetic(x, y, op)
        :param int x: x sisestab kasutaja
        :param int y: y sisestab kasutaja
        :param str op: str sisestab kasutaja
        :rtype: int
        """
        if op == "+":
            return x + y
        if op == "-":
            return x - y
        if op == "*":
            return (x * y)
        if op == "/":
            if y == 0:
                print("jagamine nulliga ei ole võimalik")
            else:
                print("tundmatu toiming")
#
#
#
#
def liigaasta(aasta:int)->bool:
    """ funktsioon loeb kas on liigasta voi ei
    liigaasta(aasta:int)
    :param int aasta: aasta sisestab kasutaja
    :rtype: bool
    """
    if aasta % 4 == 0 and aasta % 100!=0:
        return True
    else:
        return False

# 3
import math

def square(ruudukülg:float)->tuple:
    """ funktsioon tagastab kolm väärtusi(umbermoot,pindala,diagonaal)
    square(ruudukülg:float)
    :param float ruudukülg: ruudu_külg sisestab kasutaja
    :rtype: tuple
    """


    umbermoot = 4 * ruudukülg
    pindala = ruudukülg ** 2
    diagonaal = ruudukülg * math.sqrt(2)
    return umbermoot, pindala, diagonaal


def season(a:int)->str:
    """funktsioon tagastab hooaega nimetusi(talv, kevad, suvi,sügis)
    season(a:int)
    param int a: kuut sisestab kasutaja
    return: str
    """

    while True:
        if a>0 and a<13:
            break
        else:
            try:
                a=int(input("Ainult 1-12!\n  sisesta veel kord number: "))
            except:
                print("viga andmetüübiga")
    if a==12 or a==1 or a==2:
        s="talv"
    elif a>2 and a<6:
        s="kevad"
    elif a in range (6,9,1):
        s="suvi"
    elif 9<=a<=11:
        s="sugis"
    return s


def is_prime(arv:int)->bool:
    """funktsioon tagastab arvu(0,1000) kas ta on lihtne voi ei
    is_prime(arv:int)
    param int arv:arvu sisestab kasutaja
    rtype:bool
    """

    y = 0
    for i in range(1, arv + 1):
        if arv % i == 0:
            y += 1
    if y > 2:
        return False
    else:
        return True






def date(paev:int,kuu:int,aasta:int)->bool:
        """funktsioon tagastab true kui kuu paev on kalendris(paev,kuu,aasta)
        date(paev:int,kuu:int,aasta:int)
        :param int paev: paeva sisestab kasutaja
        :param int kuu: kuu sisestab kasutaja
        :param int aasta: aasta sisestab kasutaja
        return:bool
        """

        paeva_in_kuu = {1: 31,
                        2: 29 if liigaasta(aasta) else 28,
                        3: 31,
                        4: 30,
                        5: 31,
                        6: 30,
                        7: 31,
                        8: 31,
                        9: 30,
                        10: 31,
                        11: 30,
                        12: 31}

        if 1 <= kuu <= 12 and 1 <= paev <= paeva_in_kuu[kuu]:
            return True
        else:
            return False


def pank(a:float,aasta:int)->bool:
    """funktsioon tagastab summat mis on kontos kasutajal(a,aasta)
    pank(a:float,aasta:int)
    :param float a: a sisestab kasutaja
    :param int aasta: aasta sisestab kasutaja
    rtype:any
    """
    for i in range(aasta):
        a *= 1.1
    return a



