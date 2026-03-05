# practice_1 – FastAPI の練習用プロジェクト

このリポジトリは FastAPI の学習・練習を目的として作成したものです。  
Linux 上で仮想環境（venv）を構築し、VS Code を使って開発しています。

--------------------------------------------

## プロジェクト概要

FastAPI を用いた API 開発の練習として、以下の構成と機能を実装しています。

- FastAPI による API サーバー
- `/v1/health` エンドポイント（動作確認）
- ルーター（app/api）による分割
- スキーマ（app/schemas）、サービス層（app/services）による実務的構造
- pytest を用いたテスト

--------------------------------------------

## ディレクトリ構成
```
practice_1/
├── app/
│   ├── main.py            # FastAPI エントリポイント
│   ├── api/               # ルーター
│   │   └── v1/
│   │       └── health.py
│   ├── core/              # 設定・セキュリティ（今後拡張予定）
│   ├── schemas/           # Pydantic モデル
│   ├── models/            # DB モデル（未使用）
│   └── services/          # ビジネスロジック層
├── tests/                 # pytest テストコード
│   └── test_health.py
├── .gitignore
├── requirements.txt
└── README.md
```
--------------------------------------------

## 起動方法

### 1. 仮想環境の作成・有効化

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. パッケージのインストール
```
pip install -r requirem
```

### 3. FastAPIアプリの起動
```
uvicorn app.main:app --reload
API ドキュメント:
http://127.0.0.1:8000/docs
```

--------------------------------------------

## テスト実行
```
pytest -q
```

--------------------------------------------

## このプロジェクトの目的

- FastAPI を使った API 開発の基礎を練習する
- 実務的な構成（router / service / schema / test）に慣れる
- Git / GitHub の開発フローに慣れる
- Linux + VS Code（SSH リモート）での開発環境構築
- 今後は DB、認証、CI なども学習予定

--------------------------------------------

## 今後の予定（TODO）

- /v1/items API の追加（GET / POST）
- SQLite または SQLModel を使った DB 対応
- GitHub Actions による CI（pytest 自動実行）
- JWT 認証の追加
- Docker 化

--------------------------------------------

## 作者

shino0415
https://github.com/shino0415
