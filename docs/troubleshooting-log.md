# Troubleshooting Log

> 실제로 수행한 명령과 출력만 기록한다. 실행 전후의 `git log --oneline` 등을 함께 붙인다.

## 시나리오: amend

### 참여자
* 박수정

* 커밋 후 내용을 수정하여 amend를 진행한다.

### 상황

* `docs/troubleshooting-log.md`를 수정하여 커밋한 후, push하기 전에 추가 수정 사항이 발생하였다.
* 기존 커밋에 추가 수정 사항을 반영하기 위해 `git commit --amend`를 사용하였다.

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

* 첫 번째 커밋 `5a275a4`에 추가 수정 사항을 반영하였다.
* `git commit --amend --no-edit`를 사용하여 새로운 커밋을 추가하지 않고 기존 마지막 커밋을 수정하였다.
* amend 전 커밋 해시는 `5a275a4`였으며, amend 후 `441ecb2`로 변경되었다.
* 커밋 메시지는 `docs: amend 실습 내용 추가`로 유지되었다.
* 현재 로컬 브랜치가 원격 브랜치보다 1개 커밋 앞선 상태이며 아직 push하지 않았다.

### 왜 이 방법을 선택했는가(Why)

* 아직 원격 저장소에 push하지 않은 마지막 커밋을 수정하는 상황이므로 `git commit --amend`를 선택하였다.
* 별도의 수정 커밋을 추가하지 않고 기존 커밋에 수정 내용을 반영하여 커밋을 하나로 정리할 수 있기 때문이다.


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
-

### 상황
-

### 시도한 명령/절차
-

### 결과
-

### 왜 이 방법을 선택했는가(Why)
-
