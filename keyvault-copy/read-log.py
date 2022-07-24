import subprocess
log_file = open("<LOG FILE PATH>")

log_filter = []
kube_run = []

for log in log_file:
    if "<log pattern to be filtered>" in log:
        log_filter.append(x)

for i in log_filter:
    print("kubectl scale {} {} -n {}".format(i.split()[13], i.split()[14], i.split()[16]))
    kube_run.append("kubectl scale {} {} -n {}".format(i.split()[13], i.split()[14], i.split()[16]))

# TO execute a command referring to the filtered log
for i in kube_run:
    subprocess.run(i)

