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
