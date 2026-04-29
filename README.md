# English Essay Review Bot

PR（Pull Request）を作成すると、Gemini APIが自動で英文を添削してくれるリポジトリです。

## 仕組み

1. `essays/` フォルダに英文（`.md` or `.txt`）を書いてブランチにPush
2. PRを作成
3. GitHub ActionsがGemini APIに添削を依頼
4. 添削結果がPRのコメントに自動投稿される

## セットアップ

### 1. Gemini APIキーを取得

[Google AI Studio](https://aistudio.google.com/apikey) にアクセスし、APIキーを発行します。

### 2. GitHub SecretsにAPIキーを登録

リポジトリの `Settings → Secrets and variables → Actions → New repository secret` で登録します。

| Name             | Value           |
| ---------------- | --------------- |
| `GEMINI_API_KEY` | 取得したAPIキー |

### 3. ファイルを配置

以下の3ファイルをリポジトリに追加します。

```
.github/
├── workflows/
│   └── english-review.yml
└── scripts/
├── build_request.py
└── parse_gemini.py
```

## 使い方

```bash
# ブランチを作成
git checkout -b my-essay

# essaysフォルダに英文を書く

# Push
git add .
git commit -m "Add essay"
git push origin my-essay
```

GitHub上でPRを作成すると、自動で添削コメントが投稿されます。
