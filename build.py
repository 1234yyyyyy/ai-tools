import base64, html
F='#免費可用'; P='#20美元內'
T=[
("immersive","沉浸式翻譯 Immersive Translate","https://immersivetranslate.com","翻譯・雙語字幕・免費可用",
 "網頁、PDF、電子書和 YouTube 字幕都能原文和譯文對照著看，支援繁體中文。免費版每天有翻譯上限，Pro 月繳每月 14.99 美元、年繳等於每月 9.99 美元。",
 ["翻譯","字幕",F,P],"雙語對照 瀏覽器擴充 PDF 電子書 YouTube 繁中"),
("deepl","DeepL","https://www.deepl.com","翻譯・寫作・免費可用",
 "長文翻譯語氣最自然，支援繁體中文；免費版每月可翻 5 萬字元和 1 個檔案。個人版年繳每月 7.49 歐元起（約 8.7 美元，依地區計價），潤稿工具 DeepL Write 目前沒有繁中。",
 ["翻譯","寫作",F,P],"文件翻譯 Word 潤稿"),
("napkin","Napkin AI","https://www.napkin.ai","簡報・圖表・免費可用",
 "貼上一段文字，就自動變成資訊圖、流程圖或心智圖，付費版可匯出 PPT 和 SVG。免費版每週 500 點（大約 1 個字 1 點）但有浮水印，Plus 每月 9 美元。",
 ["簡報","寫作","設計",F,P],"資訊圖 流程圖 心智圖 圖表 PPT SVG"),
("ideogram","Ideogram","https://ideogram.ai","圖片・海報・免費可用",
 "生圖時畫面裡的文字最準，做海報、Logo、社群圖特別好用。免費帳號每週有慢速點數、作品預設公開；Plus 年繳每月 15 美元（月繳 20 美元），可私人生成。",
 ["圖片","設計",F,P],"生圖 海報 Logo 文字 社群圖"),
("recraft","Recraft","https://www.recraft.ai","設計・向量圖・免費可用",
 "擅長向量圖（SVG）、圖示和風格一致的品牌素材，生成後可以直接拿去排版。免費版每天每種風格 3 次、限個人使用；Basic 年繳每月 10 美元，每月 1,000 點。",
 ["設計","圖片",F,P],"SVG 向量 圖示 icon 品牌 Logo"),
("krea","Krea","https://www.krea.ai","圖片・即時生成・免費可用",
 "邊畫邊即時出圖，同一個介面就能切換多家圖片和影片模型，也能放大修圖。免費每天 100 單位；Pro 年繳每月 21 美元，略超過 20 美元預算。",
 ["圖片","設計","影片",F],"即時生成 放大 修圖 多模型 生圖"),
("vrew","Vrew","https://vrew.ai","影片・字幕・免費可用",
 "自動上中文字幕，刪掉字就等於剪掉那段影片，還能一鍵刪除停頓。免費版每月 200 點（轉字幕最多 200 分鐘）但影片有浮水印；Light 年繳每月約 11.17 美元。",
 ["影片","字幕","配音",F,P],"剪輯 剪片 自動字幕 刪停頓 AI 配音 韓國"),
("elevenlabs","ElevenLabs","https://elevenlabs.io","配音・語音・免費可用",
 "目前最自然的 AI 配音，支援中文，也能複製自己的聲音。免費版每月 1 萬點（約 10 分鐘）、不能商用；Starter 每月 6 美元就能商用。",
 ["配音","影片",F,P],"文字轉語音 TTS 聲音複製 旁白 音效"),
("runway","Runway","https://runwayml.com","影片・AI 生成・每月 20 美元內",
 "生成電影感的 AI 影片和特效，Gen-4.5、Kling 3.0 等模型都在裡面。新帳號送一次性 125 點試用；Standard 年繳每月 12 美元（月繳 15 美元），每月 625 點。",
 ["影片",P],"生成影片 特效 文生影片 圖生影片"),
("hailuo","海螺 AI Hailuo","https://hailuoai.video","影片・AI 生成・每月 20 美元內",
 "MiniMax 推出的影片生成工具，打一段文字或丟一張圖就能做出短片，動作表現自然。Standard 每月 14.99 美元（目前限時 7.99 美元），每月 1,000 點約可做 40 支 6 秒 768P 影片。",
 ["影片",P],"MiniMax 生成影片 文生影片 圖生影片 短片"),
("cursor","Cursor","https://cursor.com","寫程式・編輯器・免費可用",
 "內建 AI 的程式碼編輯器，看得懂整個專案，適合自己會寫一點程式的人。Hobby 免費但 Agent 次數有限，Pro 每月 20 美元。",
 ["寫程式","做 App",F,P],"程式碼 編輯器 IDE Agent 補全"),
("lovable","Lovable","https://lovable.dev","做 App・網站・免費可用",
 "用聊天描述需求，就生出能上線的網站或 App，完全不用寫程式。免費版每天 5 點（每月最多 30 點）；Pro 每月 25 美元，年繳送 2 個月。",
 ["做 App","寫程式",F],"網站 無程式碼 no-code 架站"),
("bolt","Bolt.new","https://bolt.new","做 App・網頁・免費可用",
 "在瀏覽器裡就能生成網頁應用並一鍵上線，免費額度在同類裡算大方。免費版每月 100 萬 tokens（每天上限 30 萬），Pro 每月 25 美元。",
 ["做 App","寫程式",F],"網站 網頁 部署 上線 no-code StackBlitz"),
("consensus","Consensus","https://consensus.app","研究・論文・免費可用",
 "直接問問題，它會告訴你學術研究怎麼說，每個結論都附論文引用。免費版可搜尋論文、每月 10 次 Pro 分析；Pro 年繳每月 12 美元（月繳 20 美元）。",
 ["研究",F,P],"論文 學術 文獻 引用 查資料"),
("elicit","Elicit","https://elicit.com","研究・文獻回顧・免費可用",
 "做文獻回顧的好幫手，能從大量論文批次抽出數據、整理成表格。Basic 免費，可在 1.38 億篇論文中無限搜尋和摘要；付費 Pro 年繳每月 49 美元，比較適合專業研究者。",
 ["研究",F],"論文 學術 文獻 系統性回顧 表格 查資料"),
("researchrabbit","ResearchRabbit","https://www.researchrabbit.ai","研究・引用地圖・免費可用",
 "把論文之間的引用關係畫成網絡圖，從幾篇論文出發幫你找到相關文獻。免費版永久可用；RR+ 年繳每月 10 美元（月繳 12.5 美元），部分國家另有折扣。",
 ["研究",F,P],"論文 學術 文獻 引用 網絡圖 Zotero"),
("scispace","SciSpace","https://scispace.com","研究・讀論文・免費可用",
 "上傳論文 PDF 就能直接對話，請它解釋看不懂的段落、整理重點。可以免費註冊使用（免費額度未查證）；Premium 年繳每月 12 美元（月繳 20 美元）。",
 ["研究",F,P],"論文 PDF 學術 文獻 摘要 查資料"),
("yating","雅婷逐字稿","https://studio.yating.tw/intro/zh-TW/transkribera","會議・逐字稿・免費可用",
 "台灣人工智慧實驗室做的語音轉文字，中文、英文、台語、日語、粵語都能轉，台灣口音和中英夾雜也聽得懂，還能分出多位講者。可以免費試用，時數方案價格未查證。",
 ["會議","字幕",F],"逐字稿 語音轉文字 台灣 台語 錄音 訪談 課堂筆記"),
("granola","Granola","https://www.granola.ai","會議・筆記・免費可用",
 "不用讓會議機器人進場，直接在電腦上聽會議、自動整理成筆記。Basic 免費但只能看有限的會議紀錄，Business 每月 14 美元。",
 ["會議","自動化",F,P],"會議紀錄 筆記 逐字稿 Zoom Meet"),
("n8n","n8n","https://n8n.io","自動化・工作流程・免費可用",
 "開源的自動化工具，可以把各種 App 和 AI 代理串成工作流程。自己架設完全免費、不限流程數；官方雲端 Starter 年繳每月 20 美元，每月 2,500 次執行。",
 ["自動化",F,P],"工作流程 workflow 開源 自架 AI 代理 Agent 串接"),
]
assert len(T)==20
def img(k):
    return "data:image/jpeg;base64,"+base64.b64encode(open(f"/workspace/ai-tools/img/{k}.jpg","rb").read()).decode()
e=html.escape
cards=[]
for i,(k,name,url,meta,intro,tags,kw) in enumerate(T,1):
    tagtxt=" ".join("#"+t if not t.startswith("#") else t for t in tags)
    cards.append(f'<a class="c" href="{e(url)}" target="_blank" rel="noopener"><img src="{img(k)}" alt="{e(name)}" loading="lazy"><div class="t"><div class="n">{i}. {e(name)}</div><div class="m">{e(meta)}</div><p>{e(intro)}</p><span class="k">{e(tagtxt)} {e(kw)}</span></div></a>')
cats=[("全部",""),("寫作","#寫作"),("翻譯","#翻譯"),("簡報","#簡報"),("圖片","#圖片"),("設計","#設計"),("影片","#影片"),("配音","#配音"),("字幕","#字幕"),("寫程式","#寫程式"),("做 App","#做 App"),("研究","#研究"),("會議","#會議"),("自動化","#自動化")]
prices=[("不限價格",""),("免費可用","#免費可用"),("每月 20 美元內","#20美元內")]
cb="".join(f'<button data-k="{e(k)}"{" class=on" if not k else ""}>{e(n)}</button>' for n,k in cats)
pb="".join(f'<button data-p="{e(k)}"{" class=on" if not k else ""}>{e(n)}</button>' for n,k in prices)
CSS='''body{margin:0;font-family:-apple-system,"PingFang TC","Noto Sans TC",sans-serif;background:#111;color:#eee}h1{font-size:22px;padding:20px 16px 4px;margin:0}.s{color:#999;padding:0 16px 12px;font-size:13px}
.g{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:14px;padding:0 16px 24px}.c{background:#1c1c1c;border-radius:12px;overflow:hidden;text-decoration:none;color:inherit;display:block}
.c img{width:100%;height:200px;object-fit:cover;display:block;background:#000}.t{padding:10px 12px 14px}.n{font-weight:700;font-size:16px}.m{color:#f5a623;font-size:12px;margin:4px 0}p{margin:6px 0 0;font-size:14px;line-height:1.5;color:#ccc}.k{display:none}.f{position:sticky;top:0;z-index:5;background:#111;display:flex;flex-wrap:wrap;gap:8px;padding:10px 16px 12px;border-bottom:1px solid #222;margin-bottom:12px}.f button{background:#1c1c1c;color:#ddd;border:1px solid #333;border-radius:999px;padding:6px 14px;font-size:14px;cursor:pointer;font-family:inherit}.f button:hover{border-color:#666}.f button.on{background:#f5a623;color:#111;border-color:#f5a623;font-weight:700}.f .pr{flex-basis:100%;display:flex;flex-wrap:wrap;gap:8px}.f .pr button.on{background:#3a8f5c;border-color:#3a8f5c;color:#fff}.f .cnt{color:#888;font-size:13px;align-self:center;margin-left:4px}.c.h{display:none}.sb{flex-basis:100%;display:flex;gap:8px;margin-bottom:2px}.sb input{flex:1;min-width:0;background:#1c1c1c;color:#eee;border:1px solid #333;border-radius:10px;padding:9px 12px;font-size:16px;font-family:inherit}.sb input:focus{outline:none;border-color:#f5a623}.sb button{flex:none}#em{display:none;color:#888;text-align:center;padding:30px 16px}'''
JS='''(function(){var bs=document.querySelectorAll('#f button[data-k]'),ps=document.querySelectorAll('#f button[data-p]'),cs=document.querySelectorAll('.c'),cnt=document.getElementById('cnt'),q=document.getElementById('q'),em=document.getElementById('em'),cat='',pri='';
function run(){var re=cat?new RegExp(cat,'i'):null,rp=pri?new RegExp(pri,'i'):null,ts=q.value.trim().toLowerCase().split(/\\s+/).filter(Boolean),n=0;
cs.forEach(function(c){var t=(c.querySelector('.t').textContent+' '+c.href).toLowerCase();var ok=(!re||re.test(t))&&(!rp||rp.test(t))&&ts.every(function(w){return t.indexOf(w)>=0});c.classList.toggle('h',!ok);if(ok)n++});
cnt.textContent=n+' 個';em.style.display=n?'none':'block';}
bs.forEach(function(b){b.addEventListener('click',function(){bs.forEach(function(x){x.classList.remove('on')});b.classList.add('on');cat=b.dataset.k;run();});});
ps.forEach(function(b){b.addEventListener('click',function(){ps.forEach(function(x){x.classList.remove('on')});b.classList.add('on');pri=b.dataset.p;run();});});
q.addEventListener('input',run);document.getElementById('qc').addEventListener('click',function(){q.value='';run();q.focus();});})();'''
H=f'''<!DOCTYPE html><html lang="zh-Hant-TW"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>AI 工具精選 20 個 2026-10-08</title><style>
{CSS}</style></head>
<body><h1>AI 工具精選 20 個</h1><div class="s">2026-10-08 更新・價格為當天官方定價頁所見・點卡片前往官網・以專門工具為主</div><div class="f" id="f"><div class="sb"><input id="q" type="search" placeholder="搜尋工具名稱、用途、關鍵字（例：字幕、SVG、台語）" autocomplete="off"><button id="qc" type="button">清除</button></div>{cb}<div class="pr">{pb}<span class="cnt" id="cnt">20 個</span></div></div><div id="em">找不到符合的工具，換個關鍵字試試</div><div class="g">{"".join(cards)}</div><script>
{JS}
</script></body></html>'''
open("/workspace/ai-tools/index.html","w",encoding="utf-8").write(H)
print(len(H))
