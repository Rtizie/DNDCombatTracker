import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle

import Enemy as e

class App:
	enemies = []

	def __init__(self, master):

		addFrame = ttk.Frame(master)
		addFrame.pack()
		self.addEnemyInput = ttk.Entry(addFrame)
		self.addEnemyInput.pack(side=tk.LEFT)
		self.button = ttk.Button(addFrame, text="Add Enemy",command=self.add_enemy)
		self.button.pack(side=tk.LEFT)

		self.enemiesFrame = ttk.Frame(master,height=400,width=600)
		self.enemiesFrame.pack()


	def add_enemy(self):
		enemy_url = self.addEnemyInput.get()
		enemy = e.Enemy(enemy_url)
		self.enemies.append(enemy)
		enemyFrame = ttk.Frame(self.enemiesFrame)
		enemyFrame.pack()
		enemyLabel = ttk.Label(enemyFrame,text=enemy.getStats())
		enemyLabel.pack(side=tk.TOP)
		enemy.getAbilityBlock(enemyFrame)

if __name__=="__main__":

	root = tk.Tk()
	root.geometry("800x600")
	app = App(root)
	root.configure(background="#4b4b4b")
	root.title("D&D Combat Tracker")
	style = ThemedStyle()
	style.theme_use('equilux')
	root.mainloop()

#wolf = e.Enemy("https://www.dndbeyond.com/monsters/wolf")
#wolf.getStats()