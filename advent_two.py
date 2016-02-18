from sys import argv
script, filename = argv
import time

wrapping_paper = 0
ribbon = 0

def advent_of_code_intro(project_num):
    print ""
    print '  --------------------------------------------------------------------------'
    time.sleep(.1)
    print '  ---------------------------- Welcome to ----------------------------------'
    time.sleep(.1)
    print '  -------------------------- Advent of Code --------------------------------'
    time.sleep(.1)
    print '  --------------------------------------------------------------------------'
    time.sleep(.1)
    print '  --------------------------------------------------------------------------'
    time.sleep(.1)
    print '  ------------------ Created by: David Daly 2016 VA ------------------------'
    time.sleep(.1)
    print '  --------------------------------------------------------------------------'
    time.sleep(.1)
    print '  --------------------------------------------------------------------------'
    time.sleep(.1)
    print '  ------- This project was done as part the adventofcode.com coding --------'
    time.sleep(.1)
    print '  ------- challenges. This is project %s. Each project has two parts. -------' % project_num
    time.sleep(.1)
    print '  ------- This program completes both parts. -------------------------------'
    time.sleep(.1)
    print '  --------------------------------------------------------------------------'
    time.sleep(.1)
    print '  --------------------------------------------------------------------------'
    time.sleep(.1)
    print '  -------- You can find me on Github at github.com/ddjr --------------------'
    time.sleep(.1)
    print '  --------------------------------------------------------------------------'
    time.sleep(.1)
    print '  --------------------------------------------------------------------------'
    print ""
    time.sleep(.8)

def open_file(filename):
    txt = open(filename)
    print "Openning file named: %r " % filename
    return txt.read()
def calculate_volume(length, width, height):
    return length * width * height
def calculate_area(length, width):
    return (length * width)
def calculate_surface_area_3D(length, width, height):
    return (2 * length * width) + (2 * width * height) + (2 * height * length)
def calculate_parameter(length,width):
    return 2 * length + 2 * width
def find_longest_side(box_dimensions):
    largest_dimension = max(box_dimensions)
    return box_dimensions.index(largest_dimension)
def order_shortest_side_first(box_dimensions):
    long_side_index = find_longest_side(box_dimensions)
    short_side_index1 = (long_side_index + 1) % 3
    short_side_index2 = (long_side_index + 2) % 3
    if box_dimensions[short_side_index1] < box_dimensions[short_side_index2]:
        length = box_dimensions[short_side_index1]
        width  = box_dimensions[short_side_index2]
    else:
        length = box_dimensions[short_side_index2]
        width  = box_dimensions[short_side_index1]
    height = box_dimensions[long_side_index]
    return (length, width, height)
def calculate_extra_paper(box_dimensions):
    length, width, height = order_shortest_side_first(box_dimensions)
    return calculate_area(length, width)
def calculate_ribbon(box_dimensions):
    length, width, height = order_shortest_side_first(box_dimensions)
    ribbon = calculate_parameter(length, width)
    ribbon += calculate_volume(length, width, height)
    return ribbon
def claculate_wrapping_paper(present):
    wrapping_paper = calculate_surface_area_3D(present[0],present[1],present[2])
    wrapping_paper += calculate_extra_paper(present)
    return wrapping_paper
def present_handler(present):
    global wrapping_paper
    global ribbon
    wrapping_paper += claculate_wrapping_paper(present)
    ribbon += calculate_ribbon(present)

def parse_present():
    presents = open_file(filename)
    presents = presents.split('\n')
    for present in presents:
        present = present.split('x')
        if present == [""]:
            pass
        else:
            present = [int(i) for i in present]
            present_handler(present)

advent_of_code_intro(2)
parse_present()
print "total paper needed is %d square feet" % wrapping_paper
print "total ribbon needed is %d feet" % ribbon
