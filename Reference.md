## 개발에 필요한 사이트
[Free Image](https://www.flaticon.com/home)

[Color Keyword](https://www.w3.org/TR/SVG11/types.html#ColorKeywords)





## TO-DO

- [x] (2,3) 정상작동, (5,4) 비정상 => 재귀 과정에서 direction 하나를 건너뛰는듯
- [x] 경계값 처리 후 전환, 모서리에 두면 리버스가 안됨
- [x] 대국 종료 조건 구현(둘다 avaliable이 없을 경우, 64수를 둔 경우) - qmessageBox
- [x] 같이하기 진행시 ServerIP 와 ServerPort 받고 연결하는 GUI
- [x] 타임값 받거나 자체적으로 표시한거 체크
- [x] 1인용 2인용 & Human, Ai 리팩토링해서 합치기
- [x] AI 올리기 (1. board정보 기반 점수 합치는 코드)
- [x] othello.py에서 return 으로 넘어오는 data['board'] 활용하기
- [x] [스레드](http://i5on9i.blogspot.com/2016/05/qt-worker-thread.html)



### Knowledge learned from the project
- pyqt, qtdesigner usage


- Access other class method member variable

  ```python
  self.server = Othello # access other class(name:Othello)
  test = self.server.wait_for_turn(self) # access other class member var
  ```

- string slicem, merge in python 

  ```python
  position = btn.objectName()
  x = int(position[0])
  y = int(position[1])
  str(i)+str(j)
  ```

- [lambda : Anonymous Function](https://dojang.io/mod/page/view.php?id=2359)

- L value assignment

  ```python
  # SyntaxError: can't assign to operator ==> lvalue assignment
  if (x+self.dx[k]) < 0:
      x+self.dx[k] = 0
  ```
  
- Recursive Algorithm

- set/get object name

- ObjectOriented Programming

- GUI Thread Programming

  - Qthread
  - threaing



> **TO-DO STUDY**
>
> 
>
> - Python concurrency control
> - Design Pattern
> - Dynamic programming
> - Heuristic Algorithm
> - [thread & queue](https://niceman.tistory.com/140?category=940952)

