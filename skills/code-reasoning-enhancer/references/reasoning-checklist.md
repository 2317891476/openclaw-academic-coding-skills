# Reasoning Checklist

Before writing ANY code, verify you have considered:

## 1. Edge Cases
- [ ] Null / undefined inputs
- [ ] Empty collections (array, list, map)
- [ ] Boundary values (min, max, overflow)
- [ ] Duplicate inputs
- [ ] Invalid input formats

## 2. Concurrency
- [ ] Race conditions
- [ ] Deadlocks potential
- [ ] Thread safety
- [ ] Async timing issues
- [ ] Shared mutable state

## 3. Memory & Resources
- [ ] Memory leaks possibilities
- [ ] Resource cleanup (files, connections)
- [ ] Large data handling
- [ ] Buffer overflow

## 4. Algorithms
- [ ] Time complexity (Big O)
- [ ] Space complexity
- [ ] Alternative approaches (at least 2)
- [ ] Trade-offs between approaches

## 5. Error Handling
- [ ] What exceptions can occur
- [ ] How to propagate errors
- [ ] Logging strategy
- [ ] Fail-fast vs fail-safe

## 6. Testing Strategy
- [ ] How to verify correctness
- [ ] What test cases needed
- [ ] Edge case coverage
