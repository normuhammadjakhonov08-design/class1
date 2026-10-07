# 1. Salom berish
def salom():
    print("Salom!")


# 2. Ism bilan salomlashish
def salom_ber(ism):
    print(f"Salom, {ism}!")


# 3. Ikki sonni qo‘shish
def qoshish(a, b):
    return a + b


# 4. Ikki sonni ayirish
def ayirish(a, b):
    return a - b


# 5. Ikki sonni ko‘paytirish
def kopaytirish(a, b):
    return a * b


# 6. Ikki sonni bo‘lish
def bolish(a, b):
    return a / b


# 7. Sonning kvadrati
def kvadrat(a):
    return a ** 2


# 8. Sonning kubi
def kub(a):
    return a ** 3


# 9. Juft sonni tekshirish
def juftmi(a):
    return a % 2 == 0


# 10. Musbat sonni tekshirish
def musbatmi(a):
    return a > 0


# 11. Ikki sondan kattasini topish
def katta(a, b):
    return max(a, b)


# 12. Ikki sondan kichigini topish
def kichik(a, b):
    return min(a, b)


# 13. Uchta sonning o‘rtachasini topish
def ortacha(a, b, c):
    return (a + b + c) / 3


# 14. To‘g‘ri to‘rtburchak yuzi
def tortburchak_yuzi(a, b):
    return a * b


# 15. To‘g‘ri to‘rtburchak perimetri
def tortburchak_perimetri(a, b):
    return 2 * (a + b)


# 16. Doira yuzini hisoblash
def doira_yuzi(r):
    return 3.14 * r ** 2


# 17. So‘z uzunligini topish
def uzunlik(soz):
    return len(soz)


# 18. Matnni katta harflarga o‘tkazish
def katta_harf(matn):
    return matn.upper()


# 19. Ro‘yxatdagi sonlar yig‘indisi
def yigindi(sonlar):
    return sum(sonlar)


# 20. Ro‘yxatdagi eng katta son
def eng_katta(sonlar):
    return max(sonlar)

    # 1. Odam
class Odam:
    def __init__(self, ism, yosh):
        self.ism = ism
        self.yosh = yosh



    #   Class uchun

# 2. Talaba
class Talaba:
    def __init__(self, ism, kurs):
        self.ism = ism
        self.kurs = kurs


# 3. Mashina
class Mashina:
    def __init__(self, marka, rang):
        self.marka = marka
        self.rang = rang


# 4. Kitob
class Kitob:
    def __init__(self, nomi, muallif):
        self.nomi = nomi
        self.muallif = muallif


# 5. Telefon
class Telefon:
    def __init__(self, model, narx):
        self.model = model
        self.narx = narx


# 6. Uy
class Uy:
    def __init__(self, manzil, xonalar):
        self.manzil = manzil
        self.xonalar = xonalar


# 7. Kompyuter
class Kompyuter:
    def __init__(self, model, ram):
        self.model = model
        self.ram = ram


# 8. Hayvon
class Hayvon:
    def __init__(self, nomi, turi):
        self.nomi = nomi
        self.turi = turi


# 9. Bank hisob
class BankHisob:
    def __init__(self, egasi, balans):
        self.egasi = egasi
        self.balans = balans


# 10. Mahsulot
class Mahsulot:
    def __init__(self, nomi, narx):
        self.nomi = nomi
        self.narx = narx