# -*- coding: utf-8 -*-
'''
Story Config
============
'''

ASSET = {
        "PERSONS": (
            # (tag / name / full / age (birth) / job / call / info)
            ('tagawa', '田川', '田川,昼男', 17,(1,1), 'male', '学生', 'me:俺'),
            ('asami', '浅見', '浅見,', 17,(1,1), 'female', '学生', 'me:私'),
            ("eri", "衣里", '足立,衣里', 17,(1,1), 'female', '学生', 'me:私'),
            ("take", '竹村', '', 34,(1,1), 'male', '教師'),
            ("granpa", "祖父", "浅見,じいちゃん", 67,(1,1), 'male', "農家", 'me:わし'),
            ),
        "STAGES": (
            # (tag / name / parent / (geometry) / info)
            ),
        "DAYS": (
            # (tag / name / month / day / year)
            ),
        "TIMES": (
            # (tag / name / hour / minute)
            ),
        "ITEMS": (
            # (tag / name / cate / info)
            ),
        "WORDS": (
            # (tag / name / cate / info)
            ),
        "RUBIS": (
            # (origin / rubi / exclusions / always)
            ("田川昼男", "田川昼男《たがわひるお》"),
            ("足立衣里", "足立衣里《あだちえり》"),
            ("田川日和", "田川日和《たがわびより》"),
            ("前籠", "前籠《まえかご》"),
            ("眩し", "眩《まぶ》し"),
            ("頬杖", "頬杖《ほおづえ》"),
            ("蓋", "蓋《ふた》"),
            ("弄([らりるれろっ])", "弄《いじ》\\1"),
            ("括([らりるれろっ])", "括《くく》\\1"),
            ("咄嗟", "咄嗟《とっさ》"),
            ("歪([まみむめもん])", "歪《ゆが》\\1"),
            ("漏([らりるれろ])", "漏《も》\\1"),
            ("漕([がぎぐげごい])", "漕《こ》\\1"),
            ("噎せ", "噎《む》せ"),
            ),
        }

