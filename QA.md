# QA ��¼

Ŀǰ�û�����ʷ��Ϣ��Ϊ��ѧ����������Ҫ��¼�� QA �
## Q1
**Q��** ���ͨ�� git ����鿴��ɾ�����޸� config��
**A��**
- �鿴��`git config --list --show-origin` ��ͬʱ����������Դ��ʹ�� `git config --global user.name` �鿴�ض������ֿ���ʹ�� `git config user.name` �鿴�ֲ����á�
- �޸�/������`git config --global user.name "�������"`��ȫ�֣������ڲֿ���ʹ�� `git config user.name "��Ŀ������"`����ֱ�ӱ༭�ļ������� `git config --global --edit`��
- ɾ����`git config --unset --global user.name` ɾ����������ͬһ�������ڶ�ֵʱ�� `git config --unset-all --global user.email`����ֻ���Ƴ��ֿ�ֲ����ã��ڲֿ���ִ�в��� `--global` ��ͬ�����
## Q2
**Q��** git diff �� git restore �ֱ���ʲô��
**A��**
- `git diff` �Ա������汾��Ĳ��졣Ĭ�ϱȽϹ��������ݴ�����`git diff --staged` �Ƚ��ݴ����������ύ��Ҳ����ָ���ύ���֧����Ϊ�ύǰ����鹤�ߡ�
- `git restore` ������ԭ�ļ���`git restore <�ļ�>` �����������Ķ���`git restore --staged <�ļ�>` ȡ���ݴ棬`git restore --source <�ύ> <�ļ�>` ���ļ��ָ���ָ����ʷ�汾���ʺ���Ե����ļ��Ļع���
## Q3
**Q��** ʲô�ǹ��������ݴ�����`git add` �� `git commit` �ֱ���޸��͵����
**A��**
- �������Ǵ����е���ĿĿ¼�����������ڱ༭���ļ����ݴ�����Index���� Git ������һ���ύ��ѡ���յĻ�������
- `git add` ���������ĸĶ����Ƶ��ݴ�����`git commit` ��ȡ�ݴ������ݴ����µ��ύ����д��汾��ʷ��
## Q4
**Q��** push �� GitHub ��Ŀ���ʲô����
**A��**
- push ��Ŀ����Զ�ֿ̲⣨Remote Repository����Ĭ������ͨ��Ϊ `origin`���������Ź�����ύ��ʷ��
