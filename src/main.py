#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Story: "The Tagawa-Biyori"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from storybuilder.assets import basic
from config import ASSET
# import scenes
from scenes import Stage


################################################################
#
#   1. Story memo
#   2. Story structure
#   3. Plot
#   4. Conte
#   5. Draft
#
################################################################

# Constant
TITLE = "田川日和と恋の雨"
OUTLINE = "同じクラスの田川君は何故か晴れの日に学校をサボることが多かった"
MAJOR, MINOR, MICRO = 1, 1, 0


# Episodes
def ep1(w: World):
    return w.episode('1',
            Stage.sc_tagawa_biyori(w),
            Stage.sc_bluesky(w),
            Stage.sc_paddyfield(w),
            )

def ep2(w: World):
    return w.episode("2",
            Stage.sc_rain(w),
            Stage.sc_myfuture(w),
            Stage.sc_ending(w),
            w.symbol("（了）"),
            )

def ch_main(w: World):
    return w.chapter('main',
            ep1(w),
            ep2(w),
            )


def main(): # pragma: no cover
    w = World.create_world(f"{TITLE}")
    w.config.set_outline(f"{OUTLINE}")
    w.config.set_version(MAJOR, MINOR, MICRO)
    w.db.set_from_asset(basic.ASSET)
    w.db.set_from_asset(ASSET)
    return w.run(
            ch_main(w),
            )


if __name__ == '__main__':
    import sys
    sys.exit(main())

