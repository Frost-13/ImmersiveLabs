#-------------------------------------------------------------------------------
#Name: Kyle Chatterley
#Program: project.KC
#-------------------------------------------------------------------------------
from math import radians, sin, cos, sqrt, asin
import pickle
from graphics import*
import sys

#A function that displays the menu and goes through all the chocies and 
#  matches it with the one the user chose and starts the coresponding function
#  that goes with that choice
#Perameters: None
#Return: None
def main():
    choice = menu()
    while choice != "0":
        if choice == "1":        
            dictionary = load_shape_IDs()
            choice = menu()
            
        elif choice == "2":            
            lat_lon_dict = load_shapes()
            choice = menu()
            
        elif choice == "3":
            stops_dict = load_stops()
            choice = menu()            
            
        elif choice == "4":
            print_shapes(dictionary)
            choice = menu()
        
        elif choice == "5":
            print_points(lat_lon_dict)
            choice = menu()
            
        elif choice == "6":
            print_stops(stops_dict)
            choice = menu()
        
        elif choice == "7":
            save_pickle(dictionary, lat_lon_dict, stops_dict)
            choice = menu()
            
        elif choice == "8":
            dictionary, lat_lon_dict, stops_dict = load_pickle()
            choice = menu()
        
        elif choice == "9":
            win = draw_map()
            draw_hud(win, dictionary, lat_lon_dict, stops_dict)
            choice = menu()
        else:
            choice = input("Please enter a valid number\n\nEnter command: ")
#-------------------------------------------------------------------------------
#                                  menu
#-------------------------------------------------------------------------------
#a function that loads the menu and asks user for a command
#parameters: none
#return: menu choice chosen by user
def menu():
    print("\n    Edmonton Transit System")
    print("-----------------------------------")
    print('''(1) Load shape IDs from  GTFS file 
(2) Load shapes from GTFS file
(3) Load stops from GTS file
    
(4) Print shape IDs for a route 
(5) print points for a shape ID
(6) Print stops for a location

(7) Save shapes and shape IDs in a pickle
(8) Load shapes and shape IDs from a pickle

(9) Display interactive map

(0) Quit
''')
    choice = input("Enter command: ")
    return choice
#-------------------------------------------------------------------------------
#                                test file
#-------------------------------------------------------------------------------
#A function that checks to see if a file exists or can be opened
#    if it does it reads and saves the lines and closes the file
#if not it prints error statement and loops until user enters valid file
#Perameters: a text file selected by user
#return: text lines
def test_file(input_file):
    counter = 0
    
    while counter == 0:
        
        try:
            file = open(input_file,"r")
            lines = file.readlines()
            file.close()
            counter = 1
            return lines
        
        except:
            print("That file does not exist or cannot be oppened")
            input_file = input("enter a file name: ")
#-------------------------------------------------------------------------------
#                               prompt 1
#-------------------------------------------------------------------------------
#A function to take a text file and separate the route ids and id shapes 
#   into a dictionary. the key is the route id and the value is a set 
#   with all of the shape ids
#Parameters: text file
#return: dictionary of all the route ids and shape ids
def load_shape_IDs():
    
    #prompt user for a file
    input_file = input("Enter a file name [data/trips.txt]: ")
    
    #if user hits enter make input_file "data/trips.txt"
    if input_file == "" :
        input_file = "data/trips.txt" 
    
    # check to see if file works
    lines = test_file(input_file)
        
    #create empty dictionary
    ids_and_shapes = {}
    
    #create empty set
    shapes = set()
    
    #goes through every line and splits everything with a "," and puts it
    #    into a new list. puts the route id into dictionary as the key
    #    and the value will be a set of all the shapes 
    #    check to see if it's the title bar and skip it if it is 
    for line in lines:
        line = line.rstrip()        
        new = line.split(',')

        if new[0] == "route_id":
            print()
            
        else:
            if new[0] not in ids_and_shapes:
                shapes = set()
                
            shapes.add(new[-1])
            ids_and_shapes[new[0]] = shapes
            
    return ids_and_shapes 
#-------------------------------------------------------------------------------
#                                   prompt 4 
#-------------------------------------------------------------------------------
#A function that takes the dictionary from option 1 and uses it.
#   it then asks for a route which is the key. 
#   and prints all of the values attached to the key
#Parameters: a dictionary with route ids and route shapes
#return: none
def print_shapes(dictionary): 
    
    #prompt user for the route
    route = input("route? ")
    
    print("\nShape ID's for", route, ":")
    
    #tests to see if route exists as key in dictionary
    #   if it does it prints the shapes out one by one
    #   if not prints error statement
    counter = 0
    while counter == 0: 
        try:
            value = dictionary[route]
            counter = 1
            for item in value:
                print("\t", item)
        except:
            print("*** NOT FOUND ***")
            route = input("route? ")        
#-------------------------------------------------------------------------------
#                               prompt 2
#-------------------------------------------------------------------------------
#A function that asks user for a text file and puts all of the lats and lons 
#   in a dictionary as the values. the keys are the ID's
#Parameters: none
#return: a dictionary with ID's and corresponding lats and lons
def load_shapes():
    
    input_file = input("Enter a file name [data/shapes.txt]: ")
            
    #if user hits enter make input_file "data/shapes.txt"
    if input_file == "" :
        input_file = "data/shapes.txt"    
    
    lines = test_file(input_file)
        
    #create empty dictionary
    shapes_lat_lon = {}
    
    #create empty master list for lat and lon values
    master_list = []
    
    #goes through every line and splits everything with a "," and puts it
    #    into a new list. puts the shape id into dictionary as the key
    #    and the value will be a set of all latitude and longitude. 
    #    check to see if it's the title bar and skip it if it is 
    for line in lines:
        line = line.rstrip()        
        new = line.split(',')

        if new[0] == "shape_id":
            print()
        
        else:
            if new[-1] == "1":
    
                master_list = []
            #latitude = new[1]
            #longitude = new[2]
            
            lat_lon_tuple = (new[1], new[2])
            
            master_list.append(lat_lon_tuple)
            

            shapes_lat_lon[new[0]] = master_list
    return shapes_lat_lon
#-------------------------------------------------------------------------------
#                              prompt 5
#-------------------------------------------------------------------------------
#A function that prints all lats and lons of a user specified ID
#parameters: dictionary from prompt 2
#return: none
def print_points(lat_lon_dict):
    
    #prompt user for the shape Id
    shape_id = input("Shape ID? ")
    
    print("\nShape for", shape_id, ":")
    
    #tests to see if shape ID exists as key in dictionary
    #   if it does it prints the ID's out one by one
    #   if not prints error statement
    counter = 0
    while counter == 0:
        try:
            value = lat_lon_dict[shape_id]
            counter = 1
            for item in value:
                print("\t", "(", item[0], ",", item[1], ")")
        except:
            print("*** NOT FOUND ***")
            shape_id = input("Shape ID? ")
#-------------------------------------------------------------------------------
#                             PROMPT 7
#-------------------------------------------------------------------------------
# A function that saves shapes and IDs into a pickle 
# perameters: perviously loaded shape_ids and shapes
# return: None
def save_pickle(shape_IDs, shapes, stops_dict):
    
    # get file name from user
    file_name = input("Enter a file name [etsdata.p]: ")
    
    # if user hits enter name is = etsdata.p 
    if file_name == "":
        file_name = "etsdata.p"
    
    # create list with both shapes and ids
    master = [shape_IDs, shapes, stops_dict]
    
    # open a pickle file named as user specifide name
    output_file = open(file_name, 'wb')
    
    # put shapes and ids into the pickle and then close it
    pickle.dump(master, output_file)
    output_file.close
    

#-------------------------------------------------------------------------------
#                             PROMPT 8
#-------------------------------------------------------------------------------
#A progam that loads a perviously saved pickle from the useers computer files
#perameters: none
#return: the lists from the pickle and the lists contain the ids and shapes
#  respectivly
def load_pickle():
    
    # get user file name
    file_name = input("Enter a file name [etsdata.p]: ")
    
    #if user hits space then file name = etsdata.p
    if file_name == "":
        file_name = "etsdata.p"
    #check to see if file exists if it does loads shapes and ids and returns
    #   them to the main function
    #if not print error statment and bring user back to main menu
    try:
        output = open(file_name, 'rb')
        dicts = pickle.load(output)
        return dicts[0], dicts[1], dicts[2]        
    except:
        print("ERROR, File does not exist")  
        return [], []


#-------------------------------------------------------------------------------
#                                 PROMPT 9
#-------------------------------------------------------------------------------
#A program to make and draw the canvas and  makes plot box and with letter
#perameters: none
#return: the window created
def draw_map ():
    
    #draw canvas with edmonton map as background
    win = GraphWin("Edmonton Transit System", 630, 768)
    ed_map = Image(Point(315, 384), "background.gif")
    ed_map.draw(win)
    
    # visual representation of plot box
    plot_box = Rectangle(Point(110,20) ,Point(220,40))
    plot_box.setFill("white")
    plot_box.setOutline("black")
    plot_box.draw(win)   
    
    # put "plot" on top of plot_box
    plot = Text(Point(164, 31), "Plot")
    plot.setSize(10)
    plot.setTextColor("black") 
    plot.draw(win)    
    
    return win

#A program that creates the entry box and then gets user click
#  if user click is on plot box and valid route is in entry bok it plots points 
#  if not on plot box then it prints user clik x and y along with
#  lat and lon points 
#perameters: the window dictionary of shapes and shape ids for ploting 
# points later
# return: None
def draw_hud(win, dictionary, lat_lon_dict, stops_dict):
    
    # draw entry box
    entry = Entry(Point(50, 30), 10)
    entry.draw(win)
    
    # set to lat and lon coords
    win.setCoords(-113.7136, 53.39576, -113.2714, 53.71605)
    
    # see if user clicks screen or not and to pervent crash if "X" is hit
    while True:
        try:
            point = win.getMouse()
        except GraphicsError:
            return
        
        # x and y point
        x, y = win.toScreen(point.getX() , point.getY())
        
        #lat and lon points
        lat , lon = point.getX() , point.getY()
        
        # if user clicks plot button it will take the route and plot
        #   route on map
        if 220 > x > 110 and 40 > y >20:
                route = entry.getText()
                
                shape = get_longest(route, dictionary, lat_lon_dict)
                plot_points(win, shape, lat_lon_dict)
                
        
        # display user points on shell
        else:
            
            # Prints lon and lat
            print("Geographical (lat, lon):","(", lon, ",", lat,")")
            
            # prints x and y            
            print("Pixle (x, y):","(", x, ",", y,")")
            
            #print to screen right away
            sys.stdout.flush()
            
            # find the closest stops to user click
            closest = find_closest(lat, lon, stops_dict)
            
            # print the closest points on the shell
            print_nearest(closest)
            
            # draw the closest stops on the map/ window
            draw_points(win, closest)
            
            
#A function to go through all the ids find the longest one then print 
# the lat and lon points from the shapes dictionary
#perameters:route chosen by user, dictionary 
# of ids and dictionary of shapes aka lat and lon points
#Return: shape which is the longest lat and lon list for the route
def get_longest(route, dictionary, lat_lon_dict ):
    
    # initiate counters and the shape id storage
    longest = 0
    shape = ""
    
    #try and except statment to see if route exists
    # if it does exist goes through shape ids and saves the one with the most
    # lat/lon points
    #if it doesnt exist return nothing
    try:
        shape_id= dictionary[route]
        
        for item in shape_id:
            
            length = len(lat_lon_dict[item]) 
            
            
            if length > longest:
                longest = length
                shape = item
                
        return shape
    except:
        return print("Route does not exist")

#A program that uses the longest shape id and uses the shape lats and
#  lons and makes a line between the points to draw a route on the map
#Perameters: the window to drw on, lat and lon list (shape), the lat 
# and lon dictionary 
#Return: none
def plot_points(win, shape, lat_lon_dict):
    
    # initiate counter for first lat and lon points
    counter = 0
    
    # a loop that goes through each lat and lon point and saves them as x2 and 
    # y2 draws a line between x1,y1 and x2,y2 and saves current x2, y2 
    # as x1,y1 for next initiation of the loop
    try:
        for point in lat_lon_dict[shape]:
            
            # for the first point it only saves them as x1 and y1 without 
            # drawing till x2 and y2 have values
            if counter == 0:
                y1 = float(point[0])
                x1 = float(point[1])
                counter = 1
            
            else: 
                y2 = float(point[0])
                x2 = float(point[1])
                
                line = Line( Point(x1,y1) , Point(x2,y2) )
                line.setFill("gray50")
                line.setWidth(3)
                line.draw(win)  
                
                y1 = y2
                x1 = x2
    except:
        return

#-------------------------------------------------------------------------------
#                               PROMPT 3
#-------------------------------------------------------------------------------
#A function that takes a user file of stops and puts them into a dictionary. 
#  the key is the lat and lon points in  a tuple
#Perameters: None
#Return: dictionary with all the stops and their info 
def load_stops():
    
    # get file name from user
    file_name = input("Enter a file name [data/stops.txt]: ")
    
    # if user hits enter make file name data/stops.txt
    if file_name == "":
        file_name = "data/stops.txt"
    
    # test to see if file exists    
    lines = test_file(file_name)
    
    # remove first line
    lines.pop(0)
    
    # create dictionary
    stops_dict = {}
    
    # goes through each line in the file strips it and makes the lst and lon the key snd the value is a list of the stop number and the street name
    for line in lines:
        line = line.strip()        
        line = line.split(',')
        
        stops_dict[(line[4].strip(), line[5])] = [line[0], line[2].strip('"')]
    
                
    return stops_dict
#-------------------------------------------------------------------------------
#                              PROMPT 6
#-------------------------------------------------------------------------------
#A function that prints the stop number and the street from a user specifide 
#  lat and lon point
#Perameters: dictionary with all the stops 
def print_stops(stops_dict):
    
    # get lat and lon location from user
    location = input("Location as 'lat,lon'? ")
    
    # print the header
    print("\nstops for ("+location+"):")
    
    # put user location into a tuple
    loc = location.split(",")
    location = (loc[0], loc[1].strip())
    
    # if lat and lon exists print the stop number and the street name if not 
    # print error statment
    try:
        print("\t", stops_dict[location][0], "\t", stops_dict[location][1])
            
    except:
        print("\t** NOT FOUND **")
        
#-------------------------------------------------------------------------------
#                    5 nearest points on map
#-------------------------------------------------------------------------------
#A program to calculate the closestpoints and saves them in a list of lists
#perameters: user lat and lon points, the stops dictionary
#Return: the first 5 lists in the distance_list
def find_closest(lat, lon, stops_dict):
    # create an empty list
    distance_list = []
    
    # go through all the keys in the stops dictionary. put the user lat and lon
    # into the haversine function and the lat and lon from the dictionary to
    # get the distance for each bus stop and adds it to the empty list 
    for key in stops_dict:
        distance = haversine(float(lon), float(lat), float(key[0]), float(key[1]))
        
        temp = [distance, stops_dict[key], key]
        distance_list.append(temp)
    
    # sort the list by the shortest distance first longest last    
    distance_list.sort()
    
    # return the top five in the lsit (the 5 shortest distances)
    return distance_list[:5]

    
#A function to  calculate the the distance between 2 points in meters
#Obbtained from:  https://rosettacode.org/wiki/Haversine_formula.
#Perameters: 2 latatuid points and 2 longitude points
#Return: the distance in meters between the two lat and lon points
def haversine(lat1, lon1, lat2, lon2):
    R = 6372.8 * 1000 # Earth radius in meters
 
    dLat = radians(lat2 - lat1)
    dLon = radians(lon2 - lon1)
    lat1 = radians(lat1)
    lat2 = radians(lat2)
    
    a = sin(dLat/2)**2 + cos(lat1)*cos(lat2)*sin(dLon/2)**2
    c = 2*asin(sqrt(a))
    
    return R * c
#-------------------------------------------------------------------------------
#                           Draw the 5 points
#-------------------------------------------------------------------------------
#A function that plots the five closest points to the users lat and lon
#Perameters: the window and the 5 of the  closest stops lists 
#Return: None
def draw_points(win, closest):
    
    # go through the list list of lists
    for item in closest:
        
        #get x point
        long = float(item[2][1])
        
        #get y point
        lat = float(item[2][0])
        
        # set window coordinates to edmonton lat and lon
        win.setCoords(-113.7136, 53.39576, -113.2714, 53.71605)
        
        # set and draw the points using the x and y created previously
        point = Point(long, lat)
        point.draw(win)


#A function prints the distance the stop number and the description on the 
#   shell
#Perameters: the 5 closest list
#REturn: None
def print_nearest(closest):
    
    # print the header
    print("\nNearest stops:\n\tDistance   Stop    Description")
    
    # go through the list of lists and print the distance the stop and
    # the description accordingly
    for item in closest:
        print ("\t", round(float(item[0]), 1), "  ", item[1][0],\
               "  ", item[1][1])
        
    # makes the text come out instantly    
    sys.stdout.flush()
    



