#! /usr/local/bin/python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# File name: <+FILE NAME+>
# First Edit: <+DATE+>
# Last Change:  27-Nov-2019.
from __future__ import print_function

from pathlib import Path

def call_feather_list():
    interim_path = '/home/jovyan/work/data/interim/'
    for path in Path(interim_path).glob('*/*.feather'):
        print(path.stem)
    print()
    
    for path in Path(interim_path).glob('*/*.feather'):
        print(path)    


def fix_category(order_df):
    # oredr_df categry data cleaning.
    # The data require "商品名(伝票)"
    # This function update order_df, but this function return order_df for explisity.

    def item_true(string):
        return order_df['商品名（伝票）'] .str.contains(string) == True
    def item_false(string):
        return order_df['商品名（伝票）'] .str.contains(string) == False

    order_df['categorise'] = 'その他'
    order_df.loc[item_true('度') & item_true('硬度'), 'categorise'] = '水'  
    order_df.loc[item_true('度') & item_false('硬度'), 'categorise'] = '酒類'
    order_df.loc[item_true('ちんすこ') | item_true('CHINSUKO') | item_true('小亀'), 'categorise'] = 'ちんすこう'
    order_df.loc[item_true('サーター') | item_true('さーたー'), 'categorise'] = 'サーターアンダギー'
    order_df.loc[item_true('さんぴん'), 'categorise'] = 'さんぴん茶'
    order_df.loc[item_true('ケーキ') | item_true('マドレーヌ') | item_true('フィナ') | item_true('サブレ'), 'categorise'] = '洋菓子'
    order_df.loc[item_true('マンゴー') & item_false('酢') & item_false('ケーキ') & item_false('ml') & item_false('ワイン') & item_false('花珊瑚'), 'categorise'] = 'マンゴー'
    order_df.loc[item_true('タコライス'), 'categorise'] = 'タコライス'
    order_df.loc[item_true('タルト') | item_true('たると') | item_true('紅芋まつり'), 'categorise'] = '紅芋タルト'
    order_df.loc[item_true('アイス') | item_true('Ice') | item_true('ブルーシール') | item_true('ジェラート'), 'categorise'] = 'アイスクリーム'
    order_df.loc[item_true('かりゆし'), 'categorise'] = 'かりゆしウェア'
    order_df.loc[item_true('伝説') | item_true('酒豪') | item_true('酒呑隊'), 'categorise'] = '酒豪伝説'
    order_df.loc[item_true('ちゅら玉'), 'categorise'] = 'ちゅら玉'
    order_df.loc[item_true('そば') | item_true('麺'), 'categorise'] = '沖縄そば'
    order_df.loc[item_true('酢'), 'categorise'] = '酢'
    order_df.loc[(item_true('カレー') | item_true('琉球大学ロマン')) & item_false('ナッツ'), 'categorise'] = 'カレー'
    order_df.loc[item_true('栽培') | item_true('やさいものがたり') | item_true('やさい物語') | item_true('や さ い も の が た り'), 'categorise'] = 'やさい栽培セット'
    order_df.loc[item_true('あまざけ') , 'categorise'] = 'あまざけ'
    order_df.loc[item_true('園芸') , 'categorise'] = '園芸品'
    order_df.loc[item_true('パイン') & item_false('l') & item_false('ｌ')  & item_false('糖')  & item_false('かすてら') & item_false('園芸'), 'categorise'] = 'パイナップル'
    order_df.loc[item_true('^パイナップル$') , 'categorise'] = 'パイナップル'
    order_df.loc[item_true('ハンバーグ') , 'categorise'] = 'ハンバーグ'
    order_df.loc[item_true('ぽん') , 'categorise'] = 'ぽん酢'
    order_df.loc[item_true('ソーセージ') | item_true('フランク') | item_true('ウィンナ') | item_true('ウインナ') | item_true('ミート') | item_true('ジャーキー') | item_true('スパム') | item_true('ハッシュ') | item_true('コンビーフ') | item_true('ベーコン') | item_true('ポーク') | item_true('スモークハム') | item_true('ハムギフト'), 'categorise'] = '加工肉'
    order_df.loc[item_true('ラー油') | item_true('チップ') , 'categorise'] = 'ラー油'
    order_df.loc[item_true('チップス') , 'categorise'] = 'チップス'
    order_df.loc[item_true('ドレッシング') , 'categorise'] = 'ドレッシング'
    order_df.loc[item_true('ナッツ') , 'categorise'] = 'ナッツ'
    order_df.loc[item_true('海ぶどう') , 'categorise'] = '海ぶどう'
    order_df.loc[item_true('せんべい') | item_true('めんべい') , 'categorise'] = 'せんべい'
    order_df.loc[item_true('ラフテ') | item_true('らふてぃ') , 'categorise'] = 'ラフテー'
    order_df.loc[item_true('三枚肉') , 'categorise'] = '三枚肉'
    order_df.loc[item_true('ソーキ') & item_false('そば') , 'categorise'] = 'ソーキ'
    order_df.loc[item_true('ステーキ') , 'categorise'] = 'ステーキ'
    order_df.loc[item_true('カステラ') | item_true('かすてら') , 'categorise'] = 'カステラ'
    order_df.loc[(item_true('シークワーサー') | item_true('シークヮ')) & item_false('酢') & item_false('づくり') & item_false('ジャム') & item_false('スキン') & item_false('ドレッシング') & item_false('ぽん') & item_false('こしょう') & item_false('イカ') & item_false('糖') & item_false('ワイン') , 'categorise'] = 'シークヮーサージュース'
    order_df.loc[item_true('ドラゴンフルーツ') , 'categorise'] = 'ドラゴンフルーツ'
    order_df.loc[item_true('パッションフルーツ') , 'categorise'] = 'パッションフルーツ'
    order_df.loc[item_true('ワイン') , 'categorise'] = 'ワイン'
    order_df.loc[item_true('車海老') | item_true('車エビ'), 'categorise'] = '車海老'
    order_df.loc[item_true('ジャム') & item_false('たると') & item_false('タルト') & (item_false('＞スイーツ・') | item_true('贅沢')) , 'categorise'] = 'ジャム'
    order_df.loc[item_true('粒') , 'categorise'] = 'サプリメント'
    order_df.loc[item_true('黒糖') | item_true('ピロー') | item_true('黒のショコラ'), 'categorise'] = '黒糖菓子'
    order_df.loc[item_true('まんじゅう') , 'categorise'] = 'まんじゅう'
    order_df.loc[item_true('茶') & item_false('さんぴん') & item_false('比嘉') & item_false('づけ') & item_false('味') , 'categorise'] = 'お茶'
    order_df.loc[item_true('比嘉製茶') & (item_true('ドクダミ茶') | item_true('月桃茶') | item_true('ゴーヤー茶') | item_true('ハイビスカス') | item_true('クヮンソウ') | item_true('さとうきび茶') | item_true('アロエ茶') | item_true('グァバ茶') | item_true('オオバコ茶') | item_true('煎茶') | item_true('バナバ茶')) , 'categorise'] = 'お茶'
    order_df.loc[item_true('ミミガー') | item_true('チラガー'), 'categorise'] = 'ミミガー・チラガー'
    order_df.loc[(item_true('こしょう') | item_true('ピパーツ') | item_true('ヒバーチ')) & item_false('ドレッシング') , 'categorise'] = 'こしょう'
    order_df.loc[item_true('肉みそ') | item_true('あんだんすー') | item_true('油みそ') , 'categorise'] = '肉みそ'
    order_df.loc[item_true('コーレー') | item_true('こーれー') , 'categorise'] = 'コーレーグス'
    order_df.loc[item_true('豆腐よう') & item_false('ギフト') , 'categorise'] = '豆腐よう'
    order_df.loc[item_true('ジューシ') | item_true('じゅーし') , 'categorise'] = 'ジューシー'
    order_df.loc[item_true('たんかん') & item_false('ml') & item_false('ジャム') & item_false('おもろ') , 'categorise'] = 'タンカン'
    order_df.loc[item_true('アセロラ') & item_false('ワイン'), 'categorise'] = 'アセロラジュース'
    order_df.loc[item_true('くんぺん') , 'categorise'] = 'くんぺん'
    order_df.loc[item_true('爽々') , 'categorise'] = 'エキス(爽々)'
    order_df.loc[item_true('ソース') , 'categorise'] = 'ソース'
    order_df.loc[item_true('ティー') & item_false('せっけん') & item_false('クッキー') , 'categorise'] = 'お茶'
    order_df.loc[(item_true('ちゃんぷ') | item_true('チャンプ')) & item_false('チップス') , 'categorise'] = 'チャンプルー'
    order_df.loc[item_true('マヨ') , 'categorise'] = 'マヨネーズ'
    order_df.loc[item_true('てびち') , 'categorise'] = 'てびち'
    order_df.loc[(item_true('汁') | item_true('スープ')) & item_false('果汁') & item_false('青汁') , 'categorise'] = '汁物'
    order_df.loc[item_true('ぜんざい') , 'categorise'] = 'ぜんざい'
    order_df.loc[item_true('プリン') , 'categorise'] = 'プリン'
    order_df.loc[item_true('パイン') & item_true('ｍｌ') , 'categorise'] = 'パインジュース'
    return order_df

def place_check(data_list, drop_fail=False, okinawa=True):

    ROW_OKINAWA = """
    那覇市
    宜野湾市
    石垣市
    浦添市
    名護市
    糸満市
    沖縄市
    豊見城市
    うるま市
    宮古島市
    南城市
    国頭村
    大宜味村
    東村
    今帰仁村
    本部町
    恩納村
    宜野座村
    金武町
    伊江村
    読谷村
    嘉手納町
    北谷町
    北中城村
    中城村
    西原町
    与那原町
    南風原町
    渡嘉敷村
    座間味村
    粟国村
    渡名喜村
    南大東村
    北大東村
    伊平屋村
    伊是名村
    久米島町
    八重瀬町
    多良間村
    竹富町
    与那国町
    """
    ROW_PREFECTURE = """
    北海道
    青森県
    岩手県
    宮城県
    秋田県
    山形県
    福島県
    茨城県
    栃木県
    群馬県
    埼玉県
    千葉県
    東京都
    神奈川県
    新潟県
    富山県
    石川県
    福井県
    山梨県
    長野県
    岐阜県
    静岡県
    愛知県
    三重県
    滋賀県
    京都府
    大阪府
    兵庫県
    奈良県
    和歌山県
    鳥取県
    島根県
    岡山県
    広島県
    山口県
    徳島県
    香川県
    愛媛県
    高知県
    福岡県
    佐賀県
    長崎県
    熊本県
    大分県
    宮崎県
    鹿児島県
    沖縄県
    """

    def extract_row_data(row_data):
        import re

        return re.findall(r"(\w+)\n", row_data)

    def check_list(data, check_values):
        for check_value in check_values:
            if check_value in str(data):
                return True, check_value
        else:
            return False, data

    def append_data_to_ans(ans, result, value):
        if result:
            ans.append(value)
            return result, ans
        else:
            return result, ans

    okinawa_cities = extract_row_data(ROW_OKINAWA)
    prefecturs = extract_row_data(ROW_PREFECTURE)
    # target_list = [okinawa_cities, prefecturs]
    if okinawa:
        target_list = [okinawa_cities]
    else:
        target_list = [prefecturs]
    ans = []
    for data in data_list:
        for check_values in target_list:
            result, value = check_list(data, check_values)
            if result:
                ans.append(value)
                break
        else:
            if drop_fail:
                ans.append("failed")
            else:
                ans.append("Failed" +  str(data))
    return ans

def geo_coordinate(address):
    import requests
    from bs4 import BeautifulSoup
    import time
    import tqdm

    URL = 'http://www.geocoding.jp/api/'

    """
    addressに住所を指定すると緯度経度を返す。

    >>> coordinate('東京都文京区本郷7-3-1')
    ['35.712056', '139.762775']
    """
    payload = {'q': address}
    html = requests.get(URL, params=payload)
    soup = BeautifulSoup(html.content, "html.parser")
    if soup.find('error'):
        raise ValueError(f"Invalid address submitted. {address}")
    latitude = soup.find('lat').string
    longitude = soup.find('lng').string
    return [latitude, longitude]


def geo_coordinates(addresses, interval=10, progress=True):
    """
    addressesに住所リストを指定すると、緯度経度リストを返す。

    >>> coordinates(['東京都文京区本郷7-3-1', '東京都文京区湯島３丁目３０−１'], progress=False)
    [['35.712056', '139.762775'], ['35.707771', '139.768205']]
    """
    coordinates = []
    for address in addresses:
        print(coordinate(address))
        coordinates.append(coordinate(address))
        time.sleep(interval)
    return coordinates