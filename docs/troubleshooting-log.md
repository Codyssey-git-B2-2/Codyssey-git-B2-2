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
- @huiwoo-jo

### 상황
- 저장소에 `.gitignore`를 추가하기 위하여 `origin/main`(`7a8f6de`) 기준으로 `feature/add-gitignore` 브랜치를 만들었다.
- 파일을 `git add`로 담다가 커밋하면 안 되는 임시 메모 `memo.txt`까지 함께 담아 커밋 후 아직 push하지 전이었다.
- 커밋 직후 `git show --stat`으로 확인하니 `.gitignore`와 `memo.txt` 2개 파일이 들어 있었다. 커밋 메시지도 `gitignore 및 임시 메모 추가`로 메모 파일이 포함된 내용이었다.

### 시도한 명령/절차
1. 브랜치 생성 및 시작 상태 확인

```
$ git worktree add --no-track -b feature/add-gitignore ../Codyssey-git-B2-2-reset-soft origin/main
$ git log --oneline -3
7a8f6de Merge pull request #20 from Codyssey-git-B2-2/feature/conflict-subtract
4320cd9 Merge branch 'feature/conflict-subtract' of https://github.com/Codyssey-git-B2-2/Codyssey-git-B2-2 into feature/conflict-subtract
385c5b9 docs: 충돌 해결 사진 첨부

$ git status -sb
## feature/add-gitignore
```

2. 트러블 발생: 메모 파일까지 함께 커밋

```
$ git add .gitignore memo.txt
$ git commit -m "chore: gitignore 및 임시 메모 추가"
$ git log --oneline -3
89f7959 chore: gitignore 및 임시 메모 추가
7a8f6de Merge pull request #20 from Codyssey-git-B2-2/feature/conflict-subtract
4320cd9 Merge branch 'feature/conflict-subtract' of https://github.com/Codyssey-git-B2-2/Codyssey-git-B2-2 into feature/conflict-subtract

$ git show --stat --format='%h %s' HEAD
89f7959 chore: gitignore 및 임시 메모 추가

 .gitignore | 6 ++++++
 memo.txt   | 1 +
 2 files changed, 7 insertions(+)

$ git log --oneline origin/main..HEAD
89f7959 chore: gitignore 및 임시 메모 추가
```

`origin/main`보다 앞선 커밋이 이 1개뿐이고 upstream 설정이 없어서 push하지 않았음을 확인했다.

3. `git reset --soft HEAD~1`로 커밋 취소 (변경 유지)

```
$ git reset --soft HEAD~1
$ git log --oneline -2
7a8f6de Merge pull request #20 from Codyssey-git-B2-2/feature/conflict-subtract
4320cd9 Merge branch 'feature/conflict-subtract' of https://github.com/Codyssey-git-B2-2/Codyssey-git-B2-2 into feature/conflict-subtract

$ git status -sb
## feature/add-gitignore
A  .gitignore
A  memo.txt

$ git diff --cached --stat
 .gitignore | 6 ++++++
 memo.txt   | 1 +
 2 files changed, 7 insertions(+)

$ git reflog -4
7a8f6de HEAD@{0}: reset: moving to HEAD~1
89f7959 HEAD@{1}: commit: chore: gitignore 및 임시 메모 추가
7a8f6de HEAD@{2}: reset: moving to HEAD
7a8f6de HEAD@{3}:
```

커밋 `89f7959`는 사라졌지만 두 파일은 `A`(스테이징된 상태)로 그대로 남아 있다.

4. 메모 파일을 빼고 올바른 커밋으로 다시 만들기

```
$ git restore --staged memo.txt
$ rm memo.txt
$ git status -sb
## feature/add-gitignore
A  .gitignore

$ git commit -m "chore: .gitignore 추가"
$ git log --oneline -3
23a201e chore: .gitignore 추가
7a8f6de Merge pull request #20 from Codyssey-git-B2-2/feature/conflict-subtract
4320cd9 Merge branch 'feature/conflict-subtract' of https://github.com/Codyssey-git-B2-2/Codyssey-git-B2-2 into feature/conflict-subtract

$ git show --stat --format='%h %s' HEAD
23a201e chore: .gitignore 추가

 .gitignore | 6 ++++++
 1 file changed, 6 insertions(+)

$ git log --oneline origin/main..HEAD | wc -l
       1
```

### 결과
- 잘못 만든 커밋 `89f7959`(`.gitignore` + `memo.txt`)가 취소되었다. `reflog`에 `reset: moving to HEAD~1`로 기록되어 있다.
- `.gitignore` 변경은 그대로 유지되어, 파일을 다시 만들지 않고 `memo.txt`만 스테이징에서 빼서 새 커밋 `23a201e`(`chore: .gitignore 추가`, 파일 1개)를 만들었다.
- `origin/main` 이후 커밋은 올바른 커밋 1개만 남았다.

### 왜 이 방법을 선택했는가(Why)
- 아직 push 전인 로컬 커밋: 내 로컬에만 있는 커밋이라 히스토리를 고쳐도 팀원에게 영향이 없다. 이미 push한 커밋이었다면 히스토리를 고치지 않고 `git revert`로 되돌리는 커밋을 만들어야 한다.
- 변경은 살리고 커밋만 취소: `--soft`는 `HEAD`만 되돌리고 스테이징 상태를 그대로 둔다. `.gitignore`는 다시 만들거나 다시 `git add`할 필요 없이 `memo.txt`만 빼면 됐다. `--mixed`는 스테이징까지 풀려 모든 파일을 다시 `git add`해야 하고 `--hard`는 변경 자체를 삭제하므로 이 상황에 맞지 않는다.
- 커밋 하나로 남기기: `git revert`는 되돌리는 커밋이 하나 더 생겨 불필요한 커밋이 늘어난다. `reset --soft`는 잘못된 커밋을 히스토리에서 없애 최종적으로 의미 있는 커밋 1개만 남긴다.
- `amend`와의 차이: `git commit --amend`로도 같은 결과를 만들 수 있지만 이 실습은 커밋을 먼저 취소(`HEAD~1`)한 뒤 스테이징 상태에서 무엇이 들어갈지 다시 점검하는 흐름을 확인하는 것이 목적이다. 마지막 커밋을 덮어쓰는 `amend`는 별도 시나리오로 다룬다.

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
-

### 상황
-

### 시도한 명령/절차
-

### 결과
-

### 왜 이 방법을 선택했는가(Why)
-
