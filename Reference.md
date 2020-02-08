## 개발에 필요한 사이트
[Free Image](https://www.flaticon.com/home)
[Color Keyword](https://www.w3.org/TR/SVG11/types.html#ColorKeywords)

[Othello Server Protocol](https://gitlab.com/UNKNOWN.UN/othello_protocol?fbclid=IwAR0ZRm-jF_qs_Svtq8qf3y0QtyqS4GF_uyDLXyyttxhvMTh7wZnTVe0LTLY)



## Server

requirements: Python 3.7

To run the server.

```
python server/othello_game_server.py [port number]
```



## TO-DO

- [ ] (2,3) 정상작동, (5,4) 비정상 => 재귀 과정에서 direction 하나를 건너뛰는듯
- [ ] 경계값 처리 후 전환, 모서리에 두면 리버스가 안됨
- [ ] 대국 종료 조건 구현(둘다 avaliable이 없을 경우, 64수를 둔 경우) - qmessageBox
- [x] 같이하기 진행시 ServerIP 와 ServerPort 받고 연결하는 GUI
- [ ] 타임값 받거나 자체적으로 표시한거 체크
- [ ] 1인용 2인용 리팩토링해서 합치기
- [ ] AI 올리기 (1. board정보 기반 점수 합치는 코드)
- [ ] othello.py에서 return 으로 넘어오는 data['board'] 활용하기



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

