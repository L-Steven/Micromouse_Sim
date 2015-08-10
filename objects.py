import time as t

multiplier = 70
mouseOffset = .2
wallsOffset = 1

class MouseObject:
	def __init__(self,canvas,Init_xpos,Init_ypos,Init_angle,window_size,vert,horz,dt = 0.1):
		self.UP = 1
		self.RIGHT = 2
		self.DOWN = 3
		self.LEFT = 4
		self.DT = dt
		self.window_size = window_size
		self.canvas = canvas
		self.vert = vert
		self.horz = horz
		
		self.xpos = Init_xpos
		self.ypos = Init_ypos
		self.ang = self.AngleTranslator(Init_angle)
		
		self.mouseSide_1 = self.canvas.create_line([0,0,0,0],fill = 'red')
		self.mouseSide_2 = self.canvas.create_line([0,0,0,0],fill = 'red')
		self.UpdateMouse()
		self.canvas.pack()
	
	def UpdateMouse(self):
		if self.ang == self.UP:
			newCoord_1 = [self.xpos, self.ypos + mouseOffset, self.xpos - mouseOffset, self.ypos - mouseOffset]
			newCoord_2 = [self.xpos, self.ypos + mouseOffset, self.xpos + mouseOffset, self.ypos - mouseOffset]
		elif self.ang == self.RIGHT:
			newCoord_1 = [self.xpos + mouseOffset, self.ypos, self.xpos - mouseOffset, self.ypos + mouseOffset]
			newCoord_2 = [self.xpos + mouseOffset, self.ypos, self.xpos - mouseOffset, self.ypos - mouseOffset]
		elif self.ang == self.DOWN:
			newCoord_1 = [self.xpos, self.ypos - mouseOffset, self.xpos - mouseOffset, self.ypos + mouseOffset]
			newCoord_2 = [self.xpos, self.ypos - mouseOffset, self.xpos + mouseOffset, self.ypos + mouseOffset]
		elif self.ang == self.LEFT:
			newCoord_1 = [self.xpos - mouseOffset, self.ypos, self.xpos + mouseOffset, self.ypos - mouseOffset]
			newCoord_2 = [self.xpos - mouseOffset, self.ypos, self.xpos + mouseOffset, self.ypos + mouseOffset]
		else:
			raise('Invalid angle')
		
		newCoord_1 = self.CoordTrans(newCoord_1)
		newCoord_2 = self.CoordTrans(newCoord_2)
		self.canvas.coords(self.mouseSide_1, newCoord_1)
		self.canvas.coords(self.mouseSide_2, newCoord_2)
		self.canvas.update()
		
	def AngleTranslator(self,angleWord):
		if angleWord == 'up':
			return self.UP
		elif angleWord == 'right':
			return self.RIGHT
		elif angleWord == 'down':
			return self.DOWN
		elif angleWord == 'left':
			return self.LEFT
		else:
			raise('invalid angle word')
			
	def CoordTrans(self,coord):
		a_o = 0.5 #alignment offset
		coord[0] = (coord[0] + a_o) * multiplier
		coord[1] = self.window_size - ((a_o + coord[1]) * multiplier)
		coord[2] = (coord[2] + a_o) * multiplier
		coord[3] = self.window_size - ((coord[3] + a_o) * multiplier)
		coord = tuple(coord)
		return coord
			
	def Move(self, direction,visible = True):
		if direction == 'straight':
			if self.ang == self.UP:
				self.ypos = self.ypos + 1
			elif self.ang == self.RIGHT:
				self.xpos = self.xpos + 1
			elif self.ang == self.DOWN:
				self.ypos = self.ypos - 1
			elif self.ang == self.LEFT:
				self.xpos = self.xpos - 1
			if visible:
				t.sleep(self.DT)
				self.UpdateMouse()
		elif direction == 'left':
			if self.ang == self.UP:
				self.ang = self.LEFT
			elif self.ang == self.RIGHT:
				self.ang = self.UP
			elif self.ang == self.DOWN:
				self.ang = self.RIGHT
			elif self.ang == self.LEFT:
				self.ang = self.DOWN
			if visible:
				t.sleep(self.DT)	
				self.UpdateMouse()
			self.Move('straight',visible = visible)
		elif direction == 'right':
			if self.ang == self.UP:
				self.ang = self.RIGHT
			elif self.ang == self.RIGHT:
				self.ang = self.DOWN
			elif self.ang == self.DOWN:
				self.ang = self.LEFT
			elif self.ang == self.LEFT:
				self.ang = self.UP
			if visible:
				t.sleep(self.DT)	
				self.UpdateMouse()
			self.Move('straight',visible = visible)
		elif direction == 'turn around':
			if self.ang == self.UP:
				self.ang = self.RIGHT
				if visible:
					t.sleep(self.DT)
					self.UpdateMouse()
				self.ang = self.DOWN
				if visible:
					t.sleep(self.DT)
					self.UpdateMouse()
			elif self.ang == self.RIGHT:
				self.ang = self.DOWN
				if visible:
					t.sleep(self.DT)
					self.UpdateMouse()
				self.ang = self.LEFT
				if visible:
					t.sleep(self.DT)
					self.UpdateMouse()
			elif self.ang == self.DOWN:
				self.ang = self.LEFT
				if visible:
					t.sleep(self.DT)
					self.UpdateMouse()
				self.ang = self.UP
				if visible:
					t.sleep(self.DT)
					self.UpdateMouse()
			elif self.ang == self.LEFT:
				self.ang = self.UP
				if visible:
					t.sleep(self.DT)
					self.UpdateMouse()
				self.ang = self.RIGHT
				if visible:
					t.sleep(self.DT)
					self.UpdateMouse()
		else:
			 raise('not an option')
	
	def WallDetect(self):
		x = self.xpos - 1
		y = self.ypos - 1
		detect = 4 * [0]
		#detect indexs:
		#0 is foward
		#1 is right
		#2 is backward
		#3 is left
		
		if self.ang == self.UP:
			detect[0] = self.horz[y + 1][x]
			detect[1] = self.vert[y][x + 1]
			detect[2] = self.horz[y][x]
			detect[3] = self.vert[y][x]
		elif self.ang == self.RIGHT:
			detect[0] = self.vert[y][x + 1]
			detect[1] = self.horz[y][x]
			detect[2] = self.vert[y][x]
			detect[3] = self.horz[y + 1][x]
		elif self.ang == self.DOWN:
			detect[0] = self.horz[y][x]
			detect[1] = self.vert[y][x]
			detect[2] = self.horz[y + 1][x]
			detect[3] = self.vert[y][x + 1]
		elif self.ang == self.LEFT:
			detect[0] = self.vert[y][x]
			detect[1] = self.horz[y + 1][x]
			detect[2] = self.vert[y][x + 1]
			detect[3] = self.horz[y][x]
		else:
			raise('invalid angle')
		return detect

		 
class WallObject:
	def __init__(self,canvas,vertWalls,horzWalls,window_size):
		self.vert = vertWalls
		self.horz = horzWalls
		self.window_size = window_size
		self.canvas = canvas
		
		self.vertHeight,self.vertWidth,self.horzHeight,self.horzWidth = self.validWalls()
		
		self.vertObjects = []
		self.horzObjects = []
		self._setup()
		
		
	def validWalls(self):
		vertHeight = len(self.vert)
		vertWidth = len(self.vert[0])
		horzHeight = len(self.horz)
		horzWidth = len(self.horz[0])
		return vertHeight,vertWidth,horzHeight,horzWidth
	def _setup(self):
		m = multiplier
		w = self.window_size
		for i in range(0,self.vertHeight):
			temp = []
			for j in range(0,self.vertWidth):
				if self.vert[i][j] == 1:
					temp.append(self.canvas.create_line( m * (j + 1), w - (m*(i + 1)),m * ( j + 1), w - (m * (i + 1 +wallsOffset))))
				else:
					temp.append(-1)
			self.vertObjects.append(temp)
			
		for i in range(0,self.horzHeight):
			temp = []
			for j in range(0,self.horzWidth):
				if self.horz[i][j] == 1:
					temp.append(self.canvas.create_line( m * (j + 1), w - (m*(i + 1)),m * (j + 1 + wallsOffset), w - (m * (i + 1))))
				else:
					temp.append(-1)
			self.horzObjects.append(temp)
			
			

