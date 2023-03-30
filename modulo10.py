import threading
import time

def proc2(a='a'):
    if a == 'c':
        if t2_c.is_alive():
            print("Thread t2_c (espera 30s) está ativo. - análise dentro da definição")
        else:
            print("Thread t2_c (espera 30s) não está ativo. - análise dentro da definição")
        time.sleep(30)
    print("Processo 2.")



def proc1(ex, a='a'):
    if ex == 1:
    #c)
        print("Thread atual (imprimindo 'processo 1'):", threading.current_thread())
        # d)
        print("Identificador da Thread atual: (imprimindo 'processo 1')", threading.get_ident())
        print("Processo 1.")
    elif ex == 2:
        if a == 'c':
            # d)
            if t1_c.is_alive():
                print("Thread t1_c (espera 5s) está ativo. - análise dentro da definição")
            else:
                print("Thread t1_ c (espera 5s) não está ativo. - análise dentro da definição")
            time.sleep(5)
        print("Processo 1.")

print()
print()
print()
# exercício 1
print("Exercício 1.")
print("----")
# a)
t1_ex1 = threading.Thread(target=proc1, args=(1,)).start()

#b)
if threading.Thread(target=proc1, args=(1,)).is_alive():
    print("Thread t1_ex1 está ativo.")
else:
    print("Thread t1_ex1 não está ativo.")
print()

# d) 2.
print("Thread atual:", threading.current_thread())
print("Identificador da Thread atual:", threading.get_ident())

# e)
print("Quantidade de Threads ativas atualmente:", threading.active_count())

# f)
print("Lista com todas as Threads ativas atualmente:")
print(threading.enumerate())
print()
print()
print()

# exercício 2)
print("Exercício 2.")
print("----")
# a)
t1 = threading.Thread(target=proc1, args=(2,))
t2 = threading.Thread(target=proc2)
t1.start()
t2.start()

# b)
if t1.is_alive():
    print("Thread t1 está ativo.")
else:
    print("Thread t1 não está ativo.")
if t2.is_alive():
    print("Thread t1 está ativo.")
else:
    print("Thread t1 não está ativo.")
print()

# c)
print("Aguardando 5s para imprimir 'Processo 1' e 30s para imprimir 'Processo 2'...")
t1_c = threading.Thread(target=proc1, args=(2, 'c',))
t2_c = threading.Thread(target=proc2, args=['c'])
t1_c.start()
t2_c.start()
print()

# d)
print("análise imediata - fora da definição da função passada na Thread: ")
if t1_c.is_alive():
    print("Thread t1_c (espera 5s) está ativo.")
else:
    print("Thread t1_ c (espera 5s) não está ativo.")
if t2_c.is_alive():
    print("Thread t2_c (espera 30s) está ativo.")
else:
    print("Thread t2_c (espera 30s) não está ativo.")

print("análise de t1_c após 2s e t2_c após 10s:")
time.sleep(2)
if t1_c.is_alive():
    print("Thread t1_c (espera 5s) está ativo.")
else:
    print("Thread t1_ c (espera 5s) não está ativo.")
time.sleep(10)
if t2_c.is_alive():
    print("Thread t2_c (espera 30s) está ativo.")
else:
    print("Thread t2_c (espera 30s) não está ativo.")
