**동기화 객체**

Synchronized 키워드가 붙은 객체, 해당 객체가 실행되는 동안에 동기화를 보장하는 것.

서버에서 다중스레드를 사용하여 요청을 처리할 경우 제일 먼저 요청한 녀석이 동기화 객체로부터 모든 일을 마치고 나올 때까지, 스레드에 붙어 줄줄이 번호표를 뽑고 기다리도록 한다. 동기화 구문이 커지면 작업 수행 속도가 느려질 수 있다.