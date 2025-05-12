#leetcode 253. Meeting Rooms II
class Solution:
    def minMeetingRooms(self, intervals):
        if not intervals:
            return 0  # No meetings, no rooms needed

        # Step 1: Extract start and end times into separate lists
        start_times = sorted(interval[0] for interval in intervals)
        end_times = sorted(interval[1] for interval in intervals)

        # Initialize pointers and counters
        start_ptr = 0  # Pointer to iterate through start_times
        end_ptr = 0    # Pointer to iterate through end_times
        rooms_needed = 0
        max_rooms = 0

        # Step 2: Iterate through all start times
        while start_ptr < len(intervals):
            # If the next meeting starts before the earliest meeting ends, need a new room
            if start_times[start_ptr] < end_times[end_ptr]:
                rooms_needed += 1  # Allocate a new room
                start_ptr += 1     # Move to next meeting's start time
            else:
                # The earliest meeting has ended; free up a room
                rooms_needed -= 1
                end_ptr += 1       # Move to next meeting's end time

            # Step 3: Update the maximum number of rooms used so far
            max_rooms = max(max_rooms, rooms_needed)

        # Step 4: Return the peak number of rooms needed at any time
        return max_rooms
