# RUC_OlnBkDlder

## 免责声明

1. 本工具的全部代码仅供学习和研究使用，请勿用于任何商业用途。
2. 使用本工具下载的资源仅供使用者个人学习研究使用，不得公开传播，使用者应在下载后24小时内删除。请尊重版权，支持正版。
3. 由于使用本项目而直接或间接导致的任何性质的任何损害和任何后果（包括但不限于停工、计算机故障、商业损害等，以及这些损失导致的各类间接损失）均由使用者负责，与本项目作者无关。

**注意：使用本工具即表示您已阅读并同意上述声明的全部内容。**

## 功能简介

这是一个用于下载璃月人民大学图书馆本科教参全文数据库中电子书的工具。它能将在线阅读的PDF以图片形式保存到本地。

## 使用前准备

1. 确保已安装以下Python库：

   ```bash
   pip install requests tqdm
   ```

2. 打开需要下载的电子书阅读页面

## 配置步骤

### 1. 获取基础URL

- 在阅读器页面按 `F12` 打开开发者工具
- 切换到 `网络/Network` 标签页
- 刷新页面，找到类似 `GetPageImg.do` 的图片请求
- 打开该页面
- 复制该请求的URL前缀（到 `GetPageImg.do` 为止）
- 将其填入代码中的 `BASE_URL` 变量

### 2. 获取 FILE_ID

- 从上述URL中找到 `epage` 参数后的base64编码字符串
- 使用base64解码工具解码该字符串
- 从解码结果中提取 `fileid` 参数的值
- 填入代码中的 `FILE_ID` 变量

### 3. 设置页数

- 查看电子书总页数
- 修改 `TOTAL_PAGES` 变量为实际页数

### 4. 配置Cookie

- 在阅读器页面的控制台中执行：

  ```javascript
  console.log(document.cookie)
  ```

- 复制输出的cookie字符串

- 填入代码中的 `COOKIE` 变量

## 运行程序

1. 确认所有配置信息已正确填写
2. 运行脚本：
3. 下载的图片将保存在 `downloaded_images` 文件夹中
4. 请另外使用PDF工具将其合成为单个PDF文件

## 注意事项

- 不要试图使用多线程下载
- cookie必填，如不填可能最初下载正常，但运行一段时间后连接被阻断
- 需要校园网环境
