# readme



```
wget https://raw.githubusercontent.com/iganari/code-labo/main/python/web-sample-01/main.py
```

```
### New Env


export _gcp_pj_id='Your GCP Project ID'
export _common='Your common value'
export _region='asia-northeast1'
```

+ GCP との認証

```
gcloud auth login -q
```

+ コンテナイメージの作成

```
docker build --tag gcr.io/${_gcp_pj_id}/${_common}:v1 .
docker images | grep gcr.io/${_gcp_pj_id}/${_common}
```

+ GCR にコンテナイメージをアップロードする

```
docker push gcr.io/${_gcp_pj_id}/${_common}:v1
```


