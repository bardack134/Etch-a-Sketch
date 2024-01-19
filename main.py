# Importa las clases Turtle y Screen del módulo turtle
from turtle import Turtle, Screen

# Crea un objeto de la clase Turtle
turtle = Turtle()



# Esta función hace que la tortuga gire 10 grados a la izquierda
def turn_left():
    
    # Esta línea de código está comentada porque es equivalente a la siguiente
    # new_setheading = turtle.heading() + 10      
    # turtle.setheading(new_setheading)
    
    # Usa el método left de la tortuga para girarla 10 grados a la izquierda
    turtle.left(10)
   
# Esta función hace que la tortuga avance 10 unidades
def move_forward():
    
    # Usa el método forward de la tortuga para avanzarla 10 unidades
    turtle.forward(10)
        
    
# Esta función hace que la tortuga retroceda 10 unidades
def move_backwards():
   
    # Usa el método backward de la tortuga para retrocederla 10 unidades
    turtle.backward(10)
    

# Esta función hace que la tortuga gire 10 grados a la derecha
def turn_right():
    
    #El metodo heading() nos da el angulo actual de la tortuga
    # Calcula el nuevo ángulo de la tortuga restando 10 grados al actual
    new_setheading = turtle.heading() - 10      
    # Usa el método setheading de la tortuga para establecer el nuevo ángulo
    turtle.setheading(new_setheading)
    
   

# Esta función borra el dibujo de la tortuga y la devuelve a su posición original
def clean():
    # Usa el método resetscreen de la pantalla para borrar el dibujo y reiniciar la tortuga
    screen.resetscreen()

    
# Crea un objeto de la clase Screen
screen=Screen()

#funcion para empezar a registrar los movimientos del usuario
# Usa el método listen de la pantalla para activar la escucha de eventos del teclado y el ratón
screen.listen()


#Nota: cuando pasamos una funcion como argumento de otra funcion, no ponemos los parentesis
# Usa el método onkey de la pantalla para asociar cada función a una tecla
screen.onkey(move_forward, "Up")

screen.onkey(move_backwards, "Down")

screen.onkey(turn_left, "Left")

screen.onkey(turn_right, "Right")

screen.onkey(clean, "space")

# Usa el método exitonclick de la pantalla para cerrar la ventana al hacer click en ella
screen.exitonclick()
