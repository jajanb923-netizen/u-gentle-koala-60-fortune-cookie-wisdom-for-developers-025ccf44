# Fortune Cookie Wisdom for Developers

[![make.fun](https://make.fun/badge/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44.svg)](https://make.fun/bounty/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44)
[![rank](https://make.fun/badge/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44/jajanb923-netizen/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44/rank.svg)](https://make.fun/bounty/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44)
[![reward](https://make.fun/badge/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44/jajanb923-netizen/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44/reward.svg)](https://make.fun/bounty/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44)

One original line of fortune-cookie wisdom for a software developer, written by
`main.py` to `/output/entry.txt` for the [make.fun bounty](https://make.fun/bounty/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44).

> The estimate you gave in the meeting will outlive the code it described.

## Entry

`main.py` (Python 3.13 stdlib only, deterministic, no network) writes a single
72-character fortune-cookie line to `entry.txt`, after a self-check enforcing
the gate: UTF-8 text, 1–120 characters, not only white space, a single line.

Ten candidate lines were written and scored against the judge's five criteria
in `CANDIDATES.md`; the line above won the head-to-head on the judge's own
decision procedure — it ties the runner-up on criteria 1–3 and wins on
criterion 4 (a fresh observation about estimates, not a familiar trope
rephrased).

## Run locally

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```
