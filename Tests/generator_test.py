import sys
sys.path.append('../..')
sys.path.append('.')
sys.path.append('./')
from Tools.ReportGenerationTool import generator

b = generator("生成2023年1月份的销售报告。")
print(b)