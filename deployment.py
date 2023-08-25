import time

import kubernetes.client
from kubernetes import client as kubernetes_client
from kubernetes import utils
from kubernetes import config
import yaml
from pathlib import Path, PureWindowsPath
import subprocess
# Initialize list
namespaces = []
print("Namespaces:")

prefix = 'uat'

for i in range(1, 2):
    namespaces.append(prefix+str(i))

print(namespaces)
print('Is this an apply or delete operation ?')
action = input()
if action == 'apply':
    for i in namespaces:
        print('###### Deploying on ' + i + ' #######')
        filename = PureWindowsPath("C:\\Users\\kumpara\\Documents\\GIT\\deployment.yaml")
        path = Path(filename)
        with open(path) as f:
            pod_yaml = yaml.safe_load(f)

        # load default config
        # assume that default setting is set in ~/.kube/config
        config.load_kube_config()

        # load kubernetes client
        k8s_client = kubernetes_client.api_client.ApiClient()


        # create pods from yaml object
        utils.create_from_yaml(k8s_client, yaml_objects=[
            pod_yaml], namespace=i)

        # wait for pods
        time.sleep(5)

        # list pods
        core_v1_api = kubernetes_client.CoreV1Api()
        pods = core_v1_api.list_namespaced_pod(i)
        for pod in pods.items:
            print(f"{pod.metadata.name} {pod.status.phase} {pod.status.pod_ip} {pod.metadata.namespace}")

        subprocess.run('kubectl get pods -n' + i)
elif action == 'delete':
    for i in namespaces:
        filename = PureWindowsPath("C:\\Users\\kumpara\\Documents\\GIT\\pod.yml")
        path = Path(filename)
        with open(path) as f:
            pod_yaml = yaml.safe_load(f)

        # load default config
        # assume that default setting is set in ~/.kube/config
        #config.load_kube_config(config_file='C:/Users/kumpara/Documents/rancher/kubeconfig/clusterms-un8-bm-kcapp001.yaml')
        #config.load_incluster_config()
        # with open('C:/Users/kumpara/Documents/rancher/kubeconfig/clusterms-un8-bm-kcapp001.yaml') as f:
        #     kubeconfig = yaml.safe_load(f)
        # make_k8s_client(kubeconfig)
        print('###### Deleting pod on ' + i + ' #######')
        subprocess.run('kubectl delete deploy/indexsre-mt-pod1 -n ' + i)
