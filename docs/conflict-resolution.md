# Conflict Resolution Log

> 실제로 수행한 충돌 해결만 기록한다. 충돌 마커는 해결하기 전에 복사해 둔다.

## 충돌 기록 #1

### 참여자
- 작성자: @huiwoo-jo (PR #20, `feature/conflict-subtract`)
- 상대: @junhnno (PR #14, `feature/add`)

### 상황(What happened)
- 두 PR이 모두 `main`에서 갈라져 나와 같은 파일 `src/utils.py`를 수정했다.
  - PR #14: `add()` 함수를 추가하고 `if __name__ == "__main__":` 블록 끝에 `add` 테스트(`assert add(...)`) 2줄을 추가했다.
  - PR #20: `subtract()` 함수를 추가하고 `if __name__ == "__main__":` 블록 끝에 `substract` 테스트(`assert subtract(...)`) 2줄을 추가했다.
- 둘 중 하나가 `main`에 먼저 병합되면 나머지 PR에서 충돌이 발생하도록 의도적으로 만든 상황이다.
#14를 먼저 병합하고 #20에서 `main`을 병합(`git merge origin/main`)하며 충돌을 해결한다.
- `add()`, `subtract()` 함수 정의 부분과 `__main__` 블록의 테스트 줄에서 충돌한다.
#14이 추가한 `add()`와 `assert` 줄 바로 뒤에 #20가 새 줄을 추가한 인접 라인 충돌이다(비자명 충돌).

### 충돌 내용(Conflict markers)
```python
def multiply(a, b):
    return a * b


<<<<<<< feature/conflict-subtract
def subtract(a: int | float, b: int | float) -> int | float:
    """a에서 b를 뺀 값을 반환한다.

    >>> subtract(3, 1)
    2
    >>> subtract(1, 3)
    -2
    """
    return a - b
=======
def add(a: int | float, b: int | float) -> int | float:
    """a와 b를 더한 값을 반환한다.

    >>> add(1, 2)
    3
    >>> add(-1, 1)
    0
    """
    return a + b
>>>>>>> main


if __name__ == "__main__":
    print("multiply test")
    assert multiply(1, 2) == 2
    assert multiply(0, 2) == 0
<<<<<<< feature/conflict-subtract
    assert subtract(3, 1) == 2
    assert subtract(1, 3) == -2
=======
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
>>>>>>> main
    print("ok")

```

### 해결 과정(How)
- 디스코드에 해당 사항을 팀원들과 공유한다.
    ![alt text](/img/image.png)
```txt
🚨 충돌 발생 상황 공유드립니다. (PR #20 ← main)

#14(feature/add)가 main에 병합된 뒤 #20 브랜치(feature/conflict-subtract)에서 git merge origin/main을 했더니 src/utils.py에서 충돌이 발생했습니다.


[충돌 위치: 두 곳]
1. multiply() 바로 아래
    add() / subtract() 함수 정의
2. if __name__ == "__main__": 블록 끝
    add 테스트 / subtract 테스트


[원인]
#14와 #20이 같은 위치에 서로 다른 함수를 추가하며 기능은 다르지만 같은 줄 위치에 코드를 넣어서 충돌 발생

<<<<<<< feature/conflict-subtract
    def subtract(...) ...
=======
    def add(...) ...
>>>>>>> main
(테스트 블록도 동일)


[해결 방향]
- 한쪽을 버리지 않고 둘 다 남기는(keep both) 방식으로 해결 예정
- 순서는 main에 이미 있는 add를 먼저, subtract를 그 뒤에 두며 정의부와 테스트부 모두 같은 순서로 작성
- 해결은 나중에 병합하는 쪽인 #20 브랜치에서 진행


[PR 링크]
- #14: https://github.com/Codyssey-git-B2-2/Codyssey-git-B2-2/pull/14
- #20: https://github.com/Codyssey-git-B2-2/Codyssey-git-B2-2/pull/20
```

- 선택한 해결 전략(keep both / choose one / refactor)과 이유
  - 선택한 해결 전략: keep both
  - `add`와 `subtract`는 서로 다른 기능이라 둘 다 필요하다. 한쪽을 버리면 다른 PR의 작업이 사라진다.
  - 순서는 `main`에 이미 있는 `add`를 먼저 #20의 `subtract`를 그 뒤에 둔다. 함수 정의부와 테스트부 모두 같은 순서로 맞춘다.
  - 충돌이 두 곳이므로 두 곳을 모두 정리해야 한다. 한 곳만 고치면 `subtract` 정의는 남았는데 테스트가 빠지는 식으로 어긋난다.
  - 해결은 나중에 병합되는 쪽인 #20 작성자가 `main`을 가져와서 한다.

- 수행 절차
  1. #14가 `main`에 병합한다.
  2. #20 브랜치(`feature/conflict-subtract`)에서 `subtract()`와 테스트를 PR한다.
  3. `src/utils.py`의 충돌 상태 및 충돌 마커를 확인한다.
  4. 팀 채널에 충돌 사실을 공유한다.
  5. 정의부는 `add()` 아래에 `subtract()`를, 테스트부는 `add` 테스트 2줄 뒤에 `subtract` 테스트 2줄을 두고 마커를 제거한다.
  6. `grep -n '<<<<<<<\|=======\|>>>>>>>' src/utils.py`로 마커가 남아 있지 않은지 확인한다.
  7. `python3 src/utils.py`로 `ok` 출력, `python3 -m doctest src/utils.py`로 docstring 예시 확인
  8. `git add src/utils.py` 후 `git commit` (병합 커밋)
  9. `git push` 후 PR #20의 충돌 표시가 사라졌는지 확인

### 결과(Outcome)
- 최종 `src/utils.py`: `multiply`, `add`, `subtract`의 정의와 각 테스트가 모두 남아 있어야 한다.
- 검증: `python3 src/utils.py` 출력 `ok`, doctest 출력 없음 / 마커 검색 결과 없음
- PR #20 상태: 충돌 해소 여부, 리뷰 승인, 병합 여부
- 관련 PR: [#14](https://github.com/Codyssey-git-B2-2/Codyssey-git-B2-2/pull/14), [#20](https://github.com/Codyssey-git-B2-2/Codyssey-git-B2-2/pull/20)

- 충돌 해결 전
![alt text](/img/image-1.png)

- 충돌 해결 후
![alt text](/img/image-2.png)

### 배운 점(Learnings)
- 서로 다른 기능이라도 같은 위치(함수 정의 바로 아래, 테스트 블록 끝)에 코드를 추가하면 충돌한다. 같은 파일에 새 함수를 추가하는 PR은 작업 전에 위치를 조율하거나 먼저 병합된 PR이 정리된 뒤에 시작한다.
- 먼저 병합된 PR 때문에 뒤의 PR이 충돌한다. 해결은 뒤에 병합하는 쪽이 `main`을 가져와서 하고 그 전에 팀에 공유한다.
- 충돌이 여러 곳일 수 있다. 한 곳을 해결한 뒤 파일 안에 마커(`<<<<<<<`, `=======`, `>>>>>>>`)가 남아 있는지 검색하고, 코드를 실행해서 확인한다.

## 충돌 기록 #2

### 참여자
- 작성자:
- 상대:

### 상황(What happened)
-

### 충돌 내용(Conflict markers)
```txt
```

### 해결 과정(How)
-

### 결과(Outcome)
-

### 배운 점(Learnings)
-
