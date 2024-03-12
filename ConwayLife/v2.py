import time
import pygame
import numpy as np

COLOR_BG = (10, 10, 10)
COLOR_GRID = (40, 40, 40)
COLOR_DIE_NEXT = (170, 170, 170)
COLOR_ALIVE_NEXT = (255, 255, 255)

def update(screen, cells, size):
    kernel = np.array([[1, 1, 1],
                       [1, 0, 1],
                       [1, 1, 1]])

    padded_cells = np.pad(cells, 1, mode='constant')
    kernel_reshaped = kernel.reshape(3, 3)
    neighbors = np.sum(padded_cells[:, :, np.newaxis, np.newaxis] * kernel_reshaped[np.newaxis, np.newaxis, :, :], axis=(2, 3))

    update_cells = np.zeros_like(cells)

    update_cells[(neighbors[1:-1, 1:-1] == 3) & (cells == 0)] = 1
    update_cells[(neighbors[1:-1, 1:-1] < 2) | (neighbors[1:-1, 1:-1] > 3)] = 0
    update_cells[(neighbors[1:-1, 1:-1] == 2) & (cells == 1)] = 1

    for row, col in np.ndindex(cells.shape):
        color = COLOR_ALIVE_NEXT if update_cells[row, col] else COLOR_DIE_NEXT if cells[row, col] else COLOR_BG
        pygame.draw.rect(screen, color, (col * size, row * size, size, size))

    return update_cells

def main():
    pygame.init()
    screen_size = (800, 600)
    screen = pygame.display.set_mode(screen_size)

    grid_size = (120, 160)  # (rows, columns)
    cell_size = screen_size[0] // grid_size[1]

    cells = np.zeros(grid_size, dtype=int)

    screen.fill(COLOR_GRID)
    for row in range(grid_size[0]):
        for col in range(grid_size[1]):
            pygame.draw.rect(screen, COLOR_BG, (col * cell_size, row * cell_size, cell_size, cell_size))

    pygame.display.flip()

    running = False
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = not running
                elif event.key == pygame.K_r:
                    cells = np.random.choice([0, 1], size=grid_size, p=[0.8, 0.2])

            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                cells[pos[1] // cell_size, pos[0] // cell_size] = 1

        if running:
            cells = update(screen, cells, cell_size)
            pygame.display.update()

        time.sleep(0.001)
        clock.tick(60)

if __name__ == "__main__":
    main()