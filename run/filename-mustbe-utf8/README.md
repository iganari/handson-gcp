# コンテナイメージに内包するファイル名は UTF-8 でなければならない

## 概要

[コンテナ ランタイムの契約 | ]File names

https://cloud.google.com/run/docs/container-contract#file-names

## ハンズオン

※ Dockerfile で COPY などを使って検証したいので Buildpacks などは使わずに行う

可能であれば Buildpacks を使うと開発スピードが早くなるのでお勧め [お知らせ: Google Cloud の Buildpacks でコンテナ イメージ作成が簡単に](https://cloud.google.com/blog/ja/products/containers-kubernetes/google-cloud-now-supports-buildpacks)

使用するサンプル [クイックスタート | Cloud Run に Python サービスをデプロイする](https://cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-python-service)




+ 準備
+ 1. 通常のデプロイ
+ 2. 



### 準備

+ 事前に定義しておきます

```
export _gcp_pj_id='Your GCP Project ID'
```

+ Cloud Run の API の有効化

```
WIP
```


### 1. 通常のデプロイ

+ 公式サンプルをダウンロード

```
cd {Your Workspace}

git clone {このリポジトリ}
cd {このリポジトリ}
```

+ ファイル名の文字コードを確認する

```
nkf --guess /media/winxp/test2.txt
```
