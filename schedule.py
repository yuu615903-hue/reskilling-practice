import json
import sys
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo


def load_schedule():
    """schedule.json を読み込む"""
    file_path = Path(__file__).parent / "schedule.json"

    if not file_path.exists():
        print("エラー: schedule.json が見つかりません。")
        sys.exit(1)

    try:
        with file_path.open("r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("エラー: schedule.json の形式が正しくありません。")
        sys.exit(1)


def filter_schedule(schedule, target_date):
    """指定した日付の予定だけを抽出し、時刻順に並べる"""
    filtered = [
        item for item in schedule
        if item.get("start", "").startswith(target_date)
    ]

    return sorted(filtered, key=lambda item: item["start"])


def format_schedule(item):
    """予定1件を指定された文字列に変換する"""
    start = datetime.fromisoformat(item["start"])
    end = datetime.fromisoformat(item["end"])

    location = item.get("location")

    if not location:
        location = "（場所なし）"

    return (
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


def main():
    # コマンドライン引数があれば使用し、なければ日本時間の今日の日付を使う
    if len(sys.argv) >= 2:
        target_date = sys.argv[1]

        try:
            datetime.strptime(target_date, "%Y-%m-%d")
        except ValueError:
            print("エラー: 日付は YYYY-MM-DD 形式で指定してください。")
            sys.exit(1)
    else:
        target_date = datetime.now(
            ZoneInfo("Asia/Tokyo")
        ).strftime("%Y-%m-%d")

    schedule = load_schedule()
    filtered = filter_schedule(schedule, target_date)

    print(f"{target_date} の予定 {len(filtered)} 件")

    for item in filtered:
        print(format_schedule(item))


if __name__ == "__main__":
        main()