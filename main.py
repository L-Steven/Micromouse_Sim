#Steven Luna 
#8/9/2015

#This is designed for python 3



from tkinter import *
import objects as o
import solver_methods as solver


size = 700
root = Tk()
canvas = Canvas(root, width = size, height = size)

vertWalls = [[1,0,0,0,1,0,0,0,1],
			 [1,0,0,1,0,1,1,1,1],
			 [1,1,0,0,0,0,1,0,1],
			 [1,1,0,1,0,1,0,0,1],
			 [1,1,0,1,0,1,1,0,1],
			 [1,0,1,0,0,1,0,0,1],
			 [1,0,1,1,0,1,0,0,1],
			 [1,0,0,0,1,0,0,0,1]]
			 
horzWalls = [[1,1,1,1,1,1,1,1],
			 [1,0,1,0,0,1,0,0],
			 [0,1,1,1,1,0,0,1],
			 [0,1,0,0,1,0,1,0],
			 [0,1,0,0,0,0,0,1],
			 [0,0,0,1,1,1,1,0],
			 [1,0,0,1,0,0,1,1],
			 [0,1,0,1,0,1,0,1],
			 [1,1,1,1,1,1,1,1]]
			 
vertWalls.reverse()
horzWalls.reverse()

mouse = o.MouseObject(canvas,1,1,'up',size,vertWalls,horzWalls)
walls = o.WallObject(canvas,vertWalls,horzWalls,size)

while True:
	solver.SimpleRunner(mouse)

root.mainloop()