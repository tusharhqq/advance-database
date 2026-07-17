# HW1 Q11(ii) — optimization notes

Assuming `ticks` is already sorted by `ID` (but not necessarily by `date`):

1. **Local sort within each ID group by date** (or by time). Because groups are contiguous after the ID sort, this is a set of independent small sorts — cheap if each stock has few rows relative to N.
2. **Single forward scan per group:** maintain `running_max` of prices seen so far; at each new price p, candidate loss is p - \texttt{running_max}; track the minimum candidate; then update `running_max ← max(running_max, p)`. This is O(n_g) per group after sorting.
3. **No self-join.** A nested loop over buy/sell pairs is O(n_g^2) per stock and unnecessary: the worst loss always sells at some j after buying at the maximum price among 0..j-1.
4. **Vectorized plan (AQuery/q style):**
  `ASSUMING ASC ID, ASC date` then  
   `min(price - maxs(prev(price))) by ID`  
   so the engine can use arrable primitives (`maxs`, `min`) without materializing a join.
5. **If ID-sorted but date-unsorted:** either sort globally by `(ID, date)` once, or hash-aggregate into per-ID vectors then sort each vector — prefer one global sort if the table is large and cold.
6. **Parallelism:** partition by ID ranges (already contiguous) and compute per-partition minima independently.

