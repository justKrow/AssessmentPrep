# Problem: Task Scheduler
# 🔍 Problem Statement:
# You are given a list of tasks represented by capital letters (like ['A', 'A', 'A', 'B', 'B', 'B']) and an integer n which represents the cooldown interval between two same tasks.

# You need to determine the least number of units of time the CPU will take to finish all the given tasks, where:

# Each task takes 1 unit of time

# Between two same tasks, there must be at least n units of cooldown time, during which the CPU can be idle or do different tasks.

# Input: tasks = ["A","A","A","B","B","B"], n = 2
# Output: 8
# Explanation: A → B → idle → A → B → idle → A → B

def taskScheduler(tasks, n):
    pass


print(taskScheduler(["A", "A", "A", "B", "B", "B"], 2))
