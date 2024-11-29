import pygame
import sys
import game_screen  # Importamos el módulo donde se encuentra la pantalla del juego

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
pantalla = pygame.display.set_mode((800, 600))  # Tamaño de la pantalla
pygame.display.set_caption("Menu Principal")

# Colores para el fondo difuminado verde
VERDE_OSCURO = (0, 128, 0)  # Verde bandera
VERDE_CLARO = (144, 238, 144)  # Verde claro

# Fuente para el texto
fuente = pygame.font.SysFont("Arial", 48)

# Función para crear un fondo verde difuminado
def fondo_verde():
    # Crear un gradiente de verde oscuro a verde claro
    for i in range(600):  # Gradiente vertical
        color = (
            VERDE_OSCURO[0] + (VERDE_CLARO[0] - VERDE_OSCURO[0]) * i // 600,
            VERDE_OSCURO[1] + (VERDE_CLARO[1] - VERDE_OSCURO[1]) * i // 600,
            VERDE_OSCURO[2] + (VERDE_CLARO[2] - VERDE_OSCURO[2]) * i // 600
        )
        pygame.draw.line(pantalla, color, (0, i), (800, i))  # Dibuja el gradiente

# Función para manejar el menú principal
def menu_principal():
    juego_corriendo = True
    while juego_corriendo:
        fondo_verde()  # Fondo verde difuminado

        # Título del juego
        texto_titulo = fuente.render("Misión Verde TESI", True, (0, 0, 0))
        pantalla.blit(texto_titulo, (200, 100))

        # Botón de "Nueva Partida"
        boton_nueva_partida = pygame.Rect(250, 250, 300, 50)
        pygame.draw.rect(pantalla, (0, 0, 0), boton_nueva_partida)  # Dibuja el rectángulo del botón
        texto_nueva_partida = fuente.render("Nueva Partida", True, (255, 255, 255))

        # Centrar el texto en el botón de "Nueva Partida"
        texto_rect_nueva_partida = texto_nueva_partida.get_rect(center=boton_nueva_partida.center)
        pantalla.blit(texto_nueva_partida, texto_rect_nueva_partida)

        # Botón de "Salir"
        boton_salir = pygame.Rect(250, 350, 300, 50)
        pygame.draw.rect(pantalla, (0, 0, 0), boton_salir)  # Dibuja el rectángulo del botón
        texto_salir = fuente.render("Salir", True, (255, 255, 255))

        # Centrar el texto en el botón de "Salir"
        texto_rect_salir = texto_salir.get_rect(center=boton_salir.center)
        pantalla.blit(texto_salir, texto_rect_salir)

        pygame.display.flip()  # Actualizar pantalla

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                juego_corriendo = False
                pygame.quit()
                sys.exit()

            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if boton_nueva_partida.collidepoint(evento.pos):  # Si se hace clic en "Nueva Partida"
                    game_screen.pantalla_del_juego(pantalla)  # Llamar a la pantalla del juego
                elif boton_salir.collidepoint(evento.pos):  # Si se hace clic en "Salir"
                    juego_corriendo = False  # Salir del juego
                    pygame.quit()
                    sys.exit()

if __name__ == "__main__":
    menu_principal()
