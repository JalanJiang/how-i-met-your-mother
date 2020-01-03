# srt2md

## 这是什么？

用于将 `.srt` 字幕文件转为 Markdown 文件的 Python 脚本。

## Markdown 格式

```markdown
| ID | Time | EN | ZH | Words | Remarks |
| ---- | ---- | ---- | ---- | ---- | ---- |
```

表格分为以下几列：

- ID
- 时间轴
- 英文句子
- 中文翻译
- 生词
- 标记
    - 😆 惊奇表达
    - 🧐 陌生句子

## 相关技术

- [Python 命令行参数](https://www.runoob.com/python/python-command-line-arguments.html)
- [错误和异常](https://docs.python.org/zh-cn/3/tutorial/errors.html)
- [正则表达式](https://www.runoob.com/python/python-reg-expressions.html)
- 文件 I/O
  - [Python 文件 I/O](https://www.runoob.com/python/python-files-io.html)
  - 读取文件
    - [Python逐行读取文件内容的三种方法](https://www.cnblogs.com/dcc001/p/5705438.html)