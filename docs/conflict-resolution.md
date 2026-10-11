# Conflict Resolution Log

> 실제로 수행한 충돌 해결만 기록한다. 충돌 마커는 해결하기 전에 복사해 둔다.

## 충돌 기록 #1

### 참여자
- 작성자:
- 상대:

### 상황(What happened)
-

### 충돌 내용(Conflict markers)
```txt
```

### 해결 과정(How)
- 선택한 해결 전략(keep both / choose one / refactor)과 이유:
- 실제로 수행한 명령 또는 절차:

### 결과(Outcome)
- 최종 병합 결과 요약, 관련 PR/커밋 링크:

### 배운 점(Learnings)
-


## 충돌 기록 #2

### 참여자
- 작성자: @SJendministrator (PR #26, feature/conflict-divide-clean)
- 상대: @huiwoo-jo (PR #20, feature/conflict-subtract)

### 상황(What happened)
- 팀원(@huiwoo-jo)이 `PR #20`(`feature/conflict-subtract`)을 통해 `src/utils.py`에 뺄셈(`subtract()`) 기능 및 테스트 코드를 작성하고 `main`에 병합함.
- 작성자(@SJendministrator)는 `PR #26`(`feature/conflict-divide-clean`)를 통해 `src/utils.py`에 나눗셈(`divide()`) 기능 및 테스트 코드를 작성하여 `main`에 병합을 시도함.
- 두 PR이 모두 `main`에서 출발했으나, 동일한 파일(`src/utils.py`)의 `add()` 함수 아래 위치와 `if __name__ == "__main__":` 테스트 블록 끝자리에 각각 새로운 코드를 추가함.
- `PR #20`이 `main`에 먼저 반영됨에 따라, `PR #26`에서 `main`을 병합(`git merge origin/main` 또는 `git pull origin main`)하는 과정에서 동일 인접 라인에 대한 비자명 병합 충돌(`Merge Conflict`)이 발생함.

### 충돌 내용(Conflict markers)
```txt
<<<<<<< HEAD
def divide(a: int | float, b: int | float) -> float:
    """a를 b로 나눈 값을 반환한다. 0으로 나눌 경우 ZeroDivisionError를 발생시킨다.

    >>> divide(6, 2)
    3.0
    >>> divide(5, 2)
    2.5
    """
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b


if __name__ == "__main__":
    print("multiply test")
    assert multiply(1, 2) == 2
    assert multiply(0, 2) == 0
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert divide(6, 2) == 3.0
    assert divide(5, 2) == 2.5
    print("ok")
=======
def subtract(a: int | float, b: int | float) -> int | float:
    """a에서 b를 뺀 값을 반환한다.

    >>> subtract(3, 1)
    2
    >>> subtract(1, 3)
    -2
    """
    return a - b


if __name__ == "__main__":
    print("multiply test")
    assert multiply(1, 2) == 2
    assert multiply(0, 2) == 0
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert subtract(3, 1) == 2
    assert subtract(1, 3) == -2
    print("ok")
>>>>>>> main

```

### 해결 과정(How)

#### 선택한 해결 전략(keep both / choose one / refactor)과 이유

* **선택한 해결 전략**: `keep both` (둘 다 유지)
* **이유**: `subtract`와 `divide`는 서로 독립적인 유틸리티 기능으로 모두 필수적임.
* **순서 규칙**: `main`에 이미 존재하는 `subtract`를 앞에 배치하고, 새로 추가하는 `divide`를 그 뒤에 배치하여 함수 정의부와 테스트 실행부의 순서를 동일하게 맞춤.
* **해결 주체**: 나중에 머지되는 `PR #26` 작성자(@SJendministrator)가 로컬 브랜치에서 `main`을 당겨와 충돌을 해결함.

#### 수행 절차

1. `PR #20`(`feature/conflict-subtract`)이 `main` 브랜치에 먼저 병합됨.
2. `PR #26`(`feature/conflict-divide-clean`) 브랜치에서 `git pull origin main`을 실행하여 최신 `main` 변경 사항을 가져옴.
3. `src/utils.py`에서 충돌 마커(`<<<<<<<`, `=======`, `>>>>>>>`) 발생 확인 후 디스코드/팀 채널에 충돌 상황 공유.
4. VS Code 병합 편집기를 이용하여 `subtract()` 아래에 `divide()`를 위치시키고, `__main__` 블록에서도 `subtract` 테스트 뒤에 `divide` 테스트 2줄을 추가한 뒤 마커를 깨끗이 제거함.
5. 터미널에서 `grep -n '<<<<<<<\|=======\|>>>>>>>' src/utils.py` 명령어로 남은 충돌 마커가 없는지 검증함.
6. `python3 src/utils.py` 실행으로 `ok` 출력 확인 및 `python3 -m doctest src/utils.py`로 docstring 예시 정상 동작 검증.
7. `git add src/utils.py` 및 `git commit -m "fix: resolve merge conflict between subtract and divide functions"` 병합 커밋 생성.
8. `git push origin feature/conflict-divide-clean` 실행 후 GitHub `PR #26` 페이지에서 빨간색 충돌 경고가 해제되었는지 확인.

### 결과(Outcome)

* **최종 `src/utils.py**`: `multiply`, `add`, `subtract`, `divide` 4개 함수의 정의와 각각의 테스트 코드가 모두 순서대로 깔끔하게 보존됨.
* **검증**: `python3 src/utils.py` 실행 결과 `ok` 출력, doctest 오류 없음, 충돌 마커 검색 결과 없음.
* **관련 이슈 및 PR**:
* 관련 이슈: `#22`
* 관련 PR: `#20`, `#26`



### 배운 점(Learnings)

* 먼저 병합된 PR이 파일 하단에 코드를 추가한 상태에서, 뒤이어 병합을 시도하는 PR 역시 파일 하단에 코드를 붙일 경우 인접 라인 충돌(Conflict)이 반드시 터진다는 점을 체득함.
* 충돌 해결 시 한쪽의 기능이 누락되지 않도록 `keep both` 전략을 사용할 때, 함수 정의부의 순서와 `__main__` 테스트 실행부의 순서를 일관되게 맞추는 컨벤션이 중요함을 배움.
* 충돌 수정 후 커밋하기 전에 항상 `doctest` 및 실행 테스트, 마커 검색(`grep`)을 거치는 것이 안전한 머지 절차임을 확인함.
