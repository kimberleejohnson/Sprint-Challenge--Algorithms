class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l          # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)

    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        
        # If the robot's position is less than the length of the list, keep moving to the right (True)
        # (False) can't move to the right, must move left 
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """

        # If the robot is away from the beginning of the list, robot can move backward to the left (True)
        # If the robot is at the beginning of the list, must move right (False)
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        
        # Can move right determined
        # Move right if it can, returns True
        # If can't move right, returns False 
        
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """

        # Can move left determined 
        # Moves left if can and returns True
        # If can't move left, returns False 
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
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
        # If the one the robot already holds is greater, returns 1 
        elif self._item > self._list[self._position]:
            return 1
        # If the one the robot already holds is smaller, returns -1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    # Potential additional conditions for looping 
    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"
    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"
    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        # Can be used to check if light is on 
        return self._light == "ON"

    ## Pseudocode for sort 
    # Robot has to start at self._position 0, because we can't store variables 
    # Pick up an item 
    # Move robot to the right 
    # Compare picked up item to item at new position 
    # If compare item is greater than the one the robot holds, returns a -1
        # Move robot to right, keep comparing -- (potential recursion?)
    # But, if compare item is smaller, returning a 1 
        # Move the robot back left 
        # Swap out the items 
        # Move robot to right, keep comparing -- (potential recursion?)
    # If new position item is same 
        # Move robot to right, keep comparing -- (potential recursion?)

    ## Pseudocode attempt 2.5 (selection sort)
    # Robot has to start at self._position 0, because we can't store variables. This means binary search and midpoints are not available to us. 
    # Robot needs to start by picking up first item. 
    # Robot then needs to move right, continuing all the way through the list, swapping out the item it holds for the smallest value it finds along the way. 
    # Then, it needs to bring that smallest value (that it has picked) all the way back to the beginning and swap it with what's there (None at first).
    # Then, it needs to move right once and repeat 
    # This cycle should continue until entire list has been sorted 
    # Since we can't store variables or incrementors, we need to store and track changes somehow with the lights 
    
    def sort(self):
        """
        Sort the robot's list.
        """
        # Base case for attempted recursion 
        ## If the robot can no longer move right
        if len(self._list) <= 0: 
            return 0 

        while self.can_move_right(): 
            # Goes from holding None to having something to compare 
            self.swap_item() 
            # Move right to compare 
            self.move_right()

            # If the compare item is greater than the one the robot holds 
            if self.compare_item == -1: 
                # Move to the right, keep comparing 
                self.move_right()
                return self.sort(self._list[self._position:])

            # If the compare item is smaller than the one the robot holds 
            elif self.compare_item == 1: 
                self.move_left() 
                self.swap_item()
                self.move_right()
                return self.sort(self._list[self._position:])


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)