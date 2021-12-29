from tkinter import *

import Enemy as e

class App:
	enemies = []

	def __init__(self, master):

		addFrame = Frame(master)
		addFrame.pack()
		self.addEnemyInput = Entry(addFrame)
		self.addEnemyInput.pack(side=LEFT)
		self.button = Button(addFrame, text="Přidej Enemy", fg="black", command=self.add_enemy)
		self.button.pack(side=LEFT)

		self.enemiesFrame = Frame(master,bg="yellow",height=400,width=600)
		self.enemiesFrame.pack()


	def add_enemy(self):
		enemy_url = self.addEnemyInput.get()
		enemy = e.Enemy(enemy_url)
		self.enemies.append(enemy)
		enemyFrame = Frame(self.enemiesFrame)
		enemyFrame.pack()
		enemyLabel = Label(enemyFrame,text=enemy.getStats())
		enemyLabel.pack(side=TOP)

if __name__=="__main__":

	root = Tk()
	root.geometry("800x600")
	app = App(root)
	root.mainloop()

#wolf = e.Enemy("https://www.dndbeyond.com/monsters/wolf")
#wolf.getStats()