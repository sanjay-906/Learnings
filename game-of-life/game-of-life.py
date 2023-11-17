# Write your code here :-)
import numpy as np
import pygame
import time

COLOR_BG= (10, 10, 10) #dark grey
COLOR_GRID= (40, 40, 40) #less lighter grey
COLOR_DIE_NEXT= (170, 170, 170) #even lighter grey
COLOR_ALIVE_NEXT= (255, 255, 255) #white


def update(screen, cells, size, with_progress= False):
    # initialize the enviroment with 0s
    updated_cells= np.zeros((cells.shape[0], cells.shape[1]))

    # iterate every single cell in the enviroment
    for row, col in np.ndindex(cells.shape):

        # calculate the number of cells alive in the neighbourhood
        alive= np.sum(cells[row-1:row+2, col-1: col+2]) - cells[row, col]

        # determine color based on cell state
        color= COLOR_BG if cells[row,col] ==0 else COLOR_ALIVE_NEXT

        # game of life rules:
        if cells[row, col]==1:
            if alive <2 or alive >3:
                if with_progress:
                    color= COLOR_DIE_NEXT
            elif 2<=alive<=3:
                updated_cells[row,col] =1
                if with_progress:
                    color= COLOR_ALIVE_NEXT
        else:
            if alive==3:
                updated_cells[row,col]=1
                if with_progress:
                    color= COLOR_ALIVE_NEXT

        # draw the enviroment
        pygame.draw.rect(screen, color, (col*size, row*size, size-1, size-1))

    return updated_cells

# ratio of the grid
SIZE= 10

def main():

    pygame.init()
    # create and display screen
    screen= pygame.display.set_mode((80*SIZE, 60*SIZE))
    cells= np.zeros((60,80))
    screen.fill(COLOR_GRID)
    update(screen, cells, 10)

    pygame.display.flip()
    pygame.display.update()

    running= False

    while True:

        for event in pygame.event.get():
            # quit condition
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            # start/stop simulation
            elif event.type== pygame.KEYDOWN:
                if event.key== pygame.K_SPACE:
                    running= not running
                    update(screen, cells, 10)
                    pygame.display.update()
            # add cell to the enviroment
            if pygame.mouse.get_pressed()[0]:
                pos= pygame.mouse.get_pos()
                cells[pos[1]//10, pos[0]//10]= 1
                update(screen, cells, 10)
                pygame.display.update()
        screen.fill(COLOR_GRID)

        # update while the enviroment is running
        if running:
            cells= update(screen, cells, 10, with_progress= True)
            pygame.display.update()

        time.sleep(0.001)

if __name__== "__main__":
    main()

