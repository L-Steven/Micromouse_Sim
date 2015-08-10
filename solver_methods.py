
def SimpleRunner(mouse):
	detect = mouse.WallDetect()
	if detect[1] == 0:
		mouse.Move('right')
	elif detect[0] == 1 and detect[1] == 1 and detect[3] == 1:
		mouse.Move('turn around')
	elif detect[0] == 0:
		mouse.Move('straight')
	elif detect[3] == 0:
		mouse.Move('left')