import git



path = r"C:\\Users\\a1140\\Desktop\\pybot\\xianbao"
# 初始化git仓库
repo = git.Repo(path)


# 添加所有更改到暂存区
repo.git.add('--all')

# 提交更改
repo.git.commit(m='update word_list')


# 创建并切换到master分支
repo.git.checkout('-b', 'master')

# 推送到GitHub
origin = repo.remote(name='origin')
origin.push('master:mybranch')

