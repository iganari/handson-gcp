# GitHub Actions

## 概要

![](https://storage.googleapis.com/gweb-cloudblog-publish/images/2_GitHub_Actions.max-1100x1100.jpg)

OIDC をサポートしていて、 GitHub Actions も OIDC を使えるようになったので。

```
Workload Identity 連携
https://cloud.google.com/iam/docs/workload-identity-federation
```
```
GitHub Actions からのキーなしの認証の有効化
https://cloud.google.com/blog/ja/products/identity-security/enabling-keyless-authentication-from-github-actions
```

![](./img/01.png)


## 手順

以下の N 個の手順が必要になる

1. Workload Identity プールの作成
1. Workload Identity プロバイダの作成
1. Workload Identity 連携を設定および構成

```
export _gcp_pj_id='Your GCP Project ID'
```

+ GCP と認証する

```
gcloud auth login -q
```

## 1. Workload Identity プールの作成

```
gcloud beta iam workload-identity-pools create handsongcp-wif-github \
  --location global \
  --display-name="Hands On GCP" \
  --project "${_gcp_pj_id}"
```

## 2. Workload Identity プロバイダの作成

```
gcloud iam workload-identity-pools providers create-oidc "my-provider" \
  --location global \
  --workload-identity-pool handsongcp-wif-github \
  --display-name="Demo provider" \
  --attribute-mapping="google.subject=assertion.sub,attribute.actor=assertion.actor,attribute.aud=assertion.aud" \
  --issuer-uri="https://token.actions.githubusercontent.com \
  --project "${_gcp_pj_id}"
```













## 1. 

```
steps:
- id: 'auth'
  name: 'Authenticate to Google Cloud'
  uses: 'google-github-actions/auth@v0.4.0'
  with:
    workload_identity_provider: 'projects/123456789/locations/global/workloadIdentityPools/my-pool/providers/my-provider'
    service_account: 'my-service-account@my-project.iam.gserviceaccount.com'
```
```
steps:
- id: auth
  uses: google-github-actions/auth@v0.4.0
  with:
    workload_identity_provider: 'projects/123456789/locations/global/workloadIdentityPools/my-pool/providers/my-provider'
    service_account: 'my-service-account@my-project.iam.gserviceaccount.com'

- id: get-gke-credentials
  uses: google-github-actions/get-gke-credentials@v0.4.0
  with:
    cluster_name: my-cluster
    location: us-central1-a

- id: get-pods
  run: kubectl get pods
```