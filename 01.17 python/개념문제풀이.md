#  Python 01. 데이터 & 제어문



## 1. Python 예약어

> **사용할 수 없는 식별자(예약어)를 찾아 작성하시오.**

1. 예약어

   ```python
   import keyword as kw
   print(kw.kwlist)
   
   >>> ['False', 'None', 'True', '__peg_parser__', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
   ```

2. 내장함수 및 모듈명 

   ```python
   print(dir(__builtins__))
   
   >>> ['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
   
   # 식별자 지정 및 값 할당까지 되지만, 해당 이름이 가진 원래의 내장함수 기능이 무시된다고 생각합니다.
   # 특히, 나중에 외부 라이브러리에서 모듈을 `import`해서 사용할땐 더욱 조심해야 할 것 같습니다.
   ```




## 2. 실수 비교

> **실수 값을 올바르게 비교하기 위한 코드를 작성하시오.**	

1. `machine epsilon`

   ```python
   import math,sys
   
   num1, num2 = 0.1 * 3, 0.3
   num3 = num1 - num2
   print(math.fabs(num3) <= sys.float_info.epsilon)
   
   >>> True     # (두 값의 차이가 매우 작아서, 같다고 봐도 무방하다)
   
   # epsilon은 반올림 오차의 상한값으로, 어떤 실수를 가장 가까운 부동소수점 실수로 반올림시
   # 상대오차는 항상 machine epsilon 이하입니다.
   ```

2.  `math.isclose`

   ```python
   import math 
   num1, num2 = 0.1 * 3, 0.3
   
   print(math.isclose(num1,num2))
   
   >>> True
   ```



## 3. 이스케이프 시퀀스

> **줄 바꿈, 탭, 백슬래시를 의미하는 이스케이프 시퀀스 작성하시오.**

1. ```python
   print('\n')  # 줄 바꿈
   print('\t')  # 탭
   print('\\')  # 백슬래시
   ```



## 4. string interpolation

> **'안녕, 철수야'를 string interpolation 사용하여 출력하시오.**

1. `f-string`

   ```python
   name = '철수'
   print('안녕, %s야' %name)
   ```

2. `str.format()`

   ```python
   name = '철수'
   print('안녕, {}야' .format(name))
   ```

3. `f-stings`

   ```python
   name = '철수'
   print(f '안녕, {name}야')
   ```



## 5. 형 변환

> **실행시 오류가 발생하는 코드 고르시오**

1. ```python
   print(str(1))      # 1
   print(int('30'))   # 30
   print(int(5))      # 5
   print(bool('50'))  # True
   
   print(int('3.5'))  # 오류
   >>> invalid literal for int() with base 10: '3.5'
   ```



## 6. 네모 출력

> 가로가n, 세로가m 인 직사각형 형태를 별(*)문자를 이용하여 출력하시오(단, 반복문 없이)

1. ```python
   n,m = 5,9
   print(('*' * m + '\n')*n)
   ```



## 7. 이스케이프 시퀀스 응용

> print() 함수를 한 번만 사용하여 다음 문장을 출력하시오.

1. ```python
   print("\"파일은 c:\\Windows\\Users\\내문서\\Python에 저장이 되었습니다.\"\n나는 생각했다. 'cd를 써서 git bash로 들어가 봐야지.'")
   
   >>> 
   "파일은 c:\Windows\Users\내문서\Python에 저장이 되었습니다."
   나는 생각했다. 'cd를 써서 git bash로 들어가 봐야지.'
   ```



## 8. 근의 공식

> 이차 방정식의 근을 찾는 수식을 코드로 작성하시오.

1. ```python
   def folmula(a,b,c):
       r1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
       r2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
       return r1,r2
   ```







---

