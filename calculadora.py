num1 = 0
num2 = 0
result = 0
op = ""

while True:

      num1 = float(input('Digite primeiro número'))
      op = input ('Digite a peração')
      num2 = float(input('Digite  segundo número'))


      if op == '+':
          result = num1 + num2
      elif op == '-':
          result = num1 - num2
      elif op == '*':
          result = num1 * num2
      elif op == '/':
          result =  num / num2
  
     else:

          print('{} {} {}= {}'.format(num1, op, num2, result))