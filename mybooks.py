mybooks = {
	"prose": ("Things Fall Apart", "Joys of Motherhood"),
	"drama": ("The Lion and the Jewel", "The gods are not to blame")

}

user_choice = input("Select prose or drama: \n")

#if statement to get the book category
if user_choice == "prose":
	books = mybooks[user_choice]
	print(f"Here are the books in this category \n{books}")
	specific = int(input("Type 0 or 1 to retrieve a book: \n"))
#end of book category selection

	#if statement to get a specific book
	if specific == specific:
		retrieve = mybooks[user_choice][specific]
		print(f"""
			We have found your book
			{retrieve}
			""")	
	else:
		print("We couldnt find your book")
		#end of specific book selection

elif user_choice == "drama":
	books = mybooks[user_choice]
	print(f"Here are the books in this category \n{books}")
else:
	print("Your input can't be found")
input()