# Code start

'''
The structure correspond:
"num + num" = yes
"num+num" = no
"num+ num" = no
"num +num" = no
'''

# arithmetic_arranger function
def arithmetic_arranger(arr,boolean=None):
  try:
    if len(arr) < 5:
      for i in arr:
        # Add
        if "+" in i:
          x = i.find('+')
          y = i.find('+')
          num1 = int(i[:x-1])
          num2 = int(i[y+2:])
          num1Str = str(num1)
          num2Str = str(num2)
          
          # Length of numbers
          if len(num1Str) < 5 and len(num2Str) < 5:
            sup = ''
            inf = ''
            line = ''
            i = 0
            j = 0
            k = 0
    
            # Superior less than inferior
            if len(num1Str) < len(num2Str):
              sup = sup + num1Str
              inf = '+' + ' ' + num2Str
              for i in range(len(inf)-len(num1Str)):
                num1Str = ' ' + num1Str
              print(num1Str)
              print(inf)

              # Bottom line
              for j in range(len(inf)):
                line = line + '-'
              print(line)
              
            # First same as second
            elif len(num1Str) == len(num2Str):
              for i in range(2):
                sup = sup + ' '
              sup = sup + num1Str
              inf = '+' + ' ' + num2Str
              print(sup)
              print(inf)

              # Bottom line
              for j in range(len(inf)):
                line = line + '-'
              print(line)
      
            # Upper greater than lower
            else:
              for i in range(2):
                sup = sup + ' '
              sup = sup + num1Str
              inf = '+'
              for i in range(len(sup)-len(num2Str)-1):
                inf = inf + ' '
              inf = inf + num2Str
              print(sup)
              print(inf)
              
              # Bottom line
              for j in range(len(inf)):
                line = line + '-'
              print(line)
    
            # If True
            if boolean == True:
              num3 = num1 + num2
              num3Str = str(num3)
              res = ''
              
              # More than 4 digits
              if len(num3Str) > 4:
                for k in range(1):
                  res = res + ' '
                res = res + num3Str
                print(res)
                print()
              else:
                for k in range(len(line)-len(num3Str)):
                  res = res + ' '
                res = res + num3Str
                print(res)
                print()
    
            # If None or another
            else:
              print()
              
          else:
            # Error number digits
            print('Only numbers of 4 digits')
            print()
            
        # Subtraction
        elif "-" in i:
          x = i.find('-')
          y = i.find('-')
          num1 = int(i[:x-1])
          num2 = int(i[y+1:])
          num1Str = str(num1)
          num2Str = str(num2)
          
          # Length of numbers
          if len(num1Str) < 5 and len(num2Str) < 5:
            sup = ''
            inf = ''
            line = ''
            i = 0
            j = 0
            k = 0
    
            # Superior less than inferior
            if len(num1Str) < len(num2Str):
              sup = sup + num1Str
              inf = '-' + ' ' + num2Str
              for i in range(len(inf)-len(num1Str)):
                num1Str = ' ' + num1Str
              print(num1Str)
              print(inf)
              
              # Bottom line
              for j in range(len(inf)):
                line = line + '-'
              print(line)
              
            # First same as second
            elif len(num1Str) == len(num2Str):
              for i in range(2):
                sup = sup + ' '
              sup = sup + num1Str
              inf = '-' + ' ' + num2Str
              print(sup)
              print(inf)
              
              # Bottom line
              for j in range(len(inf)):
                line = line + '-'
              print(line)
      
            # Upper greater than lower
            else:
              for i in range(2):
                sup = sup + ' '
              sup = sup + num1Str
              inf = '-'
              for i in range(len(sup)-len(num2Str)-1):
                inf = inf + ' '
              inf = inf + num2Str
              print(sup)
              print(inf)
              
              # Bottom line
              for j in range(len(inf)):
                line = line + '-'
              print(line)
    
            # If True
            if boolean == True:
              num3 = num1 - num2
              num3Str = str(num3)
              res = ''
              
              # More than 4 digits
              if len(num3Str) > 4 or num3 < 0:
                for k in range(1):
                  res = res + ' '
                res = res + num3Str
                print(res)
                print()
              else:
                for k in range(len(line)-len(num3Str)):
                  res = res + ' '
                res = res + num3Str
                print(res)
                print()
    
            else:
              # If None or another
              print()
              
          else:
            # If a number is more of 4 digits
            print('Only numbers of 4 digits')
            print()
            
        else:
          # Syntax error
          print('Error: structure num + num or num - num')
          print()
  
    else:
      # If arr has more than 5 operations
      print('Error: Too many problems.')
      print()
  except:
    print('Error: only numbers')
    print()

# Function testing
print('Make sure to mach the structure:')
print()
print('arithmetic_arranger.arithmetic_arranger([arr],Boolean)')
print()
print('[arr] is a list of elements')
print()
print('boolean is a True or None variable')
print()
print('Example:')
print()
print('arithmetic_arranger.arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"])')
print()
print('Output:')
print()
arithmetic_arranger.arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"])
print()
print('if you want the anwers, just put (boolean = True):')
print()
print('arithmetic_arranger.arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)')
print()
arithmetic_arranger.arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"],True)
