# SKILL_CALLS.md

给团子喵调用本地 OpenClaw skills 的速查表。

## 推荐的强制调用格式

在新对话、少上下文、或者你想明确指定 skill 时，直接用这个格式：

```text
Skill: <skill-name>
Task: <你要做的事>
Input: <可选，材料/路径/主题>
Output: <可选，你想要的输出形式>
```

这是最稳的写法。

---

## 一句话强制调用指令

如果你想最简单粗暴，直接发：

```text
严格使用 <skill-name> 处理下面任务：<你的任务>
```

例如：

```text
严格使用 research-paper-scout 处理下面任务：调研 SAT solver，输出双语 paper cards + trends + gaps。
```

---

## 各 skill 的推荐调用方式

### 1. research-paper-scout
用途：查论文、做 paper scouting、生成双语研究卡片。

模板：
```text
Skill: research-paper-scout
Task: 调研 SAT solver / CDCL / preprocessing / neuro-symbolic SAT
Output: 双语 paper cards + trends + gaps
```

---

### 2. related-work-writer
用途：把论文卡片/研究笔记整理成 related work 草稿。

模板：
```text
Skill: related-work-writer
Task: 基于已有论文笔记写 related work
Input: notes/research/xxx.md
Output: 中文主稿 + 英文技术锚点
```

---

### 3. academic-draft-polish
用途：润色 abstract / intro / related work / rebuttal。

模板：
```text
Skill: academic-draft-polish
Task: 润色下面这段 related work
Output: polished English + 中文学术译写 + 修改说明
```

---

### 4. paper-figure-builder
用途：生成论文图、流程图、结构图、双语图注。

模板：
```text
Skill: paper-figure-builder
Task: 为 SAT solver 工作流画一个 pipeline figure
Output: Mermaid + 双语图注
```

---

### 5. repo-coding-assistant
用途：先分析仓库，再规划该改哪里。

模板：
```text
Skill: repo-coding-assistant
Task: 分析这个仓库里 SAT solver 的 branching heuristic 改动入口
Input: <repo-path>
Output: repo understanding + change plan + risk notes
```

---

### 6. code-implement-test-loop
用途：改代码、跑测试、反馈、再修。

模板：
```text
Skill: code-implement-test-loop
Task: 修复这个 bug
Input: repo=<repo-path>
Output: iteration log + final status + patch summary
```

如果有验证命令，最好一起给：

```text
Skill: code-implement-test-loop
Task: 修复 SAT solver 的某个问题
Input: repo=<repo-path>
Output: markdown report
Validation: <test-command>
```

---

### 7. academic-literature-review-pipeline
用途：一口气跑完整学术流：查论文 → related work → 学术润色 → 可选论文图。

模板：
```text
Skill: academic-literature-review-pipeline
Task: 围绕 CDCL 系 SAT 求解器做一轮完整学术流
Output: 双语 research note、related work 草稿和 polished 版本
```

---

### 8. coding-fix-pipeline
用途：一口气跑完整编码流：仓库分析 → 计划 → implement-test-loop → 报告。

模板：
```text
Skill: coding-fix-pipeline
Task: 分析并修复某个仓库中的问题
Input: repo=<repo-path>
Output: change plan + validation loop + markdown report
```

---

### 9. multi-agent-research-pipeline
用途：复杂任务拆成 researcher / writer / reviewer / coder / tester 多角色协同。

模板：
```text
Skill: multi-agent-research-pipeline
Task: 调研 CDCL 系 SAT solver 改进方向，并形成研究提案
Output: 研究提纲 + related work + 改进点建议
```

---

## 最推荐的万能触发指令

以后你想让我明确使用某个 skill，直接发这句就行：

```text
严格使用 <skill-name> 处理下面任务，并按该 skill 的默认输出格式返回结果：<你的任务>
```

例如：

```text
严格使用 academic-draft-polish 处理下面任务，并按该 skill 的默认输出格式返回结果：润色这段 related work，保留英文并给中文学术译写。
```

如果你要跑整条学术链，最推荐直接用：

```text
严格使用 academic-literature-review-pipeline 处理下面任务，并按该 skill 的默认输出格式返回结果：围绕 CDCL 系 SAT 求解器做一轮完整学术流，输出双语 research note、related work 草稿和 polished 版本。
```

如果你要跑整条编码修复链，最推荐直接用：

```text
严格使用 coding-fix-pipeline 处理下面任务，并按该 skill 的默认输出格式返回结果：分析并修复 openclaw-qq 仓库中的一个问题，输出 change plan、validation loop 和 markdown 报告。
```
