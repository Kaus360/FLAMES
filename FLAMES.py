from tkinter import *
def remove_match_char(list1, list2):

	for i in range(len(list1)) :
		for j in range(len(list2)) :
			if list1[i] == list2[j] :
				c = list1[i]
				list1.remove(c)
				list2.remove(c)
				list3 = list1 + ["*"] + list2
				return [list3, True]

	list3 = list1 + ["*"] + list2
	return [list3, False]
def tell_status() :

# Player 1 algorithm	
	player1 = Player1_field.get()
	player1 = player1.lower()
	player1.replace(" ", "")
	player1_list = list(player1)

# Player 2 algorithm
	player2 = Player2_field.get()
	player2 = player2.lower()
	player2.replace(" ", "")
	player2_list = list(player2)

	proceed = True
	while proceed :
		ret_list = remove_match_char(player1_list, player2_list)
		con_list = ret_list[0]
		proceed = ret_list[1]
		star_index = con_list.index("*")
		
		player1_list = con_list[ : star_index]
		player2_list = con_list[star_index + 1 : ]

# Total characters remaining
	count = len(player1_list) + len(player2_list)

	# list of FLAMES acronyms
	result = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"]

	while len(result) > 1 :
		split_index = (count % len(result) - 1)

		# anti-clockwise circular fashion counting algorithm loop
		if split_index >= 0 :
			right = result[split_index + 1 : ]
			left = result[ : split_index]
			result = right + left

		else :
			result = result[ : len(result) - 1]

	Status_field.insert(10, result[0])


def clear_all() :
	Player1_field.delete(0, END)
	Player2_field.delete(0, END)
	Status_field.delete(0, END)
	Player1_field.focus_set()


# Driver code
if __name__ == "__main__" :
	window = Tk()
	window.configure(background = 'light green')
	window.geometry("350x125")
	window.title("FLAMES")
	
	label1 = Label(window, text = "Player 1 Name: ",
				fg = 'black', bg = 'dark green')

	label2 = Label(window, text = "Player 2 Name: ",
				fg = 'black', bg = 'dark green')
	
	label3 = Label(window, text = "Relationship Status: ",
				fg = 'black', bg = 'red')

	label1.grid(row = 1, column = 0, sticky ="E")
	label2.grid(row = 2, column = 0, sticky ="E")
	label3.grid(row = 4, column = 0, sticky ="E")

	Player1_field = Entry(window)
	Player2_field = Entry(window)
	Status_field = Entry(window)

	Player1_field.grid(row = 1, column = 1, ipadx ="50")
	Player2_field.grid(row = 2, column = 1, ipadx ="50")
	Status_field.grid(row = 4, column = 1, ipadx ="50")

	button1 = Button(window, text = "Submit", bg = "red",
					fg = "black", command = tell_status)

	button2 = Button(window, text = "Clear", bg = "red",
					fg = "black", command = clear_all)

	
	button1.grid(row = 3, column = 1)
	button2.grid(row = 5, column = 1)

	window.mainloop()
