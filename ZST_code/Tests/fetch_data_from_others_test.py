import sys
sys.path.append('../..')
sys.path.append('.')
sys.path.append('./')
from Tools.FetchFromOtherSys import fetch_data_from_external_systems
from Tools.ExtractInfo import extract_info

a = extract_info("根据我的扫地机器人的使用情况，生成一份使用报告,要2025年6月份的")
b = fetch_data_from_external_systems(info_dict=a)
print(b)