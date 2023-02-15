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

# call the operation
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

# call the operation
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
reason = "Check count after multiple  and positive values are added"

# call the operation
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
reason = "Check count after a float value is added"

# call the operation
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
reason = "Check count after a negative float value is added"

# call the operation
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
reason = "Check average after zero is added"

# call the operation
stats = S.Statistics()
for v in data_in:
    stats.add(v)
result = stats.mean()

if not close_enough(expected, result, 0.0001):
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))

print('*** Test script completed ***')

# Test Statistics.mean() when a negative integer is the only value
test_item = 'add() + mean()'
data_in = [0]
expected = 0.0
reason = "Check average after zero is added"

# call the operation
stats = S.Statistics()
for v in data_in:
    stats.add(v)
result = stats.mean()

if not close_enough(expected, result, 0.0001):
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))

print('*** Test script completed ***')