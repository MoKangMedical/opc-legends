"""
OPC Legends — 一人公司名人堂数据

展示成功的OPC创业者案例，激励后来者
"""

LEGENDS = [
    {
        "name": "Pieter Levels",
        "company": "Nomad List / Remote OK",
        "revenue": "$2.7M/年",
        "team": "1人",
        "story": "从沙发客到全球最大的数字游民社区",
        "tech": ["PHP", "Stripe", "Airtable"],
        "lesson": "做到极致的简单 = 做到极致的赚钱"
    },
    {
        "name": "Jon Yong",
        "company": "PhotoAI / InteriorAI",
        "revenue": "$1M+/年",
        "team": "1人",
        "story": "用AI生成照片，每月稳定收入10万美金",
        "tech": ["Next.js", "Replicate", "Stripe"],
        "lesson": "AI时代，一个人可以替代一家公司"
    },
]

def get_legends():
    """获取所有名人"""
    return LEGENDS

def get_stats():
    """获取统计"""
    return {
        "total": len(LEGENDS),
        "combined_revenue": "$3.7M+/年",
        "avg_team_size": 1,
    }
