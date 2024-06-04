import os
import re

def edit_config_file(config_path, key_value_dict):
    """
    编辑config.cfg文件，查找指定的键并将其值更改为指定的值。

    :param config_path: 配置文件的路径
    :param key_value_dict: 包含要修改的键值对的字典
    """
    if not os.path.exists(config_path):
        raise FileNotFoundError('配置文件丢失，请启动游戏重新生成。')

    # 读取文件内容
    with open(config_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # 记录找到的键
    keys_found = set()

    # 查找并修改指定的键值对
    for i, line in enumerate(lines):
        for key, new_value in key_value_dict.items():
            # 使用正则表达式确保完全匹配
            pattern = re.compile(rf'^uset {re.escape(key)}\s+"')
            if pattern.match(line.strip()):
                lines[i] = f'uset {key} "{new_value}"\n'
                keys_found.add(key)

    # 检查是否所有键都被找到
    missing_keys = set(key_value_dict.keys()) - keys_found
    if missing_keys:
        raise ValueError(f'指定参数未找到，可能是版本出现较大改动，请联系开发者适配: {", ".join(missing_keys)}')

    # 写回文件
    with open(config_path, 'w', encoding='utf-8') as file:
        file.writelines(lines)

    print('INFO: 配置文件参数修改成功')

# 示例使用
config_path = os.path.join(os.getenv('USERPROFILE'), 'Documents', 'American Truck Simulator', 'config.cfg')
key_value_dict = {
    'g_developer': '1',
    'g_console': '1'
}
print('欢迎使用欧卡/美卡脚本项目,资源共享QQ群732632912')
print('当前脚本适用于ATS-美卡')
print('运行前请确保游戏已关闭，按下任意键继续')
input()

try:
    edit_config_file(config_path, key_value_dict)
except (FileNotFoundError, ValueError) as e:
    print(e)

input('运行完毕，按下任意键退出')
