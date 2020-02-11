def validate_pin(psw):
 c=0
 state=0
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
   state=state+1
 if state==1:
     return True
 else:
     return False
