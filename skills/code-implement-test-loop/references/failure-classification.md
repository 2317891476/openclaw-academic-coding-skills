# Failure Classification

Classify test failures into one of these buckets:

## implementation_bug
The code change is wrong or incomplete.

## regression
A previously working behavior broke elsewhere.

## missing_requirement
The task description is insufficient or ambiguous.

## environment_problem
Missing dependency, service, credential, fixture, or external runtime issue.

## flaky_test
The failure appears nondeterministic.

## scope_explosion
The requested change is triggering a broader refactor than expected.

Use the bucket in the final summary so the user can decide whether to continue automatically.
