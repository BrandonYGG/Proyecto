import pygame
import sys
import menu_principal  # Importamos el módulo del menú principal

# Inicializar Pygame
pygame.init()

# Cargar imagen del personaje
personaje = pygame.image.load("Imagenes/Personaje.png")  # Asegúrate de que la imagen esté en la ruta correcta

# Configuración de la pantalla
pantalla = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pantalla del Juego")

# Posición inicial del personaje
personaje_rect = personaje.get_rect()
personaje_rect.x = 50  # Coordenada X (fija)
personaje_rect.y = 300  # Coordenada Y inicial (centro vertical)

# Velocidad de movimiento del personaje
velocidad = 5

# Función para manejar la pantalla del juego
def pantalla_del_juego(pantalla):
    juego_corriendo = True
    pausa = False

    # Crear el botón de pausa (círculo) en la parte superior izquierda
    boton_pausa = pygame.Rect(10, 10, 40, 40)  # Rectángulo para el botón de pausa (posición superior izquierda)
    
    # Botón de pausa visible (circular, de color gris con borde negro)
    pygame.draw.circle(pantalla, (169, 169, 169), (30, 30), 20)  # Botón de pausa circular con color gris

    while juego_corriendo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                juego_corriendo = False
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if boton_pausa.collidepoint(evento.pos):
                    pausa = not pausa  # Cambiar el estado de la pausa

        # Si está en pausa, mostrar botones de reanudar y salir
        if pausa:
            # Fondo transparente para la pausa
            pantalla.fill((135, 206, 235))  # Color azul cielo

            # Crear los botones de reanudar y salir
            boton_reanudar = pygame.Rect(300, 250, 200, 50)
            pygame.draw.rect(pantalla, (0, 0, 0), boton_reanudar)
            texto_reanudar = pygame.font.SysFont("Arial", 48).render("Reanudar", True, (255, 255, 255))
            texto_rect_reanudar = texto_reanudar.get_rect(center=boton_reanudar.center)  # Centrar el texto
            pantalla.blit(texto_reanudar, texto_rect_reanudar)

            boton_salir = pygame.Rect(300, 350, 200, 50)
            pygame.draw.rect(pantalla, (0, 0, 0), boton_salir)
            texto_salir = pygame.font.SysFont("Arial", 48).render("Salir", True, (255, 255, 255))
            texto_rect_salir = texto_salir.get_rect(center=boton_salir.center)  # Centrar el texto
            pantalla.blit(texto_salir, texto_rect_salir)

            pygame.display.flip()  # Actualizar pantalla

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    juego_corriendo = False
                    pygame.quit()
                    sys.exit()

                elif evento.type == pygame.MOUSEBUTTONDOWN:
                    if boton_reanudar.collidepoint(evento.pos):
                        pausa = False  # Volver al juego
                    elif boton_salir.collidepoint(evento.pos):
                        juego_corriendo = False  # Salir del juego y regresar al menú principal
                        return  # Salir de la función y regresar al menú principal

        else:
            # Fondo de pantalla (azul cielo)
            pantalla.fill((135, 206, 235))  # Color azul cielo

            # Mover el personaje con las teclas
            teclas = pygame.key.get_pressed()

            # Mover el personaje hacia arriba y abajo
            if teclas[pygame.K_UP]:  # Flecha hacia arriba
                personaje_rect.y -= velocidad  # Mueve hacia arriba
            if teclas[pygame.K_DOWN]:  # Flecha hacia abajo
                personaje_rect.y += velocidad  # Mueve hacia abajo

            # Limitar el movimiento para que el personaje no se salga de la pantalla
            if personaje_rect.top < 0:
                personaje_rect.top = 0
            if personaje_rect.bottom > 600:
                personaje_rect.bottom = 600

            # Dibujar el personaje en su nueva posición
            pantalla.blit(personaje, personaje_rect)

            # Actualizar la pantalla
            pygame.display.flip()

    pygame.quit()
