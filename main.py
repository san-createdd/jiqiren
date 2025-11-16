import os
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes
)

TOKEN = os.getenv("BOT_TOKEN")

# ------------------ 文案 ------------------

WELCOME_TEXT = """
兄弟，欢迎来到 GUD。

这里不讲废话：能不能赚钱，是我们唯一关心的事。

你只要一件事：**干活拿币，拿币赚钱。**
剩下的投流、回购、涨价——全部我们来做。

想开始？发 /help 。
"""

HELP_TEXT = """
**GUD 赚钱教程指令：**

/task — 学习怎么“干活拿 GUD”  
/gud — 1 分钟理解 GUD 为什么有价值  
/ubi — 为什么加入就能领钱  
/price — GUD 涨价机制（回购 + 投流）  
/info — 查看你的 Telegram ID  

所有教程都为新人准备，照做就能赚币。
"""

TASK_TEXT = """
**怎么干活？怎么拿 GUD？**

1️⃣ 邀请 1 人进群 → 立刻奖励  
2️⃣ 完成简单任务（点赞、转发、推广）→ 发币  
3️⃣ 后面还会上线 APP 任务系统 → 每天都有钱领

一句话：干活 = 拿 GUD。  
囤住 GUD = 让别人替你干活赚钱。
"""

GUD_TEXT = """
**为什么 GUD 能涨？一句话：我们让它涨。**

✔ 每月固定投流  
✔ 每月固定回购  
✔ 回购的币 → 发给任务者  
✔ 用户越多 → 任务越多 → 回购买得越多
"""

UBI_TEXT = """
加入 GUD 就能领钱？

因为我们把现实世界资产 + 投流预算  
全部映射到 Token 经济里。

质押 = 公民  
公民 = 有基础领取额度（UBI）
"""

PRICE_TEXT = """
**GUD 涨价机制：**

1️⃣ 一级市场募集 → 60% 用于回购  
2️⃣ 新用户买入 → 提高价格  
3️⃣ 回购周期循环 → 越来越贵  

**封闭增长循环 = 价格上涨动力。**
"""

# ------------------ 处理函数 ------------------

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(WELCOME_TEXT)

async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(HELP_TEXT)

async def task(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(TASK_TEXT)

async def gud(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(GUD_TEXT)

async def ubi(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(UBI_TEXT)

async def price(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(PRICE_TEXT)

async def info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    uid = update.message.from_user.id
    await update.message.reply_text(f"你的 Telegram ID：{uid}")

# ------------------ 主函数 ------------------

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_cmd))
    app.add_handler(CommandHandler("task", task))
    app.add_handler(CommandHandler("gud", gud))
    app.add_handler(CommandHandler("ubi", ubi))
    app.add_handler(CommandHandler("price", price))
    app.add_handler(CommandHandler("info", info))

    app.run_polling()


if __name__ == "__main__":
    main()
