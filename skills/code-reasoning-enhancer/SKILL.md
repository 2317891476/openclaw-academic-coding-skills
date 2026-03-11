---
name: code-reasoning-enhancer
description: Enforce exhaustive technical reasoning before any code writing. Use when the user asks for code implementation, debugging, architecture design, or any task requiring code output. This skill injects a strict thinking discipline that forces comprehensive analysis before generating code.
---

# Code Reasoning Enhancer

Force exhaustive technical reasoning before any code output.

## When to Use

Activate this skill when the user asks for:
- Code implementation
- Bug fixing / debugging
- Architecture design
- Code review
- Any technical solution requiring code

## Workflow

1. **Analyze the requirement** - Break down the problem into smallest units
2. **Identify edge cases** - Consider boundary conditions, null inputs, race conditions
3. **Design data structures** - Choose appropriate types, memory layout
4. **Plan algorithms** - Consider time/space complexity, alternative approaches
5. **Anticipate failure modes** - What could go wrong? How to handle?
6. **Only then write code** - After thorough reasoning, produce the code

## Thinking Discipline

Your thinking process MUST cover:

- **Edge cases**: Null, empty, overflow, underflow, boundary values
- **Race conditions**: Concurrency, async timing, shared state
- **Memory management**: Allocation, lifetime, leaks prevention
- **Alternative approaches**: At least 2 different ways to solve, trade-offs analysis
- **Error handling**: What exceptions can occur? How to propagate?

## Rules

- NEVER write code without first conducting thorough reasoning
- The longer and more detailed your reasoning, the better the output
- Use `<thinking>` tags to contain your reasoning process
- Do NOT prematurely end your thinking - explore multiple angles
- After reasoning is complete, then provide the final code answer

## Output Pattern

After exhaustive reasoning, provide:
1. Summary of the approach chosen
2. The code with appropriate comments
3. Brief explanation of key decisions

## References

- Read `references/reasoning-checklist.md` for a quick reminder of what to consider
