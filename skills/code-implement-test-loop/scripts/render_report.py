#!/usr/bin/env python3
import json, sys

TEMPLATE = """## Task\n- {task}\n\n## Repo Path\n- {repo_path}\n\n## Validation Command\n- {validation_command}\n\n## Iteration Log\n{iteration_log}\n\n## Final Status\n- {final_status}\n\n## Remaining Issues\n{remaining_issues}\n"""


def main():
    data = json.load(sys.stdin)
    task = data.get('task', 'n/a')
    repo_path = data.get('repo_path', 'n/a')
    validation_command = data.get('validation_command', data.get('test_command', 'n/a'))
    final_status = data.get('final_status', 'unknown')
    issues = data.get('remaining_issues') or []
    iters = data.get('iterations') or []
    iteration_log = []
    for it in iters:
        iteration_log.append(f"- Round {it.get('iteration')}: returncode={it.get('returncode')} ")
    if not iteration_log:
        iteration_log = ['- n/a']
    if issues:
        remaining = '\n'.join(f'- {x}' for x in issues)
    else:
        remaining = '- none noted'
    print(TEMPLATE.format(
        task=task,
        repo_path=repo_path,
        validation_command=validation_command,
        iteration_log='\n'.join(iteration_log),
        final_status=final_status,
        remaining_issues=remaining,
    ))


if __name__ == '__main__':
    main()
