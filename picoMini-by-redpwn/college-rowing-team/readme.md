# college-rowing-team

> I just joined my college's rowing team! To make a good first impression, I started sending my teammates positive automated messages every day. I even send them flags from time to time!

Have a look at the given program: we get all the ciphertexts, but we don't know which ciphertext corresponds to which plaintext. The chinese remainder theorem would probably do the trick: I think the name of the challenge is a hint at the CRT too. However, I tried my usual tools `factordb.com` and [`RsaCtfTool`](https://github.com/RsaCtfTool/RsaCtfTool) first.

I had some luck as it seems like I chose the right ciphertext immediately, and `RsaCtfTool` did the trick:

```
~/c/RsaCtfTool ❯❯❯ python3 RsaCtfTool.py -n 19928073532667002674271126242460424264678302463110874370548818138542019092428748404842979311103440183470341730391245
8204613605819892718048874580518526134352048570980172492550069515817906503295707214613112768976250642690976112969947522782361165940185651115117064681139957405552
2772357933378082513394748845683400639111367471904546831724200047820904823726212598316484480893820693353176523038698721112596824602672191661003498130638527639637
1953013685639581894384852327010462345466019070637326891690322855254242653309376909918630162231006323084408189767751387637751885504520154800908122596020421247199
812233589471220112129 -e 3 --uncipher 86893891006724995283854813014390877172735163869036169496565461737741926829273252426484138905500712279566881578262823696620
4158649165906515577110359828106902273777845254662657769226252541358969664729057766137223708711076408191405916270405924028675044493393635591080904521417531944771
74987394954897424151839006206598186417617292433784471465084923195909989 

private argument is not set, the private key will not be displayed, even if recovered.

[*] Testing key /var/folders/98/68wgw4r51hxd99kggk87t6lw0000gn/T/tmpywhsn5sj.
attack initialized...
attack initialized...
[*] Performing lucas_gcd attack on /var/folders/98/68wgw4r51hxd99kggk87t6lw0000gn/T/tmpywhsn5sj.
100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 9999/9999 [00:00<00:00, 98178.35it/s]
[+] Time elapsed: 0.1512 sec.
[*] Performing pastctfprimes attack on /var/folders/98/68wgw4r51hxd99kggk87t6lw0000gn/T/tmpywhsn5sj.
100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 113/113 [00:00<00:00, 1267262.97it/s]
[+] Time elapsed: 0.0003 sec.
[*] Performing system_primes_gcd attack on /var/folders/98/68wgw4r51hxd99kggk87t6lw0000gn/T/tmpywhsn5sj.
100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 7007/7007 [00:00<00:00, 905071.70it/s]
[+] Time elapsed: 0.0243 sec.
[*] Performing factordb attack on /var/folders/98/68wgw4r51hxd99kggk87t6lw0000gn/T/tmpywhsn5sj.
[!] Composite not in factordb, couldn't factorize...
[+] Time elapsed: 0.1794 sec.
[*] Performing fibonacci_gcd attack on /var/folders/98/68wgw4r51hxd99kggk87t6lw0000gn/T/tmpywhsn5sj.
100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 9999/9999 [00:00<00:00, 72745.83it/s]
[+] Time elapsed: 0.1382 sec.
[*] Performing smallq attack on /var/folders/98/68wgw4r51hxd99kggk87t6lw0000gn/T/tmpywhsn5sj.
[+] Time elapsed: 0.1879 sec.
[*] Performing mersenne_primes attack on /var/folders/98/68wgw4r51hxd99kggk87t6lw0000gn/T/tmpywhsn5sj.
 29%|███████████████████████████████████                                                                                    | 15/51 [00:00<00:00, 515693.11it/s]
[+] Time elapsed: 0.0003 sec.
[*] Performing nonRSA attack on /var/folders/98/68wgw4r51hxd99kggk87t6lw0000gn/T/tmpywhsn5sj.
[+] Time elapsed: 0.0031 sec.
[*] Performing wiener attack on /var/folders/98/68wgw4r51hxd99kggk87t6lw0000gn/T/tmpywhsn5sj.
100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 3/3 [00:00<00:00, 187804.66it/s]
[*] Cracking failed...
[+] Time elapsed: 0.0002 sec.
[*] Performing wolframalpha attack on /var/folders/98/68wgw4r51hxd99kggk87t6lw0000gn/T/tmpywhsn5sj.
[*] Performing fermat attack on /var/folders/98/68wgw4r51hxd99kggk87t6lw0000gn/T/tmpywhsn5sj.
[!] Timeout.
[+] Time elapsed: 60.0016 sec.
[*] Performing small_crt_exp attack on /var/folders/98/68wgw4r51hxd99kggk87t6lw0000gn/T/tmpywhsn5sj.
[!] Timeout.
[+] Time elapsed: 60.0021 sec.
[*] Performing primorial_pm1_gcd attack on /var/folders/98/68wgw4r51hxd99kggk87t6lw0000gn/T/tmpywhsn5sj.
100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 10000/10000 [00:00<00:00, 12432.88it/s]
[+] Time elapsed: 0.8049 sec.
[*] Performing partial_d attack on /var/folders/98/68wgw4r51hxd99kggk87t6lw0000gn/T/tmpywhsn5sj.
[!] partial_d attack is only for partial private keys not pubkeys...
[!] partial_d internal error...
[+] Time elapsed: 0.0001 sec.
[*] Performing factor_2PN attack on /var/folders/98/68wgw4r51hxd99kggk87t6lw0000gn/T/tmpywhsn5sj.
[+] Time elapsed: 0.0001 sec.
[*] Performing carmichael attack on /var/folders/98/68wgw4r51hxd99kggk87t6lw0000gn/T/tmpywhsn5sj.
[!] Timeout.
[+] Time elapsed: 59.9991 sec.
[*] Performing kraitchik attack on /var/folders/98/68wgw4r51hxd99kggk87t6lw0000gn/T/tmpywhsn5sj.
[!] Timeout.
[+] Time elapsed: 59.9992 sec.
[*] Performing highandlowbitsequal attack on /var/folders/98/68wgw4r51hxd99kggk87t6lw0000gn/T/tmpywhsn5sj.
[+] Time elapsed: 0.0054 sec.
[*] Performing mersenne_pm1_gcd attack on /var/folders/98/68wgw4r51hxd99kggk87t6lw0000gn/T/tmpywhsn5sj.
100%|████████████████████████████████████| 2045/2045 [00:00<00:00, 94850.73it/s]
[+] Time elapsed: 0.0221 sec.
[*] Performing noveltyprimes attack on /var/folders/98/68wgw4r51hxd99kggk87t6lw0000gn/T/tmpywhsn5sj.
100%|███████████████████████████████████████| 21/21 [00:00<00:00, 657316.30it/s]
[+] Time elapsed: 0.0002 sec.
[*] Performing pisano_period attack on /var/folders/98/68wgw4r51hxd99kggk87t6lw0000gn/T/tmpywhsn5sj.
[+] Time elapsed: 0.0001 sec.
[*] Performing factorial_pm1_gcd attack on /var/folders/98/68wgw4r51hxd99kggk87t6lw0000gn/T/tmpywhsn5sj.
100%|███████████████████████████████████| 29998/29998 [00:07<00:00, 4223.42it/s]
[+] Time elapsed: 7.1029 sec.
[*] Performing SQUFOF attack on /var/folders/98/68wgw4r51hxd99kggk87t6lw0000gn/T/tmpywhsn5sj.
[!] Timeout.
[+] Time elapsed: 59.9991 sec.
[*] Performing pollard_p_1 attack on /var/folders/98/68wgw4r51hxd99kggk87t6lw0000gn/T/tmpywhsn5sj.
  3%|█▎                                        | 32/997 [00:58<29:46,  1.85s/it][!] Timeout.
  3%|█▎                                        | 32/997 [00:59<30:09,  1.87s/it]
[+] Time elapsed: 59.9996 sec.
[*] Performing hart attack on /var/folders/98/68wgw4r51hxd99kggk87t6lw0000gn/T/tmpywhsn5sj.
[!] Timeout.
[+] Time elapsed: 60.0028 sec.
[*] Performing boneh_durfee attack on /var/folders/98/68wgw4r51hxd99kggk87t6lw0000gn/T/tmpywhsn5sj.
[+] Time elapsed: 2.5975 sec.
[*] Performing ecm2 attack on /var/folders/98/68wgw4r51hxd99kggk87t6lw0000gn/T/tmpywhsn5sj.
[!] Timeout.
[+] Time elapsed: 60.0044 sec.
[*] Performing qs attack on /var/folders/98/68wgw4r51hxd99kggk87t6lw0000gn/T/tmpywhsn5sj.
[+] Time elapsed: 60.0028 sec.
[*] Performing lattice attack on /var/folders/98/68wgw4r51hxd99kggk87t6lw0000gn/T/tmpywhsn5sj.
[+] Time elapsed: 1.6629 sec.
[*] Performing z3_solver attack on /var/folders/98/68wgw4r51hxd99kggk87t6lw0000gn/T/tmpywhsn5sj.
[!] Timeout.
[+] Time elapsed: 60.0598 sec.
[*] Performing cube_root attack on /var/folders/98/68wgw4r51hxd99kggk87t6lw0000gn/T/tmpywhsn5sj.
[+] Time elapsed: 0.0031 sec.
[*] Performing classical_shor attack on /var/folders/98/68wgw4r51hxd99kggk87t6lw0000gn/T/tmpywhsn5sj.
[!] Timeout.
[+] Time elapsed: 60.0028 sec.
[*] Performing compositorial_pm1_gcd attack on /var/folders/98/68wgw4r51hxd99kggk87t6lw0000gn/T/tmpywhsn5sj.
100%|████████████████████████████████████| 9999/9999 [00:00<00:00, 15793.41it/s]
[+] Time elapsed: 0.6337 sec.
[*] Performing comfact_cn attack on /var/folders/98/68wgw4r51hxd99kggk87t6lw0000gn/T/tmpywhsn5sj.
[+] Time elapsed: 0.0001 sec.
[*] Performing fermat_numbers_gcd attack on /var/folders/98/68wgw4r51hxd99kggk87t6lw0000gn/T/tmpywhsn5sj.
100%|███████████████████████████████████████████| 28/28 [00:00<00:00, 37.23it/s]
[+] Time elapsed: 0.7540 sec.
[*] Performing lehmer attack on /var/folders/98/68wgw4r51hxd99kggk87t6lw0000gn/T/tmpywhsn5sj.
[!] Timeout.
[+] Time elapsed: 1241.8648 sec.
[*] Performing qicheng attack on /var/folders/98/68wgw4r51hxd99kggk87t6lw0000gn/T/tmpywhsn5sj.
[+] Time elapsed: 27.9307 sec.
[*] Performing partial_q attack on /var/folders/98/68wgw4r51hxd99kggk87t6lw0000gn/T/tmpywhsn5sj.
[!] partial_q attack is only for partial private keys not pubkeys...
[+] Time elapsed: 0.0004 sec.
[*] Performing siqs attack on /var/folders/98/68wgw4r51hxd99kggk87t6lw0000gn/T/tmpywhsn5sj.
Can't load siqs because yafu binary is not installed
[*] Performing lehman attack on /var/folders/98/68wgw4r51hxd99kggk87t6lw0000gn/T/tmpywhsn5sj.
[!] Timeout.
[+] Time elapsed: 60.0057 sec.
[*] Performing smallfraction attack on /var/folders/98/68wgw4r51hxd99kggk87t6lw0000gn/T/tmpywhsn5sj.
[+] Time elapsed: 9.2216 sec.
[*] Performing williams_pp1 attack on /var/folders/98/68wgw4r51hxd99kggk87t6lw0000gn/T/tmpywhsn5sj.
[!] Timeout.
[+] Time elapsed: 60.0040 sec.
[*] Performing ecm attack on /var/folders/98/68wgw4r51hxd99kggk87t6lw0000gn/T/tmpywhsn5sj.
[!] Timeout.
[+] Time elapsed: 60.0070 sec.
[*] Performing binary_polinomial_factoring attack on /var/folders/98/68wgw4r51hxd99kggk87t6lw0000gn/T/tmpywhsn5sj.
[+] Time elapsed: 1.7936 sec.
[*] Performing londahl attack on /var/folders/98/68wgw4r51hxd99kggk87t6lw0000gn/T/tmpywhsn5sj.
100%|██████████████████████████| 10000001/10000001 [00:04<00:00, 2151358.59it/s]
  0%|              | 27096776/100000000000001 [00:55<55545:46:28, 500087.91it/s][!] Timeout.
  0%|              | 27119732/100000000000001 [00:55<56694:36:36, 489954.34it/s]
[+] Time elapsed: 60.4251 sec.
[*] Performing roca attack on /var/folders/98/68wgw4r51hxd99kggk87t6lw0000gn/T/tmpywhsn5sj.
[-] This key is not roca, skiping test...
[+] Time elapsed: 0.0018 sec.
[*] Performing pollard_rho attack on /var/folders/98/68wgw4r51hxd99kggk87t6lw0000gn/T/tmpywhsn5sj.
[!] Timeout.
[+] Time elapsed: 60.0013 sec.
[*] Performing neca attack on /var/folders/98/68wgw4r51hxd99kggk87t6lw0000gn/T/tmpywhsn5sj.
Can't load neca because neca binary is not installed
[*] Performing XYXZ attack on /var/folders/98/68wgw4r51hxd99kggk87t6lw0000gn/T/tmpywhsn5sj.
[+] Time elapsed: 13.0605 sec.
[*] Performing brent attack on /var/folders/98/68wgw4r51hxd99kggk87t6lw0000gn/T/tmpywhsn5sj.
[!] Timeout.
[+] Time elapsed: 60.0045 sec.
[*] Performing dixon attack on /var/folders/98/68wgw4r51hxd99kggk87t6lw0000gn/T/tmpywhsn5sj.
[-] Dixon is too slow for pubkeys > 10^10...
[+] Time elapsed: 0.0001 sec.
[*] Performing euler attack on /var/folders/98/68wgw4r51hxd99kggk87t6lw0000gn/T/tmpywhsn5sj.
[!] Timeout.
[+] Time elapsed: 60.0026 sec.
[+] Total time elapsed min,max,avg: 0.0001/1241.8648/48.7484 sec.

Results for /var/folders/98/68wgw4r51hxd99kggk87t6lw0000gn/T/tmpywhsn5sj:

Unciphered data :
HEX : 0x7069636f4354467b315f67753373735f703330706c335f7034645f6d337373346733735f6630725f345f72333473306e7d
INT (big endian) : 4429245455869293815079972080083415826407263145486268640583411444889535104721282447026455386576187267483573457800687229
INT (little endian) : 4942210453539368652250844067913862968068035484862385496139787961201021885687598269635423492169717200393229464087259504
utf-8 : picoCTF{1_gu3ss_p30pl3_p4d_m3ss4g3s_f0r_4_r34s0n}
STR : b'picoCTF{1_gu3ss_p30pl3_p4d_m3ss4g3s_f0r_4_r34s0n}'
```
