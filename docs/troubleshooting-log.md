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
-

### 상황
-

### 시도한 명령/절차
-

### 결과
-

### 왜 이 방법을 선택했는가(Why)
-
