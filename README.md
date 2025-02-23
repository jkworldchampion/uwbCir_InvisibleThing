# uwbCir_InvisibleThing

논문 및 UWB CIR에 대해서 공부한 것.  

이 연구를 통해 내가 하고 싶은 말: UWB 기기 2개만을 가지고도, passive 위치추정을 할 수 있다.

# 어떻게? 
: 현재는 4개 또는 3개로 passive 위치 추정을하는데, 이때 기본이 되는 방법은 background subtraction으로 지연시간(CIR 상에서 나타난 multipath신호의 특이점.)을 갖고, 타원추정을 하여 particle filter를 갖고 위치를 추정해.
