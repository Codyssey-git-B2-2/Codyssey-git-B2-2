# Troubleshooting Log

> 실제로 수행한 명령과 출력만 기록한다. 실행 전후의 `git log --oneline` 등을 함께 붙인다.

## 시나리오: amend

### 참여자
- 작성자: 박수정 (@SJendministrator)

### 상황
- `docs/troubleshooting-log.md`를 수정하여 커밋한 후, push하기 전에 추가 수정 사항이 발생하였다.
- 기존 커밋에 추가 수정 사항을 반영하기 위해 `git commit --amend`를 사용하였다.

### 시도한 명령/절차
1. 첫 번째 커밋 생성
```powershell
git add docs/troubleshooting-log.md
git commit -m "docs: amend 실습 내용 추가"

```

2. 첫 번째 커밋 확인

```powershell
git log --oneline -3

```

실행 결과:

```text
5a275a4 (HEAD -> troubleshooting-amend) docs: amend 실습 내용 추가
59ca7dd (origin/feature/troubleshooting-amend) docs: add git commit amend troubleshooting log
77016a9 (origin/feature/conflict-divide) feat: add divide function and refactor test suite

```

3. 커밋 후 `docs/troubleshooting-log.md`를 다시 수정

```powershell
git status
git diff

```

수정된 내용을 확인한 후 staging:

```powershell
git add docs/troubleshooting-log.md

```

4. 마지막 커밋 수정

```powershell
git commit --amend --no-edit

```

실행 결과:

```text
[troubleshooting-amend 441ecb2] docs: amend 실습 내용 추가
Date: Tue Oct 6 08:38:04 2026 +0900
1 file changed, 4 insertions(+), 3 deletions(-)

```

5. amend 후 커밋 확인

```powershell
git log --oneline -3

```

실행 결과:

```text
441ecb2 (HEAD -> troubleshooting-amend) docs: amend 실습 내용 추가
59ca7dd (origin/feature/troubleshooting-amend) docs: add git commit amend troubleshooting log
77016a9 (origin/feature/conflict-divide) feat: add divide function and refactor test suite

```

### 결과

* 불필요한 별도의 커밋을 추가 생성하지 않고, 누락된 변경 사항이 기존 커밋 하나로 깔끔하게 통합됨.
* 커밋 히스토리가 오염되지 않은 상태로 원격 저장소에 push할 준비가 완료됨.

### 왜 이 방법을 선택했는가(Why)

* 아직 원격 저장소에 push하지 않은 로컬 커밋 수정 상황이므로 `git commit --amend`를 선택하였다.
* 동일한 목적의 수정 사항을 단일 커밋으로 유지하여 작업 이력을 명확하고 깔끔하게 관리할 수 있기 때문이다.


## 시나리오: reset --soft
### 참여자
-

### 상황
-

### 시도한 명령/절차
-

### 결과
-

### 왜 이 방법을 선택했는가(Why)
-

## 시나리오: revert
### 참여자
- 임종현

### 상황
- 잘못된 commit 메시지와 필요없는 파일 push

### 시도한 명령/절차
- 잘못된 commit
  ```
  > git commit -m "revert 실습용 잘못된 commit 형식"
  [chore/src-scaffold b4dd2c3] revert 실습용 잘못된 commit 형식
  1 file changed, 0 insertions(+), 0 deletions(-)
  create mode 100644 src/testfile
  ```
- 잘못된 commit push
  ```
  > git push origin chore/src-scaffold
  Enumerating objects: 5, done.
  Counting objects: 100% (5/5), done.
  Delta compression using up to 8 threads
  Compressing objects: 100% (3/3), done.
  Writing objects: 100% (3/3), 579 bytes | 579.00 KiB/s, done.
  Total 3 (delta 1), reused 0 (delta 0), pack-reused 0
  remote: Resolving deltas: 100% (1/1), completed with 1 local object.
  To github.com:Codyssey-git-B2-2/Codyssey-git-B2-2.git
   17c7f67..b4dd2c3  chore/src-scaffold -> chore/src-scaffold
  ```
- 잘못된 commit을 revert
  ```
  > git revert HEAD
  [chore/src-scaffold cb16a1d] Revert "revert 실습용 잘못된 commit 형식"
  1 file changed, 0 insertions(+), 0 deletions(-)
  ```
- 다시 push
  ```
  > git push origin chore/src-scaffold
  Enumerating objects: 5, done.
  Counting objects: 100% (5/5), done.
  Delta compression using up to 8 threads
  Compressing objects: 100% (2/2), done.
  Writing objects: 100% (3/3), 586 bytes | 586.00 KiB/s, done.
  Total 3 (delta 1), reused 0 (delta 0), pack-reused 0
  remote: Resolving deltas: 100% (1/1), completed with 1 local object.
  To github.com:Codyssey-git-B2-2/Codyssey-git-B2-2.git
   b4dd2c3..cb16a1d  chore/src-scaffold -> chore/src-scaffold
  ```

### 결과
- `git log --oneline --graph` 결과 일부: 이전의 commit을 되돌리는 revert commit 생성
  ```
  * cb16a1d (HEAD -> chore/src-scaffold, origin/chore/src-scaffold) Revert "revert 실습용 잘못된 commit 형식"
  * b4dd2c3 revert 실습용 잘못된 commit 형식
  * 17c7f67 chore: 빈 src/utils.py 생성
  ```

### 왜 이 방법을 선택했는가(Why)
remote repository에 이미 push 했다면 동료가 해당 commit 위에 수정사항 commit을 쌓았을 수도 있다. 이 상황에서 reset을 통해서 commit을 삭제해서 remote에 force-push하면 동료의 commit이 삭제된다. revert를 사용하면 해당 commit의 내용을 취소하면서 안전하게 remote에 반영할 수 있다.

### 주의점
- revert는 commit을 삭제하는 것이 아니다. 취소했다는 기록은 모두 남는다.
- 특이 케이스: revert를 revert 해야 할 경우.
  1. feature branch에서 commit A를 main에 병합
  2. main에서 해당 commit A를 revert하여 commit A' 생성
  3. revert 기록이 없는 feature branch에서 A 위에 새로운 commit B를 쌓음
  4. 이때, feature branch를 main에 병합하면 main에는 이미 commit A가 존재하기 때문에 A의 변경사항은 반영되지 않음.
  - A'를 다시 revert 하여 A'' commit을 만들면 main에 A의 변경사항이 살아난다.

## 시나리오: stash
### 참여자
- junhnno

### 상황
- `feature/add` 브랜치에서 커밋하지 않은 수정(`src/utils.py`)이 있는 상태에서 다른 브랜치로 전환해야 하는 상황을 재현했다.
- `add` 함수는 이미 커밋·push된 상태라 실제 미완성 작업이 없었다. 그래서 `src/utils.py` 끝에 주석 한 줄(`# stash 실습용 임시 수정`)을 추가해 커밋 전 수정을 만들었다. **실습을 위한 임시 수정이다.**
- 전환 대상은 `src/utils.py`가 빈 파일이던 옛 커밋(`17c7f67`)에서 만든 **로컬 연습용 브랜치** `practice/stash-demo`이다(push하지 않음). 팀원의 실제 브랜치가 아니다.
- 전환을 시도하자 Git이 거부했다.

```txt
$ git switch practice/stash-demo
error: Your local changes to the following files would be overwritten by checkout:
        src/utils.py
Please commit your changes or stash them before you switch branches.
Aborting
```

### 시도한 명령/절차
1. 연습용 브랜치 생성 (전환하지 않음). 처음에는 브랜치를 만들기 전에 `git switch`를 시도해 `fatal: invalid reference: practice/stash-demo`가 났고, 브랜치를 먼저 만들었다.

```txt
$ git branch practice/stash-demo 17c7f67
$ git branch
* feature/add
  feature/junhnno-doc-skeleton
  main
  practice/stash-demo
```

2. 임시 수정 생성

```txt
$ echo "# stash 실습용 임시 수정" >> src/utils.py
$ git status -sb
## feature/add...origin/feature/add
 M src/utils.py
```

3. 수정 보관

```txt
$ git stash push -m "utils.py 임시 수정 보관"
warning: in the working copy of 'src/utils.py', LF will be replaced by CRLF the next time Git touches it
Saved working directory and index state On feature/add: utils.py 임시 수정 보관
$ git stash list
stash@{0}: On feature/add: utils.py 임시 수정 보관
$ git status -sb
## feature/add...origin/feature/add
```

4. 전환 (이번에는 성공)

```txt
$ git switch practice/stash-demo
Switched to branch 'practice/stash-demo'
$ git log --oneline -3
17c7f67 (HEAD -> practice/stash-demo) chore: 빈 src/utils.py 생성
9128e3c Merge pull request #2 from Codyssey-git-B2-2/feature/junhnno-doc-skeleton
101106c (origin/feature/junhnno-doc-skeleton, feature/junhnno-doc-skeleton) docs: add collaboration docs and submission index skeletons
$ wc -c src/utils.py
0 src/utils.py
```

5. 복귀 및 복구

```txt
$ git switch feature/add
Switched to branch 'feature/add'
Your branch is up to date with 'origin/feature/add'.
$ git stash pop
On branch feature/add
Your branch is up to date with 'origin/feature/add'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   src/utils.py

no changes added to commit (use "git add" and/or "git commit -a")
Dropped refs/stash@{0} (ca750edec239b70bdcaba4f0025c5d8992d0492c)
$ git stash list
(출력 없음)
$ git status -sb
## feature/add...origin/feature/add
 M src/utils.py
$ git diff --ignore-cr-at-eol
diff --git a/src/utils.py b/src/utils.py
index 8798ba4..1634baf 100644
--- a/src/utils.py
+++ b/src/utils.py
@@ -20,3 +20,4 @@ if __name__ == "__main__":
     assert add(1, 2) == 3
     assert add(-1, 1) == 0
     print("ok")
+# stash 실습용 임시 수정
```

6. 정리 (임시 수정 폐기, 연습용 브랜치 삭제)

```txt
$ git restore src/utils.py
$ git status -sb
## feature/add...origin/feature/add
$ git branch -d practice/stash-demo
Deleted branch practice/stash-demo (was 17c7f67).
$ git branch
* feature/add
  feature/junhnno-doc-skeleton
  main
```

### 결과
- 커밋하지 않은 수정이 있을 때 브랜치 전환이 거부됐고, `git stash push`로 보관하자 작업 트리가 깨끗해져(`git status -sb`에 수정 표시 없음) 전환할 수 있었다.
- 원래 브랜치로 돌아와 `git stash pop`을 하자 수정이 그대로 복구됐고 stash 목록은 비었다(`Dropped refs/stash@{0}`).
- 복구된 diff는 임시로 넣은 한 줄뿐이었다.
- 주의할 점: stash는 로컬 저장소에만 있고 이번 실습에서 push한 것이 없어 원격 히스토리와 협업에는 영향이 없었다.
- 주의할 점(stash 충돌, 이번 실습에서는 발생하지 않아 재현하지 않은 참고 사항): stash를 보관한 뒤 다른 브랜치에서 같은 줄이 바뀐 상태로 `git stash pop`을 하면 충돌이 날 수 있다.
  - 충돌이 나면 stash 항목은 삭제되지 않고 `git stash list`에 남는다. 충돌 마커를 직접 수정하고 `git add`로 해결을 표시한 뒤, 내용을 확인하고 `git stash drop`으로 직접 지운다.
  - 작업 트리에 같은 파일의 커밋하지 않은 수정이 있으면 pop 자체가 거부될 수 있으므로, pop 전에 `git status`로 작업 트리 상태를 확인한다.

### 왜 이 방법을 선택했는가(Why)
- 커밋: 작업 중인 미완성 변경을 임시 커밋으로 남기면 의미 없는 커밋이 팀 히스토리에 남기 때문에 피했다.
- 변경 버리기(`git restore` 등): 수정이 사라져 다시 복구할 수 없어서 피했다.
- stash: 수정을 임시로 치워 깨끗한 상태로 전환하고, 돌아와서 그대로 복구할 수 있어 선택했다.
