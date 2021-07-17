import turtle
t = turtle.Turtle()
condicao1 = True
while condicao1:
    n1 = int(input('Digite um número inteiro para n1: '))
    n2 = int(input('Digite um número inteiro para n2: '))
    if n1 >= 0 and n2 >= 0:
        if n1 < n2:
            n3 = 0
            n4 = 0
            for i in range(n2 + 1):
                if i >= n1:
                    if i != 0:
                        #DESENHO
                        t.left(90)
                        t.begin_fill()
                        for j in range (4):
                            #professor vou colocar uma escala para ficar melhor a visualização do desenho
                            t.color('blue')
                            t.forward(n4 * 20)
                            t.right(90)

                        t.end_fill()
                        t.penup()
                        t.right(90)
                        t.forward(n4*10)
                        t.right(90)
                        t.forward(20)
                        t.color('black')
                        t.write('F', align='left', font=('Arial', 10, 'normal'))
                        t.left(90)
                        t.forward(5)
                        t.write(str(i), align='left', font=('Arial', 6, 'normal'))
                        t.left(90)
                        t.forward(20)
                        t.right(90)
                        t.forward(n4*4 + 20)
                        t.pendown()

                n4 = n4 + n3
                n3 = n4 - n3
                if n4 == 0:
                    n4 = n4 + 1
                condicao1 = False
        else:
            print('Digite valores tal que n1 < n2.')
    else:
        print('Digite valores inteiros maior ou igual a 0.')
        condicao = True
