# =============================================
# RSA Starter 1
# =============================================
print(pow(101, 17, 22663))

# =============================================
# RSA Starter 2
# =============================================
e = 65537
n = 17 * 23
message = 12
print(pow(message, e, n))


# =============================================
# RSA Starter 3
# =============================================
p = 857504083339712752489993810777
q = 1029224947942998075080348647219
print((p - 1) * (q - 1))

# =============================================
# RSA Starter 4
# =============================================
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    while a < 0:
        a += m
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m


p = 857504083339712752489993810777
q = 1029224947942998075080348647219

totient = (p - 1) * (q - 1)
e = 65537
secret_exp = modinv(e, totient)
print(secret_exp)

# =============================================
# RSA Starter 5
# =============================================
N = p*q
c = 77578995801157823671636298847186723593814843845525223303932
print(pow(c, secret_exp, N))

# =============================================
# RSA Starter 6
# =============================================
import hashlib
N = 15216583654836731327639981224133918855895948374072384050848479908982286890731769486609085918857664046075375253168955058743185664390273058074450390236774324903305663479046566232967297765731625328029814055635316002591227570271271445226094919864475407884459980489638001092788574811554149774028950310695112688723853763743238753349782508121985338746755237819373178699343135091783992299561827389745132880022259873387524273298850340648779897909381979714026837172003953221052431217940632552930880000919436507245150726543040714721553361063311954285289857582079880295199632757829525723874753306371990452491305564061051059885803
d = 11175901210643014262548222473449533091378848269490518850474399681690547281665059317155831692300453197335735728459259392366823302405685389586883670043744683993709123180805154631088513521456979317628012721881537154107239389466063136007337120599915456659758559300673444689263854921332185562706707573660658164991098457874495054854491474065039621922972671588299315846306069845169959451250821044417886630346229021305410340100401530146135418806544340908355106582089082980533651095594192031411679866134256418292249592135441145384466261279428795408721990564658703903787956958168449841491667690491585550160457893350536334242689
flag = b'crypto{Immut4ble_m3ssag1ng}'
h = hashlib.sha256(flag).hexdigest()
signature = pow(int(h, 16), d, N)
print(signature)