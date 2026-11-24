# Running the project (WSL2 + Docker)

Copy these files over your unzipped `Big-Data-Project-main/` folder (merge/overwrite), then from that folder:

```bash
docker compose up -d --build          # first run downloads several GB of images; be patient
docker compose ps                     # everything should be Up (app containers restart until infra is ready)
docker compose logs -f stream         # you should see "Data inserted into HBase"
docker compose logs -f hdfs-ingest    # "Stored in HDFS: /batch-layer/raw/..."
docker compose logs -f batch-loop     # "data stored in postgresql" after a few records exist
```

| What | Where |
|---|---|
| Real-time dashboard (Flask) | http://localhost:5000 |
| HDFS UI | http://localhost:9870 |
| HBase master UI | http://localhost:16010 |
| Postgres (Power BI / DBeaver) | localhost:5433, db `bigdata`, user/pass `postgres`, table `Phone` |

Check the batch result:
```bash
docker compose exec postgres psql -U postgres -d bigdata -c 'SELECT brand, price FROM "Phone" LIMIT 5;'
```
Stop: `docker compose down` (add `-v` to wipe data).
