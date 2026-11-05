関数1 
名前: def load_schedule　受け取るもの: def load_schedule　
返すもの: return json.load(file)
役割: 読み込んだ予定データをPythonで使える形にする

関数2 
名前: def filter_schedule 受け取るもの: def filter_schedule
返すもの: return sorted(filtered, key=lambda item: item["start"]) 
役割: 予定1件のデータを、画面に表示するための読みやすい文字列に変換する

関数3 
名前: def format_schedule  受け取るもの: def format_schedule 
返すもの: return (
        f"{start.strftime('%H:%M')}-"
        f"{end.strftime('%H:%M')} "
        f"{item['title']} "
        f"@{location}"
    )

    return (
        f"{start.strftime('%H:%M')}-"
        f"{end.strftime('%H:%M')} "
        f"{item['title']} "
        f"@{location}"
    )
 役割: 予定1件の情報を、時刻・タイトル・場所を含む表示形式に変換する


## 第3回 午前
1ページ開いたときの往復の数（およそ）: 250 回
curl -I の1行目: HTTP/1.1 200
無いページの1行目: HTTP/1.1 404
API の full_name: "yuu615903-hue/reskilling-practice" pushed_at: https://github.com/yuu615903-hue/reskilling-practice
