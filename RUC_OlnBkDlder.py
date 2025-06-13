"""
Public by MIT License
See LICENSE file for full license details.
#免责声明
1. 本工具的全部代码仅供学习和研究使用，请勿用于任何商业用途。
2. 使用本工具下载的资源仅供使用者个人学习研究使用，不得公开传播，使用者应在下载后24小时内删除。请尊重版权，支持正版。
3. 由于使用本项目而直接或间接导致的任何性质的任何损害和任何后果（包括但不限于停工、计算机故障、商业损害等，以及这些损失导致的各类间接损失）均由使用者负责，与本项目作者无关。
"""

import requests
import base64
import os
import time
from tqdm import tqdm

# 配置信息

# 0. 获取PDF阅读器页面的URL（例如：https://xxx.libproxy.ruc.edu.cn/foxit-htmlreader-web/Reader.do;jsessionid=xxx?fileid=xxx&lang=zh-cn&pi=255）
# 按F12进入控制台，进入网络选项卡，刷新页面，你会看到获取到了一些页面的URL，打开其中一个（注意要选择清晰的原图而非缩略图的URL）。
# 这个URL是需要下载的PDF图片的基础URL。

# 1. 基础URL (将下面的xxx替换为实际的你的图书馆代理地址，到GetPageImg.do以前即可)
BASE_URL = "https://xxx.libproxy.ruc.edu.cn/foxit-htmlreader-web/GetPageImg.do"

# 2. fileid（你需要自行寻找一个base64解码工具，对图片的基础URL中epage后面的部分进行解码，获取fileid）
FILE_ID = ""

# 3. 你需要下载的总页数
TOTAL_PAGES = 276

# 4. 存放图片的文件夹名称
OUTPUT_DIR = "downloaded_images"

# 5. Cookie信息（回到PDF阅读器的页面，按F12进入控制台，运行"console.log(document.cookie)"）
#    有些时候不需要cookie也能下载一小部分，但一段时间后连接会被阻断。
COOKIE = ''

# 6. ZOOM（不要修改）
ZOOM_LEVEL = 100

# =====================================================================


# 请求头
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Cookie': COOKIE
}

def download_images():

    # 检查并创建输出文件夹
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        print(f"创建文件夹: {OUTPUT_DIR}")

    print(f"准备下载，共 {TOTAL_PAGES} 页...")
    
    # 使用tqdm创建进度条
    for page_num in tqdm(range(TOTAL_PAGES), desc="下载进度"):
        try:
            # 原始参数字符串
            params_str = f"fileid={FILE_ID}&page={page_num}&zoom={ZOOM_LEVEL}"
            
            # 对参数字符串进行Base64编码
            encoded_params = base64.b64encode(params_str.encode('utf-8')).decode('utf-8')
            
            # 完整的URL
            full_url = f"{BASE_URL}?epage={encoded_params}"
            
            # 发送GET请求
            response = requests.get(full_url, headers=HEADERS, timeout=30)
            
            # 检查响应状态
            if response.status_code == 200:
                file_path = os.path.join(OUTPUT_DIR, f"{page_num + 1:04d}.png")
                
                # 保存图片
                with open(file_path, 'wb') as f:
                    f.write(response.content)
            else:
                print(f"\n下载第 {page_num + 1} 页失败，状态码: {response.status_code}")

            # 避免过快请求导致服务器拒绝连接
            time.sleep(0.5)

        except requests.exceptions.RequestException as e:
            print(f"\n下载第 {page_num + 1} 页时发生网络错误: {e}")
            time.sleep(5)
            
    print("\n所有任务完成！")


if __name__ == "__main__":
    # 确认配置信息是否已填写
    if "..." in COOKIE or TOTAL_PAGES == 10:
        print("="*60)
        print("【重要提醒】")
        print("请确保你已经修改了脚本中的 TOTAL_PAGES 和 COOKIE。")
        print("如果已修改，请忽略本消息。程序将在3秒后继续...")
        print("="*60)
        time.sleep(3)

    # 开始下载
    download_images()