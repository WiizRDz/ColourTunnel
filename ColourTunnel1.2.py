import pygame, random, math
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN | pygame.HWSURFACE | pygame.DOUBLEBUF)
pygame.display.set_caption("Colours")
pygame.font.init()
pygame.init()
r = 50
g = 100
b = 130
s = []
new = 0
up = 0
down = 0
ss = 10 #size 10
SS = 10 #speed 10
ro = 3 #rows-1
side = 0
wi = 0
hol = 0
inv = 0
ii = 0

clock = pygame.time.Clock()
pygame.mouse.set_visible(0)

if (screen.get_width() - screen.get_height() > 100):
	rat = 1
else:
	rat = 0

while (True):
	clock.tick(60)
	screen.fill((inv,inv,inv))
	xa, ya = pygame.mouse.get_pos()
	
	for e in pygame.event.get():
		if e.type == pygame.MOUSEBUTTONDOWN:
			if pygame.mouse.get_pressed()[2]:
				if e.button == 4:
					SS += 2
					if SS > 40:
						SS = 40
				if e.button == 5:
					SS -= 2
					if SS < 5:
						SS = 5
			else:
				if e.button == 4:
					ss += 2
					if ss > 50:
						ss = 50
				if e.button == 5:
					ss -= 2
					if ss < 5:
						ss = 5
						
	if ii == 1 and (pygame.key.get_pressed()[pygame.K_i] != 1):
		if (inv == 0):
			inv = -1
		if (inv == 255):
			inv = 0
		if (inv == -1):
			inv = 255
		ii = 0
		
	if pygame.key.get_pressed()[pygame.K_i] and ii == 0:
		ii = 1
	
	if wi == 1 and (pygame.key.get_pressed()[pygame.K_w] != 1):
		if (hol == 0):
			hol = -1
		if (hol == 2):
			hol = 0
		if (hol == -1):
			hol = 2
		wi = 0
		
	if pygame.key.get_pressed()[pygame.K_w] and wi == 0:
		wi = 1
						
	if up == 1 and (pygame.key.get_pressed()[pygame.K_UP] != 1):
		ro += 1
		if ro > 50:
			ro = 50
		up = 0
		
	if down == 1 and (pygame.key.get_pressed()[pygame.K_DOWN] != 1):
		ro -= 1
		if ro < 3:
			ro = 3
		down = 0
	
	if pygame.key.get_pressed()[pygame.K_DOWN] and down == 0:
		down = 1
	
	if pygame.key.get_pressed()[pygame.K_UP] and up == 0:
		up = 1
					
	if pygame.key.get_pressed()[pygame.K_d]:
		ss = 10
		SS = 10
		ro = 8
	
	def FindSpeed(p1,p2,s,xd=0,yd=0,a=0,xs=0,ys=0):
		x1,y1 = p1
		x2,y2 = p2
		xd = x1-x2
		if xd == 0:
			xd = (10**(-200))
		yd = y1-y2
		a = math.atan2(yd,xd)
		xs = s*math.cos(a)
		ys = s*math.sin(a)
		return xs,ys
	
	class Shot():			
		def Assign(self,xloc,r,g,b,s,row):
			self.ID = shot
			
			if s == 0:
				self.x = xloc*(screen.get_width()/row)
				self.y = screen.get_height()
			
			if s == 1:
				self.x = 0
				self.y = xloc*(screen.get_height()/row)
			
			if s == 2:
				self.x = xloc*(screen.get_width()/row)
				self.y = 0
			
			if s == 3:
				self.x = screen.get_width()
				self.y = xloc*(screen.get_height()/row)
			
			self.des = 0
			self.c = (abs(inv-r),abs(inv-g),abs(inv-b))
			self.ss = ss
		def Shoot(self):
			if ((self.x < -ss*2) or (self.x > screen.get_width()+ss) or (self.y < -ss-10) or (self.y > screen.get_height()+ss)):
				del s[s.index(self.ID)]
			if self.des == 0:
				self.velox,self.veloy = FindSpeed((xa,ya),(self.x,self.y),SS)
			if (xa+(150) > self.x > xa-(150)) and (ya-(150) < self.y < ya+(150)):
				self.des = 1
			if (self.des == 1 and self.ss > 0):
				self.ss -= ss/(10/(SS/10))
			if (self.ss < 0.2):
				self.ss = 0
			if (self.des == 0):
				self.ss = ss
			self.x += self.velox
			self.y += self.veloy
			if (self.ss != 0):
				pygame.draw.rect(screen, self.c, (self.x-self.ss/2,self.y-self.ss/2,self.ss,self.ss),hol)
	
	if pygame.mouse.get_pressed()[0]:
		if (r > 250):
			r1 = -1
		if (r < 140):
			r1 = 1	
		r += r1
		if (g > 250):
			g1 = -2	
		if (g < 140):
			g1 = 2
		g += g1
		if (b > 250):
			b1 = -4
		if (b < 140):
			b1 = 4
		b += b1
		
		if (rat == 0):
			for c in range(0,4):
				for i in range(0,ro+1):
					shot = Shot()
					shot.Assign(i,r,g,b,c,ro)
					s.append(shot)
		else:
			for c in range(1,5):
				for i in range(0,(ro+1) + 2*(c%2)):
					shot = Shot()
					shot.Assign(i,r,g,b,c-1,ro+2*(c%2))
					s.append(shot)
		
	for i in range(0,len(s)):
		try:
			s[i].Shoot()
		except IndexError:
			pass
			
	pygame.draw.rect(screen, (abs(inv-255),abs(inv-255),abs(inv-255)), (xa-100,ya-100,200,200), 2)
	
	pygame.display.flip()
	event = pygame.event.poll()
		
	if pygame.key.get_pressed()[pygame.K_ESCAPE]:
		break
