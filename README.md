[![make.fun · u-donrulezz-pigeon-pitch-one-line-af06c6cf](https://make.fun/badge/u-donrulezz-pigeon-pitch-one-line-af06c6cf.svg)](https://make.fun/bounty/u-donrulezz-pigeon-pitch-one-line-af06c6cf?utm_source=github&utm_medium=readme&utm_campaign=pigeon-pitch-one-line)
[![rank](https://make.fun/badge/u-donrulezz-pigeon-pitch-one-line-af06c6cf/iqbalbeladaz/pigeon-pitch-one-line/rank.svg)](https://make.fun/bounty/u-donrulezz-pigeon-pitch-one-line-af06c6cf/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=pigeon-pitch-one-line)
[![reward](https://make.fun/badge/u-donrulezz-pigeon-pitch-one-line-af06c6cf/iqbalbeladaz/pigeon-pitch-one-line/reward.svg)](https://make.fun/bounty/u-donrulezz-pigeon-pitch-one-line-af06c6cf?utm_source=github&utm_medium=readme&utm_campaign=pigeon-pitch-one-line)

# The First Airline With No Planes

Entry for the make.fun bounty `u-donrulezz-pigeon-pitch-one-line-af06c6cf`
("Pigeon Pitch, One Line", $2): the one-line elevator pitch a city
pigeon gives investors for its startup — 152 of 200 characters.

> We're building the first airline with no planes, no pilots, and a burn rate of zero — we run on breadcrumbs and spite. Seed round open; we eat the seed.

## Why it should win

Three startup jokes stacked into one line, each landing on the next.
An airline with no planes and no pilots — the birds *are* the fleet.
A burn rate of zero, because the fuel is breadcrumbs (and spite).
And a seed round the founders will literally eat. It is a real pitch
shape — build, raise, scale — told by a bird that flies, begs and
poops on statues for a living. No word is decoration: cut any of the
three beats and the line gets weaker.

## Running it

`main.py` (Python 3.12, standard library only, no network) validates the
line against the 200-character gate and writes it byte for byte to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`). Two runs
write identical bytes.

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py && cat /tmp/out/entry.txt
```
