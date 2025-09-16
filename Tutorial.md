# Git ѧϰ·����ʵ���滮

## ʹ�÷�ʽ
- �Ƽ����ڣ�6 �ܣ��ɸ��ݸ��˽��������
- ÿ��Ͷ�룺5~8 Сʱ������ 2h������ 4h���Բ� 1h����
- ���鹤�ߣ������� Git��VS Code �� JetBrains ϵ�С�GitHub �˺š�GitHub Desktop �����������۲졣
- ��¼��ʽ������Ŀ���½� `docs/git-notes.md` ��������ĵ�ժ¼��ÿ�ܸ���һ�Ρ�

---

## �� 0 �ܣ�����׼��������ģ��
**Ŀ�꣺** ��ȷ Git �Ĺ�����ʽ����ɻ������á�
1. �Ķ���Pro Git����һ�� or [Official Getting Started](https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control)��
2. ��װ Git��
   - Windows���� git-scm.com �������°�װ��������Ĭ��ѡ����� "Git from the command line"��
   - macOS��`brew install git` �� Xcode Command Line Tools��
3. ����ȫ����Ϣ��
   ```bash
   git config --global user.name "�������"
   git config --global user.email "�������"
   git config --global core.autocrlf true   # Windows
   git config --global core.autocrlf input  # macOS/Linux
   git config --global init.defaultBranch main
   ```
4. ���� `git config --list --show-origin` �˶����ã����� `~/playground/git-lab` Ŀ¼��ʵ�顣
5. ���� GitHub �˺ţ����� 2FA���˽� Issues / Pull Requests �������

---

## �� 1 �ܣ����زֿ������
**Ŀ�꣺** �ܹ���ʼ���ֿ⡢�����ļ��������ո��
- ����ѧϰ�����������ݴ������ύ��HEAD �Ĺ�ϵ��
- ʵ�ٲ��裺
  1. `git init demo`���� `.git` ����ĿĿ¼���롣
  2. �½� `README.md`��`src/main.py`������ `git status` �� `git status -sb`��
  3. ʹ�� `git add`��`git commit -m "feat: initial commit"` ����״��ύ��
  4. �޸��ļ������� `git diff` �� `git diff --staged` �Ƚϡ�
  5. ��ϰ `git restore <file>`��`git restore --staged <file>`��
- ����ύ��ͼ + һƪ��¼���᳣ܽ�����������⣩��
- �Բ⣺�ܽ����ݴ������ڵ����壿��γ���δ�ݴ���޸ģ�

---

## �� 2 �ܣ������ճ� Workflow
**Ŀ�꣺** �γɡ��༭-���-�ύ���ջ���
- ѧϰ `commit` ����ɣ��Ķ� Conventional Commits ��̹淶��
- ���ñ�����
  ```bash
  git config --global alias.st "status -sb"
  git config --global alias.lg "log --oneline --graph --decorate --all"
  ```
- ÿ����ϰѭ����
  1. �޸��ļ� -> `git st`��
  2. `git add -p` ��׼�ݴ棬��� h/j/k/s ���
  3. `git commit` ��д��Ϣ������һ�仰��
  4. `git lg` �鿴��ʷ��ȷ���ύ���С�
- ���� `git log` ������`--stat`��`--patch`����
- ѧϰ `git tag`��Ϊ�׶��Գɹ����ϱ�ǩ��
- ��ϰ `git rm`��`git mv` ���۲���ʷ��¼�仯��
- �Բ⣺����޸����һ���ύ��Ϣ��`git commit --amend` �ķ�����ʲô��

---

## �� 3 �ܣ���֧����ʷά��
**Ŀ�꣺** ���շ�֧���������ͻ�������ύ��
- ѧϰ��֧�ڲ����ƣ�`HEAD` ָ�롢���������á�
- ʵѵ��
  1. `git switch -c feature/login` ���·�֧��
  2. ��ɹ��ܲ�����ύ��
  3. �� `main` �������ͻ����ϰ `git merge` ���ͻ��Ǵ���
  4. ʹ�� `git rebase main` ���������ʷ���Ƚ� `merge` �� `rebase`��
- ��ϰ `git cherry-pick`��`git revert`�������Ӧ�ó�����
- �˽� `git stash` �����ò�����`save`/`push`��`list`��`apply`��`drop`��
- �Բ⣺��ʱӦ��ʹ�� rebase����ΰ�ȫ��ȡ�� rebase ������

---

## �� 4 �ܣ�GitHub Э��������
**Ŀ�꣺** �ܽ����زֿ��� GitHub ͬ������Ϥ Pull Request��
- ���� SSH Key (`ssh-keygen -t ed25519`) ����ӵ� GitHub��
- ����Զ�ֿ̲⣺GitHub �� New Repository������ʼ�� README��
- ����ִ�У�
  ```bash
  git remote add origin git@github.com:username/project.git
  git push -u origin main
  ```
- ���÷�֧������Require PR��Require status checks����
- Fork ��Դ��Ŀ��`git clone` �Լ��� fork��
- �½���֧����С���ܣ��ύ�� `git push origin feature/...`���� GitHub ���� Pull Request��
- ѧϰʹ�� GitHub PR Review��������ۡ������������� squash merge��
- �Բ⣺���ͬ�����βֿ⣿`git remote add upstream`��`git fetch upstream`��`git merge upstream/main`��

---

## �� 5 �ܣ��Ŷ��������Զ���
**Ŀ�꣺** ��ƿ��ظ�����Э�������̡�
- �˽� Git Flow��GitHub Flow��Trunk-Based Development��ѡ���ʺϸ���/�Ŷӵ�ģʽ��
- ʹ�� Issue + Branch �����淶������ `feature/123-login-form`��
- ���� `git rebase -i` �ϲ��ύ������ PR ��ࡣ
- ���ü� CI��GitHub Actions `lint.yml`���� PR �Զ����в��ԡ�
- ѧϰ Release ���̣�ʹ�� `git tag v0.1.0` + GitHub Release Notes��
- �˽� `git blame`��`git bisect` ������λ���⡣
- �Բ⣺������Ŷ�Э���� force push �����ʲôӰ�죿��α��⣿

---

## �� 6 �ܼ��Ժ������չ
**Ŀ�꣺** ���������Ų顢�Ż�·�������뿪Դ��
- �����Ķ���Pro Git�������½ڣ�����������ģ�顢�ڲ�ԭ����
- ѧϰ�߼����`git worktree`��`git submodule`��`git filter-repo`��
- �μ�һ�ο�Դ���ף���ѡ First Issues�����չ淶�ύ PR��
- ��ע������Դ��GitHub Explore��Git Rev News��StackOverflow��
- ÿ���ȸ��̸��� Workflow�������Ƿ���Ҫ����������Hook��CI��

---

## ÿ�ܸ����嵥
- ? �Ƿ���ɼƻ��е�ѧϰ���ϣ�
- ? �Ƿ����µ������¼�� `docs/git-notes.md`��
- ? �Ƿ�ͨ��ʵ����Ŀ������
- ? �Ƿ��� GitHub �ϱ��ֻ�Ծ��Push / PR / Issue����
- ? �Ƿ��ܽ������ĿӼ����������

---

## �Ƽ���Դ
- �ٷ��ĵ���[https://git-scm.com/doc](https://git-scm.com/doc)
- ͼ�飺��Pro Git����GitȨ��ָ�ϡ���Learn Git the Hard Way��
- ��Ƶ��The Net Ninja Git Tutorial��Traversy Media Git & GitHub Crash Course��
- ���ߣ�gitignore.io��Oh My Zsh Git �����GitLens��

�����ϰ -> ��¼�ʼ� -> ���̵������Ƕ�ʱ�������� Git �Ĺؼ���ףѧϰ˳����
