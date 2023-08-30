# Greedy Algorithm
------------
  

"Greedy" 란 탐욕스러운, 욕심많은 이라는 뜻으로 그리디 알고리즘은 단순하며 탐욕적으로 문제를 해결한다고 하여 이러한 명칭으로 불리고 있습니다.  
  
여기서 단순하게 혹은 탐욕스럽게 이를 해결한다는 것을 조금 더 풀어서 설명할 필요가 있다.  
이를 설명하면 **선택의 순간마다 당장 가장 최선의 선택을 하여 최종적인 해답에 도착하는 것**라고 할 수 있다.  

그리드 알고리즘은 최적해를 구하는 근사적인 방법으로 당장 처해진 상황에서의 최선의 선택을 하지만 현재의 선택이 나중에 미칠 영향에 대해서는 고려하지 않기에 도출해낸 최종적인 해답이 완벽한 최적해라고 할 수 없다.  
그리드 알고리즘이 정상적으로 최적해를 구하기 위해서, 해당 문제는 다음과 같은 조건 성립해야 한다.
- **탐욕적 선택 속성(Greedy Choice Property):** 앞의 선택이 이후의 선택에 영향을 주지 않는다.  

- **최적 부분 구조(Optimal Substructure):** 문제에 대한 최종 해결 방법은 부분 문제에 대한 최적 문제 해결 방법으로 구성된다.

물론 해당 조건을 만족하지 않더라도 그리디 알고리즘은 근사 알고리즘으로서 사용이 가능하다.(최적해를 구하지 못 하는 것뿐이다.)  
  
****
### Problem Solved

- [**큰 수의 법칙**](https://github.com/ChanghyunRyu/Python_CodingTest_note/tree/main/greedy_algorithm/law%20of%20large%20numbers)  
- [**잃어버린 괄호**](https://github.com/ChanghyunRyu/Python_CodingTest_note/tree/main/greedy_algorithm/missing%20parenthesis)
- [**회의실 배정**](https://github.com/ChanghyunRyu/Python_CodingTest_note/tree/main/greedy_algorithm/meeting%20room%20assignment)
- [**설탕 배달**](https://github.com/ChanghyunRyu/Python_CodingTest_note/tree/main/greedy_algorithm/suger_delivery)
- [**숫자 카드 게임**](https://github.com/ChanghyunRyu/Python_CodingTest_note/tree/main/greedy_algorithm/number%20card%20game)