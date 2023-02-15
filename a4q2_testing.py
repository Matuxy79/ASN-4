#John Matukutire
#11303324
#CMPT 145 CRN 27177
#L16

#importing the starter file
import Statistics as S
import test_statistics as TS

#Test for statistics add and one negative value
test_item = 'add() + count()'
data_in = [-3]
expected = 1
reason = "Check count after adding a negative value"

stats = S.Statistics()
stats.add(data_in)
result = stats.count()

if result != expected:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))

#Tests for statistics add and multiple negative values
test_item = 'add() + count()'
data_in = [-4,-7,-9]
expected = 3
reason = "Check count after multiple negative values are added"

stats = S.Statistics()
for v in data_in:
    stats.add(v)
result = stats.count()

if result != expected:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))

#Tests for statistics add and a mix of positive and negative values
test_item = 'add() + count()'
data_in = [-4,-7,-9,4,6]
expected = 5
reason = "Check count after multiple and positive values are added"

stats = S.Statistics()
for v in data_in:
    stats.add(v)
result = stats.count()

if result != expected:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))

#Tests for float values
test_item = 'add() + count()'
data_in = [1.6]
expected = 1
reason = "Check count for float values"

stats = S.Statistics()
for v in data_in:
    stats.add(v)
result = stats.count()

if result != expected:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))

#Tests for negative float values
test_item = 'add() + count()'
data_in = [-3.4]
expected = 1
reason = "Check count for negative float values"

stats = S.Statistics()
for v in data_in:
    stats.add(v)
result = stats.count()

if result != expected:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))

#Tests for negative float values and positive float values
test_item = 'add() + count()'
data_in = [-3.4, 6.0, 4.2, -2,1, 7.5]
expected = 5
reason = "Check count for negative float values and positive float values"

stats = S.Statistics()
for v in data_in:
    stats.add(v)
result = stats.count()

if result != expected:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))


# Test Statistics.mean() when zero is the only value
test_item = 'add() + mean()'
data_in = [0]
expected = 0.0
reason = "Check average when zero is the only value"

stats = S.Statistics()
for v in data_in:
    stats.add(v)
result = stats.mean()

if not close_enough(expected, result, 0.0001):
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))

# Test Statistics.mean() when a negative float is the only value
test_item = 'add() + mean()'
data_in = [-3.0]
expected = -3.0
reason = "Check average after a negative float is the only value"

stats = S.Statistics()
for v in data_in:
    stats.add(v)
result = stats.mean()

if not close_enough(expected, result, 0.0001):
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))

# Test Statistics.mean() when a positive float is the only value
test_item = 'add() + mean()'
data_in = [5.0]
expected = 5.0
reason = "Check average after a positive float is the only value"

stats = S.Statistics()
for v in data_in:
    stats.add(v)
result = stats.mean()

if not close_enough(expected, result, 0.0001):
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))

# Test Statistics.mean() when multiple integer and floats are added
test_item = 'add() + mean()'
data_in = [3, 7, 4, 2.4, 8.6]
expected = 5.0
reason = "Check average after multiple integer and floats are added"

stats = S.Statistics()
for v in data_in:
    stats.add(v)
result = stats.mean()

if not close_enough(expected, result, 0.0001):
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))

# Test Statistics.mean() when multiple negative floats and negative integers are added
test_item = 'add() + mean()'
data_in = [-1, -8, -6, -3.4, -8.8]
expected = -5.44
reason = "Check average after multiple negative floats and negative integers are added"

stats = S.Statistics()
for v in data_in:
    stats.add(v)
result = stats.mean()

if not close_enough(expected, result, 0.0001):
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason)) 

# Test Statistics.mean() when a mixture of negative and positive floats are added 
test_item = 'add() + mean()'
data_in = [-4.5, -6.7, -9.1, 8.2 ,6.7]
expected = -1.08
reason = "Check average after a mixture of negative and positive floats are added"

stats = S.Statistics()
for v in data_in:
    stats.add(v)
result = stats.mean()

if not close_enough(expected, result, 0.0001):
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))   

# Test Statistics.mean() when multiple positive floats and positive integers are added
test_item = 'add() + mean()'
data_in = [1, 8, 6, 3.4, 8.8]
expected = 5.44
reason = "Check average after multiple poitive floats and positive integers are added"

stats = S.Statistics()
for v in data_in:
    stats.add(v)
result = stats.mean()

if not close_enough(expected, result, 0.0001):
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason)) 

print('*** Test script completed ***')