# DFS (Depth-First Search)

### 깊이 우선 탐색이라고도 부르며, 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘



# 그래프 (Graph)

### 그래프는 노드(Node)와 간선(Edge)로 표현되며, 이때 노드를 정점(Vertex)이라고도 말한다.

    그래프 탐색이란 하나의 노드를 시작으로 다수의 노드를 방문하는 것을 말함
    또한 두 노드가 간선으로 연결되어 있다면, '두 노드는 인접하다(adjacent)'라고 표현

<img src="https://user-images.githubusercontent.com/30036777/103998102-1661d800-51df-11eb-81f7-c83f9dd1f7d4.png" width="400" height="370"></img>


### 그래프의 표현 방식

    그래프는 크게 2가지 방식으로 표현할 수 있다

    1. 인접 행렬(Adjacency Matrix) : 2차원 배열로 그래프의 연결 관계를 표현하는 방식
    2. 인접 리스트(Adjacency List) : 리스트로 그래프의 연결 관계를 표현하는 방식

#### 인접 행렬

![img](https://user-images.githubusercontent.com/30036777/104000007-fcc19000-51e0-11eb-8dae-d04b77d63898.png)


    인접 행렬 방식은 2차원 배열에 각 노드가 연결된 형태를 기록하는 방식
    파이썬에서는 2차원 리스트로 구현 가능
    
    연결이 되어 있지 않은 노드끼리는 무한(INF, Infinity)의 비용이라고 작성
    실제 코드에서는 논리적으로 정답이 될 수 없는 큰 값 중에서 999999999, 987654321 등의 값으로 초기화 하는 경우가 많다

    그래프를 인접 행렬 방식으로 처리할 때는 [5_6_인접_행렬_방식_예제.py]와 같이 데이터를 초기화한다.

[5_6_인접_행렬_방식_예제.py](https://github.com/SeoHyungjun/Coding_Test/blob/master/%EC%9D%B4%EA%B2%83%EC%9D%B4%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8%EB%8B%A4/ch5.DFS_BFS/2_%ED%83%90%EC%83%89_%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98_DFS_BFS/5_6_%EC%9D%B8%EC%A0%91_%ED%96%89%EB%A0%AC_%EB%B0%A9%EC%8B%9D_%EC%98%88%EC%A0%9C.py)

#### 인접 리스트

    인접 리스트 방식에서는 아래 그림과 같이 모든 노드에 연결된 노드에 대한 정보를 차례대로 연결하여 저장

![다운로드](https://user-images.githubusercontent.com/30036777/104000213-43af8580-51e1-11eb-9bff-0b7b953270a4.png)

    인접 리스트는 '연결 리스트'라는 자료구조를 이용하여 구현
    C++/JAVA 같은 프로그래밍 언어세서는 별도로 연결 리스트 기능을 위한 표준 라이브러리를 제공
    파이썬은 기본 자료형인 리스트 자료형이 appnd() 메소드를 제공하므로, 연결 리스트의 기능을 제공

    그래프를 인접 리스트 방식으로 처리할 때는 [5_7_인접_리스트_방식_예제.py]와 같이 데이터를 초기화한다.

[5_7_인접_리스트_방식_예제.py](https://github.com/SeoHyungjun/Coding_Test/blob/master/%EC%9D%B4%EA%B2%83%EC%9D%B4%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8%EB%8B%A4/ch5.DFS_BFS/2_%ED%83%90%EC%83%89_%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98_DFS_BFS/5_7_%EC%9D%B8%EC%A0%91_%EB%A6%AC%EC%8A%A4%ED%8A%B8_%EB%B0%A9%EC%8B%9D_%EC%98%88%EC%A0%9C.py) 