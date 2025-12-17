print(" chapter two: lists unlocked\n ")
# creating a list, square brackets = list
groceries = ["weed", "diet coke", "keto bread", "trappist beer", "egg bagles", "pipes"]
# show the whole list 
print("my grocery list:", groceries)
#how many items?
print("total items:", len(groceries))
# grab single items (index starts at 0)
print("first item:", groceries[0])
print("last item:", groceries[-1]) #negative index counts from the back
print("third item:", groceries[2])
#change an item
groceries[3] = "gambling juice" # replace beer with monster 
print("updated list:", groceries)
# add new stuff
groceries.append("oreos") 
print("after adding oreos:", groceries)
# remove something 
groceries.remove("pipes")
print("no more pipes:", groceries)
# quick check
if "weed" in groceries:
    print("dont forget the weed!")
else:
    print("we are out of weed?!?! end of the world!!!")
# your two new lines go here 
print("Items 2 through 4:", groceries[1:4])
groceries.sort()
print("sorted alphabetically:", groceries)
        