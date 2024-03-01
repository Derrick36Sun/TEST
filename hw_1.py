BINANRY = [0,1]

HEX_NUM = [i for i in range(10) ]
HEX_ALPHABET = [chr(i) for i in range(65, 71)]


def PRINT(type_, code_):
   print("The demical number to %s is " %(type_))
   for i in code_:
      print(i, end="")
   print("")

def READ():
   demical = int(input("plz enter a demical number between 1~255, thx. "))
   return demical

def demical_to_bi(demical_num):
   ans = []
   for square in range(7, -1, -1):
      if (demical_num-pow(2,square))>=0 :
         demical_num = demical_num-pow(2, square)
         ans.append(BINANRY[1])
      else:
         ans.append(BINANRY[0])
   return ans

def choose_num_alph(hex):
   print(hex)
   if hex>9:
      
      return HEX_ALPHABET[hex-10]
   return HEX_NUM[hex]

def demical_to_hex(demical_num):
   ans = []
   for square in range(1, -1, -1):
      q = demical_num//pow(16,square)
      r = demical_num%pow(16,square)
      # print("q is ", q)
      # print("r is ", r)
      
      demical_num = demical_num-pow(16, square)*q
      ans.append(choose_num_alph(q))
   return ans
   
   print(ans)

def START():
   while(True):
      input_ = input("plz enter 2(binary) or 16(hex), thank you.\nYou can also enter Stop can end this game. \n")
      
      if int(input_) == 2:
         PRINT("binary", demical_to_bi(READ()))
      elif int(input_) == 16:
         PRINT("hex", demical_to_hex(READ()))
      elif input_== ("STOP" or "stop" or "Stop"):
         break
      # else:
      #    input_ = input("plz enter 2(binary) or 16(hex), thank you. \n")
         
START()      