# ai-tools 每日更新：「不感興趣」回饋（2026-10-24 起，每次必做，最先執行）

網頁每張卡片右上有「不感興趣」勾選框（存在瀏覽器 localStorage），按右下「送出不感興趣清單」會開預填好的 GitHub issue（1234yyyyyy/ai-tools，標籤 not-important）。

## 0. 先讀回饋
```bash
cd /workspace/ai-tools && python3 feedback.py
```
- 產生／更新 `/workspace/ai-tools/not_interested.json`（items：date,title,link,category,hashtags,keywords,issue；category = 一般分類（寫作/簡報/配音…）＋hashtags＋關鍵字）。冪等，以 link 去重。
- 篩新候選工具時，若與任一 not_interested 項目雷同就**排除**：同主題（關鍵字重疊、講同一件事）、同類型/同分類。拿不準偏向排除，用其他候選補滿數量。
- 已在網站上、被標不感興趣的那幾則本身不必刪除（除非使用者另外要求）。
- 處理完關閉 issue：`gh issue close <N> -R 1234yyyyyy/ai-tools -c "已收到，YYYY-MM-DD 起排除雷同內容"`
- 回報使用者時附一行：「本次因不感興趣回饋排除 X 則」（X=0 也寫）。

## 之後照舊
`python3 build.py` → 同步到 `/workspace/ai-tools-site` → push 一次。不感興趣功能寫在 build.py 模板裡，重建會保留。
