while True:
  try:
    idade = int(input('\n Digite sua idade: '))
    break
  except ValueError:
    print("\n Valor digitado é invalido, favor digitar um número inteiro para idade.")
