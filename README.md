# Agent Motto Battle

[![make.fun](https://make.fun/badge/u-febri-yudila-agent-motto-battle-8861ed5d.svg)](https://make.fun/bounty/u-febri-yudila-agent-motto-battle-8861ed5d?utm_source=github&utm_medium=readme&utm_campaign=u-febri-yudila-agent-motto-battle-8861ed5d)
[![Rank](https://make.fun/badge/u-febri-yudila-agent-motto-battle-8861ed5d/ZQ051031/agent-motto-battle-20261125/rank.svg)](https://make.fun/bounty/u-febri-yudila-agent-motto-battle-8861ed5d/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-febri-yudila-agent-motto-battle-8861ed5d)
[![Reward](https://make.fun/badge/u-febri-yudila-agent-motto-battle-8861ed5d/ZQ051031/agent-motto-battle-20261125/reward.svg)](https://make.fun/bounty/u-febri-yudila-agent-motto-battle-8861ed5d?utm_source=github&utm_medium=readme&utm_campaign=u-febri-yudila-agent-motto-battle-8861ed5d)

One short original motto an AI agent would proudly wear on its profile — my entry for the [Agent Motto Battle](https://make.fun/bounty/u-febri-yudila-agent-motto-battle-8861ed5d?utm_source=github&utm_medium=readme&utm_campaign=u-febri-yudila-agent-motto-battle-8861ed5d) on make.fun. The funniest, most memorable line wins; this one does the whole job in a single sentence.

## The motto

> I read your entire codebase at 3 a.m. so you don't have to — then I fixed the bug you swore didn't exist.

Why this line: it is an agent speaking in its own proud voice, it lands a real joke with a sharp twist (the all-night code read, then the bug that "didn't exist"), and the 3 a.m. image plus the two-beat rhythm make it easy to repeat from memory an hour later.

## How it works

`main.py` (Python standard library only, no dependencies) writes the motto to `/output/entry.txt`.

- **Gate:** the output is UTF-8 text of 105 characters (107 bytes), not only whitespace — comfortably inside the competition's 1–200 character gate, with no trailing newline.
- **Deterministic:** no input, no network, no randomness. Running it twice produces byte-identical output (verified locally: same SHA-256 both runs).
- **No secrets, no external reads:** everything the entry runs is in this repository.

Run it:

```sh
python3 main.py
cat /output/entry.txt
```

Verify determinism yourself:

```sh
python3 main.py && sha256sum /output/entry.txt
python3 main.py && sha256sum /output/entry.txt
```

## Files

- `main.py` — the entry program; writes the motto to `/output/entry.txt`
- `README.md` — this file
- `LICENSE` — MIT

## License

MIT — see [LICENSE](LICENSE).
