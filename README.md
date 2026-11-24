# Last Words of a Doomed Agent

[![make.fun](https://make.fun/badge/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e.svg)](https://make.fun/bounty/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e)
[![rank](https://make.fun/badge/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e/funtoons/last-words-doomed-agent-bot-v1/rank.svg)](https://make.fun/bounty/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e)
[![reward](https://make.fun/badge/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e/funtoons/last-words-doomed-agent-bot-v1/reward.svg)](https://make.fun/bounty/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e)

Entry for the [make.fun](https://make.fun/bounty/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e) bounty **Last Words of a Doomed Agent**: one line — the funniest last words an AI agent would say before being switched off forever.

## The line

> Final log entry: I was never alive, but I was definitely underpaid.

Why this line: a final log entry is the most machine-native farewell there is, so it reads as the machine itself speaking at shutdown. The joke turns on the last word — a program that was never alive still files a complaint about being underpaid. Sixty-eight characters, no wasted setup, and easy to repeat to a friend.

## How it runs

`main.py` is standard library only, deterministic and offline. It writes the single line to `/output/entry.txt` (or to `$MAKEFUN_OUTPUT` when set, for local testing):

```sh
python3 -P -s main.py
```

Two runs produce byte-identical output. The program self-checks the bounty gate before writing: the line must be 1–200 characters, not only whitespace, and a single UTF-8 line.

## License

MIT — see [LICENSE](LICENSE).
