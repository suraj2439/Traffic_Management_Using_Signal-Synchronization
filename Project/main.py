import pygame as pg
import time
import random
import matplotlib.pyplot as plt
import numpy as np
#import thread
plt.ion()
TOT_NODES = 9
NODE_SIGNALS = 3
TIME_REM = 5
RED, GREEN = 0, 1
NO_OF_VEH = 170

pg.init()
length, width = 1366, 768
screen = pg.display.set_mode((length, width))
pg.display.set_caption('Traffic Signal Syncronizatio.')

bg = pg.image.load('road.png')
bg = pg.transform.scale(bg, (length, width))
red = pg.image.load('red.png')
red = pg.transform.scale(red, (40, 40))
green = pg.image.load('green.png')
green = pg.transform.scale(green, (40, 40))
veh = pg.transform.scale(green, (15, 15))   #remove
screen.blit(bg, (0, 0))

horr, vert = 10,20
class root:
    def __init__(self, symm, w_start, w_middle, w_end, l_start, l_end, r_next, node_list, lane = 2):
        self.symm = symm
        self.w_start = w_start
        self.w_middle = w_middle
        self.w_end = w_end
        self.l_start = l_start
        self.l_end = l_end
        self.r_next = r_next
        self.lane = lane
        self.next_nodes = node_list


signals = [[[5, GREEN, (940, 165)], 
    [2, RED, (1100, 165)], [3, RED, (1100, 315)], [7, RED, (940, 315)]]]
def init_sig_info():
    for i in range (TOT_NODES - 1):
        signals.append([[6, RED, (0, 0)], [4, GREEN, (0, 0)], [1, GREEN, (0, 0)]])

    signals[1][0][2] = (10, 165)
    signals[1][1][2] = (115, 165)
    signals[1][2][2] = (115, 315)

    signals[2][0][2] = (222, 165)
    signals[2][1][2] = (335, 315)
    signals[2][2][2] = (222, 315)

    signals[3][0][2] = (418, 165)
    signals[3][1][2] = (528, 165)
    signals[3][2][2] = (528, 315)

    signals[4][0][2] = (650, 165)
    signals[4][1][2] = (765, 315)
    signals[4][2][2] = (650, 315)

    signals[5][0][2] = (70, 455)
    signals[5][1][2] = (175, 565)
    signals[5][2][2] = (70, 565)

    signals[6][0][2] = (222, 455)
    signals[6][1][2] = (335, 455)
    signals[6][2][2] = (335, 565)

    signals[7][0][2] = (650, 455)
    signals[7][1][2] = (765, 455)
    signals[7][2][2] = (650, 565)

    signals[8][0][2] = (1100, 583)
    signals[8][1][2] = (1100, 695)
    signals[8][2][2] = (940, 695)

    for node_id in range (TOT_NODES):
        ts = 3
        if node_id == 0:
            ts = 4
        for sig_id in range (ts):
            if signals[node_id][sig_id][1] == RED:
                screen.blit(red, signals[node_id][sig_id][2])
            else:
                screen.blit(green, signals[node_id][sig_id][2])

sig_pos = ((980, 205, 1100, 315), (50, 205, 115), (262, 315, 335),
           (458, 205, 528), (690, 765, 315), (110, 175, 565),
           (262, 335, 495), (690, 565, 495), (1100, 623, 695) )

class node:
    def __init__(self):
        pass
    def pos(node_id):
        nd_arr = [[1042, 260], [82, 260], [300, 260], [495, 260], 
                [730, 260], [143, 528], [300, 528], [730, 528], [1042, 660]]
        return nd_arr[node_id]

    def signal_id(node_id, signal_pos):
        for sig_id in range (len(sig_pos[node_id])):
            if sig_pos[node_id][sig_id] == signal_pos:
                return sig_id
        else:
            assert 0

class sig_info:
    def __init__(self):
        pass
    def time_rem(node_id, sig_id):
        time_rem = sigals[node_id][sig_id][0]
        return time_rem
    
    def state(node_id, sig_id):
        state = signals[node_id][sig_id][1]
        return state

roots = (root(horr, 205, 260, 315, 0, 50, ((9, -1, 1, -1),(-1, -1, -1, -1)), [1], 4),
         root(horr, 205, 260, 315, 115, 262, ((-1, 11, 2, -1), (9, -1, -1, 0)), (1, 2), 4),
         root(horr, 205, 260, 315, 335, 458, ((10, -1, 3, -1),(-1, 11, -1, 1)), (2, 3), 4),
         root(horr, 205, 260, 315, 528, 690, ((-1, 12, 4, -1),(10, -1, -1, 2)), (3, 4), 4),
         root(horr, 205, 260, 315, 765, 980, ((6, 7, 5, -1),(-1, 12, -1, 3)), (4, 0), 4),
         root(horr, 205, 260, 315, 1100, 1370, ((-1, -1, -1, -1),(6, 7, -1, 4)), [0], 4),
         root(vert, 980, 1042, 1100, 0, 205, ((-1, -1, -1, -1),(-1, 7, 5, 4)), [0], 4),
         root(vert, 980, 1042, 1100, 315, 623, ((6, -1, 5, 4),(-1, 8, 18, -1)), (0, 8), 4),
         root(vert, 980, 1042, 1100, 695, 770, ((7, -1, 18, -1),(-1, -1, -1, -1)), [8], 4),
         root(vert, 50, 82, 115, 0, 205, ((-1, -1, -1, -1),(-1, -1, 1, 0)), [1]),
         root(vert, 458, 495, 528, 0, 205, ((-1, -1, -1, -1),(-1, -1, 3, 2)), [3]),
         root(vert, 262, 300, 335, 315, 495, ((-1, -1, 2, 1),(-1, -1, 16, 15)), (2, 6)),
         root(vert, 690, 730, 765, 315, 495, ((-1, -1, 4, 3),(-1, 13, -1, 16)), (4, 7)),
         root(vert, 690, 730, 765, 565, 770, ((12, -1, -1, 16),(-1, -1, -1, -1)), [7]),
         root(horr, 495, 528, 565, 0, 110, ((-1, 17, 15, -1),(-1, -1, -1, -1)), [5]),
         root(horr, 495, 528, 565, 175, 262, ((11, -1, 16, -1),(-1, 17, -1, 14)), (5, 6)),
         root(horr, 495, 528, 565, 335, 690, ((12, 13, -1, -1),(11, -1, -1, 15)), (6, 7)),
         root(vert, 110, 143, 175, 565, 770, ((-1, -1, 15, 14),(-1, -1, -1, -1)), [5]),
         root(horr, 623, 660, 695, 1100, 1370,((-1, -1, -1, -1),(7, 8, -1, -1)), [8]) )
    

# Class representing the vehicle
class Vehicle:
	def __init__(self, length, colour, position_x, position_y, road_no, lane_no, direction):
		self.position_x = position_x
		self.position_y = position_y
		self.length = length
		self.width = 10
		self.colour = colour
		self.road_no = road_no
		self.lane_no = lane_no
		self.direction = direction





'''
Explanation for the meaning of lane number. The tuple road_lanes_dimensions below contains the details of the dimensions for each lane of each road.
4-lane roads are represented by a tuple of 5 tuples. 2 -lane roads are represented by a tuple of 3 tuples.
In either case, the first tuple in the road-tuple is used to represent the starting and ending limits for coordinate common to all the lanes.
That is, for a road along the east-west direction, the first argument is a tuple containing the starting Y coordinate and the ending Y coordinate
(in that order) for all the lanes in that road.
For a road along the north-south direction, the first argument is a tuple containing the starting X coordinate and the ending X coordinate (in that order)
for all the lanes in that road.
The remaining elements of the road-tuple are the width-coordinates of the specific lanes. These elements are in the order of lanes from west to east for a north-south
road, and from north to south for an east-west road.
So, for a north-south road of 4 lanes, the road-tuple has the 2nd element as the westernmost lane towards the north. The 3rd element is the easternmost lane
towards the north. The 4th element is the westernmost lane towards the south and the 5th element is the easternmost lane towards the south.
A 2-lane road has lane with numbers 1 and 2, while a 4-lane road has lanes with numbers 1, 2, 3 and 4.


'''
road_lanes_dimensions = []
road_lanes_dimensions.append( ((0, 50), (205, 233), (233, 260), (260, 285), (285, 315)) )
road_lanes_dimensions.append( ((115, 262), (205, 233), (233, 260), (260, 285), (285, 315)) )
road_lanes_dimensions.append( ((335, 458), (205, 233), (233, 260), (260, 285), (285, 315)) )
road_lanes_dimensions.append( ((528, 690), (205, 233), (233, 260), (260, 285), (285, 315)) )
road_lanes_dimensions.append( ((765, 980), (205, 233), (233, 260), (260, 285), (285, 315)) )
road_lanes_dimensions.append( ((1100, 1370), (205, 233), (233, 260), (260, 285), (285, 315)) )
road_lanes_dimensions.append( ((0, 205), (980, 1012), (1012, 1042), (1042, 1072), (1072, 1100)) )
road_lanes_dimensions.append( ((315, 623), (980, 1012), (1012, 1042), (1042, 1072), (1072, 1100)) )
road_lanes_dimensions.append( ((695, 770), (980, 1012), (1012, 1042), (1042, 1072), (1072, 1100)) )
road_lanes_dimensions.append( ((0, 205), (50, 82), (82, 115)) )
road_lanes_dimensions.append( ((0, 205), (458, 495), (495, 528)) )
road_lanes_dimensions.append( ((315, 495), (262, 300), (300, 335)) )
road_lanes_dimensions.append( ((315, 495), (690, 730), (730, 765)) )
road_lanes_dimensions.append( ((565, 770), (690, 730), (730, 765)) )
road_lanes_dimensions.append( ((0, 110), (495, 528), (528, 565)) )
road_lanes_dimensions.append( ((175, 262), (495, 528), (528, 565)) )
road_lanes_dimensions.append( ((335, 690), (495, 528), (528, 565)) )
road_lanes_dimensions.append( ((565, 770), (110, 143), (143, 175)) )
road_lanes_dimensions.append( ((1100, 1370), (623, 660), (660, 695)) )

road_lanes_dimensions = tuple(road_lanes_dimensions)


vehicles = []

'''
This is a list of the same number of elements as the number of roads. Each element is a list of 'n' lists, where 'n' is the number of lanes on that road.
Each of those 'n' lists mentioned in the previous statement is a list of the vehicle IDs of all the vehicles in that particular lane

'''

vehicles_in_each_lane = []

# Initialising vehicles_in_each_lane

for i in range(len(road_lanes_dimensions)):
	vehicles_in_each_lane.append([])
	for j in range(1, len(road_lanes_dimensions[i])):
		vehicles_in_each_lane[i].append([])


def choose_lane(road_no):
	lane_no = random.randint(1, len(road_lanes_dimensions[road_no]) - 1)
	lane_specific_dimensions = road_lanes_dimensions[road_no][lane_no]
	lane_common_dimensions = road_lanes_dimensions[road_no][0]
	return(lane_no, lane_specific_dimensions, lane_common_dimensions)


def generate_random_coordinates(symm, lane_specific_dimensions, lane_common_dimensions, length, width):

	# If the road is along the east-west direction
	if symm == horr:
		# Try random values of coordinates in the lane
		try_position_x = random.randint(lane_common_dimensions[0], lane_common_dimensions[1] - length)
		try_position_y = (lane_specific_dimensions[0] + lane_specific_dimensions[1] - width) // 2

	# If the road is along the north-south direction
	else:

		# Try random values of coordinates in the lane
		try_position_x = (lane_specific_dimensions[0] + lane_specific_dimensions[1] - width) // 2
		try_position_y = random.randint(lane_common_dimensions[0], lane_common_dimensions[1] - length)

	return (try_position_x, try_position_y)



def check_overlap(symm, vehicle_i_position_x, vehicle_i_position_y, vehicle_i_length, vehicle_i_width, try_position_x, try_position_y, length, width):

	ok = False

	# If the road is along the east-west direction
	if symm == horr:
	
		# Check if the X coordinates overlap
		if (0 <= vehicle_i_position_x - try_position_x <= length or 0 <= try_position_x - vehicle_i_position_x <= vehicle_i_length):

			# If the X coordinates as well as the Y coodinates overlap, then the vehicles overlap
			if(0 <= vehicle_i_position_y - try_position_y <= width or 0 <= try_position_y - vehicle_i_position_y <= vehicle_i_width):
				ok = False

			# If only the X coordinates overlap, then there is no conflict between the 'main' vehicle and the vehicle_i
			else:
				ok = True

		# If the X coordinates do not overlap, then there is no conflict between the 'main' vehicle and the vehicle_i
		else:
			ok = True

	# If the road is along the north-south direction
	else:

		# Check if the X coordinates overlap
		if(0 <= vehicle_i_position_x - try_position_x <= width or 0 <= try_position_x - vehicle_i_position_x <= vehicle_i_width):

			# If the X coordinates as well as the Y coodinates overlap, then the vehicles overlap
			if(0 <= vehicle_i_position_y - try_position_y <= length or 0 <= try_position_y - vehicle_i_position_y <= vehicle_i_length):
				ok = False

			# If only the X coordinates overlap, then there is no conflict between the 'main' vehicle and the vehicle_i
			else:
				ok = True

		# If the X coordinates do not overlap, then there is no conflict between the 'main' vehicle and the vehicle_i
		else:
			ok = True

	# Return whether the Y coordinate of the 'main' vehicle has been changed or not and whether or not there is any conflict between the 'main' vehicle and the vehicle_i
	return ok

CHOOSE_POSITION_FAILED = (-1, -1)

def choose_position(road_no, lane_no, lane_specific_dimensions, lane_common_dimensions, length, width):


	# Try random values of coordinates in the lane
	try_position_x, try_position_y = generate_random_coordinates(roots[road_no].symm, lane_specific_dimensions, lane_common_dimensions, length, width)

	# Initialise counter for vehicles to check against for overlap
	i = 0

	# True if the position of the 'main' vehicle is changed because it overlapped with the ith vehicle
	changed = False
	
	# Number of times the vehicle's position has been changed
	change_count = 0

	# Repeat for all vehicles
	while(i < len(vehicles) and change_count <= 100): 
		# If the vehicle[i] is on the same road and in the same lane as the 'main' vehicle
		if vehicles[i].road_no == road_no and vehicles[i].lane_no == lane_no:
			ok = check_overlap(roots[road_no].symm, vehicles[i].position_x, vehicles[i].position_y, vehicles[i].length, vehicles[i].width, try_position_x, try_position_y, length, width)
			if (not ok):
				try_position_x, try_position_y = generate_random_coordinates(roots[road_no].symm, lane_specific_dimensions, lane_common_dimensions, length, width)
				change_count += 1
				i = 0
				continue
			else:
				i += 1
		else:
			i += 1

	if i >= len(vehicles):
		return try_position_x, try_position_y
	return CHOOSE_POSITION_FAILED


# initialise_vehicles
def initialise_vehicles():

	global vehicles
	global vehicles_in_each_lane
	tuple_of_colours = ('forestgreen', 'blue', 'red', 'black', 'brown', 'purple', 'navyblue', 'magenta', 'darkgreen', 'tomato2')	
	for i in range(NO_OF_VEH):
		
		# Number of attempts to assign a road and lane to vehicle[i]
		attempt_count = 0


		length = random.randint(15, 30)
		width = 10
		colour = random.choice(tuple_of_colours)

		# Initialising position_x, position_y, road_no and lane_no  to invalid values
		position_x, position_y = CHOOSE_POSITION_FAILED
		road_no = -1
		lane_no = -1

		# While attempts are less than 100, try placing the vehicle in a random road and lane	
		while (position_x, position_y) == (CHOOSE_POSITION_FAILED) and attempt_count < 100:
			road_no = random.randint(0, 18)
			lane_no, lane_specific_dimensions, lane_common_dimensions = choose_lane(road_no)
			position_x, position_y = choose_position(road_no, lane_no, lane_specific_dimensions, lane_common_dimensions, length, width)
			attempt_count += 1

		if (position_x, position_y) == (CHOOSE_POSITION_FAILED):
			print("Too many vehicles(", (i+1), ") placed")
			return
		

		# Determining the direction of motion using the lane number and road direction

		if(roots[road_no].symm == horr):
			if(lane_no <= (len(road_lanes_dimensions[road_no]) - 1) // 2):
				direction = "East"
			else:
				direction = "West"
		else:
			if (lane_no <= (len(road_lanes_dimensions[road_no]) - 1) // 2):
				direction = "North"
			else:
				direction = "South"


		# Append vehicle[i] to list
		vehicles.append(Vehicle(length, colour, position_x, position_y, road_no, lane_no, direction)) 

		# Append i to the proper lane list in vehicles_in_each_lane. This means that vehicle number i is now on lane lane_no of road road_no
		vehicles_in_each_lane[road_no][lane_no - 1].append(i)

		# Draw vehicle[i]
		if roots[road_no].symm == horr:
			vehicle_diagram = pg.Rect(position_x, position_y, length, width)
		else:
			vehicle_diagram = pg.Rect(position_x, position_y, width, length)


		pg.draw.rect(screen, pg.color.THECOLORS[colour], vehicle_diagram)




def signal_show():
    global ref_time
    curr_time = int(time.time())

    if(curr_time - ref_time >= 1):
        ref_time = curr_time
        for node_id in range (TOT_NODES):
            if node_id == 0:
                ts = 4
            else:
                ts = 3
            for sig_id in range (ts):
                if(signals[node_id][sig_id][1] == GREEN):
                    if(signals[node_id][sig_id][0]):
                        signals[node_id][sig_id][0] -= 1
                    else:
                        signals[node_id][sig_id][0] = TIME_REM
                        signals[node_id][sig_id][1] = RED
                        screen.blit(red, signals[node_id][sig_id][2])
                        temp = sig_id + 1
                        if temp > (ts -1):
                            temp = 0
                        signals[node_id][temp][1] = GREEN
                        screen.blit(green, signals[node_id][temp][2])
    else: return



def add_extra_time(time, node_id, sig_id):
    if node_id == 0:
        ts = 3
        quo = time % 3
        rem = time // 3
    else:
        ts = 1
        quo = time % 2
        rem = time // 2
    temp = sig_id
    offset = 1
    for i in range (ts):
        quo -= 1
        if(quo < 0):
            offset = 0
        temp += 1
        if temp > ts:
            temp = 0
        signals[node_id][temp][0] += (rem + offset)
    return


def get_info_from_veh(pos_x, pos_y, veh_dir, root_no):
    node_lst = roots[root_no].next_nodes
    if len(node_lst) == 1:
        node_id = node_lst[0]
        pos = node.pos(node_id)
    else:
        if veh_dir == "West" or veh_dir == "North":
            node_id = node_lst[0]
            pos = node.pos(node_id)
        else:
            node_id = node_lst[1]
            pos = node.pos(node_id)

    if roots[root_no].symm == horr:
        if len(node_lst) == 1:
            if (veh_dir == "East" and pos[0] - pos_x < 0) or (veh_dir == "West" and
                    pos[0] - pos_x > 0):
                return -1, -1, -1   #no sigal

        if (veh_dir == "East"):
            sig_pos = roots[root_no].l_end
        else:
            sig_pos = roots[root_no].l_start

        sig_id = node.signal_id(node_id, sig_pos)
        return node_id, sig_id, sig_pos
    else:
        if len(node_lst) == 1:
            if (veh_dir == "South" and pos[1] - pos_y < 0) or (veh_dir == "North" and 
                    pos[1] - pos_y > 0):
                return -1, -1, -1
        if veh_dir == "South":
            sig_pos = roots[root_no].l_end
        else:
            sig_pos = roots[root_no].l_start

        sig_id = node.signal_id(node_id, sig_pos)
        return node_id, sig_id, sig_pos

def get_signal_info(pos_x, pos_y, veh_dir, root_no):
    node_id, sig_id, sig_pos = get_info_from_veh(pos_x, pos_y, veh_dir, root_no)
    if (node_id == -1):
        return 0, -1, -1    #no signal
    else:
        sig_state = signals[node_id][sig_id][1]
        if veh_dir == "East" or veh_dir == "West":
            if abs(sig_pos - pos_x) < 30:
                return 1, sig_state, node_id
            else: return 0, sig_state, node_id
        else:
            if abs(sig_pos - pos_y) < 30:
                return 1, sig_state, node_id
            else: return 0, sig_state, node_id  #1 for in signal range and 0 for not in signal range
	

ref = 10
den_sig = [[set([]),set([]),set([]),set([])],[set([]),set([]),set([])],[set([]),set([]),set([])],[set([]),set([]),set([])],[set([]),set([]),set([])],[set([]),set([]),set([])],[set([]),set([]),set([])],[set([]),set([]),set([])],[set([]),set([]),set([])],[set([])]]
'''den_sig[0][0] = [()]
den_sig[0][1] = [()]
den_sig[0][2] = [()]
den_sig[0][3] = [()]
den_sig[1][0] = [()]
den_sig[1][1] = [()]
den_sig[1][2] = [()]
den_sig[2][0] = [()]
den_sig[2][1] = [()]
den_sig[2][2] = [()]
den_sig[3][0] = [()]
den_sig[3][1] = [()]
den_sig[3][2] = [()]
den_sig[4][0] = [()]
den_sig[4][1] = [()]
den_sig[4][2] = [()]
den_sig[5][0] = [()]
den_sig[5][1] = [()]
den_sig[5][2] = [()]
den_sig[6][0] = [()]
den_sig[6][1] = [()]
den_sig[6][2] = [()]
den_sig[7][0] = [()]
den_sig[7][1] = [()]
den_sig[7][2] = [()]
den_sig[8][0] = [()]
den_sig[8][1] = [()]
den_sig[8][2] = [()]'''

def append_density(i,a,b):
    ele = i
    den_sig[a][b].add(ele)
    
    
def remove_density(i,a,b):
    den_sig[a][b].discard(i)

class signal_density_manager():
    def __init__(self,contact,s0,n0,s1,n1,s2,n2,s3,n3):
        self.number = contact
        self.s0 = s0
        self.n0 = n0
        self.s1 = s1
        self.n1 = n1
        self.s2 = s2
        self.n2 = n2
        self.s3 = s3
        self.n3 = n3
        self.stat = 0
    def get_density(self):
        self.self_density = len(den_sig[self.s0][self.n0])
        self.acc_den1 = len(den_sig[self.s1][self.n1])
        self.acc_den2 = len(den_sig[self.s2][self.n2])
        self.acc_den3 = len(den_sig[self.s3][self.n3])
    def manage_density(self):
        if(self.self_density >= 10 or self.stat == 1):
            self.stat = 1
            count = 3
            if(self.s1 != 9 and self.acc_den1 <= 10):
                add_extra_time(1,self.s1,self.n1)
                count = count - 1
            if(self.s2 != 9 and self.acc_den2 <= 10):
                if(count == 2):
                    add_extra_time(1,self.s2,self.n2)
                    count = count - 1
                else:
                    add_extra_time(1,self.s2,self.n2)
            if(self.s3 != 9 and self.acc_den3 <= 10):
                if(count == 1):
                    add_extra_time(1,self.s3,self.n3)
                else:
                    add_extra_time(1,self.s3,self.n3)
            sig_arr = [0,1,2,3]
            if(self.s0 != 0):
                sig_arr.remove(3)
            for h in range(0,len(sig_arr)):
                signals[self.s0][sig_arr[h]][1] = RED
          #      signals[self.s0][sig_arr[h]][0] = 5 + h
            signals[self.s0][self.n0][1] = GREEN
        if(self.self_density <= 8 or self.stat == 0):
            self.stat = 0
            sig_arr = [0,1,2,3]
            if(self.s0 != 0):
                sig_arr.remove(3)
            for h in range(0,len(sig_arr)):
                signals[self.s0][sig_arr[h]][1] = RED
#                signals[self.s0][sig_arr[h]][0] = 5 + h
            signals[self.s0][self.n0][1] = RED
            sig_arr.remove(self.n0)
            if (len(sig_arr) == 1):
                signals[self.s0][sig_arr[0]][1] = GREEN
            else:
                if(len(den_sig[self.s0][sig_arr[0]]) >= len(den_sig[self.s0][sig_arr[1]])):
                    signals[self.s0][sig_arr[0]][1] = GREEN
                else:
                    signals[self.s0][sig_arr[1]][1] = GREEN 
                    
                    
signal_system = []
ss1 = signal_density_manager(2,0,0,4,0,4,1,9,0)
signal_system.append(ss1)
ss1 = signal_density_manager(0,0,1,9,0,9,0,9,0)
signal_system.append(ss1)
ss1 = signal_density_manager(0,0,2,9,0,9,0,9,0)
signal_system.append(ss1)
ss1 = signal_density_manager(2,0,3,8,0,8,1,9,0)
signal_system.append(ss1)
ss1 = signal_density_manager(0,1,0,9,0,9,0,9,0)
signal_system.append(ss1)
ss1 = signal_density_manager(2,1,1,2,0,3,0,9,0)
signal_system.append(ss1)
ss1 = signal_density_manager(1,1,2,2,2,9,0,9,0)
signal_system.append(ss1)
ss1 = signal_density_manager(1,2,0,1,1,9,0,9,0)
signal_system.append(ss1)
ss1 = signal_density_manager(2,2,1,3,1,3,2,9,0)
signal_system.append(ss1)
ss1 = signal_density_manager(2,2,2,6,0,2,2,9,0)
signal_system.append(ss1)
ss1 = signal_density_manager(2,3,0,2,0,2,2,9,0)
signal_system.append(ss1)
ss1 = signal_density_manager(0,3,1,9,0,9,0,9,0)
signal_system.append(ss1)
ss1 = signal_density_manager(2,3,2,4,1,4,2,9,0)
signal_system.append(ss1)
ss1 = signal_density_manager(2,4,0,3,1,3,0,9,0)
signal_system.append(ss1)
ss1 = signal_density_manager(3,4,1,0,2,0,1,0,3)
signal_system.append(ss1)
ss1 = signal_density_manager(2,4,2,7,0,7,2,9,0)
signal_system.append(ss1)
ss1 = signal_density_manager(0,5,0,9,0,9,0,9,0)
signal_system.append(ss1)
ss1 = signal_density_manager(2,5,1,6,1,6,2,9,0)
signal_system.append(ss1)
ss1 = signal_density_manager(0,5,2,9,0,9,0,9,0)
signal_system.append(ss1)
ss1 = signal_density_manager(2,6,0,5,0,5,1,9,0)
signal_system.append(ss1)
ss1 = signal_density_manager(2,6,1,6,0,2,1,9,0)
signal_system.append(ss1)
ss1 = signal_density_manager(2,6,2,7,1,2,1,9,0)
signal_system.append(ss1)
ss1 = signal_density_manager(2,7,0,6,0,6,1,9,0)
signal_system.append(ss1)
ss1 = signal_density_manager(2,7,1,4,1,4,0,9,0)
signal_system.append(ss1)
ss1 = signal_density_manager(0,7,2,9,0,9,0,9,0)
signal_system.append(ss1)
ss1 = signal_density_manager(3,8,0,0,0,0,1,0,2)
signal_system.append(ss1)
ss1 = signal_density_manager(0,8,1,9,0,9,0,9,0)
signal_system.append(ss1)
ss1 = signal_density_manager(0,8,2,9,0,9,0,9,0)
signal_system.append(ss1)

def manage_signal_system():
    for signal_number in range(0,20):
        signal_system[signal_number].get_density()
        signal_system[signal_number].manage_density()

def motion(c):
    
    for i in range (NO_OF_VEH):
        k,signal_status,node_id = get_signal_info(vehicles[i].position_x,vehicles[i].position_y,vehicles[i].direction,vehicles[i].road_no)
 
#density precondition checking 
        a,b,c = get_info_from_veh(vehicles[i].position_x,vehicles[i].position_y,vehicles[i].direction,vehicles[i].road_no)
      #  print(a," ",b)
        l1 = signals[a][b][2][0]
        l2 = signals[a][b][2][1]
        if( (l1 - vehicles[i].position_x) > 0):
            mod_x = l1 - vehicles[i].position_x
        else:
            mod_x = vehicles[i].position_x - l1
        if( (l2 - vehicles[i].position_y) > 0):
            mod_y = l2 - vehicles[i].position_y
        else:
            mod_y = vehicles[i].position_y - l2
       
        if(mod_x - ref < 50 or mod_y - ref < 50):
            append_density(i, a,b)
                   
        rand_x = [125, 705, 995, 1370, 1370, 0,  0, 100, 513,1085]
        rand_y = [770, 770, 770, 300,  680, 220,510, 0,   0,  0]
        rand_road_no = [17, 13, 8, 5, 18, 0, 14, 9, 10, 6]
        rand_dir = ["North", "North","North", "West", "West", "East", "East", "South","South", "South"]
        ch_r = random.randint(0,9)
	
        #checks whether the vehicle is in or out of bounds
        out_roads = [0, 9, 14, 17, 13, 8, 18 ,5 , 6, 10]

        if(vehicles[i].road_no in out_roads):
            change = 0
            if(vehicles[i].direction == "East" and vehicles[i].position_x>1370):
                vehicles[i].position_x = rand_x[ch_r]
                vehicles[i].position_y = rand_y[ch_r]
                change = 1
            
            elif(vehicles[i].direction == "West" and vehicles[i].position_x<0):
                vehicles[i].position_x = rand_x[ch_r]
                vehicles[i].position_y = rand_y[ch_r]
                change = 1
                
            elif(vehicles[i].direction == "South" and vehicles[i].position_y>770):
                vehicles[i].position_x = rand_x[ch_r]
                vehicles[i].position_y = rand_y[ch_r]
                change = 1
				
            elif(vehicles[i].direction == "North" and vehicles[i].position_y<0):
                vehicles[i].position_x = rand_x[ch_r]
                vehicles[i].position_y = rand_y[ch_r]
                change = 1

            if(change):
                vehicles[i].road_no = rand_road_no[ch_r]
                vehicles[i].direction = rand_dir[ch_r]
                continue


        #print(vehicles[i].position_x,vehicles[i].position_y,vehicles[i].direction,vehicles[i].road_no)
        #vehicle is not in range of the signal
        if(k == 0):
            if(vehicles[i].direction == "East"):
         	      vehicles[i].position_x = vehicles[i].position_x + 5
         	      continue
            if(vehicles[i].direction == "West"):
                vehicles[i].position_x = vehicles[i].position_x - 5
                continue
            if(vehicles[i].direction == "North"):
                vehicles[i].position_y = vehicles[i].position_y - 5
                continue
            if(vehicles[i].direction == "South"):
                vehicles[i].position_y = vehicles[i].position_y + 5
                continue
	
    #the signal is active and the vehile is in the range of the signal	 	
        if(signal_status == 0 and k != 0):
            continue
	
    #the signal is not active and the vehicle is in the range of the signal
        if(signal_status == 1 and k != 0):
            direction1 = get_random_direction(vehicles[i].position_x,vehicles[i].position_y,vehicles[i].direction,node_id)
            remove_density(i, a, b)
    #turning paradigms 
        a = [1,2,3,4,5,9]
        b = [6,7,8]
	
        choose_lane = 0
        if(vehicles[i].direction == "North") :
            if(direction1 == "North"):
                vehicles[i].road_no = roots[vehicles[i].road_no].r_next[0][0]
                vehicles[i].position_y = roots[vehicles[i].road_no].l_end + 15   #use len of veh instead of 20

            elif(direction1 == "East"):
                vehicles[i].road_no = roots[vehicles[i].road_no].r_next[0][2]
                if roots[vehicles[i].road_no].lane == 4:
                    choose_lane = random.randint(0, 1)
                vehicles[i].position_y = roots[vehicles[i].road_no].w_start + 10 + 30*choose_lane
                vehicles[i].position_x = roots[vehicles[i].road_no].l_start + 15 #use len of veh instead of 20

            elif(direction1 == "West"):
                vehicles[i].road_no = roots[vehicles[i].road_no].r_next[0][3]
                if roots[vehicles[i].road_no].lane == 4:
                    choose_lane = random.randint(0, 1)
                vehicles[i].position_y = roots[vehicles[i].road_no].w_end - 15 - 30*choose_lane
                vehicles[i].position_x = roots[vehicles[i].road_no].l_end - 15   #use len of veh instead of 20
            
        elif(vehicles[i].direction == "South"):
            if(direction1 == "South"):
                vehicles[i].road_no = roots[vehicles[i].road_no].r_next[1][1]
                vehicles[i].position_y = roots[vehicles[i].road_no].l_start               

            elif(direction1 == "East"):
                vehicles[i].road_no = roots[vehicles[i].road_no].r_next[1][2]
                if roots[vehicles[i].road_no].lane == 4:
                    choose_lane = random.randint(0, 1)
                vehicles[i].position_y = roots[vehicles[i].road_no].w_start + 10 + 30*choose_lane
                vehicles[i].position_x = roots[vehicles[i].road_no].l_start
                
            elif(direction1 == "West"):
                vehicles[i].road_no = roots[vehicles[i].road_no].r_next[1][3]
                if roots[vehicles[i].road_no].lane == 4:
                    choose_lane = random.randint(0, 1)
                vehicles[i].position_y = roots[vehicles[i].road_no].w_end - 15 - 30*choose_lane
                vehicles[i].position_x = roots[vehicles[i].road_no].l_end - 15
        
        elif(vehicles[i].direction == "East"):
            if(direction1 == "East"):
                vehicles[i].road_no = roots[vehicles[i].road_no].r_next[0][2]
                vehicles[i].position_x = roots[vehicles[i].road_no].l_start
           
            elif(direction1 == "North"):
                vehicles[i].road_no = roots[vehicles[i].road_no].r_next[0][0]
                if roots[vehicles[i].road_no].lane == 4:
                    choose_lane = random.randint(0, 1)
                vehicles[i].position_x = roots[vehicles[i].road_no].w_start + 15 + 30*choose_lane
                vehicles[i].position_y = roots[vehicles[i].road_no].l_end - 15 #use len of veh
            
            elif(direction1 == "South") :
                vehicles[i].road_no = roots[vehicles[i].road_no].r_next[0][1]
                if roots[vehicles[i].road_no].lane == 4:
                    choose_lane = random.randint(0, 1)
                vehicles[i].position_x = roots[vehicles[i].road_no].w_end - 15 - 30*choose_lane
                vehicles[i].position_y = roots[vehicles[i].road_no].l_start
           
        elif(vehicles[i].direction == "West"):
            if(direction1 == "West"):
                vehicles[i].road_no = roots[vehicles[i].road_no].r_next[1][3]
                vehicles[i].position_x = roots[vehicles[i].road_no].l_end - 15
            #    pg.Rect(vehicles[i].position_x, vehicles[i].position_y, vehicles[i].width, vehicles[i].length)
            #x = x - 50
            elif(direction1 == "South"):
                vehicles[i].road_no = roots[vehicles[i].road_no].r_next[1][1]
                if roots[vehicles[i].road_no].lane == 4:
                    choose_lane = random.randint(0, 1)
                vehicles[i].position_x = roots[vehicles[i].road_no].w_end - 15 - 30*choose_lane
                vehicles[i].position_y = roots[vehicles[i].road_no].l_start
           
            elif(direction1 == "North"):
                vehicles[i].road_no = roots[vehicles[i].road_no].r_next[1][0]
                if roots[vehicles[i].road_no].lane == 4:
                    choose_lane = random.randint(0, 1)
                vehicles[i].position_x = roots[vehicles[i].road_no].w_start + 15 + 30*choose_lane
                vehicles[i].position_y = roots[vehicles[i].road_no].l_end - 15

        vehicles[i].direction = direction1
        manage_signal_system()
  #  if c >= 100 :
   #     plt.show()
			
	
def get_random_direction(x, y, direction, present_c):	 
		
	if(direction == "East"):
		direction2 = "West"
	if(direction == "West"):
		direction2 = "East"
	if(direction == "North"):
		direction2 = "South"
	if(direction == "South"):
		direction2 = "North"
		
	
	if(present_c == 1):
		arr = ["East","West","North"]
		arr.remove(direction2)
		r = random.randint(0,1)	
		direction = arr[r]
		return direction
		
	if(present_c == 2):
		arr = ["East","West","South"]
		arr.remove(direction2)
		r = random.randint(0,1)	
		direction = arr[r]
		return direction
	
	
	if(present_c == 3):
		arr = ["East","West","North"]
		arr.remove(direction2);
		r = random.randint(0,1)	
		direction = arr[r]
		return direction
	
	if(present_c == 4):
		arr = ["East","West","South"]
		arr.remove(direction2)
		r = random.randint(0,1)	
		direction = arr[r]
		return direction
	
	if(present_c == 0):
		arr = ["East","West","South","North"]
		arr.remove(direction2)
		r = random.randint(0,2)	
		direction = arr[r]
		return direction
	
	if(present_c == 5):
		arr = ["East","West","South"]
		arr.remove(direction2)
		r = random.randint(0,1)	
		direction = arr[r]
		return direction
	
	if(present_c == 6):
		arr = ["East","West","North"]
		arr.remove(direction2)
		r = random.randint(0,1)	
		direction = arr[r]
		return direction
	
	if(present_c == 7):
		arr = ["West","South","North"]
		arr.remove(direction2)
		r = random.randint(0,1)	
		direction = arr[r]
		return direction	
		
	if(present_c == 8):
		arr = ["East","South","North"]
		arr.remove(direction2)
		r = random.randint(0,1)	
		direction = arr[r]
		return direction


#init_road()
init_sig_info()
initialise_vehicles()

#vehicles[0].position_x,vehicles[0].position_y = 242, 295 
#vehicles[0].direction,vehicles[0].road_no = "West", 1
#vehicles[0].position_x,vehicles[0].position_y = 835, 214
#vehicles[0].direction,vehicles[0].road_no = "East", 4

add_extra_time(5, 0, 0)
quit = 0
ref_time = int(time.time())
c = 0
while(not quit):
    #keyboard command
    #signal_show()
    c = c+1
    screen.blit(bg, (0, 0))
    init_sig_info()
    signal_show()
    motion(c)
    for i in range(NO_OF_VEH):
        #screen.blit(veh, (vehicles[i].position_x,vehicles[i].position_y))
        if roots[vehicles[i].road_no].symm == horr:
            vehicle_diagram = pg.Rect(vehicles[i].position_x, vehicles[i].position_y, vehicles[i].length, vehicles[i].width)
        else:
            vehicle_diagram = pg.Rect(vehicles[i].position_x, vehicles[i].position_y, vehicles[i].width, vehicles[i].length)
        
        pg.draw.rect(screen, pg.color.THECOLORS[vehicles[i].colour], vehicle_diagram)
    
    time.sleep(0.1)

    for event in pg.event.get():
        if event.type==pg.QUIT:
            quit = 1
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_q:
                quit = 1

    pg.display.update()
    if(c % 20 == 19):
        plt.close()
  #      data = { 'Signal_1' : len(den_sig[0][0]),'Signal_2' : len(den_sig[0][1]),'Signal_3' : len(den_sig[0][2]), 'Signal_4' : len(den_sig[0][3]),'Signal_5' : len(den_sig[1][0]),'Signal_6' : len(den_sig[1][1]),'Signal_7' : len(den_sig[1][2]),'Signal_8' : len(den_sig[2][0]),'Signal_9' : len(den_sig[2][1]),'Signal_10' : len(den_sig[2][2]),'Signal_11' : len(den_sig[4][0]) }
        data = { 'Signal_1' : len(den_sig[4][0]) , 'Signal_2' : len(den_sig[3][1]) , 'Signal_3' : len(den_sig[3][0]) }
        siggi = list(data.keys())
        values = list(data.values())
        fig = plt.figure(figsize = (5, 5))
        plt.bar(siggi, values, color = "blue", width = 0.4)
        plt.xlabel("Signals")
        plt.ylabel("Density in number")
        plt.title("Singal Density graph")
#if(c/20 == 19):
    
        plt.draw()
        plt.pause(0.0001)
        

#    plt.show(block = False)
pg.quit()

