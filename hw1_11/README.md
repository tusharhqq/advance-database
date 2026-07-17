# HW1 Q11 — AQuery maximum loss per stock

Source: `../database-interview/hw1/aquery/` (same files).

## (i) Executable AQuery

`max_loss.a` — uses built-ins `maxs`, `prev`, `min` with `ASSUMING ASC ID, ASC date`:

```
SELECT ID,
       min(endofdayprice - maxs(prev(endofdayprice))) AS worst_loss
FROM ticks
ASSUMING ASC ID, ASC date
GROUP BY ID
```

Example expects: s1 = -3, s2 = -60.

## (ii) Optimization

See `optimization_notes.md`.

## Run on Modal (plain `aquery` image)

```bash
modal run aquery/example/run_hw1_11.py
```

This mounts `mountain/hw1_11` at `/work`, compiles with `a2q`, and executes with licensed `q`.

## Compile locally (Docker)

```bash
docker build --platform=linux/amd64 -t aquery:local -f dockerr/aquery/Dockerfile aquery
docker run --rm --platform=linux/amd64 \
  -v "$PWD/mountain/hw1_11:/work" -w /work aquery:local \
  a2q -c -a 1 -o max_loss.generated.q max_loss.a
```

`a2q` needs no KX license. See [`dockerr/aquery/README.md`](../../dockerr/aquery/README.md).
