"""Generate fix_batch.py with batch 44 cycle 3 data (last 3 tickers)"""
import json, os

DATA = {
    "3523": {
        "desc": "迎輝科技 (3523，[[EFUN Technology]]) 專注於光學膜與光電材料開發製造。核心產品包括量子點膜 (Quantum Dot Film)、ITO 導電膜、3D 電影銀幕及各式顯示器膜材 (防窺/防霧/抗藍光)。\n\n技術優勢在於精密塗佈與 Roll-to-Roll 製程。曾為增亮膜大廠，現轉型高階顯示應用與工控觸控材料：(1) [[Mini LED]]/量子點 — 為面板廠供應量子點增亮膜，應用於高色域顯示器；(2) ITO 導電膜 — 供應工控觸控面板與智慧家居觸控模組；(3) 3D 銀幕 — 為國際 3D 電影院供應高增益投影銀幕。上游原料仰賴 PET 基膜、光學膠與量子點材料供應商。主要客戶為[[友達]]、[[群創]]等面板廠及觸控模組廠。",
        "supply_chain": "**上游 (光學材料):**\n- **PET 基膜:** PET 光學級基膜供應商\n- **光學膠:** 光學膠材料供應商\n- **量子點:** 量子點材料供應商\n\n**中游 (光學膜製造):**\n- **量子點膜:** **迎輝** ([[Mini LED]]/量子點增亮膜)\n- **ITO 導電膜:** **迎輝** (工控觸控用 ITO 膜)\n- **光學膜材:** **迎輝** (防窺/防霧/抗藍光膜)\n\n**下游 (面板廠與觸控模組):**\n- **面板廠:** [[友達]]、[[群創]] — 量子點增亮膜\n- **觸控模組:** 工控觸控面板廠 — ITO 導電膜\n- **3D 銀幕:** 國際 3D 電影院 — 高增益投影銀幕\n- **背光模組:** 背光模組廠 — [[Mini LED]] 膜材",
        "cust": "### 主要客戶\n- **面板廠:** [[友達]]、[[群創]] — 量子點增亮膜與光學膜\n- **觸控模組:** 工控觸控面板廠 — ITO 導電膜\n- **3D 銀幕:** 國際 3D 電影院 — 高增益投影銀幕\n- **背光模組:** [[Mini LED]] 背光模組廠 — 量子點膜材\n\n### 主要供應商\n- **PET 基膜:** PET 光學級基膜供應商\n- **光學膠:** 光學膠材料供應商\n- **量子點:** 量子點材料供應商",
    },
    "3548": {
        "desc": "兆利 (3548，[[Jarllytec]]) 為全球前三大筆電樞紐 (Hinge) 製造商，近年成功切入摺疊手機鉸鏈市場成為核心成長引擎。\n\n業務結構與動能：(1) 摺疊手機 — 為 [[Huawei]] 摺疊機主力鉸鏈供應商，同時供應 [[OPPO]]、[[小米]] 等品牌，摺疊手機營收占比已過半，獲利能力顯著優於傳統 NB 鉸鏈；(2) NB/Monitor — 供應 [[Apple]]、[[Dell]] 等品牌筆電鉸鏈，透過 [[廣達]]、[[英業達]] 等 ODM 廠出貨；(3) 摺疊 PC — 市場預期未來有望切入 [[Apple]] 摺疊產品供應鏈。核心技術為精密多軸鉸鏈設計與 MIM (金屬粉末射出成型) 製程。",
        "supply_chain": "**上游 (金屬與精密零件):**\n- **MIM 零件:** 金屬粉末射出成型零件供應商\n- **鋼材:** 不鏽鋼與特殊鋼材供應商\n- **精密軸承:** 微型軸承與彈簧供應商\n\n**中游 (鉸鏈設計製造):**\n- **摺疊手機鉸鏈:** **兆利** (多軸摺疊鉸鏈)\n- **NB 鉸鏈:** **兆利** (筆電轉軸設計製造)\n- **Monitor 鉸鏈:** **兆利** (顯示器支架與轉軸)\n\n**下游 (手機品牌與NB ODM):**\n- **摺疊手機:** [[Huawei]]、[[OPPO]]、[[小米]] — 摺疊手機鉸鏈\n- **NB 品牌:** [[Apple]]、[[Dell]] — NB 鉸鏈\n- **NB ODM:** [[廣達]]、[[英業達]] — NB 鉸鏈代工出貨",
        "cust": "### 主要客戶\n- **摺疊手機:** [[Huawei]] — 摺疊機主力鉸鏈供應商\n- **摺疊手機:** [[OPPO]]、[[小米]] — 摺疊手機鉸鏈\n- **NB 品牌:** [[Apple]]、[[Dell]] — 筆電鉸鏈\n- **NB ODM:** [[廣達]]、[[英業達]] — NB 鉸鏈代工出貨\n\n### 主要供應商\n- **MIM 零件:** 金屬粉末射出成型零件供應商\n- **鋼材:** 不鏽鋼與特殊鋼材供應商\n- **精密零件:** 微型軸承與彈簧供應商",
    },
    "3591": {
        "desc": "艾笛森光電 (3591，[[Edison Opto]]) 原為高功率 LED 封裝廠，近年成功轉型為 LED 模組與車用照明解決方案供應商。\n\n業務重心與成長動能：(1) 車用 LED 模組 — 發展車用 LED 模組 (尾燈、日行燈、霧燈)，直接供應歐美 Tier 1 車燈大廠如 [[Valeo]]、[[Magneti Marelli]]，車用成品線營收比重持續提升，帶動毛利率改善；(2) 商用照明 — 提供商業空間照明、路燈及特殊照明模組；(3) 光傳輸 — 投入 POF (塑膠光纖) 與[[矽光子]]相關封裝技術研發。上游 LED 晶粒主要採購自[[富采]]、[[億光]]等供應商。",
        "supply_chain": "**上游 (LED 晶粒與材料):**\n- **LED 晶粒:** [[富采]]、[[億光]] — 高功率 LED 晶粒\n- **封裝材料:** 螢光粉、矽膠封裝膠供應商\n- **基板:** LED 封裝用陶瓷/金屬基板\n\n**中游 (LED 封裝與模組製造):**\n- **車用 LED 模組:** **艾笛森** (車燈 LED 模組)\n- **照明模組:** **艾笛森** (商用照明/路燈模組)\n- **光傳輸:** **艾笛森** (POF/[[矽光子]]封裝技術研發)\n\n**下游 (車燈廠與照明市場):**\n- **車燈 Tier 1:** [[Valeo]]、[[Magneti Marelli]] — 車用 LED 模組\n- **商業照明:** 商業空間照明品牌 — LED 照明模組\n- **路燈:** 公共工程 — LED 路燈模組\n- **光通訊:** [[矽光子]]與 POF 光傳輸應用",
        "cust": "### 主要客戶\n- **車燈 Tier 1:** [[Valeo]]、[[Magneti Marelli]] — 車用尾燈/日行燈/霧燈 LED 模組\n- **商業照明:** 商業空間照明品牌 — LED 照明模組\n- **路燈:** 公共工程 — LED 路燈模組\n\n### 主要供應商\n- **LED 晶粒:** [[富采]]、[[億光]] — 高功率 LED 晶粒\n- **封裝材料:** 螢光粉與矽膠封裝膠供應商\n- **基板:** LED 封裝用陶瓷/金屬基板廠",
    },
}

# Read current fix_batch.py for tail
with open(os.path.join(os.path.dirname(__file__), 'fix_batch.py'), 'r', encoding='utf-8') as f:
    content = f.read()
idx = content.index('BASE_DIR')
tail = content[idx:]

# Write new fix_batch.py
with open(os.path.join(os.path.dirname(__file__), 'fix_batch.py'), 'w', encoding='utf-8') as f:
    f.write('import os, glob, sys, re\n')
    f.write('sys.path.append(os.path.dirname(__file__))\n\n')
    f.write('DATA = ' + json.dumps(DATA, ensure_ascii=False, indent=4) + '\n\n\n')
    f.write('# Metadata fixes for files missing fields\nMETADATA_FIXES = {\n}\n\n')
    f.write(tail)

print(f"Generated fix_batch.py with {len(DATA)} tickers for cycle 3")
