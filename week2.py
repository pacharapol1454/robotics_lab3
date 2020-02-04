c=0
psw = input()
for i in psw:
 if i.isalpha():
  c=c+1
if c==0:
 psw_int = int(psw)
 digit = 0
 while(psw_int > 0):
  psw_int = psw_int//10
  digit = digit + 1
 if digit == 4 or digit == 6:
  print("true")
 else:
  print("false")
else:
 print("false has alphabet")