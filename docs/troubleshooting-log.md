# Troubleshooting Log

> 실제로 수행한 명령과 출력만 기록한다. 실행 전후의 `git log --oneline` 등을 함께 붙인다.

## 시나리오: amend
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
-

### 상황
-

### 시도한 명령/절차
-

### 결과
-

### 왜 이 방법을 선택했는가(Why)
-

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

### 왜 이 방법을 선택했는가(Why)
- 커밋: 작업 중인 미완성 변경을 임시 커밋으로 남기면 의미 없는 커밋이 팀 히스토리에 남기 때문에 피했다.
- 변경 버리기(`git restore` 등): 수정이 사라져 다시 복구할 수 없어서 피했다.
- stash: 수정을 임시로 치워 깨끗한 상태로 전환하고, 돌아와서 그대로 복구할 수 있어 선택했다.
