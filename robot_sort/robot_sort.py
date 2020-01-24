# NO CAN DOS
# * You may NOT modify any pre-defined robot methods.
# * You may NOT store any variables. (`=`)
# * You may NOT access any instance variables directly. (`self._anything`)
# * You may NOT use any Python libraries or class methods. (`sorted()`, etc.)


# DO THIS STUFF
# * You may use any pre-defined robot methods.
# * You may use logical operators. (`if`, `and`, `or`, `not`, etc.)
# * You may use comparison operators. (`>`, `>=`, `<`, `<=`, `==`, `is`, etc.)
# * You may use iterators. (`while`, `for`, `break`, `continue`)
# * You may define robot helper methods, as long as they follow all the rules.


# UPER
# > rearranged the rules so that the things i can do are listed 
# separately than the things I can't do. This was confusing at first.
# > class with methods
# > cannot access instance variables, but I can access methods
# self.can_move_right, for instance
# > Inputs received are:
#   - list to be sorted "l"
# > input is fixed

# Plan
# Basically, use these methods to alter the list
# Read through the methods and try to understand what each one does
# play around with it if it's not immediately clear
# Use the light as a boolean toggle
# Position starts at 0
# 


class SortingRobot:
    def __init__(self, l):
        """SortingRobot takes a list and sorts it."""
        self._list = l          # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)

    def can_move_right(self):
        """Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        """If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        """Turn on the robot's light"""
        self._light = "ON"
    def set_light_off(self):
        """Turn off the robot's light"""
        self._light = "OFF"
    def light_is_on(self):
        """Returns True if the robot's light is on and False otherwise."""
        return self._light == "ON"

    def sort(self):
        # Turn the light on to start
        # self.set_light_on()
        # Loop over commands while light is on
        # Light becomes the base case. We shut it off when we are all the way to the right
        # while self.light_is_on():
            # # print('self._time: ', self._time) # time counter
            # if self.compare_item() == None:
            #     # print(robot._list)  # Every index one at a time, swappin
            #     self.swap_item()

            # # # This runs if the position can move right. stops at index (last)
            # while self.can_move_right():    # Boolean if index + 1 is possible
            #     self.move_right()   # if the position is in range, position + 1
            #     if self.compare_item() == -1 and self.can_move_right():
            #         self.swap_item() 
            #     elif self.compare_item() == 1 and not self.can_move_right():
            #         self.swap_item()

            # # # This runs if the position can move left. Stops at index 0
            # while self.can_move_left():
            #     print(l)
            #     print("")
            #     self.move_left()
            #     if self.compare_item() == 1:
            #         self.swap_item()

            #     elif self.compare_item() == None and self.can_move_right():
            #         self.swap_item()
            #     # Turn off the light and shut down the robot
            #     # If cannot compare item and cannot move right
        while not self.light_is_on():
            # This doesn't get hit if we run out of moves to the right. 
            # IF we hit the end moving to the right, the if block gets hit
            self.set_light_on()     # Turns on the light in the beginning
            # print(l)
            # print("")
            # print(self._item)
            # print(self._position)
            # print(self._time)
            while self.can_move_right():    # Can we move right?
                # print("")
                # print(l)
                # print("")
                # print(self._item)
                # print(self._position)
                # Picks up an item as in stores a number in _item
                # Puts None in our list
                self.swap_item()
                self.move_right()
                # print("")
                # print(l)
                # print("")
                # print(self._item)
                # print(self._position)
                # # Compares _item at current position it to the item held
                if self.compare_item() > 0:
                    # print("")
                    # print("start. compare_item > 0")
                    # print(l)
                    # print("")
                    # print(self._item)
                    # print(self._position)
                    self.swap_item()    # This swaps out pos with None
                    self.move_left()    # Moves to left
                    # print("")
                    # print("just moved left")
                    # print(l)
                    # print("")
                    # print(self._item)
                    # print(self._position)
                    self.swap_item()
                    self.move_right()
                    # print("")
                    # print("just moved right")
                    # print(l)
                    # print("")
                    # print(self._item)
                    # print(self._position)
                    self.set_light_off()    # Turn off the light
                # if number to the right is greater, do this:
                else:
                    # print("")
                    # print(">>> else: compare item == 0 or less than 0")
                    # print(l)
                    # print("")
                    # print(self._item)
                    # print(self._position)
                    self.move_left()    # Go to correct index
                    self.swap_item()    # Replace None with current number
                    self.move_right()   # Continue
            # This resets the robot. Moves position all the way left
            if not self.light_is_on():  # Check that light is OFF
                while self.can_move_left():
                    self.move_left()



if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)