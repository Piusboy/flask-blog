from Blog import blog

# __name__ changes to __main__ whenever the file is running
if __name__ == "__main__":
    blog = blog()
    blog.run(debug = True, port = 3000) # for Development purpose


