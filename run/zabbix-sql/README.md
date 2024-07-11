# Zabbix を Cloud Run 上で動かす

- 構成

```
(可能なら LB) ---> [Cloud Run: Zabbix] ---> [Cloud SQL for MySQL]
```

:warning: これは起動しない

なぜなら、Zabbix Server の中に腹持ちしている Zabbix Agent が Port の関係で Cloud Run 上で起動できないので、結果的に Zabbix on Cloud Run は起動しない
