FROM node:20.13.0
# 作業ディレクトリを設定
WORKDIR /app

# パッケージファイルをコピー
COPY ./package*.json ./

# プロジェクトのファイルをコピー
COPY . .

RUN npm install -g npm@latest

RUN npm install

# Node.jsのヒープサイズを増やす場合は、ビルドスクリプトにオプションを追加
RUN NODE_OPTIONS=--max-old-space-size=4096 npm run build

# アプリケーションがリッスンするポートを指定
EXPOSE 3000