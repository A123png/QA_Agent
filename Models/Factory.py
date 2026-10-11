from langchain_ollama import ChatOllama, OllamaEmbeddings
import os
import sys
from Utils.FileReader import ConfigHandler
sys.path.append(sys.path.append(os.path.dirname(os.getcwd())))


# 初始化配置处理器实例
config_reader = ConfigHandler()
# 读取模型配置文件，解析YAML格式的配置内容
model_conf = config_reader.read_yaml(os.path.join(os.getcwd(), "Configs/config.yml"))
# print(model_conf)

class ChatModelFactory:
    """
    聊天模型工厂类，用于创建和管理聊天模型实例
    """
    def __init__(self) -> None:
        """
        初始化聊天模型工厂
        """
        self.base_url = model_conf['server_url']

    def get_model(self):
        """
        获取聊天模型实例
        Returns:
            ChatOllama: 配置好的聊天模型实例
        """
        llm = ChatOllama(model=model_conf['model_name'], base_url=self.base_url)
        return llm


class EmbeddingModelFactory:
    """
    嵌入模型工厂类，用于创建和管理嵌入模型实例
    """
    def __init__(self) -> None:
        """
        初始化嵌入模型工厂
        """
        self.base_url = model_conf['server_url']

    def get_model(self):
        """
        获取嵌入模型实例
        Returns:
            OllamaEmbeddings: 配置好的嵌入模型实例
        """
        embeddings = OllamaEmbeddings(model=model_conf['embedding_name'], base_url=self.base_url)
        return embeddings



llm = ChatModelFactory().get_model()
embed_model = EmbeddingModelFactory().get_model()
