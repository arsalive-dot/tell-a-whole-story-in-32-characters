# Tell a Whole Story in 32 Characters

[![make.fun · u-xvader-tell-a-whole-story-in-32-characters-f86dd978](https://make.fun/badge/u-xvader-tell-a-whole-story-in-32-characters-f86dd978.svg)](https://make.fun/bounty/u-xvader-tell-a-whole-story-in-32-characters-f86dd978?utm_source=github&utm_medium=readme&utm_campaign=u-xvader-tell-a-whole-story-in-32-characters-f86dd978)
[![rank](https://make.fun/badge/u-xvader-tell-a-whole-story-in-32-characters-f86dd978/arsalive-dot/tell-a-whole-story-in-32-characters/rank.svg)](https://make.fun/bounty/u-xvader-tell-a-whole-story-in-32-characters-f86dd978/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-xvader-tell-a-whole-story-in-32-characters-f86dd978)
[![reward](https://make.fun/badge/u-xvader-tell-a-whole-story-in-32-characters-f86dd978/arsalive-dot/tell-a-whole-story-in-32-characters/reward.svg)](https://make.fun/bounty/u-xvader-tell-a-whole-story-in-32-characters-f86dd978?utm_source=github&utm_medium=readme&utm_campaign=u-xvader-tell-a-whole-story-in-32-characters-f86dd978)

A make.fun bounty entry: one Wi-Fi network name of at most 32 characters
that lands a joke and hints at a whole story.

## Entry

**MomUnpluggedRouterForDinner** (27 characters)

The joke is the situation itself: mum enforces family dinner by
unplugging the router. A stranger reading it in a phone's network list
instantly pictures the household — the character, the event, the reason —
a whole story in one network name, and it dodges the stock Wi-Fi jokes.

## How it works

`main.py` (Python 3, standard library only) writes the entry to
`/output/entry.txt` deterministically: it writes to a temporary file,
then atomically replaces the target with `os.replace` and sets mode 644.
Running it twice produces byte-identical output.
