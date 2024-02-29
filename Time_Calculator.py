# # Code start

# Start of function
def add_time(hour='00:00 AM',plusHour='00:00',day=None):
  
  try:
    # Arreglo
    splitHour = hour.split()
    contadorDias = 0
    i = 0
    counter = 0
    resp = ''
  
    # Condicional
    if len(splitHour) == 2:
    
      # First and second digit series (hour)
      x = hour.find(':')
      num1 = int(hour[:x])
      num2 = int(hour[x+1:x+3])
  
      # First and second digit series (plusHour)
      y = plusHour.find(':')
      num3 = int(plusHour[:y])
      num4 = int(plusHour[y+1:y+3])
  
      # Add hours and minutes
      res1 = num1 + num3 # hours
      res2 = num2 + num4 # minutes
      
      # Conditional minutes
      n2 = res2 // 60
      res2m = res2 - (n2 * 60)
      if len(str(res2m)) == 1:
        res2m = '0' + str(res2m)
      
      # Conditional time
      n1 = res1 // 12
      res1h = res1 - (n1 * 12) + n2
  
      # AM y PM
      ap = str(hour[x+4:])
      if n1 == 0 and n2 >= 1 and ap == 'AM':
        ap = 'PM'
      elif n1 == 0 and n2 >= 1 and ap == 'PM':
        ap = 'AM'
      else:
        for counter in range (n1):
          if ap == 'AM':
            ap = 'PM'
          elif ap == 'PM':
            ap = 'AM'
  
      # All previous
      resp = str(res1h) + ':' + str(res2m) + ' ' + str(ap)
          
      # Days that pass
      contadorDias = res1 // 24
      for i in range(contadorDias):
        if day == 'Monday':
          day = 'Tuesday'
        elif day == 'Tuesday':
          day = 'Wednesday'
        elif day == 'Wednesday':
          day = 'Thursday'
        elif day == 'Thursday':
          day = 'Friday'
        elif day == 'Friday':
          day = 'Saturday'
        elif day == 'Saturday':
          day = 'Sunday'
        elif day == 'Sunday':
          day = 'Monday'
      
      # Juntando todo
      if n1 > 1:
        resp = resp + ' ' + '(' + str(contadorDias+1) + ' ' + 'days later' + ')'
        print(resp)
      elif n1 == 1 and ap == 'AM':
        resp = resp + ' ' + '(' + 'next day' + ')'
        print(resp)
      else:
        if day == None:
          print(resp)
        else:
          # Juntar todo
          resp = resp + ',' + ' ' + str(day)
          print(resp)
      
    else:
      # Error
      print('put the structure correctly')
      print()
  
  except:
    # Type-error
    print('put the structure correctly, only numbers')

# For testing
print('Time 3:00 PM plus 3:10:')
print()
print('timeCalculator.add_time("3:00 PM", "3:10") => ')
timeCalculator.add_time("3:00 PM", "3:10")
print()
print('Time 11:30 AM plus 2:32 on Monday:')
print()
print('timeCalculator.add_time("11:30 AM", "2:32", "Monday") => ')
timeCalculator.add_time("11:30 AM", "2:32", "Monday")
print()
print('Time 11:43 AM plus 00:20:')
print()
print('timeCalculator.add_time("11:43 AM", "00:20") => ')
timeCalculator.add_time("11:43 AM", "00:20")
print()
print('Time 10:10 PM plus 3:30:')
print()
print('timeCalculator.add_time("10:10 PM", "3:30") => ')
timeCalculator.add_time("10:10 PM", "3:30")
print()
print('Time 11:43 PM plus 24:20 on tuesday:')
print()
print('timeCalculator.add_time("11:43 PM", "24:20", "tuesday") => ')
timeCalculator.add_time("11:43 PM", "24:20", "tuesday")
print()
print('Time 6:30 PM plus 205:12":')
print()
print('timeCalculator.add_time("6:30 PM", "205:12") => ')
timeCalculator.add_time("6:30 PM", "205:12")
