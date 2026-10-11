import sys
sys.path.append('../..')
sys.path.append('.')
sys.path.append('./')
from Tools.RagQATool import rag_qa

print(rag_qa("为什么有些机器人会'迷路'？"))