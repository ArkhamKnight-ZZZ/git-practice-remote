# Git 学习路线与实践规划

## 使用方式
- 推荐周期：6 周，可根据个人节奏调整。
- 每周投入：5~8 小时（理论 2h、动手 4h、自查 1h）。
- 建议工具：命令行 Git、VS Code 或 JetBrains 系列、GitHub 账号、GitHub Desktop 仅用作辅助观察。
- 记录方式：在项目中新建 `docs/git-notes.md` 做命令和心得摘录；每周复盘一次。

---

## 第 0 周：环境准备与心智模型
**目标：** 明确 Git 的工作方式，完成环境配置。
1. 阅读《Pro Git》第一章 or [Official Getting Started](https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control)。
2. 安装 Git：
   - Windows：从 git-scm.com 下载最新安装包，保持默认选项；开启 "Git from the command line"。
   - macOS：`brew install git` 或 Xcode Command Line Tools。
3. 配置全局信息：
   ```bash
   git config --global user.name "你的名字"
   git config --global user.email "你的邮箱"
   git config --global core.autocrlf true   # Windows
   git config --global core.autocrlf input  # macOS/Linux
   git config --global init.defaultBranch main
   ```
4. 运行 `git config --list --show-origin` 核对配置；建立 `~/playground/git-lab` 目录做实验。
5. 创建 GitHub 账号，启用 2FA；了解 Issues / Pull Requests 基本概念。

---

## 第 1 周：本地仓库基本功
**目标：** 能够初始化仓库、跟踪文件、理解快照概念。
- 理论学习：工作区、暂存区、提交、HEAD 的关系。
- 实操步骤：
  1. `git init demo`，把 `.git` 与项目目录分离。
  2. 新建 `README.md`、`src/main.py`，体验 `git status` 和 `git status -sb`。
  3. 使用 `git add`、`git commit -m "feat: initial commit"` 完成首次提交。
  4. 修改文件后运行 `git diff` 与 `git diff --staged` 比较。
  5. 练习 `git restore <file>`、`git restore --staged <file>`。
- 产物：提交截图 + 一篇记录（总结常用命令与问题）。
- 自测：能解释暂存区存在的意义？如何撤销未暂存的修改？

---

## 第 2 周：构建日常 Workflow
**目标：** 形成“编辑-检查-提交”闭环。
- 学习 `commit` 的组成，阅读 Conventional Commits 简短规范。
- 设置别名：
  ```bash
  git config --global alias.st "status -sb"
  git config --global alias.lg "log --oneline --graph --decorate --all"
  ```
- 每日练习循环：
  1. 修改文件 -> `git st`。
  2. `git add -p` 精准暂存，理解 h/j/k/s 命令。
  3. `git commit` 编写信息，保持一句话表达。
  4. `git lg` 查看历史，确认提交序列。
- 深入 `git log` 参数（`--stat`、`--patch`）。
- 学习 `git tag`：为阶段性成果打上标签。
- 练习 `git rm`、`git mv` 并观察历史记录变化。
- 自测：如何修改最近一次提交信息？`git commit --amend` 的风险是什么？

---

## 第 3 周：分支与历史维护
**目标：** 掌握分支管理、解决冲突、整理提交。
- 学习分支内部机制：`HEAD` 指针、快照与引用。
- 实训：
  1. `git switch -c feature/login` 开新分支。
  2. 完成功能并多次提交。
  3. 在 `main` 上制造冲突，练习 `git merge` 与冲突标记处理。
  4. 使用 `git rebase main` 理解线性历史；比较 `merge` 与 `rebase`。
- 练习 `git cherry-pick`、`git revert`，理解其应用场景。
- 了解 `git stash` 及常用参数：`save`/`push`、`list`、`apply`、`drop`。
- 自测：何时应该使用 rebase？如何安全地取消 rebase 操作？

---

## 第 4 周：GitHub 协作初体验
**目标：** 能将本地仓库与 GitHub 同步，熟悉 Pull Request。
- 生成 SSH Key (`ssh-keygen -t ed25519`) 并添加到 GitHub。
- 创建远程仓库：GitHub 上 New Repository，不初始化 README。
- 本地执行：
  ```bash
  git remote add origin git@github.com:username/project.git
  git push -u origin main
  ```
- 设置分支保护（Require PR、Require status checks）。
- Fork 开源项目，`git clone` 自己的 fork。
- 新建分支开发小功能，提交后 `git push origin feature/...`，在 GitHub 创建 Pull Request。
- 学习使用 GitHub PR Review：添加评论、请求变更、最终 squash merge。
- 自测：如何同步上游仓库？`git remote add upstream`、`git fetch upstream`、`git merge upstream/main`。

---

## 第 5 周：团队流程与自动化
**目标：** 设计可重复、可协作的流程。
- 了解 Git Flow、GitHub Flow、Trunk-Based Development，选择适合个人/团队的模式。
- 使用 Issue + Branch 命名规范：例如 `feature/123-login-form`。
- 体验 `git rebase -i` 合并提交，保持 PR 简洁。
- 配置简单 CI：GitHub Actions `lint.yml`，让 PR 自动运行测试。
- 学习 Release 流程：使用 `git tag v0.1.0` + GitHub Release Notes。
- 了解 `git blame`、`git bisect` 帮助定位问题。
- 自测：如果在团队协作中 force push 会造成什么影响？如何避免？

---

## 第 6 周及以后：深化与拓展
**目标：** 提升问题排查、优化路径，参与开源。
- 深入阅读《Pro Git》后续章节（服务器、子模块、内部原理）。
- 学习高级命令：`git worktree`、`git submodule`、`git filter-repo`。
- 参加一次开源贡献：挑选 First Issues，按照规范提交 PR。
- 关注社区资源：GitHub Explore、Git Rev News、StackOverflow。
- 每季度复盘个人 Workflow，评估是否需要调整别名、Hook、CI。

---

## 每周复盘清单
- ? 是否完成计划中的学习材料？
- ? 是否有新的命令被记录在 `docs/git-notes.md`？
- ? 是否通过实践项目演练？
- ? 是否在 GitHub 上保持活跃（Push / PR / Issue）？
- ? 是否总结遇到的坑及解决方案？

---

## 推荐资源
- 官方文档：[https://git-scm.com/doc](https://git-scm.com/doc)
- 图书：《Pro Git》《Git权威指南》《Learn Git the Hard Way》
- 视频：The Net Ninja Git Tutorial、Traversy Media Git & GitHub Crash Course。
- 工具：gitignore.io、Oh My Zsh Git 插件、GitLens。

坚持练习 -> 记录笔记 -> 复盘迭代，是短时间内熟练 Git 的关键。祝学习顺利！
