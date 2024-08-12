# "Why is everyone so obsessed with multiplying two primes for RSA. Why not just use one?"
from Crypto.Util.number import long_to_bytes

# Given numbers:
n = 171731371218065444125482536302245915415603318380280392385291836472299752747934607246477508507827284075763910264995326010251268493630501989810855418416643352631102434317900028697993224868629935657273062472544675693365930943308086634291936846505861203914449338007760990051788980485462592823446469606824421932591                                                                  
e = 65537
ct = 161367550346730604451454756189028938964941280347662098798775466019463375610700074840105776873791605070092554650190486030367121011578171525759600774739890458414593857709994072516290998135846956596662071379067305011746842247628316996977338024343628757374524136260758515864509435302781735938531030576289086798942  

# The totient of N is easy to calculate as n is prime:
totient_of_n = n - 1

# ... making it easy to calculate the private exponent and decrypt:
d = pow(e, -1, totient_of_n)
plaintext = pow(ct, d, n)

print(long_to_bytes(plaintext))
