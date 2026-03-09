#!/usr/bin/env python3
import json, subprocess, sys, time
from pathlib import Path

USAGE = "run_loop.py '<test-command>' [max-iterations]"


def run(cmd):
    p = subprocess.run(cmd, shell=True, text=True, capture_output=True)
    return {
        'returncode': p.returncode,
        'stdout': p.stdout[-8000:],
        'stderr': p.stderr[-8000:],
    }


def main():
    if len(sys.argv) < 2:
        print(USAGE, file=sys.stderr)
        sys.exit(2)
    cmd = sys.argv[1]
    limit = int(sys.argv[2]) if len(sys.argv) > 2 else 3
    out = {
        'test_command': cmd,
        'max_iterations': limit,
        'started_at': int(time.time()),
        'iterations': [],
    }
    for i in range(1, limit + 1):
        result = run(cmd)
        out['iterations'].append({'iteration': i, **result})
        if result['returncode'] == 0:
            out['final_status'] = 'passed'
            break
    else:
        out['final_status'] = 'failed'
    out['finished_at'] = int(time.time())
    print(json.dumps(out, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
