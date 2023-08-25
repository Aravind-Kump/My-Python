# import subprocess, os, re, sys
#
# myjobs = subprocess.run(["kubectl", "get", "jobs", "-n", "indexsre"])
# pattern = [r".*\bscheduled-autoscale-scaledown\b"]
# # for i in list:
# #     if re.match(r'scheduled-autoscale-scaledown-*', output, re.M|re.I):
# #         print(i)
#
# #list = filter('scheduled-autoscale-scaledown', myjobs)
#
# for p in pattern:
#  if (re.match("scheduled-autoscale-scaledown",p) is true:

# import re
#
# target_string = "Jessa loves Python and pandas,and Jessa has gift"
# pattern = r"Jessa"
#
# # match() method
# result = re.match(pattern, target_string)
# print(result)

# import re
import subprocess, os, re, sys
target_string = subprocess.run(["kubectl", "get", "jobs", "-n", "indexsre"])
result = re.findall(r"scheduled-autoscale-scaledown", target_string)
print("Matching string literal: ", result)
# Output ['player']

fileName = subprocess.run(["kubectl", "get", "jobs", "-n", "indexsre"])
print("Enter the String: ")
text = "scheduled-autoscale"
fileHandle = open(fileName, "r")
lines = fileHandle.readlines()
for line in lines:
  if text in line:
    print(line)
fileHandle.close()