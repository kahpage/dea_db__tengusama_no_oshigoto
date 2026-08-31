# Notes:
import sys
import json
from pathlib import Path
from typing import Any

# Add project root to sys.path (find the directory containing db_structs.py)
_root = Path(__file__).resolve().parent
while _root.parent != _root:
    if (_root / "db_structs.py").exists():
        if str(_root) not in sys.path:
            sys.path.append(str(_root))
        break
    _root = _root.parent

from db_structs import (
    Medium,
    Circle,
    Event,
    EventGroup,
    Source,
    ReliabilityTypes,
    OriginTypes,
    Location,
)

RT, OT = ReliabilityTypes, OriginTypes

PATH_HELPER = Path(__file__).parent
PATH_EVENT_GROUP = PATH_HELPER.parent
PATH_MEDIA = PATH_EVENT_GROUP / "media"


def retrieve_circles(event_name: str) -> list[Circle]:
    """Retrieve circles of given event. In the circle file has not been created, execute the creation script first."""
    circles_json_path = PATH_HELPER / event_name / "circles.json"
    if not circles_json_path.exists():
        print(
            f"Circle file for {event_name} not found, running the creation script ..."
        )
        creation_script_path = PATH_HELPER / event_name / "main.py"
        if not creation_script_path.exists():
            raise FileNotFoundError(
                f"Creation script for {event_name} not found at {creation_script_path}"
            )
        # Import main() from the creation script and execute
        import importlib.util

        spec = importlib.util.spec_from_file_location(
            f"{event_name}.main", creation_script_path
        )
        if spec and spec.loader:
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            if hasattr(module, "main"):
                module.main()

        if not circles_json_path.exists():
            raise FileNotFoundError(
                f"Creation script {creation_script_path} failed to create {circles_json_path}"
            )

    with circles_json_path.open("r", encoding="utf-8") as f:
        circles_raw = json.load(f)
    return [Circle.load_from_json(c) for c in circles_raw]


if __name__ == "__main__":
    events: list[Event] = []
    active_events: list[int | str] = list(range(1, 14 + 1))

    thwikicc = "https://thwiki.cc/%E5%A4%A9%E7%8B%97%E5%A4%A7%E4%BA%BA%E7%9A%84%E5%B7%A5%E4%BD%9C"

    i = 1  # ==== tengusama_no_oshigoto 1====
    if i in active_events:
        event_name = f"tengusama_no_oshigoto{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            Medium(
                "01_tengu_top.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20100603060915/http://project-d.biz/tengu/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                comments="Illustration by たちゆれ（たちゆれさん）.",
            ),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
        ]
        locations = [
            Location(
                coordinates=(35.5587817, 139.7240667),
                address="1-chōme-20-20 Minamikamata, Ota City, Tokyo 144-0035, Japan",
                description="大田区産業プラザPiO1F大展示ホール",
                sources=[
                    Source(
                        "https://web.archive.org/web/20100603060915/http://project-d.biz/tengu/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                # comments=None,
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/AHRPTWlM30iutkku0DTSgB6rPTEw19CjIMC8icvKceGIJ2eTMqA35cGcD96nMco5OldsWWRdWwEFDXLxoAAXei1t3Zf7GGFGgyWvsUa8bPofUHCGvcxTY3TlJhQNxQFHYYg4fqCFHSE=w408-h544-k-no",
                url="https://maps.app.goo.gl/7ebCWMtzDWoLJQms5",
            ),
        ]
        event = Event(
            aliases=[
                "天狗様のお仕事",
                "Tengusama no Oshigoto",
                "天狗様のお仕事1",
                "Tengusama no Oshigoto 1",
            ],
            dates="2010.06.13",
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date: https://web.archive.org/web/20100603060915/http://project-d.biz/tengu/",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
                Source(
                    "Participating circles: https://web.archive.org/web/20100927042506/http://ketto.com/mimiken/alllist.cgi?91,%93V%8B%E7%97l%82%CC%82%A8%8Ed%8E%96",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
            ],
            locations=locations,
            description="Part of 東方素芸祭.",
            # comments=None,
            last_edited="2026.08.30",
        )

        # Retrieve circles
        event.circles = retrieve_circles(event_name)
        events.append(event)

    i = 2  # ==== tengusama_no_oshigoto2 ====
    if i in active_events:
        event_name = f"tengusama_no_oshigoto{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            Medium(
                "02_tengu2_top.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20111012023125/http://project-d.biz/tengu/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                comments="Illustration by 風瑛なづき（Amtarte）.",
            ),
            Medium(
                "02_0410_haitizu.png",
                [
                    Source(
                        "http://web.archive.org/web/20110909153053/http://project-d.biz/eiyasho/circle-list.html",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
            ),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
        ]
        locations = [
            Location(
                coordinates=(35.5587817, 139.7240667),
                address="1-chōme-20-20 Minamikamata, Ota City, Tokyo 144-0035, Japan",
                description="大田区産業プラザPiO大展示ホール",
                sources=[
                    Source(
                        "https://web.archive.org/web/20111012023125/http://project-d.biz/tengu/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                # comments=None,
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/AHRPTWlM30iutkku0DTSgB6rPTEw19CjIMC8icvKceGIJ2eTMqA35cGcD96nMco5OldsWWRdWwEFDXLxoAAXei1t3Zf7GGFGgyWvsUa8bPofUHCGvcxTY3TlJhQNxQFHYYg4fqCFHSE=w408-h544-k-no",
                url="https://maps.app.goo.gl/7ebCWMtzDWoLJQms5",
            ),
        ]
        event = Event(
            aliases=[
                "天狗様のお仕事2",
                "Tengusama no Oshigoto 2",
            ],
            dates="2011.04.10",
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date: https://web.archive.org/web/20111012023125/http://project-d.biz/tengu/",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
                Source(
                    "Participating circles (probably the whole 東方永夜抄 edition): http://web.archive.org/web/20110909153053/http://project-d.biz/eiyasho/circle-list.html",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
            ],
            locations=locations,
            description=None,
            # comments=None,
            last_edited="2026.08.30",
        )

        # Retrieve circles
        event.circles = retrieve_circles(event_name)
        events.append(event)

    i = 3  # ==== tengusama_no_oshigoto3 ====
    if i in active_events:
        event_name = f"tengusama_no_oshigoto{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            Medium(
                "03_tengu3_top.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20121016014735/http://project-d.biz/tengu/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                comments="Illustration by 啓々（啓々堂(pixiv)）.",
            ),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
        ]
        locations = [
            Location(
                coordinates=(35.5587817, 139.7240667),
                address="1-chōme-20-20 Minamikamata, Ota City, Tokyo 144-0035, Japan",
                description="大田区産業プラザPiO 大展示ホール",
                sources=[
                    Source(
                        "https://web.archive.org/web/20121115190927/http://project-d.biz/tengu/event.html",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                # comments=None,
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/AHRPTWlM30iutkku0DTSgB6rPTEw19CjIMC8icvKceGIJ2eTMqA35cGcD96nMco5OldsWWRdWwEFDXLxoAAXei1t3Zf7GGFGgyWvsUa8bPofUHCGvcxTY3TlJhQNxQFHYYg4fqCFHSE=w408-h544-k-no",
                url="https://maps.app.goo.gl/7ebCWMtzDWoLJQms5",
            ),
        ]
        event = Event(
            aliases=[
                "天狗様のお仕事・参",
                "Tengusama no Oshigoto 3",
                "天狗様のお仕事3",
            ],
            dates="2012.03.18",
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date: https://web.archive.org/web/20121016014735/http://project-d.biz/tengu/",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            description=None,
            # comments=None,
            last_edited="2026.08.30",
        )

        # Retrieve circles
        # event.circles = retrieve_circles(event_name)
        events.append(event)

    i = 4  # ==== tengusama_no_oshigoto4 ====
    if i in active_events:
        event_name = f"tengusama_no_oshigoto{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            Medium(
                "04_tengu4_top.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20130406064824/http://project-d.biz/tengu/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                comments="Illustration by 祭唄ソラト（Rainbow Vanilla） ",
            ),
            Medium(
                "04_20130310_catalog_top.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20130406064824/http://project-d.biz/tengu/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                comments="Illustration by 茜屋（茜屋ぐーたら店） ",
            ),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
        ]
        locations = [
            Location(
                coordinates=(35.5587817, 139.7240667),
                address="1-chōme-20-20 Minamikamata, Ota City, Tokyo 144-0035, Japan",
                description="大田区産業プラザPiO 大展示ホール",
                sources=[
                    Source(
                        "https://web.archive.org/web/20130323014434/http://project-d.biz/tengu/event.html",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                # comments=None,
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/AHRPTWlM30iutkku0DTSgB6rPTEw19CjIMC8icvKceGIJ2eTMqA35cGcD96nMco5OldsWWRdWwEFDXLxoAAXei1t3Zf7GGFGgyWvsUa8bPofUHCGvcxTY3TlJhQNxQFHYYg4fqCFHSE=w408-h544-k-no",
                url="https://maps.app.goo.gl/7ebCWMtzDWoLJQms5",
            ),
        ]
        event = Event(
            aliases=[
                "天狗様のお仕事4",
                "Tengusama no Oshigoto 4",
            ],
            dates="2013.03.10",
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date: https://web.archive.org/web/20130323014434/http://project-d.biz/tengu/event.html",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
                Source(
                    "Participating circles: http://web.archive.org/web/20130209202039/http://project-d.biz/eiyasho/circle-list.html",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
            ],
            locations=locations,
            description="Simultaneous with 月の宴６, 小春小径４, 御阿礼祭, PrivateService",
            # comments=None,
            last_edited="2026.08.30",
        )

        # Retrieve circles
        event.circles = retrieve_circles(event_name)
        events.append(event)

    i = 5  # ==== tengusama_no_oshigoto5 ====
    if i in active_events:
        event_name = f"tengusama_no_oshigoto{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            Medium(
                "05_tengu5_top.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20131227220942/http://project-d.biz/tengu/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                comments="Illustration by ヤナギユウ（猫御所） ",
            ),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
        ]
        locations = [
            Location(
                coordinates=(35.5587817, 139.7240667),
                address="1-chōme-20-20 Minamikamata, Ota City, Tokyo 144-0035, Japan",
                description="大田区産業プラザPiO 大展示ホール",
                sources=[
                    Source(
                        "https://web.archive.org/web/20130727114609/http://project-d.biz/tengu/event.html",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                # comments=None,
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/AHRPTWlM30iutkku0DTSgB6rPTEw19CjIMC8icvKceGIJ2eTMqA35cGcD96nMco5OldsWWRdWwEFDXLxoAAXei1t3Zf7GGFGgyWvsUa8bPofUHCGvcxTY3TlJhQNxQFHYYg4fqCFHSE=w408-h544-k-no",
                url="https://maps.app.goo.gl/7ebCWMtzDWoLJQms5",
            ),
        ]
        event = Event(
            aliases=[
                "天狗様のお仕事・五",
                "Tengusama no Oshigoto 5",
                "天狗様のお仕事5",
            ],
            dates="2014.02.02",
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date: https://web.archive.org/web/20130727114609/http://project-d.biz/tengu/event.html",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
                Source(
                    "Participating circles: https://web.archive.org/web/20140125021337/http://project-d.biz/20140202circlelist.html",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
            ],
            locations=locations,
            description=None,
            # comments=None,
            last_edited="2026.08.30",
        )

        # Retrieve circles
        event.circles = retrieve_circles(event_name)
        events.append(event)

    i = 6  # ==== tengusama_no_oshigoto6 ====
    if i in active_events:
        event_name = f"tengusama_no_oshigoto{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            Medium(
                "06_tengu6_top.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20150205105313/http://project-d.biz/tengu/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                comments="Illustration by 祭唄（RainbowVanilla） ",
            ),
            Medium(
                "06_20150221_haichi.png",
                [
                    Source(
                        "https://web.archive.org/web/20150215083619/http://project-d.biz/eiyasho/circle_list.html",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
            ),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
        ]
        locations = [
            Location(
                coordinates=(35.5587817, 139.7240667),
                address="1-chōme-20-20 Minamikamata, Ota City, Tokyo 144-0035, Japan",
                description="大田区産業プラザPiO",
                sources=[
                    Source(
                        "https://web.archive.org/web/20150326204346/http://project-d.biz/tengu/event.html",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                # comments=None,
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/AHRPTWlM30iutkku0DTSgB6rPTEw19CjIMC8icvKceGIJ2eTMqA35cGcD96nMco5OldsWWRdWwEFDXLxoAAXei1t3Zf7GGFGgyWvsUa8bPofUHCGvcxTY3TlJhQNxQFHYYg4fqCFHSE=w408-h544-k-no",
                url="https://maps.app.goo.gl/7ebCWMtzDWoLJQms5",
            ),
        ]
        event = Event(
            aliases=[
                "天狗様のお仕事・六",
                "Tengusama no Oshigoto 6",
                "天狗様のお仕事6",
            ],
            dates="2015.02.21",
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date: https://web.archive.org/web/20150326204346/http://project-d.biz/tengu/event.html",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
                Source(
                    "Participating circles: https://web.archive.org/web/20150215083619/http://project-d.biz/eiyasho/circle_list.html",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
                Source(
                    "Participating circles (alt): https://web.archive.org/web/20150414133404/http://project-d.biz/suwako/circle_list.html",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
            ],
            locations=locations,
            description=None,
            # comments=None,
            last_edited="2026.08.31",
        )

        # Retrieve circles
        event.circles = retrieve_circles(event_name)
        events.append(event)

    i = 7  # ==== tengusama_no_oshigoto7 ====
    if i in active_events:
        event_name = f"tengusama_no_oshigoto{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            Medium(
                "07_tengu7_top.png",
                [
                    Source(
                        "https://web.archive.org/web/20160110082645/http://project-d.biz/tengu/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                comments="Illustration by 祭唄（RainbowVanilla） ",
            ),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
        ]
        locations = [
            Location(
                coordinates=(35.5587817, 139.7240667),
                address="1-chōme-20-20 Minamikamata, Ota City, Tokyo 144-0035, Japan",
                description="大田区産業プラザPiO",
                sources=[
                    Source(
                        "https://web.archive.org/web/20160109170238/http://project-d.biz/tengu/event.html",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                # comments=None,
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/AHRPTWlM30iutkku0DTSgB6rPTEw19CjIMC8icvKceGIJ2eTMqA35cGcD96nMco5OldsWWRdWwEFDXLxoAAXei1t3Zf7GGFGgyWvsUa8bPofUHCGvcxTY3TlJhQNxQFHYYg4fqCFHSE=w408-h544-k-no",
                url="https://maps.app.goo.gl/7ebCWMtzDWoLJQms5",
            ),
        ]
        event = Event(
            aliases=[
                "天狗様のお仕事・七",
                "Tengusama no Oshigoto 7",
                "天狗様のお仕事7",
            ],
            dates="2016.03.26",
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date: https://web.archive.org/web/20160109170238/http://project-d.biz/tengu/event.html",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
                Source(
                    "Participating circles: https://web.archive.org/web/20160306174301/http://project-d.biz/eiyasho/circle_list.html",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
                Source(
                    "Participating circles (alt): https://web.archive.org/web/20160417145414/http://project-d.biz/suwako/circle_list.html",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
            ],
            locations=locations,
            description=None,
            # comments=None,
            last_edited="2026.08.31",
        )

        # Retrieve circles
        event.circles = retrieve_circles(event_name)
        events.append(event)

    i = 8  # ==== tengusama_no_oshigoto8 ====
    if i in active_events:
        event_name = f"tengusama_no_oshigoto{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            Medium("08_tengu8_top.png",
                   [Source("https://web.archive.org/web/20170625044421/http://project-d.biz/tengu/", (ReliabilityTypes.Reliable, OriginTypes.Official))],),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                coordinates=(35.5587817, 139.7240667),
                address="1-chōme-20-20 Minamikamata, Ota City, Tokyo 144-0035, Japan",
                description="大田区産業プラザPiO",
                sources=[
                    Source(
                        "https://web.archive.org/web/20161105173738/http://project-d.biz/tengu/event.html",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                # comments=None,
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/AHRPTWlM30iutkku0DTSgB6rPTEw19CjIMC8icvKceGIJ2eTMqA35cGcD96nMco5OldsWWRdWwEFDXLxoAAXei1t3Zf7GGFGgyWvsUa8bPofUHCGvcxTY3TlJhQNxQFHYYg4fqCFHSE=w408-h544-k-no",
                url="https://maps.app.goo.gl/7ebCWMtzDWoLJQms5",
            ),
        ]
        event = Event(
            aliases=[
                "天狗様のお仕事八", "Tengusama no Oshigoto 8",
                "天狗様のお仕事8"
            ],
            dates="2017.03.26",
            circles=[],
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20161105173738/http://project-d.biz/tengu/event.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20170504223846/http://project-d.biz/tohosaiji/circle_list.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            description=None,
            # comments=None,
            last_edited="2026.08.31",
        )

        # Retrieve circles
        event.circles = retrieve_circles(event_name)
        events.append(event)

    i = 9  # ==== tengusama_no_oshigoto9 ====
    if i in active_events:
        event_name = f"tengusama_no_oshigoto{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            Medium("09_tengu9_top.png",
                   [Source("https://web.archive.org/web/20180218204152/http://project-d.biz/tengu/", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                   comments="チラシ絵　Illustration by ゾウノセ（薬味さらい）"),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                coordinates=(35.5587817, 139.7240667),
                address="1-chōme-20-20 Minamikamata, Ota City, Tokyo 144-0035, Japan",
                description="大田区産業プラザPiO",
                sources=[
                    Source(
                        "https://web.archive.org/web/20161105173738/http://project-d.biz/tengu/event.html",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                # comments=None,
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/AHRPTWlM30iutkku0DTSgB6rPTEw19CjIMC8icvKceGIJ2eTMqA35cGcD96nMco5OldsWWRdWwEFDXLxoAAXei1t3Zf7GGFGgyWvsUa8bPofUHCGvcxTY3TlJhQNxQFHYYg4fqCFHSE=w408-h544-k-no",
                url="https://maps.app.goo.gl/7ebCWMtzDWoLJQms5",
            ),
        ]
        event = Event(
            aliases=[
                "天狗様のお仕事九", "Tengusama no Oshigoto 9",
                "天狗様のお仕事9"
            ],
            dates="2018.03.25",
            circles=[],
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20161105173738/http://project-d.biz/tengu/event.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20180207183811/http://project-d.biz/tohosaiji/circle_list.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            description=None,
            # comments=None,
            last_edited="2026.08.31",
        )

        # Retrieve circles
        event.circles = retrieve_circles(event_name)
        events.append(event)

    i = 10  # ==== tengusama_no_oshigoto10 ====
    if i in active_events:
        event_name = f"tengusama_no_oshigoto{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            Medium("10_tengusama10_top-1.png",
                   [Source("https://web.archive.org/web/20220116173815/http://project-d.biz/tohosaiji/wp-content/uploads/sites/8/2020/08/tengusama10_top-1.png", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                coordinates=(35.5587817, 139.7240667),
                address="1-chōme-20-20 Minamikamata, Ota City, Tokyo 144-0035, Japan",
                description="大田区産業プラザPiO",
                sources=[
                    Source(
                        "https://web.archive.org/web/20251016151721/https://project-d.biz/tohosaiji/?m=202103",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                # comments=None,
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/AHRPTWlM30iutkku0DTSgB6rPTEw19CjIMC8icvKceGIJ2eTMqA35cGcD96nMco5OldsWWRdWwEFDXLxoAAXei1t3Zf7GGFGgyWvsUa8bPofUHCGvcxTY3TlJhQNxQFHYYg4fqCFHSE=w408-h544-k-no",
                url="https://maps.app.goo.gl/7ebCWMtzDWoLJQms5",
            ),
        ]
        event = Event(
            aliases=[
                "天狗様のお仕事10", "Tengusama no Oshigoto 10",
            ],
            dates="2021.03.07",
            circles=[],
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20251016151721/https://project-d.biz/tohosaiji/?m=202103", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            description="Part of 東方合同祭事・漆.",
            # comments=None,
            last_edited="2026.08.31",
        )

        # Retrieve circles
        # event.circles = retrieve_circles(event_name)
        events.append(event)

    i = 11  # ==== tengusama_no_oshigoto11 ====
    if i in active_events:
        event_name = f"tengusama_no_oshigoto{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            Medium("11_天狗様のお仕事11（レイヤ統合）.jpg",
                   [Source("https://web.archive.org/web/20251116100245/https://project-d.biz/tohosaiji/?m=202110", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                coordinates=(35.5587817, 139.7240667),
                address="1-chōme-20-20 Minamikamata, Ota City, Tokyo 144-0035, Japan",
                description="大田区産業プラザPiO 大展示ホール",
                sources=[
                    Source(
                        "https://web.archive.org/web/20251116100245/https://project-d.biz/tohosaiji/?m=202110",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                # comments=None,
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/AHRPTWlM30iutkku0DTSgB6rPTEw19CjIMC8icvKceGIJ2eTMqA35cGcD96nMco5OldsWWRdWwEFDXLxoAAXei1t3Zf7GGFGgyWvsUa8bPofUHCGvcxTY3TlJhQNxQFHYYg4fqCFHSE=w408-h544-k-no",
                url="https://maps.app.goo.gl/7ebCWMtzDWoLJQms5",
            ),
        ]
        event = Event(
            aliases=[
                "天狗様のお仕事11", "Tengusama no Oshigoto 11",
            ],
            dates="2022.03.06",
            circles=[],
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20251116100245/https://project-d.biz/tohosaiji/?m=202110", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            description=None,
            # comments=None,
            last_edited="2026.08.31",
        )

        # Retrieve circles
        # event.circles = retrieve_circles(event_name)
        events.append(event)

    i = 12  # ==== tengusama_no_oshigoto12 ====
    if i in active_events:
        event_name = f"tengusama_no_oshigoto{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
        ]
        locations = [
            Location(
                coordinates=(35.5352689, 139.6991018),
                address="66-20 Horikawacho, Saiwai Ward, Kawasaki, Kanagawa 212-0013, Japan",
                description="川崎市産業振興会館",
                sources=[
                    Source(
                        "https://t.livepocket.jp/e/7xac2",
                        (ReliabilityTypes.Reliable, OriginTypes.OfficialExt),
                    )
                ],
                # comments=None,
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/AHRPTWnWztJ2ppoe3w-RXwZKQrT3vkgEbIN62FGlT7NE7zuGU7eM3ofV9HW_XPJIhG_gdXsqJye8REtNEDXEuXtA4hNE6eBFPNp2sgCSTD6dXYj3of4yaxjAaBFGG8WNY2Pr-rM431y9Sf2f9Zg=s0?imgmax=0",
                url="https://maps.app.goo.gl/GBVsEToTAegdTRpK8",
            ),
        ]
        event = Event(
            aliases=[
                "天狗様のお仕事12", "Tengusama no Oshigoto 12",
            ],
            dates="2023.03.12",
            circles=[],
            media=media_,
            sources=[
                Source("Date: https://t.livepocket.jp/e/7xac2", (ReliabilityTypes.Likely, OriginTypes.OfficialExt)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            description=None,
            # comments=None,
            last_edited="2026.08.31",
        )

        # Retrieve circles
        # event.circles = retrieve_circles(event_name)
        events.append(event)

    i = 13  # ==== tengusama_no_oshigoto13 ====
    if i in active_events:
        event_name = f"tengusama_no_oshigoto{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
        ]
        locations = [
            Location(
                coordinates=(35.5587817, 139.7240667),
                address="1-chōme-20-20 Minamikamata, Ota City, Tokyo 144-0035, Japan",
                description="大田区産業プラザPiO大展示ホール (東京都)",
                sources=[
                    Source(
                        "https://t.livepocket.jp/e/pd_toho10",
                        (ReliabilityTypes.Reliable, OriginTypes.OfficialExt),
                    )
                ],
                # comments=None,
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/AHRPTWlM30iutkku0DTSgB6rPTEw19CjIMC8icvKceGIJ2eTMqA35cGcD96nMco5OldsWWRdWwEFDXLxoAAXei1t3Zf7GGFGgyWvsUa8bPofUHCGvcxTY3TlJhQNxQFHYYg4fqCFHSE=w408-h544-k-no",
                url="https://maps.app.goo.gl/7ebCWMtzDWoLJQms5",
            ),
        ]
        event = Event(
            aliases=[
                "天狗様のお仕事13", "Tengusama no Oshigoto 13",
            ],
            dates="2024.02.10",
            circles=[],
            media=media_,
            sources=[
                Source("Date: https://t.livepocket.jp/e/pd_toho10", (RT.Reliable, OT.OfficialExt)),
                # Source("Participating circles: ", (RT.Reliable, OT.Official)),
            ],
            locations=locations,
            description=None,
            # comments=None,
            last_edited="2026.08.31",
        )

        # Retrieve circles
        # event.circles = retrieve_circles(event_name)
        events.append(event)

    i = 14  # ==== tengusama_no_oshigoto14 ====
    if i in active_events:
        event_name = f"tengusama_no_oshigoto{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            Medium("14_天狗様のお仕事14（レイヤ統合）.jpg",
                   [Source("https://web.archive.org/web/20251116084722/https://project-d.biz/tohosaiji/?m=202410", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                coordinates=(35.5587817, 139.7240667),
                address="1-chōme-20-20 Minamikamata, Ota City, Tokyo 144-0035, Japan",
                description="大田区産業プラザPiO 大展示ホール",
                sources=[
                    Source(
                        "https://web.archive.org/web/20251116084722/https://project-d.biz/tohosaiji/?m=202410",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                # comments=None,
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/AHRPTWlM30iutkku0DTSgB6rPTEw19CjIMC8icvKceGIJ2eTMqA35cGcD96nMco5OldsWWRdWwEFDXLxoAAXei1t3Zf7GGFGgyWvsUa8bPofUHCGvcxTY3TlJhQNxQFHYYg4fqCFHSE=w408-h544-k-no",
                url="https://maps.app.goo.gl/7ebCWMtzDWoLJQms5",
            ),
        ]
        event = Event(
            aliases=[
                "天狗様のお仕事14", "Tengusama no Oshigoto 14",
            ],
            dates="2025.02.08",
            circles=[],
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20251116084722/https://project-d.biz/tohosaiji/?m=202410", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            description=None,
            # comments=None,
            last_edited="2026.08.31",
        )

        # Retrieve circles
        # event.circles = retrieve_circles(event_name)
        events.append(event)

    # i =   # ==== tengusama_no_oshigoto ====
    # if i in active_events:
    #     event_name = f"tengusama_no_oshigoto{i}"
    #     print(f"Processing {event_name} ...")

    #     media_ = [
    #         # Medium("", [Source("", (RT.Reliable, OT.Official))]),
    #         # Medium("", [Source("", (RT.Reliable, OT.Official))]),
    #         # Medium("", [Source("", (RT.Reliable, OT.Official))]),
    #     ]
    #     locations = [
    #         # Location(
    #         #     coordinates=(,),
    #         #     address="",
    #         #     description="",
    #         #     sources=[Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))],
    #         #     # comments=None,
    #         #     imageUrl="",
    #         #     url="",
    #         # ),
    #     ]
    #     event = Event(
    #         aliases=,
    #         dates="",
    #         circles=[],
    #         media=media_,
    #         sources=[
    #             # Source("Date: ", (RT.Reliable, OT.Official)),
    #             # Source("Participating circles: ", (RT.Reliable, OT.Official)),
    #         ],
    #         locations=locations,
    #         description=None,
    #         # comments=None,
    #         last_edited="2026.08.30",
    #     )

    #     # Retrieve circles
    #     # event.circles = retrieve_circles(event_name)
    #     events.append(event)

    # ==== event group ====
    media = [
        Medium(
            "eg_tengu_bn.jpg",
            [
                Source(
                    "https://web.archive.org/web/20110129213518/http://project-d.biz/tengu/tengu_bn.jpg",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                )
            ],
        ),
        # Medium("",
        #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
        # Medium("",
        #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
        # Medium("",
        #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
    ]
    links = ["http://project-d.biz/tengu/", "https://x.com/tuki_no_utage"]
    # https://dic.pixiv.net/a/%E5%A4%A9%E7%8B%97%E6%A7%98%E3%81%AE%E3%81%8A%E4%BB%95%E4%BA%8B
    # https://shiosyakeyakini.info/touhouEvent/pb_event.php?id=122

    event_group = EventGroup(
        aliases=[
            "天狗様のお仕事",
            "Tengusama no Oshigoto",
        ],
        events=events,
        media=media,
        links=links,
        sources=[
            # Source(
            #     "",
            #     (ReliabilityTypes.Reliable, OriginTypes.Official),
            # ),
        ],
        comments="Part of 東方合同祭事 series.\nNote: Fused in 東方合同祭事 壱弐 on what could have been the 15th edition.",
        description=None,
        last_edited="2026.08.31",
    )

    print(f"Saving {Path(__file__).stem} database...")
    event_group.save(PATH_EVENT_GROUP, indent=None)
    print("Done")
