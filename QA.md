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

## Q5
**Q：** git diff 有哪些实用的用法？
**A：**
- 默认 `git diff` 比较工作区与暂存区，检查未暂存的变更。
- `git diff --staged`（`--cached`）比较暂存区与最近一次提交，确认待提交内容；`git diff HEAD` 查看所有本地差异。
- `git diff origin/main..HEAD` 等比较当前分支与远程分支差异，提交前自检。
- `git diff <提交1> <提交2>`、`git diff <提交> -- <文件>` 用于任意提交或指定文件的对比；`--stat`、`--name-only` 等参数可调节输出摘要。
- `git difftool` 配合外部工具获得图形化差异展示。

## Q6
**Q：** git restore 有哪些常用用法？
**A：**
- `git restore <文件>`：丢弃工作区未暂存的改动，将文件恢复到暂存区/当前提交状态。
- `git restore --staged <文件>`：取消暂存，把文件移回工作区；`git restore --staged .` 可批量处理。
- `git restore --source <提交> <文件>`：从指定提交恢复某个文件，也可用远程分支如 `origin/main` 作为来源。
- 结合 `--worktree`、`--staged` 控制恢复目的地，可精确回滚单个文件而不影响其它历史。

## Q7
**Q：** `git diff` 返回的每一行表示什么？
**A：**
- `diff --git ...` 与 `index ...` 行说明比较的文件路径、对象哈希及权限。
- `---`、`+++` 行分别标记旧版本（a/）与新版本（b/）的文件名。
- `@@ -21,4 +21,4 @@` 是 Hunk 头，表示旧文件从第 21 行起 4 行、新文件从第 21 行起 4 行被对比。
- 以空格开头的行表示上下文（未改动部分），以 `-` 开头表示旧版本被删除的内容，以 `+` 开头表示新版本新增的内容。
- Git 可能在 diff 前给出额外 warning（如换行符提示），帮助你理解工作区状态。

![git diff 示例](images/git-diff-example.png)

## Q8
**Q：** git diff 输出中出现 “-” + 空行代表什么？warning “LF will be replaced by CRLF” 又是什么意思？
**A：**
- 以 “-” 开头且内容为空的行表示旧版本有一行纯空白被删除，Git 仍会显示它以提示空行差异。
- warning “LF will be replaced by CRLF the next time Git touches it” 表示文件当前使用 LF 换行符，在你的配置（如 `core.autocrlf=true`）下写回时会转换为 Windows 的 CRLF。这提醒你将发生换行符转换，对 diff 内容没有影响。

![git diff warning](images/git-diff-warning.png)
## Q9
**Q：** `git reset --soft` 与 `git reset --hard` 有什么区别？分别在什么场景使用？
**A：**
- `git reset --soft <提交>` 仅移动 `HEAD`（当前分支指针），暂存区和工作区不变，常用于整理最近提交、合并多次提交重新编写 commit。
- `git reset --hard <提交>` 在移动 `HEAD` 的同时，将暂存区和工作区都恢复到目标提交状态，未保存的改动会丢失，适合放弃实验性修改、回滚到干净版本。
## Q11
**Q：** git stash 有哪些常用用法？
**A：**
- `git stash push -m "备注"`：保存当前工作区与暂存区的改动并回到干净状态，`-m` 便于区分不同 stash。
- `git stash list` / `git stash show -p stash@{0}`：查看 stash 列表与某条记录的具体差异。
- `git stash apply [stash@{n}]`：恢复保存的改动且保留 stash；`git stash pop` 恢复后删除那条记录。
- `git stash drop stash@{n}` 或 `git stash clear`：删除指定或全部 stash。
- 常用变体：`git stash push --keep-index` 仅保存工作区改动；`git stash push --include-untracked` 将未跟踪文件一并保存。
## Q12
**Q：** 为什么 `git push -u origin main` 会被拒绝？`--force-with-lease` 是什么意思？
**A：**
- 远端 `main` 已有本地缺失的提交（例如通过 GitHub 网页或其它机器推送），未同步前推送会被拒绝。先执行 `git pull --ff-only origin main` 获取最新历史，解决冲突后再推送。
- `git push --force-with-lease` 会在强制推送前检查远端分支是否仍指向你上次拉取的 commit，若已被他人更新则拒绝覆盖，比 `--force` 更安全；仅在确认远端历史可以被重写时使用。
## Q13
**Q：** git rebase 是什么意思？如何使用？
**A：**
- `git rebase <目标分支>` 会把当前分支的提交重新应用到目标分支最新提交之后，保持历史线性。常用于在功能分支上同步主分支的最新变化。
- 基本流程：更新目标分支（`git switch main && git pull --ff-only`）→ 切回功能分支执行 `git rebase main`，冲突时逐个解决并 `git rebase --continue`，若放弃则 `git rebase --abort`。
- rebase 改写提交哈希，若分支已推送需使用 `git push --force-with-lease origin <branch>` 更新远端；避免对公共分支 rebase 以免影响他人。
- 交互式 `git rebase -i main` 可合并、重排、修改提交信息，便于整理历史。
## Q14
**Q：** 在 `dev` 分支有未提交的修改，直接切换到 `main` 会怎样？如何补救？
**A：**
- 若改动不会与 `main` 冲突，切换成功但修改会带到 `main` 的工作区，容易误提交；若存在冲突则会被 Git 拒绝，要求先处理。
- 补救：
  1. 切回 `dev`（必要时加 `--merge`）：`git switch dev --merge`。
  2. 立即 `git stash push -m "dev WIP"` 或完成提交 `git commit`，再切换分支。
  3. 若已经在 `main` 上提交了这些改动，可用 `git revert` 或 `git reset` 回退，再到 `dev` 使用 `git cherry-pick`/`git stash pop` 恢复。
- 建议养成切换分支前 `git status` 检查、必要时使用 `stash` 的习惯。
## Q15
**Q：** `git switch dev --merge` 是什么意思？为什么能作为补救措施？执行后 `main` 上还会保留那些未提交的修改吗？
**A：**
- `git switch dev --merge` 在切换到 `dev` 分支时，会尝试把当前工作区的未提交改动一起带过去，相当于将这些改动临时套用到 `dev` 上；若无冲突即可保留，遇到冲突则暂停让你解决。
- 当误把 `dev` 的修改带到 `main` 时，使用该命令能把改动“搬回” `dev`，这样你就能在正确的分支上 `commit` 或 `stash`，从而补救。
- 改动一直存在于工作区，而非 `main` 的提交历史；切换成功后它们附着在 `dev` 上，`main` 仍保持原状，之后再切回 `main`（在干净工作区下）看不到这些改动。
## Q16
**Q：** 如何手动制造一次 Git 冲突并进行练习？
**A：**
1. 保证 `main` 分支干净：`git status` 应为空；如有远端更新先 `git pull --ff-only origin main`。
2. 在 `main` 上修改某文件同一段内容（改动 A），`git commit -m "feat: main change for conflict"`，`git push origin main`。
3. 新建分支 `git switch -c feature/conflict-demo`，在同一位置做不同改动 B，`git commit -m "feat: conflicting change"`。
4. 回到 `main` 再修改相同位置（改动 C），`git commit -m "feat: diverging main"` 并推送。
5. 切换回 `feature/conflict-demo`，执行 `git pull --rebase origin main`（或 `git merge origin/main`），此时会因同一行有不同改动而产生冲突。
6. 打开冲突文件，手动选择正确内容并删除 `<<<<<<<`/`=======`/`>>>>>>>` 标记，`git add` 后 `git commit` 或 `git rebase --continue`。
7. 解决后 `git push origin feature/conflict-demo`（若 rebase 过需 `--force-with-lease`），即可练习冲突解决流程。
## Q17
**Q：** `git pull --ff-only origin main` 是什么意思？如果本地 `main` 已有改动会怎样？应如何处理冲突，`merge` 和 `rebase` 有何区别？
**A：**
- 该命令先抓取远端 `origin/main`，仅当本地 `main` 可以直接快进（没有额外提交）时才移动本地指针，因此能保证本地历史完全对齐远端且不生成额外 merge commit。
- 若本地 `main` 有本地提交或未提交改动导致无法快进，命令会报错提示不能 fast-forward。此时需先处理：提交或 stash 本地修改，然后选择 `git merge origin/main`（生成 merge commit，保留分叉历史）或 `git rebase origin/main`（将本地提交改写到远端最新提交之后，得到线性历史）。冲突出现时，手动编辑冲突文件，`git add` 标记已解决，再 `git commit`（merge）或 `git rebase --continue`（rebase）。
- `merge` 保留各分支原始拓扑，更易追溯谁在何时合并；`rebase` 让历史呈线性，便于阅读，但会改写提交哈希，需要谨慎在共享分支上使用。
## Q18
**Q：** `git merge` 时想保留原始提交信息怎么办？
**A：**
- `git merge --no-ff feature/branch`：禁止快进，生成 merge commit 并保留被合并分支的所有提交；历史中可看到完整提交信息。
- 若想先检查再手动提交，可使用 `git merge --no-ff --no-commit feature/branch`，解决冲突后再 `git commit` 自定义合并说明。
## Q19
**Q：** 以下 workflow 是否合理：`main` 只用于同步远端，`dev` 负责开发？
**A：**
- 思路正确，但无需在 `main` 上额外提交。推荐流程：
  1. `git fetch origin` 获取远端最新引用。
  2. 在 `dev` 完成交付，直接 `git commit` 保存变更。
  3. `git rebase origin/main`（或 `git merge origin/main`）将远端更新整合进 `dev`，冲突在 `dev` 上解决。
  4. 功能验证后推送 `dev` 并创建 PR，或在 `main` 用 `git merge --no-ff dev` 合并再推送。
- 只有在需要临时切换时才 `git stash`；若功能已完成，直接提交即可。保持 `main` 无本地自定义提交，可随时 `git switch main && git pull --ff-only` 快速同步远端。
