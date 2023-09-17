import git

path = r"C:\\Users\\a1140\\Desktop\\pybot\\xianbao"
def git_push():
    try:
        # 初始化git仓库
        repo = git.Repo(path)

        # # 切换到master分支
        # repo.git.checkout('master')

        # 拉取远程分支（master:mybranch）
        origin = repo.remote(name='origin')
        origin.pull('mybranch')

        # 添加所有更改到暂存区
        repo.git.add('--all')

        # 提交更改
        repo.git.commit(m='update word_list')

        # 推送到GitHub
        origin.push('mybranch')
        return True, True
    except Exception as e:
        print(e)
        return False, e

git_push()