import json

from app.import_process.agent.main_graph import kb_import_app
from app.import_process.agent.state import create_default_state
import sys
from app.core.logger import logger

logger.info("===== 开始测试 =====")

# 1. 创建state
state = create_default_state(task_id="002",local_file_path="xx.pdf")
# 2. 执行编译后的图对象
result = kb_import_app.invoke(state)
logger.info(f"执行结构{result}")


