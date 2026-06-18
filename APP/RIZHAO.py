"""
日照 家乡旅行推荐 / 르자오 고향 여행 추천 앱
"""

import tkinter as tk
from tkinter import ttk

THEME_COLORS = {
    "bg": "#F5F0EB",
    "card": "#FFFFFF",
    "text": "#3E2723",
    "subtext": "#8D6E63",
    "muted": "#BCAAA4",
    "tag_bg": "#EFEBE9",
    "tag_text": "#5D4037",
    "shadow": "#D0C8C0",
    "hc": "#00695C",
    "ac": "#80CBC4",
}


CITY = {
    "name_zh": "日照", "name_ko": "르자오",
    "tagline_zh": "东方太阳城 · 水上运动之都", "tagline_ko": "동방 태양의 도시 · 수상 스포츠의 수도",
    "icon": "🌊", "header_color": "#00695C", "accent_color": "#80CBC4",
    "desc_zh": '日照市位于山东省东南部黄海之滨，因「日出初光先照」得名。总面积5359平方公里。',
    "desc_ko": '르자오시는 산둥성 동남부 황해 연안, 해가 가장 먼저 비추는 곳. 총면적 5,359km².',
    "highlights": [{"zh": "东方太阳城", "ko": "동방 태양의 도시"}, {"zh": "联合国人居奖城市", "ko": "UN 해비타트상 수상 도시"}, {"zh": "中国优秀旅游城市", "ko": "중국 우수 관광 도시"}, {"zh": "水上运动之都", "ko": "수상 스포츠의 수도"}],
    "attractions": [
            {"name_zh": "万平口海滨风景区", "name_ko": "완핑커우 해변 풍경구", "desc_zh": "日照最具代表性海滨景区，4公里优质沙滩。", "desc_ko": "르자오 대표 해변, 4km 우수 모래사장.", "tags": ["4A景区", "海滨浴场", "免费开放"], "famous": "金沙滩·潮汐塔·帆船基地", "img_icon": "🏖️", "img_color": "#FF8F00"},
            {"name_zh": "日照海滨国家森林公园", "name_ko": "르자오 해변 국가삼림공원", "desc_zh": "全国首批国家森林公园，林海相依天然氧吧。", "desc_ko": "강북 최대 삼나무 숲, 천연 산소방.", "tags": ["4A景区", "森林公园", "天然氧吧"], "famous": "水杉林·森林浴场·木栈道", "img_icon": "🌲", "img_color": "#2E7D32"},
            {"name_zh": "五莲山风景区", "name_ko": "우롄산 풍경구", "desc_zh": "奇峰异石峡谷幽深。苏轼赞叹「奇秀不减雁荡」。", "desc_ko": "기이한 봉우리와 깊은 계곡.", "tags": ["4A景区", "地质奇观", "佛教名山"], "famous": "五莲山大佛·光明寺·九仙山", "img_icon": "⛰️", "img_color": "#4E342E"},
            {"name_zh": "灯塔风景区", "name_ko": "등대 풍경구", "desc_zh": "日照标志性景点，观日出听涛声最佳地点。", "desc_ko": "르자오 랜드마크.", "tags": ["标志景点", "日出观景", "免费"], "famous": "灯塔·礁石公园·日出广场", "img_icon": "🗼", "img_color": "#1565C0"},
            {"name_zh": "刘家湾赶海园", "name_ko": "류자완 갯벌 체험원", "desc_zh": "中国最大赶海园，适合亲子家庭。", "desc_ko": "중국 최대 갯벌 체험원.", "tags": ["4A景区", "亲子旅游", "渔家文化"], "famous": "赶海体验·海鲜加工·渔家乐", "img_icon": "🦐", "img_color": "#00838F"}
        ],
    "foods": [
            {"name_zh": "日照海鲜大咖", "name_ko": "르자오 해산물 대가", "desc_zh": "螃蟹、对虾、扇贝等新鲜海味大铁盘蒸制。", "desc_ko": "신선 해산물을 대형 철판에 쪄냄.", "features": "地方招牌 · 海鲜盛宴", "img_icon": "🦞", "img_color": "#D84315"},
            {"name_zh": "日照煎饼", "name_ko": "르자오 젠빙", "desc_zh": "小米玉米等杂粮为原料，薄如纸香脆可口。", "desc_ko": "잡곡 원료, 종이처럼 얇고 바삭.", "features": "传统主食 · 非遗美食", "img_icon": "🫓", "img_color": "#F9A825"},
            {"name_zh": "西施舌", "name_ko": "서시설", "desc_zh": "日照海域特产贝类，肉质细嫩。", "desc_ko": "르자오 해역 특산 조개.", "features": "海产珍品 · 季节限定", "img_icon": "🐚", "img_color": "#AD1457"},
            {"name_zh": "日照绿茶", "name_ko": "르자오 녹차", "desc_zh": "中国最北端绿茶产区。", "desc_ko": "중국 최북단 녹차 산지.", "features": "地理标志产品 · 江北第一茶", "img_icon": "🍵", "img_color": "#33691E"},
            {"name_zh": "海沙子面", "name_ko": "하이샤쯔 몐", "desc_zh": "极小贝类熬浓汤做面卤。", "desc_ko": "작은 조개로 진한 육수.", "features": "地方特色 · 渔家风味", "img_icon": "🍜", "img_color": "#BF360C"}
        ],
    "routes": [
            {"name_zh": "一日滨海休闲游", "name_ko": "1일 해변 레저", "duration": "1天", "stops": ["清晨：灯塔看日出", "上午：万平口沙滩", "中午：海鲜大咖", "下午：森林公园骑行"]},
            {"name_zh": "两日山海风光游", "name_ko": "2일 산해 풍경", "duration": "2天", "stops": ["Day1：灯塔日出 → 万平口 → 森林公园", "Day2：五莲山 → 九仙山 → 绿茶品鉴 → 返程"]},
            {"name_zh": "三日深度体验游", "name_ko": "3일 심층 체험", "duration": "3天", "stops": ["Day1：灯塔 → 万平口 → 海鲜夜市", "Day2：五莲山 → 光明寺 → 九仙山", "Day3：刘家湾赶海 → 绿茶茶园 → 返程"]}
        ],
}

class TravelApp:
    def __init__(self, root):
        self.root = root
        self.root.title(f"{CITY['name_zh']} 家乡旅行推荐 / {CITY['name_ko']} 고향 여행 추천")
        self.root.geometry("1100x750")
        self.root.minsize(900, 600)
        self.root.configure(bg=THEME_COLORS["bg"])
        self.current_page = None
        self.main = tk.Frame(self.root, bg=THEME_COLORS["bg"])
        self.main.pack(fill=tk.BOTH, expand=True)
        self._build_layout()

    def _clear_main(self):
        self.root.unbind_all("<MouseWheel>")
        for w in self.main.winfo_children():
            w.destroy()

    def _build_layout(self):
        c = CITY
        hc = THEME_COLORS["hc"]
        ac = THEME_COLORS["ac"]

        sidebar = tk.Frame(self.main, bg="#2C1A14", width=210)
        sidebar.pack(side=tk.LEFT, fill=tk.Y)
        sidebar.pack_propagate(False)

        st = tk.Frame(sidebar, bg="#2C1A14")
        st.pack(fill=tk.X, pady=(30, 12), padx=18)
        tk.Label(st, text=c['icon'], font=("Segoe UI Emoji", 38), bg="#2C1A14").pack()
        tk.Label(st, text=c['name_zh'], font=("Microsoft YaHei", 22, "bold"), fg="#FFF8E1", bg="#2C1A14").pack(pady=(2, 0))
        tk.Label(st, text=c['name_ko'], font=("Malgun Gothic", 12), fg=ac, bg="#2C1A14").pack()

        tk.Frame(sidebar, bg=ac, height=1).pack(fill=tk.X, padx=18, pady=8)

        nav_items = [
            ("home", "\U0001f3e0  首页 / \ud648"),
            ("attractions", "\U0001f3ef  景点 / \uad00\uad11\uc9c0"),
            ("foods", "\U0001f35c  美食 / \ubbf8\uc2dd"),
            ("routes", "\U0001f5fa\ufe0f  路线 / \uacbd\ub85c"),
            ("ai_info", "\U0001f916  AI 使用"),
        ]
        self._nav_btns = {}
        for key, label in nav_items:
            btn = tk.Button(sidebar, text=label, font=("Microsoft YaHei", 12, "bold"),
                          bg="#2C1A14", fg="#A1887F",
                          activebackground="#45302B", activeforeground="#FFFFFF",
                          bd=0, cursor="hand2", anchor="w", padx=22, pady=12,
                          command=lambda k=key: self._page(k))
            btn.pack(fill=tk.X)
            self._nav_btns[key] = btn

        tk.Label(sidebar, text="\u00a9 2025 \u5bb6\u4e61\u65c5\u884c\nFlutter \uacfc\uc81c", font=("Microsoft YaHei", 8),
                fg="#5D4037", bg="#2C1A14", justify=tk.CENTER).pack(side=tk.BOTTOM, pady=20)

        self._content = tk.Frame(self.main, bg=THEME_COLORS["bg"])
        self._content.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self._page("home")

    def _page(self, page_key):
        self.current_page = page_key
        hc = THEME_COLORS["hc"]
        ac = THEME_COLORS["ac"]
        for key, btn in self._nav_btns.items():
            active = key == page_key
            btn.configure(bg="#45302B" if active else "#2C1A14",
                         fg=ac if active else "#A1887F")
        for w in self._content.winfo_children():
            w.destroy()
        if page_key == "home": self._render_home()
        elif page_key == "attractions": self._render_attractions()
        elif page_key == "foods": self._render_foods()
        elif page_key == "routes": self._render_routes()
        elif page_key == "ai_info": self._render_ai_info()

    def _title(self, text, sub=""):
        f = tk.Frame(self._content, bg=THEME_COLORS["bg"])
        f.pack(fill=tk.X, padx=35, pady=(30, 8))
        tk.Label(f, text=text, font=("Microsoft YaHei", 22, "bold"), fg="#3E2723", bg=THEME_COLORS["bg"]).pack(anchor="w")
        if sub:
            tk.Label(f, text=sub, font=("Malgun Gothic", 10), fg=THEME_COLORS["subtext"], bg=THEME_COLORS["bg"]).pack(anchor="w")
        tk.Frame(self._content, bg="#D7CCC8", height=2).pack(fill=tk.X, padx=35, pady=(4, 18))

    def _scrollable(self):
        cv = tk.Canvas(self._content, bg=THEME_COLORS["bg"], bd=0, highlightthickness=0)
        sb = ttk.Scrollbar(self._content, orient="vertical", command=cv.yview)
        sf = tk.Frame(cv, bg=THEME_COLORS["bg"])
        sf.bind("<Configure>", lambda e: cv.configure(scrollregion=cv.bbox("all")))
        cv.create_window((0, 0), window=sf, anchor="nw", width=860)
        cv.configure(yscrollcommand=sb.set)
        cv.pack(side="left", fill="both", expand=True)
        sb.pack(side="right", fill="y")
        cv.bind("<Enter>", lambda e: cv.bind_all("<MouseWheel>",
                lambda ev: cv.yview_scroll(int(-1 * (ev.delta / 120)), "units")))
        cv.bind("<Leave>", lambda e: cv.unbind_all("<MouseWheel>"))
        return sf

    def _card(self, parent):
        shadow = tk.Frame(parent, bg="#D0C8C0")
        card = tk.Frame(shadow, bg=THEME_COLORS["card"], bd=0)
        card.pack(padx=2, pady=2)
        return shadow

    def _render_home(self):
        c = CITY
        hc = THEME_COLORS["hc"]
        ac = THEME_COLORS["ac"]
        self._title(f"{c['name_zh']}欢迎您 / {c['name_ko']}에 오신 것을 환영합니다")
        sf = self._scrollable()

        card = self._card(sf)
        card.pack(fill=tk.X, padx=30, pady=(0, 14))
        tk.Label(card.children['!frame'], text=f"🏙️  {c['name_zh']}概况 / {c['name_ko']} 개요",
                font=("Microsoft YaHei", 15, "bold"), fg=hc, bg=THEME_COLORS["card"]).pack(anchor="w", padx=22, pady=(18, 8))
        tk.Label(card.children['!frame'], text=c['desc_zh'], font=("Microsoft YaHei", 11), fg="#4E342E",
                bg=THEME_COLORS["card"], wraplength=780, justify=tk.LEFT).pack(anchor="w", padx=22)
        tk.Label(card.children['!frame'], text=c['desc_ko'], font=("Malgun Gothic", 10), fg=THEME_COLORS["subtext"],
                bg=THEME_COLORS["card"], wraplength=780, justify=tk.LEFT).pack(anchor="w", padx=22, pady=(4, 18))

        hl = self._card(sf)
        hl.pack(fill=tk.X, padx=30, pady=(0, 14))
        tk.Label(hl.children['!frame'], text="✨ 城市亮点 / 도시 하이라이트", font=("Microsoft YaHei", 15, "bold"),
                fg=hc, bg=THEME_COLORS["card"]).pack(anchor="w", padx=22, pady=(18, 12))
        hi = tk.Frame(hl.children['!frame'], bg=THEME_COLORS["card"])
        hi.pack(fill=tk.X, padx=22, pady=(0, 18))
        for i, h in enumerate(c['highlights']):
            t = tk.Frame(hi, bg=ac)
            t.pack(side=tk.LEFT, padx=(0 if i == 0 else 10, 0), pady=4)
            tk.Label(t, text=f"  {h['zh']}  ", font=("Microsoft YaHei", 11, "bold"), fg="#FFFFFF", bg=ac).pack(padx=10, pady=6)
            tk.Label(t, text=h['ko'], font=("Malgun Gothic", 9), fg="#3E2723", bg=ac).pack(padx=10, pady=(0, 6))

    def _render_attractions(self):
        c = CITY
        hc = THEME_COLORS["hc"]
        ac = THEME_COLORS["ac"]
        self._title("代表旅游景点 / 대표 관광지")
        sf = self._scrollable()
        for a in c['attractions']:
            card = self._card(sf)
            card.pack(fill=tk.X, padx=30, pady=(0, 16))

            img_area = tk.Frame(card.children['!frame'], bg=a.get('img_color', hc), height=100)
            img_area.pack(fill=tk.X)
            img_area.pack_propagate(False)
            tk.Label(img_area, text=a.get('img_icon', '🏯'), font=("Segoe UI Emoji", 48),
                    bg=a.get('img_color', hc)).place(relx=0.5, rely=0.5, anchor="center")

            hd = tk.Frame(card.children['!frame'], bg=a.get('img_color', hc))
            hd.pack(fill=tk.X)
            tk.Label(hd, text=f"  {a['name_zh']}", font=("Microsoft YaHei", 14, "bold"),
                    fg="#FFFFFF", bg=a.get('img_color', hc)).pack(side=tk.LEFT, padx=18, pady=(10, 5))
            tk.Label(hd, text=f"{a['name_ko']}  ", font=("Malgun Gothic", 10),
                    fg="#FFE0B2", bg=a.get('img_color', hc)).pack(side=tk.RIGHT, padx=18, pady=(10, 5))

            bd = tk.Frame(card.children['!frame'], bg=THEME_COLORS["card"])
            bd.pack(fill=tk.X, padx=18, pady=12)
            tk.Label(bd, text=a['desc_zh'], font=("Microsoft YaHei", 11), fg="#4E342E",
                    bg=THEME_COLORS["card"], wraplength=780, justify=tk.LEFT).pack(anchor="w")
            tk.Label(bd, text=a['desc_ko'], font=("Malgun Gothic", 10), fg=THEME_COLORS["subtext"],
                    bg=THEME_COLORS["card"], wraplength=780, justify=tk.LEFT).pack(anchor="w", pady=(3, 0))

            bt_row = tk.Frame(bd, bg=THEME_COLORS["card"])
            bt_row.pack(fill=tk.X, pady=(10, 0))
            for tag in a['tags']:
                tag_f = tk.Frame(bt_row, bg=THEME_COLORS["tag_bg"])
                tag_f.pack(side=tk.LEFT, padx=(0, 6))
                tk.Label(tag_f, text=f" #{tag} ", font=("Microsoft YaHei", 9),
                        fg=THEME_COLORS["tag_text"], bg=THEME_COLORS["tag_bg"]).pack(padx=6, pady=2)
            tk.Label(bt_row, text=f"   📍 必看：{a['famous']}", font=("Microsoft YaHei", 9),
                    fg=ac, bg=THEME_COLORS["card"]).pack(side=tk.LEFT, padx=(8, 0))

    def _render_foods(self):
        c = CITY
        hc = THEME_COLORS["hc"]
        self._title("代表美食 / 대표 음식")
        sf = self._scrollable()
        for f in c['foods']:
            card = self._card(sf)
            card.pack(fill=tk.X, padx=30, pady=(0, 16))

            left_bar = tk.Frame(card.children['!frame'], bg=f.get('img_color', hc), width=100)
            left_bar.pack(side=tk.LEFT, fill=tk.Y)
            left_bar.pack_propagate(False)
            tk.Label(left_bar, text=f.get('img_icon', '🍜'), font=("Segoe UI Emoji", 40),
                    bg=f.get('img_color', hc)).pack(expand=True)

            right = tk.Frame(card.children['!frame'], bg=THEME_COLORS["card"])
            right.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=18, pady=14)

            nr = tk.Frame(right, bg=THEME_COLORS["card"])
            nr.pack(fill=tk.X)
            tk.Label(nr, text=f"🍜 {f['name_zh']}", font=("Microsoft YaHei", 15, "bold"),
                    fg=hc, bg=THEME_COLORS["card"]).pack(side=tk.LEFT)
            tk.Label(nr, text=f" ({f['name_ko']})", font=("Malgun Gothic", 10),
                    fg=THEME_COLORS["muted"], bg=THEME_COLORS["card"]).pack(side=tk.LEFT, padx=(5, 0))

            tk.Label(right, text=f['desc_zh'], font=("Microsoft YaHei", 11), fg="#4E342E",
                    bg=THEME_COLORS["card"], wraplength=680, justify=tk.LEFT).pack(anchor="w", pady=(8, 2))
            tk.Label(right, text=f['desc_ko'], font=("Malgun Gothic", 10), fg=THEME_COLORS["subtext"],
                    bg=THEME_COLORS["card"], wraplength=680, justify=tk.LEFT).pack(anchor="w")

            feat_f = tk.Frame(right, bg=f.get('img_color', "#FF6F00"))
            feat_f.pack(anchor="w", pady=(10, 0))
            tk.Label(feat_f, text=f"  🏷 {f['features']}  ", font=("Microsoft YaHei", 9, "bold"),
                    fg="#FFFFFF", bg=f.get('img_color', "#FF6F00")).pack(padx=8, pady=3)

    def _render_routes(self):
        c = CITY
        icons = ["☀️", "🌅", "🌟"]
        route_colors = ["#E65100", "#1565C0", "#6A1B9A"]
        self._title("推荐旅行路线 / 추천 여행 코스")
        sf = self._scrollable()
        for i, r in enumerate(c['routes']):
            card = self._card(sf)
            card.pack(fill=tk.X, padx=30, pady=(0, 16))
            rc = route_colors[i]

            hd = tk.Frame(card.children['!frame'], bg=rc)
            hd.pack(fill=tk.X)
            tk.Label(hd, text=f"  {icons[i]}  {r['name_zh']}  ({r['name_ko']})",
                    font=("Microsoft YaHei", 14, "bold"), fg="#FFFFFF", bg=rc).pack(side=tk.LEFT, padx=18, pady=(12, 5))
            tk.Label(hd, text=f"{r['duration']}  ", font=("Malgun Gothic", 10),
                    fg="#FFE0B2" if i == 0 else "#BBDEFB" if i == 1 else "#E1BEE7", bg=rc).pack(side=tk.RIGHT, padx=18, pady=(12, 5))

            bd = tk.Frame(card.children['!frame'], bg=THEME_COLORS["card"])
            bd.pack(fill=tk.X, padx=22, pady=18)
            for j, s in enumerate(r['stops']):
                step = tk.Frame(bd, bg=THEME_COLORS["card"])
                step.pack(fill=tk.X, pady=4)
                nf = tk.Frame(step, bg=rc, width=30, height=30)
                nf.pack(side=tk.LEFT, padx=(0, 12))
                nf.pack_propagate(False)
                tk.Label(nf, text=str(j + 1), font=("Microsoft YaHei", 11, "bold"),
                        fg="#FFFFFF", bg=rc).pack(expand=True)
                tk.Label(step, text=s, font=("Microsoft YaHei", 11), fg="#4E342E",
                        bg=THEME_COLORS["card"], anchor="w").pack(side=tk.LEFT)

    def _render_ai_info(self):
        self._title("AI 使用内容 / AI 활용 내용")
        card = self._card(self._content)
        card.pack(fill=tk.BOTH, expand=True, padx=30, pady=10)

        tk.Label(card.children['!frame'], text="🤖 AI 辅助开发说明", font=("Microsoft YaHei", 15, "bold"),
                fg="#3E2723", bg=THEME_COLORS["card"]).pack(anchor="w", padx=22, pady=(18, 12))

        items = [
            ("📝 内容生成 / 콘텐츠 생성", "景区介绍文本由AI辅助生成和润色。\\n관광지 소개 텍스트는 AI가 생성 및 윤색했습니다."),
            ("🌐 双语翻译 / 이중 언어 번역", "中韩双语翻译由AI辅助完成。\\n중한 이중 언어 번역은 AI가 보조했습니다."),
            ("🗺️ 路线规划 / 경로 계획", "旅行路线由AI根据景点距离等因素优化。\\n여행 경로는 AI가 최적화했습니다."),
            ("💻 代码框架 / 코드 프레임", "程序代码框架由AI辅助搭建。\\n프로그램 코드 프레임은 AI의 보조로 구축되었습니다."),
            ("🎨 界面设计 / UI 디자인", "配色方案和布局设计由AI辅助生成。\\n색상 구성 및 레이아웃은 AI가 보조했습니다."),
        ]
        for title, desc in items:
            it = tk.Frame(card.children['!frame'], bg="#FAF6F2")
            it.pack(fill=tk.X, padx=22, pady=(0, 10))
            tk.Label(it, text=title, font=("Microsoft YaHei", 12, "bold"),
                    fg="#5D4037", bg="#FAF6F2").pack(anchor="w", padx=16, pady=(12, 4))
            tk.Label(it, text=desc, font=("Microsoft YaHei", 11), fg="#4E342E",
                    bg="#FAF6F2", wraplength=760, justify=tk.LEFT).pack(anchor="w", padx=16, pady=(0, 12))

        bt = tk.Frame(card.children['!frame'], bg="#FFF8E1")
        bt.pack(fill=tk.X, padx=22, pady=(12, 18))
        tk.Label(bt, text="※ AI 사용 고지 / AI 使用声明", font=("Microsoft YaHei", 9, "bold"),
                fg="#F57F17", bg="#FFF8E1").pack(anchor="w", padx=16, pady=(12, 4))
        tk.Label(bt, text="본 프로그램의 텍스트 콘텐츠, 번역, 코드 및 디자인 요소는 AI 기술을 활용하여 생성되었습니다.\\n本程序的文本内容、翻译、代码及设计元素均借助AI技术生成。",
                font=("Microsoft YaHei", 9), fg="#E65100", bg="#FFF8E1",
                wraplength=760, justify=tk.LEFT).pack(anchor="w", padx=16, pady=(0, 12))


def main():
    root = tk.Tk()
    app = TravelApp(root)
    root.update_idletasks()
    sw, sh = root.winfo_screenwidth(), root.winfo_screenheight()
    w, h = root.winfo_width(), root.winfo_height()
    root.geometry(f"+{(sw - w) // 2}+{(sh - h) // 2}")
    root.mainloop()


if __name__ == "__main__":
    main()
