"""
Problem: First Negative Integer in Every Window of Size K

Given an array of integers and a window size k, find the first negative
integer in every window of size k. If a window does not contain a negative
integer, output 0 for that window.

Example:
Input: nums = [12, -1, -7, 8, -15, 30, 16, 28], k = 3
Output: [-1, -1, -7, -15, -15, 0]

Approach:
- Use a deque to store indices of negative numbers.
- Remove indices that fall outside the current window.
- The front of the deque always contains the first negative element
  in the current window.
- If the deque is empty, append 0.

Time Complexity: O(n)
Space Complexity: O(k)
"""

from collections import deque


def first_negative_in_window(nums, k):
    dq = deque()
    result = []

    for i in range(len(nums)):

        
        if dq and dq[0] <= i - k:
            dq.popleft()

        
        if nums[i] < 0:
            dq.append(i)

        if i >= k - 1:
            if dq:
                result.append(nums[dq[0]])
            else:
                result.append(0)

    return result


if __name__ == "__main__":
    nums = [12, -1, -7, 8, -15, 30, 16, 28]
    k = 3

    output = first_negative_in_window(nums, k)
    print("First negative integer in every window:", output)