import json
import requests
import os
from datetime import datetime

# 读取url.json文件
with open('url.json', 'r') as file:
    data = json.load(file)

# 确保dailyhitssvg文件夹存在
if not os.path.exists('dailyhitssvg'):
    os.makedirs('dailyhitssvg')

# 确保history文件夹存在
if not os.path.exists('history'):
    os.makedirs('history')

# 遍历json数据中的每个对象
for item in data:
    name = item['name']
    url = item['url']

    # 获取当前时间并格式化为字符串
    current_time = datetime.now().strftime('%Y%m%d%H%M%S')

    # 创建文件名
    filename = f'dailyhitssvg/{name}_{current_time}.svg'

    # 使用requests库下载.svg文件
    response = requests.get(url)

    # 将下载的文件保存到指定的文件名
    with open(filename, 'wb') as file:
        file.write(response.content)

    # 检查是否存在名为"name.md"的文件，如果不存在，则创建该文件
    history_file = f'history/{name}.md'
    if not os.path.exists(history_file):
        with open(history_file, 'w') as file:
            pass

    # 在文件的顶部写入一行，内容为"# {图片名称，去掉.svg}"
    # 在下一行写入"![图片名称](./dailyhitssvg/图片名称)"
    with open(history_file, 'r+') as file:
        content = file.read()
        file.seek(0, 0)
        file.write(f"# {name}_{current_time}\n")
        file.write(f"![{name}_{current_time}](/dailyhitssvg/{name}_{current_time}.svg)\n")
        file.write(content)