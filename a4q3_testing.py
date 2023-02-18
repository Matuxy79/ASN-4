#John Matukutire
#11303324
#CMPT 145 CRN 27177
#L16

#importing the object
from a4q3 import Statistics

#print test case results for max
print("Test case results for max")
#Testing info
test_item = 'max'
data_in = [1, 3, 9, 2, 4]
expected = 9
reason = "Check max of the positive values added"
#setting a variable for easy use in testing
#adding values to test
my_calc = Statistics()
for v in data_in:
    my_calc.add(v)
result = my_calc.get_max()

if result != expected:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))
else:
    print("Test passed")

#Testing info
test_item = 'max'
data_in = [-1, -3, -9, -2, -4]
expected = -1
reason = "Check max of the negative values added"
#setting a variable for easy use in testing
#adding values to test
my_calc = Statistics()
for v in data_in:
    my_calc.add(v)
result = my_calc.get_max()

if result != expected:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))
else:
    print("Test passed")

#Testing info
test_item = 'max'
data_in = [0]
expected = 0
reason = "Check max of the one value added"
#setting a variable for easy use in testing
#adding values to test
my_calc = Statistics()
for v in data_in:
    my_calc.add(v)
result = my_calc.get_max()

if result != expected:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))
else:
    print("Test passed")

#Testing info
test_item = 'max'
data_in = []
expected = None
reason = "Check max of the empty list"
#setting a variable for easy use in testing
#adding values to test
my_calc = Statistics()
for v in data_in:
    my_calc.add(v)
result = my_calc.get_max()

if result != expected:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))
else:
    print("Test passed")

#Testing info
test_item = 'max'
data_in = [-1, -3, 9, 2, -4]
expected = 9
reason = "Check max of the mixture of pos and neg values added"
#setting a variable for easy use in testing
#adding values to test
my_calc = Statistics()
for v in data_in:
    my_calc.add(v)
result = my_calc.get_max()

if result != expected:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))
else:
    print("Test passed")


#print results of tests for min
print("Test case results for min")
#Testing info
test_item = 'min'
data_in = [1, 3, 9, 2, 4]
expected = 1
reason = "Check min of the positive values added"
#setting a variable for easy use in testing
#adding values to test
my_calc = Statistics()
for v in data_in:
    my_calc.add(v)
result = my_calc.get_min()

if result != expected:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))
else:
    print("Test passed")

#Testing info
test_item = 'min'
data_in = [-1, -3, -9, -2, -4]
expected = -9
reason = "Check min of the negative values added"
#setting a variable for easy use in testing
#adding values to test
my_calc = Statistics()
for v in data_in:
    my_calc.add(v)
result = my_calc.get_min()

if result != expected:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))
else:
    print("Test passed")

#Testing info
test_item = 'min'
data_in = [0]
expected = 0
reason = "Check min of the one value added"
#setting a variable for easy use in testing
#adding values to test
my_calc = Statistics()
for v in data_in:
    my_calc.add(v)
result = my_calc.get_min()

if result != expected:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))
else:
    print("Test passed")

#Testing info
test_item = 'min'
data_in = []
expected = None
reason = "Check min of the empty list"
#setting a variable for easy use in testing
#adding values to test
my_calc = Statistics()
for v in data_in:
    my_calc.add(v)
result = my_calc.get_min()

if result != expected:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))
else:
    print("Test passed")

#Testing info
test_item = 'min'
data_in = [-1, -3, 9, 2, -4]
expected = -4
reason = "Check min of the mixture of pos and neg values added"
#setting a variable for easy use in testing
#adding values to test
my_calc = Statistics()
for v in data_in:
    my_calc.add(v)
result = my_calc.get_min()

if result != expected:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))
else:
    print("Test passed")

#print the test case results for range
print("Test case results for range")
#Testing info
test_item = 'range'
data_in = [1, 3, 9, 2, 4]
expected = 8
reason = "Check range of the positive values added"
#setting a variable for easy use in testing
#adding values to test
my_calc = Statistics()
for v in data_in:
    my_calc.add(v)
result = my_calc.get_range()

if result != expected:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))
else:
    print("Test passed")

#Testing info
test_item = 'range'
data_in = [-1, -3, -9, -2, -4]
expected = 8
reason = "Check range of the negative values added"
#setting a variable for easy use in testing
#adding values to test
my_calc = Statistics()
for v in data_in:
    my_calc.add(v)
result = my_calc.get_range()

if result != expected:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))
else:
    print("Test passed")

#Testing info
test_item = 'range'
data_in = [0]
expected = 0
reason = "Check range of the one value added"
#setting a variable for easy use in testing
#adding values to test
my_calc = Statistics()
for v in data_in:
    my_calc.add(v)
result = my_calc.get_range()

if result != expected:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))
else:
    print("Test passed")

#Testing info
test_item = 'range'
data_in = []
expected = None
reason = "Check range of the empty list"
#setting a variable for easy use in testing
#adding values to test
my_calc = Statistics()
for v in data_in:
    my_calc.add(v)
result = my_calc.get_range()

if result != expected:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))
else:
    print("Test passed")

#Testing info
test_item = 'range'
data_in = [-1, -3, 9, 2, -4]
expected = 13
reason = "Check max of the mixture of pos and neg values added"
#setting a variable for easy use in testing
#adding values to test
my_calc = Statistics()
for v in data_in:
    my_calc.add(v)
result = my_calc.get_range()

if result != expected:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))
else:
    print("Test passed")

#print test cases for the mode
print("Test cases for mode")
#Testing info
test_item = 'mode'
data_in = [-1, -3, 9, 2, -4]
expected = None
reason = "Check mode when there is no duplicates"
#setting a variable for easy use in testing
#adding values to test
my_calc = Statistics()
for v in data_in:
    my_calc.add(v)
result = my_calc.get_mode()

if result != expected:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))
else:
    print("Test passed")

#Testing info
test_item = 'mode'
data_in = [-1, -3, 9, 2, -4, 6, 6]
expected = 6
reason = "Check mode when there is one duplicate"
#setting a variable for easy use in testing
#adding values to test
my_calc = Statistics()
for v in data_in:
    my_calc.add(v)
result = my_calc.get_mode()

if result != expected:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))
else:
    print("Test passed")

#Testing info
test_item = 'mode'
data_in = [-1, -3, 9, 2, -4, -4, -3, 9, 9]
expected = 9
reason = "Check mode when there is multiple duplicates"
#setting a variable for easy use in testing
#adding values to test
my_calc = Statistics()
for v in data_in:
    my_calc.add(v)
result = my_calc.get_mode()

if result != expected:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))
else:
    print("Test passed")

#Testing info
test_item = 'mode'
data_in = []
expected = None
reason = "Check mode when there is empty list"
#setting a variable for easy use in testing
#adding values to test
my_calc = Statistics()
for v in data_in:
    my_calc.add(v)
result = my_calc.get_mode()

if result != expected:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))
else:
    print("Test passed")


