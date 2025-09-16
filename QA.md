# QA 记录

目前用户的历史消息均为教学请求，暂无需要记录的 QA 项。
## Q1
**Q：** 如何通过 git 命令查看、删除和修改 config？
**A：**
- 查看：`git config --list --show-origin` 可同时看到配置来源；使用 `git config --global user.name` 查看特定键，仓库内使用 `git config user.name` 查看局部配置。
- 修改/新增：`git config --global user.name "你的名字"`（全局），或在仓库内使用 `git config user.name "项目内名字"`；想直接编辑文件可运行 `git config --global --edit`。
- 删除：`git config --unset --global user.name` 删除单条；当同一个键存在多值时用 `git config --unset-all --global user.email`；若只想移除仓库局部设置，在仓库内执行不带 `--global` 的同类命令。
## Q2
**Q：** git diff 和 git restore 分别做什么？
**A：**
- `git diff` 对比两个版本间的差异。默认比较工作区与暂存区，`git diff --staged` 比较暂存区与最新提交；也可以指定提交或分支，作为提交前的审查工具。
- `git restore` 用来还原文件。`git restore <文件>` 丢弃工作区改动，`git restore --staged <文件>` 取消暂存，`git restore --source <提交> <文件>` 将文件恢复到指定历史版本，适合针对单个文件的回滚。
## Q3
**Q：** 什么是工作区和暂存区？`git add` 与 `git commit` 分别把修改送到哪里？
**A：**
- 工作区是磁盘中的项目目录，包含你正在编辑的文件；暂存区（Index）是 Git 保存下一次提交候选快照的缓冲区。
- `git add` 将工作区的改动复制到暂存区；`git commit` 读取暂存区内容创建新的提交对象，写入版本历史。
## Q4
**Q：** push 到 GitHub 的目标叫什么区？
**A：**
- push 的目标是远程仓库（Remote Repository），默认名称通常为 `origin`，它保存着共享的提交历史。
