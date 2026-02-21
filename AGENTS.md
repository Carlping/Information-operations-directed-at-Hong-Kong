# AGENTS.md

## 1) 開發環境
- Python 3.11
- 套件管理請擇一使用：`uv` 或 `poetry`

## 2) 常用命令
以下以兩種工具各給一組常用指令，擇一執行即可。

### 使用 uv
- 安裝依賴：`uv sync`
- 跑測試：`uv run pytest -q`
- lint：`uv run ruff check .`
- format：`uv run ruff format .`

### 使用 poetry
- 安裝依賴：`poetry install`
- 跑測試：`poetry run pytest -q`
- lint：`poetry run ruff check .`
- format：`poetry run ruff format .`

## 3) Repo 規範
- `data/raw`、`data/interim`、`data/processed` 不納入版控，目錄內只放 `.gitkeep`。
- `configs/` 只放 `config.example.yaml`（避免提交真實環境設定）。
- 環境變數範本使用 `.env.example`，不要提交真實 `.env`。

## 4) 合規與倫理
- 只使用官方 API 或已授權資料來源。
- 不儲存可識別個人資料（PII）。
- 禁止將本專案用於任何隱蔽操控、欺騙式散播或其他不當資訊操作用途。
