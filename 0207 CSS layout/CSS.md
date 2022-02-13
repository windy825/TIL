## CSS



- **Cascading Style Sheets**

- 스타일을 지정하기 위한 언어 **선택 하고, 스타일을 지정한다.**

- css 구문 용어 장리

     

  ![제목 없음](https://user-images.githubusercontent.com/89068148/153737950-2072faa8-5fae-4a58-b004-0e41b3befb4b.png)

  - 선택자를 통해 스타일을 지정할 HTML 요소를 선택
  - 중괄호 안에서는 속성과 값, 하나의 쌍으로 이루어진 선언을 진행
  - 각 쌍은 선택한 요소의 속성, 속성에 부여할 값을 의미
    - **Property 속성** : 어떤 스타일 기능을 변경할지 결정
    - **Value 값** : 어떻게 스타일 기능을 변경할지 결정

  

- **css 정의 방법**

  - **인라인** : 해당 태그에 직접 style 속성을 활용

    ```html
    <h1 style="color: blue; font-size: 100px;">HELLO, PYTHON HTML5</h1>
    ```

  - **내부 참조** : `<head>`태그 내에 <style>에 지정 

    ```html
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Document</title>
      <style>
        h1 {
          color: blue;
          font-size: 100px;
        }
      </style>
    </head>
    ```

     

  - **외부 참조**  : 외부 css 파일을 `<head>` 내의  `<link>`를 통해 불러오기

    ```html
    <head>
        <title>Mysite</title>
        <link rel="stylesheet" href="####">
    </head>
    ```

    ```css
    h1 {
        color: blue;
        font-size: 20px
    }
    ```

      

- **선택자**
  - 기본 선택자
    - `*`전체 선택자,  `h2`요소 선택자
    - `.green`클래스 선택자, `#purple`아이디 선택자, 속성 선택자
  - 결합자 `Combinators`
    - `.box p`자손 결합자, `.box > p`자식 결합자
    - 일반 형제 결합자, 인접 형제 결합자
  - 의사 클래스/요소 `Pseudo Class`
    - 링크, 동적 의사 클래스
    - 구조적 의사 클래스, 기타 의사 클래스, 의사 엘리먼트, 속성 선택자
  
  ```
  HTML 태그를 직접 선택 : 요소 선택자
  
  마침표(.)로 시작하며 해당 클래스가 적용된 항목을 선택 : 클래스 선택자
  
  # 으로 시작하며, 해당 아이디가 적용된 항목을 선택
  하나의 문서에 1번만 사용, 여러 번 쓰더라도, 단일 ID를 사용하는 것을 권장 : id 선택자
  ```
  
   

- **CSS 적용 우선순위**
  - 중요도 importance : `!important`
  - 우선순위 Specificity :
    - 인라인 > id > class, 속성, pesudo-class > 요소, pesudo-element
  - css 파일 로딩 순서

  

- **CSS 상속**
  - 부모 요소의 속성을 자식에게 상속
  - 상속 되는 속성, 프로퍼티
    - text관련 요소(font, color, text-align), opacity, visibility
  - 상속 안되는 속성, 프로퍼티
    - box model 관련 요소 (width, height, margin, padding, border, box-sizing, display)
    - position 관련 요소 (position, top/right/bottom/left/z-index)

  

- **색상 단위** (대소문자 구분 없음, 특정 색 직접 나타냄)
  - RGB : 16진수 or 함수형 표기법
  - HSL : 색상, 채도, 명도

   

- **크기 단위**

  - **px** 모니터 해상도의 한 화소, 고정적인 단위

  - **%** 백분율 단위, 가변적인 레이아웃에서 자주 사용

  - **em** 바로 위 부모 요소에 대한 상속의 영향을 받음

    배수 단위, 요소에 지정된 사이즈에 상대적인 사이즈를 가짐

  - **rem** 바로 위 부모 요소에 대한 상속의 영향을 받지 않음

    최상위 요소(html)의 사이즈를 기준으로 배수 단위를 가짐

  - **viewport** 웹 페이지 방문자에게 바로 보이게 되는 웹 컨텐츠 영역 (디바이스 화면)

    디바이스의 viewport를 기준으로 상대적인 사이즈가 결정됨

  - ex ) vw, vh, vmin, vmax

  

  

- **결합자** Combinators
  - `div span`자손 결합자 : 하위의 모든 요소
  - `div > span`자식 결합자 : 바로 아래 요소
  - `p ~ span`일반 형제 결합자 : 형제 요소 중 뒤에 있는 모든 요소
  - `p + span`인접 형제 결합자 : 형제 요소 중 바로 뒤에 있는 한 요소

  

- **Box model**
  - 모든 html요소는 박스로 이루어져 있다.
    - content : 글이나 이미지, 요소의 실제 내용
    - padding : 테두리 안의 내부 여백 **배경색 가능** **이미지는 padding까지** 적용
    - border : 테두리 영역
    - margin : 테두리 밖의 외부 여백 **배경색 불가능**
  - 한개만 단위 적으면 상하좌우
  - shorthand
    - margin : 10px;   전체
    - margin : 10px 20px;   y축, x축
    - margin : 10px 20px 30px;   상 우 하
    - margin : 10px 20px 30px 40px;   상 우 하 좌

  

  

- **Display**

  - **display: block **
    - **`div / ul, ol, li / p / hr / form`** 등
    - 줄 바꿈이 일어나는 요소
    - 화면 크기 전체의 가로 폭을 차지 (기본 너비가 100%, 가질 수 없다면 자동 마진 처리)
    - 안에 인라인 레벨 요소가 들어갈 수 있음
  - **display: inline**
    - **`span / a / img / input, label / b, em, i, strop`**  등
    - 줄 바꿈이 일어나지 않는 행의 일부
    - content 넓이 만큼 가로 폭을 차지
    - width, height, margin-top, margin-bottom 지정 불가
    - 상하 여백은 line-height로 지정

    

  ![제목 없음](https://user-images.githubusercontent.com/89068148/153744173-99e0e64a-3d5d-4671-92d2-11233b2d1bd1.png)

  - **display: inline-block**
    - 블럭과 인라인 레벨 요소 특징을 모두 가짐
    - 한 줄에 표시 가능하고, 블럭처럼 width, height, margin 속성을 모두 지정 가능
  - **display: none**
    - 해당 요소를 화면에 표시하지 않고, 공간조차 부여되지 않음
    - `visibility: hidden`은 표시는 안되지만, 공간은 차지할 수 있다.

  

- **CSS position**
  - 문서 상에서 요소 위치를 선정
  - static : 모든 태그의 기본 값 (기준 위치)
    - 일반적인 요소의 배치 순서에 따름, 좌측상단
    - 부모 요소 내에서 배치될 때는 부모 요소의 위치를 기준으로 배치됨
  - 좌표 프로퍼티(top, bottom, left, right)를 사용하여 이동 가능
    - **relative 상대 위치 **
      - 자기 자신의 static 기준으로 이동 (normal flow 유지)
      - 레이아웃에서 요소가 차지하는 공간은 static일 때와 같음 (normal position 대비 offset)
    - **absolute 절대 위치** *부모 기준*
      - 요소를 일반적 문서 흐름에서 제거 후 레이아웃에 공간을 차지하지 않음 (out of normal flow)
      - static 이 아닌 가장 가까이 있는 부모/조상 요소를 기준으로 이동 (없는 경우 body)
    - **fixed 고정 위치** *브라우저 기준*
      - 요소를 일반적 문서 흐름에서 제거 후 레이아웃에 공간을 차지하지 않음 (out of normal flow)
      - 부모 요소와 관계없이 viewport를 기준으로 이동 (스크롤 시에도 항상 같은 곳 위치)

  

  

- **CSS 원칙**
  - **1,2 : Normal flow**
    - 모든 요소는 네모(박스모델), 좌측 상단에 위치
    - display에 따라 크기와 배치가 달라짐
  - **3 : position 으로 위치의 기준점 변경**
    - relative : 본인의 원래 위치
    - absolute : 특정 부모의 위치
    - fixed : 화면의 위치