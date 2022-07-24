import subprocess
val = input("Enter file path:")
pattern = input("Enter pattern to be filtered:")
log_file = open(val)

log_filter = []
kube_run = []

for log in log_file:
    if pattern in log:
        log_filter.append(log)
        print(log)

# # Read pattern from log
# for i in log_filter:
#     print("kubectl scale {} {} -n {}".format(i.split()[13], i.split()[14], i.split()[16]))
#     kube_run.append("kubectl scale {} {} -n {}".format(i.split()[13], i.split()[14], i.split()[16]))
#
# # TO execute a command referring to the filtered log
# for i in kube_run:
#     subprocess.run(i)

