import diagrams
import diagrams.k8s.infra
import diagrams.k8s.controlplane
from diagrams import Cluster, Diagram
import diagrams.aws.devtools

with Diagram(" Kubernetes Cluster", show=False):
    with Cluster("Kubernetes Cluster", direction="RL"):
        with Cluster("control plane"):
            cm = diagrams.k8s.controlplane.CM
            ccm = diagrams.k8s.controlplane.CCM
            api = diagrams.k8s.controlplane.API
            etcd = diagrams.k8s.infra.ETCD
            sched = diagrams.k8s.controlplane.Sched
            api_service = api('api')
            myccm = ccm('ccm')
            [myccm,
             cm("cm"),
             etcd('etc'),
             sched('sched')] << api_service
        providerapi = diagrams.aws.devtools.Cloud9
        myccm >> providerapi("cloud provider api")
        for i in range(3):
            with Cluster("Node" + str(i), direction="LR"):
                kubelet = diagrams.k8s.controlplane.Kubelet
                kproxy = diagrams.k8s.controlplane.KProxy
                ku = kubelet('container manager')
                kp = kproxy('k-proxy')
                (ku - diagrams.Edge(penwidth="0") - kp)
                api_service << ku



