# 智扫通 InsightScan

面向扫地机器人用户的智能客服。用户可以咨询购买和使用问题，系统也能根据运行日志生成使用报告和优化建议。

## 项目架构

![项目架构](images/architecture.png)

## 运行效果

命令行问答：

![命令行效果](images/cli-demo.png)

Web 页面：

![Web 效果](images/web-demo.png)

Streamlit：

![Streamlit 界面](images/streamlit-1.png)
![Streamlit 对话](images/streamlit-2.png)

Gradio：

![Gradio 界面](images/gradio-1.png)
![Gradio 对话](images/gradio-2.png)

## 代码

核心代码在 `ZST_code`。安装依赖：

```bash
pip install -r ZST_code/requirements.txt
```

`bert-base-chinese` 的模型权重超过 GitHub 单文件 100MB 限制，没有放进仓库。请把 `model.safetensors` 或 `pytorch_model.bin` 下载到 `ZST_code/bert-base-chinese/`。向量库 `Chroma` 也未上传，需要在本地重新构建。
