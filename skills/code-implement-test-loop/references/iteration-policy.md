# Iteration Policy

Default loop:
1. Make a minimal change
2. Run validation
3. Read failures carefully
4. Fix the most proximal cause first
5. Repeat until success or limit

Stop early when:
- requirements are ambiguous
- failures are flaky or unrelated
- the patch scope is exploding
- a dependency or environment problem blocks progress

Always end with a concise iteration log.
