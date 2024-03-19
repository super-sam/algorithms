# Unbounded Knapsack
- Don't consider once rejected and move ahead
- If considered, you can take it again

```
dp[n][w] = max(
   dp[n - 1][w],
   val[n - 1] + dp[n][w - val[n - 1]]
)
```

## Mapping
| 0/1 Knapsack | Unbounded Knapsack |
| -- | -- |
| wt[] | length[] |
| val[] | price[] |