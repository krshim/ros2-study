# ROS2 Autonomous Driving with Turtlebot3
#### (따라하기 쉽게 작성하는 것을 목표로 하였습니다. Linux와 ROS에 대한 기초지식이 있으면 좋습니다.)

<details open="open">
  <summary>목차</summary>
  <ol>
    <li><a href="#1-ubuntu20.04-설치">Ubuntu20.04 설치</a></li>
    <li><a href="#2-ROS2_foxy-설치">ROS2_foxy 설치</a></li>
    <li><a href="#3-개발-환경-설정">개발 환경 설정</a></li>
  </ol>
</details>

## 1. ubuntu20.04 설치
+ Rufus usb만들기 (https://ckrmsckrmstjdwkdwnd123.tistory.com/5)
+ 데스크탑에 ubuntu설치 (https://ckrmsckrmstjdwkdwnd123.tistory.com/6)
+ Ubuntu 설치가 완료된 후 터미널에서 창분할을 할 수 있도록 되어있는 Terminator를 설치한다.

ctrl+shift+T(터미널 열기)
```
sudo apt update # Terminator를 설치하기 전 데비안 패키지의 인덱스 정보를 업데이트
sudo apt install terminator # Terminator설치
```
+ 자주 쓰이는 Terminator 단축키
>
>Ctrl+ Shift+O : 터미널을 수평으로 분할
>
>Ctrl+ Shift+E : 터미널을 세로로 나누기 ## 실행이 안될 때 ```ibus-setup``` 에서 Emoji annotation 설정을 삭제해준다
>
>Ctrl + Shift + W : 현재 패널 닫기
>
>Ctrl + Shift + T : 새 탭 열기
>
>Alt+방향키 : 현재 터미널에서 방향키 입력 방향의 터미널로 이동한다.


## 2. ROS2_foxy 설치
+ ### Set locale(지역 설정)
```
locale  # UTF-8 인코딩을 사용하는지 점검

sudo apt update && sudo apt install locales
sudo locale-gen en_US en_US.UTF-8
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
export LANG=en_US.UTF-8

locale  # 시스템 설정 확인
```
+ ### Setup Sources(소스 설정)

Ubuntu Universe repository 저장소가 활성화 되어있는지 확인
```
sudo apt install software-properties-common
sudo add-apt-repository universe
```
apt를 사용하여 ROS2 GPG 키를 추가
```
sudo apt update && sudo apt install curl -y
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
```
소스 목록에 저장소 추가
```
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
```
+ ### Install ROS2 packages (ROS2 설치)
패키지 목록 최신화 (업그레이드 가능 패키지 표시 o, 패키지 버전 업그레이드 x)
```
sudo apt update
```
패키지를 최신 버전으로 업그레이드
```
sudo apt upgrade
```
데스크톱 설치(추천): ROS2, RViz, 데모, 튜토리얼
```
sudo apt install ros-foxy-desktop python3-argcomplete
```
ROS-Base 설치(RViz, Gazebo가 포함되지 않기에 비추천): 통신 라이브러리, 메시지 패키지, 명령줄 도구. GUI 도구 없음.
```
sudo apt install ros-foxy-ros-base python3-argcomplete
```
개발 도구: ROS 패키지를 빌드하기 위한 컴파일러 및 기타 도구
```
sudo apt install ros-dev-tools
```
+ ### Environment setup(환경 설정)
ROS2를 사용하기 위해서는 현재 터미널 세션을 ROS2환경으로 초기화 시켜주어야 한다.
```
source /opt/ros/foxy/setup.bash
```
터미널을 새로 열 때마다 환경설정을 해주기 귀찮다면 ```vi```, ```vim```, ```gedit``` 중 원하는 텍스트 편집기를 사용하여 ```.bashrc``` 파일을 수정해주어야 한다. (```vi```, ```vim```은 TUI, GUI, CLI 환경 모두에서 사용이 가능하고 ```gedit```은 GUI환경에서만 사용이 가능하다.)
```
gedit ~/.bashrc # ~(틸드)은 현재 사용자의 홈 디렉토리를 나타낸다.
```
.bashrc 파일의 맨 밑 줄에 ```source /opt/ros/foxy/setup.bash```를 추가하고 ctrl+S(저장)를 해주게 되면 터미널을 새로 열거나 창을 분할할 때마다 ros2 환경설정이 적용된다. 이후로는 모두 환경설정이 되었다는 가정하에 진행하겠다.

설치 확인을 위해서 ROS2를 다운받을 때 제공되는 기본 예제 패키지를 사용한다.
```
ros2 run demo_nodes_cpp talker # 토픽, 서비스 등 ROS 2 기능을 사용하는 방법을 보여주기 위해 C++로 작성된 예제 노드
```
새로운 터미널을 킨 후
```
ros2 run demo_nodes_py listener # 토픽, 서비스 등 ROS 2 기능을 사용하는 방법을 보여주기 위해 Python으로 작성된 예제 노드
```
위 두개의 노드를 실행시키면 서로 통신이 되는 것을 볼 수 있다.(talker가 없으면 listner가 동작하지 않음)

노드 간 통신을 확인하기 위해 시각화 도구인```rqt_graph```을 사용한다.

통신 목록을 확인하기 위해서는 ```ros2 topic list``` , ```ros2 service list```를 사용한다.


## 3. 개발 환경 설정
