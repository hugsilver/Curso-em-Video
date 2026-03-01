try:
    a = int(input('Denominador: '))
    b = int(input('Numerador: '))
    r = b/a

except (ValueError, TypeError):
    print('Tivemso um problema com os tipos de dados que você digitou.')

except ZeroDivisionError:
    print('Não é possivel dividir número por zero!')

except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados!')

except Exception as erro:
    print(f'O erro encontrao foi {erro.__cause__}')

else:
    print(f'O resultado é {r:.1f}')
finally:
    print(f'Volte sempre! Muito Obrigado!')

'''
except Exception as erro:
    print(f'Problema encontrado foi {erro.__class__}') #Podento ter vários argumentos
'''
#Sempre iniciar o teste pelo certo
#Try: Operação
#Except: Falhou
#Else: Deu certo
#Finally: Independente se deu Certo ou Erro - Finally e else são opcionais
#Todo Try pode ter mais de um Exceps



