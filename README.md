# opinion-lab

一個可發展為學術論文投稿的「輿論觀測研究工程骨架」，強調：

- 可重現（reproducibility）
- 模組化方法（methods-to-code mapping）
- 可持續擴充（從最小可運行版本開始）

## Project Objective

`opinion-lab` 目標是建立一條可追溯的研究管線，將資料擷取、清理、分析與可視化拆解成獨立模組，便於論文寫作時對應到 Methods 章節。

## Data Source Boundaries

本專案預設採取以下資料邊界：

1. 僅使用合法、可授權或公開取得資料。
2. 遵守資料平台 TOS 與 robots 規範。
3. 不蒐集、儲存或公開可識別個資（PII）。
4. 研究報告以聚合統計為主，避免個體追蹤。
5. 每次研究需在 `docs/` 中記錄資料來源、時間範圍與限制。

## Quick Start

### 1) Prerequisites

- Python 3.11
- [uv](https://docs.astral.sh/uv/)

### 2) Install dependencies

```bash
uv sync --extra dev
```

### 3) Prepare environment and config

```bash
cp .env.example .env
cp configs/config.example.yaml configs/config.yaml
```

### 4) Run minimal pipeline

```bash
uv run opinion-lab run-minimal-pipeline
```

產出檔案：`data/processed/minimal_metrics.csv`

### 5) Run tests and checks

```bash
uv run pytest
uv run pre-commit run --all-files
```

## Project Structure

```text
src/opinion_lab/         # 核心程式模組
notebooks/               # 探索型分析與實驗紀錄
data/raw/                # 原始資料
data/interim/            # 中間處理資料
data/processed/          # 分析輸出
docs/                    # 研究問題與 Methods 對照
tests/                   # 單元測試與 smoke tests
configs/                 # 研究配置檔
```

## Development Notes

- 使用 `pre-commit` 統一程式品質（ruff + black）。
- `pytest` 提供最小流程可運行驗證。
- 模組目前為最小可運行版本，後續可擴充更多模型、特徵與因果推論流程。
