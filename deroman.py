
#python program to turn a roman numeral into an integer
#Good morning! Here's your coding interview problem for today.
#This problem was asked by Facebook.
#Given a number in Roman numeral format, convert it to decimal.
#The values of Roman numerals are as follows:

#    'M': 1000,
#    'D': 500,
#    'C': 100,
#    'L': 50,
#    'X': 10,
#    'V': 5,
#    'I': 1

def deromanize(string):
   value = {'M': 1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1}
   num=0 
   val = 0

   total = 0
   leng = len(string)
   leng = leng-1
   while (leng>0):
      if (int(value.get(string[leng-1]))< int(value.get(string[leng]))):
         total = total + int(value.get(string[leng]))-int(value.get(string[leng-1]))
         leng = leng - 2
         print(leng)
      else:
         total = total + int(value.get(string[leng]))
         print(leng)
         leng = leng-1
   if (leng==0):
      total = total + int(value.get(string[leng]))
      print(leng)
   print(total)

deromanize('MMMIX')
