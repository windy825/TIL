### CSS Flexible Box Layout

  

- **행과 열 형태**로 아이템들을 배치하는 **1차원 레이아웃 모델**
- **축** (설정한 값이 main이다 : row가로행 coloum세로열)
  - main axis
  - cross axis

- **구성요소**
  - **Flex Container** (부모 요소)
    - flexbox 레이아웃을 형성하는 가장 기본적인 모델
    - Flex item 들이 놓여있는 영역
    - display 속성을 `flex`혹은 `inline-flex`로 지정
  - **Flex Item** (자식 요소)
    - 컨테이너에 속해 있는 컨텐츠(박스)

- 원래 Normal Flow를 벗어나는 수단은 `Float` 혹은`Position`

​    

- **속성**

  - **배치 설정**

    - `flex-direction` : `row`, `row-reverse`, `column`, `column-reverse`

      메인 방향 설정하기

    - `flex-wrap` : `wrap` (넘치면, 그 다음 줄로 배치),  `nowrap` (한줄에 배치)

      기본적으로 flex container 영역을 벗어나지 않도록 해준다

      요소들이 강제로 한줄에 배치 되게 할 것인지 여부 설정

    - `flex-flow` : direction과 wrap의 shorthand

      ex) `flex-flow: row nowrap`

    - `flex-grow` : 남은 영역을 아이템에 분배

       

        

  - **공간 나누기**

    - `justify-content` (main axis를 기준으로 공간 배분)

      ![제목 없음](https://user-images.githubusercontent.com/89068148/153757497-b5e0155f-e000-4260-b58f-c482a64f7b71.png)

        

    - `align-content` (cross axis를 기준으로 공간 배분)

      ![제목 없음22](https://user-images.githubusercontent.com/89068148/153757549-b235ef24-f9a7-4c89-842c-36274ce8712b.png)

        

     

  - **정렬**

    - `align-items` (모든 아이템을 cross를 기준 정렬)

      ![제목 없음](https://user-images.githubusercontent.com/89068148/153757711-b9ad6eae-b5a4-4d6b-9a37-8c7640e6efbd.png)

        `align-items: baseline` 의 경우 텍스트 baseline에 기준선을 맞춤

        

    - `align-self` (cross를 기준으로 개별 아이템 설정)