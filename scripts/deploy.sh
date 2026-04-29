#!/bin/bash
# OPC Legends 部署脚本
PORT=${1:-8082}

echo "🏆 OPC Legends — 一人公司名人堂"
echo "================================"

# 本地测试：开启静态服务器
echo "本地访问: http://localhost:$PORT/index.html"
cd "$(dirname "$0")/.."
python3 -m http.server "$PORT"
