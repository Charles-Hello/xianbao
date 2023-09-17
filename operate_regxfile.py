# 读取文件并修改




filename = 'regx_text.py'

def modify_regx(text):
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    # 寻找word_list所在行
    for i, line in enumerate(lines):
        if text in line:
            return False
        if 'word_list' in line:
            last_comma_index = line.rfind(',')
            lines[i] = line[:last_comma_index] + f', "{text}",]\n'
            break

    # 保存修改后的内容
    with open(filename, 'w') as file:
        file.writelines(lines)
    return True
        
        

 
# modify_regx("你好呀")