# readme



```
wget https://raw.githubusercontent.com/iganari/code-labo/main/python/web-sample-01/main.py
```

```
### New Env


export _gcp_pj_id='Your GCP Project ID'


export _gcp_pj_id='daiwast-gss-dwh-lab'


export _common='ca-igrs'
export _region='asia-northeast1'
```
```
gcloud auth login -q
```
```
docker build --tag gcr.io/${_gcp_pj_id}/${_common}:v1 .
docker images | grep gcr.io/${_gcp_pj_id}/${_common}
```
```
docker push gcr.io/${_gcp_pj_id}/${_common}:v1
```


