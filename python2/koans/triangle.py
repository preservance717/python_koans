#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.


# triangle(a, b, c) analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#

def all_sides_are_greater_than_0(a, b, c):
    return a and b and c

def sum_of_any_two_sides_greater_than_third_one(a, b, c):
    return a+b > c and a+c > b and b+c > a

def triangle(a, b, c):
    # DELETE 'PASS' AND WRITE THIS CODE
    # result = len(set([a, b, c]))
    # if result == 1: return 'equilateral'
    # if result == 2: return 'isosceles'
    # if result == 3: return 'scalene'

    # lengths_of_sides = len(set([a, b, c]))

    if not ( all_sides_are_greater_than_0(a, b, c)
             and
             sum_of_any_two_sides_greater_than_third_one(a, b, c)
           ):
        raise TriangleError
    
    type_dict = {1: 'equilateral', 2: 'isosceles', 3: 'scalene'}
    return type_dict[len(set([a, b, c]))]

# Error class used in part 2.  No need to change this code.
class TriangleError(StandardError):
    pass
