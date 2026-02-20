# Methods Mapping

本文件將程式模組對應至論文 Methods 小節，確保研究流程可追溯、可重現。

## 1. Data Collection

- **對應模組**：`src/opinion_lab/ingestion.py`
- **Methods 說明**：資料來源讀取、收集時間範圍、欄位規格。
- **輸入**：原始資料（API/檔案/資料庫）
- **輸出**：標準化欄位的原始資料表（DataFrame）

## 2. Data Cleaning & Normalization

- **對應模組**：`src/opinion_lab/preprocessing.py`
- **Methods 說明**：缺值處理、時間格式統一、去重與欄位正規化。
- **輸入**：`ingestion` 產出資料
- **輸出**：乾淨可分析資料表

## 3. Indicator / Feature Construction

- **對應模組**：`src/opinion_lab/analysis.py`
- **Methods 說明**：最小指標建構（例如貼文數、唯一作者數、平均互動量）。
- **輸入**：清理後資料
- **輸出**：指標資料表

## 4. Reporting & Visualization

- **對應模組**：`src/opinion_lab/visualization.py`
- **Methods 說明**：將分析指標轉為可報告格式（CSV/圖表）。
- **輸入**：分析結果
- **輸出**：摘要結果與輸出檔

## 5. Reproducibility & Configuration

- **對應模組**：`src/opinion_lab/cli.py`, `configs/config.example.yaml`
- **Methods 說明**：固定參數、版本鎖定、執行命令記錄。
- **輸入**：設定檔、環境變數
- **輸出**：可重複執行的研究流程
