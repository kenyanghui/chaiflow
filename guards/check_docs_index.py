#!/usr/bin/env python3
"""check_docs_index.py — chaiflow 文档索引漂移防护.

机制借鉴内部 loong-workflow guards/（文档声称 vs 仓库实际互相断言）。
决策见 docs/decisions/2026-11-04-borrow-loong-workflow-mechanisms.md（D21）。

断言四项（全过 exit 0，任一失败 exit 1 并逐项指出改哪里）:
  1. PROJECT-OVERVIEW「文档索引」与 README「仓内结构」树引用的
     docs/ 相对路径全部真实存在（拦截 pending/、core/ 式幻影路径）
  2. decisions/ 每篇文件正文含编号（## 或 # 行内 D+数字），编号无重复
  3. README 决策编号区间（如「D1–D21」）与 decisions/ 实际最大编号一致
  4. retrospectives/TEMPLATE.md 存在（复盘纪律的模板件）

设计原则：仅标准库、零第三方依赖、只读（不修改任何文件）。
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"


def fail(msg):
    print(f"  ✗ {msg}")
    return False


def ok(msg):
    print(f"  ✓ {msg}")
    return True


def main():
    results = []

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    overview = (DOCS / "PROJECT-OVERVIEW.md").read_text(encoding="utf-8")

    # 1. 索引引用路径全部存在（README 结构树 + OVERVIEW 索引里的 docs/ 相对路径）
    refs = set(re.findall(r"`((?:decisions|retrospectives|playbooks|pending)/[^`]+)`", readme + overview))
    # 忽略目录型引用（无扩展名结尾的父目录本身，如 `docs/decisions/`）
    file_refs = {r for r in refs if "." in r.rsplit("/", 1)[-1]}
    missing = [r for r in sorted(file_refs) if not (DOCS / r).exists()]
    if missing:
        results.append(fail(f"断言1: 索引引用了不存在的文件: {missing}——删索引行或补文件"))
    else:
        results.append(ok(f"断言1: 索引引用的 {len(file_refs)} 个文档路径全部真实存在"))

    # 2. 决策编号无重复
    nums = {}
    for f in sorted((DOCS / "decisions").glob("*.md")):
        m = re.search(r"\bD(\d+)\b", f.read_text(encoding="utf-8")[:400])
        if m:
            n = int(m.group(1))
            nums.setdefault(n, []).append(f.name)
    dup = {n: fs for n, fs in nums.items() if len(fs) > 1}
    if dup:
        results.append(fail(f"断言2: 决策编号重复: {dup}"))
    else:
        results.append(ok(f"断言2: decisions/ 编号无重复（当前 {len(nums)} 篇带编号）"))

    # 3. README 编号区间上限 == 实际最大编号
    max_n = max(nums) if nums else 0
    m = re.search(r"D1[–-]D(\d+)", readme)
    if not m:
        results.append(fail("断言3: README 未找到「D1–D<N>」编号区间表述"))
    elif int(m.group(1)) == max_n:
        results.append(ok(f"断言3: README 区间 D1–D{m.group(1)} == 实际最大编号 D{max_n}"))
    else:
        results.append(fail(f"断言3: README 写 D1–D{m.group(1)}，实际最大编号 D{max_n}——两处一起改"))

    # 4. 复盘模板存在
    tpl = DOCS / "retrospectives" / "TEMPLATE.md"
    results.append(ok("断言4: retrospectives/TEMPLATE.md 存在") if tpl.exists() else fail("断言4: retrospectives/TEMPLATE.md 缺失——复盘纪律模板件丢了"))

    n_ok = sum(1 for r in results if r is True)
    print(f"索引漂移防护: {'PASS' if all(results) else 'FAIL'} （{n_ok}/{len(results)} 断言通过）")
    sys.exit(0 if all(results) else 1)


if __name__ == "__main__":
    main()
