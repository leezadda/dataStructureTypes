"""
A List Of Data Structures (Created with OOP)
"""
#-------------------------------------------------------------------------

#Array
    #1. Create an empty array
        newArray = []
    #2. Append new elements
        newArray.append(example)
    #3. Read/print with for loop
        for i in range(len(newArray)):
            print(newArray[i])

#-------------------------------------------------------------------------

#Linked List 
TO BE CONTINUED
    #1. Create Node class
        class Node():
            def __init__(self, data):
                self.data = data
                self.next = None

    #2. Linking Nodes class
        class Link():
            def __init__(self):
                self.head = None

#-------------------------------------------------------------------------

#Stacks (pancakes)
    #Create an empty stack (literally an array)
        stack = []
    #Append() function to insert at end of stack
        stack.append('example')
    #Pop() fucntion to remove from end of stack
        stack.pop('example')

#-------------------------------------------------------------------------

#Queues (line of people)
    #Create an empty stack (literally an array)
        queue = []
    #Append() function to insert at end of queue
        queue.append('example')
    #Pop() fucntion to remove from end of stack
        queue.pop(0)

#-------------------------------------------------------------------------

#Graphs
    TO BE CONTINUED

#-------------------------------------------------------------------------

#Trees
    #1. Create Node class
        class Node():
            def __init__(self, data):
                self.data = data
                self.left = None
                self.right = None
    #2. Compare the new value with the parent node
        TO BE CONTINUED

#-------------------------------------------------------------------------

#Hash Tables (literally a dictionary)
    # Declare a dictionary 
        dict = {'Name': example, 'Age': example, 'Class': example}
    # Accessing the dictionary with its key
        dict['Name']

#-------------------------------------------------------------------------

LINKED-LISTS, GRAPHS, AND TREES.

misc: hashmap