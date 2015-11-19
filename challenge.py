# '''
# The parameter weekday is True if it is a weekday, and the parameter vacation
# is True if we are on vacation. We sleep in if it is not a weekday or we're on
# vacation. Return True if we sleep in.
# '''


def sleep_in(weekday, vacation):
    pass


sleep_in(False, False)  # Should return True
sleep_in(True, False)  # Should return False
sleep_in(False, True)  # Should return True


# '''
# Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!".
# '''


def hello_name(name):
    pass


hello_name('Bob')  # Should return 'Hello Bob!'
hello_name('Alice')  # Should return 'Hello Alice!'
hello_name('X')  # Should return 'Hello X!'


# '''
# We have two monkeys, a and b, and the parameters a_smile and
# b_smile indicate if each is smiling. We are in trouble if they
# are both smiling or if neither of them is smiling. Print True
# if we are in trouble.
# '''


def monkey_trouble(a_smile, b_smile):
    pass


monkey_trouble(True, True)  # True
monkey_trouble(False, False)  # True
monkey_trouble(True, False)  # False


# '''
# Given 3 int values, a b c, return their sum. However, if one
# of the values is 13 then it does not count towards the sum
# and values to its right do not count. So for example, if b is
#  13, then both b and c do not count.
# '''


def lucky_sum(a, b, c):
    pass


lucky_sum(1, 2, 3)  # 6
lucky_sum(1, 2, 13)  # 3
lucky_sum(1, 13, 3)  # 1


# '''
# Given 3 int values, a b c, return their sum. However, if any
# of the values is a teen -- in the range 13..19 inclusive
# -- then that value counts as 0, except 15 and 16 do not
# count as a teens. Write a separate helper
# "def fix_teen(n):"that takes in an int value and returns
# that value fixed for
# the teen rule. In this way, you avoid repeating the teen code
#  3 times (i.e. "decomposition"). Define the helper below and
#  at the same indent level as the main no_teen_sum().
# '''


def no_teen_sum(a, b, c):
    pass


no_teen_sum(1, 2, 3)  # 6
no_teen_sum(2, 13, 1)  # 3
no_teen_sum(2, 1, 14)  # 3
