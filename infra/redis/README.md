# Redis local implementation

I have implemented this small redis instance locally just for some tests. Tried to implement using ingress, but it did not work, so I am using, for now, a nodeport deployment. 

For that I have added toleration just to keep the deployment on the same node.

- Taint

> k taint node ${KIND-WORKER-NAME} node=infra:NoSchedule

- Toleration

```
spec:
  tolerations:
  - key: node
    operator: Equal
    value: infra
    effect: NoSchedule
```