# ROS2 Autonomous Driving with Turtlebot3
#### (따라하기 쉽게 작성하는 것을 목표로 하였습니다. Linux와 ROS에 대한 기초지식이 있으면 좋습니다.)

<details open="open">
  <summary>목차</summary>
  <ol>
    <li><a href="#개발-환경-설정">개발 환경 설정</a></li>
    <li><a href="#ROS2-패키지-노드-생성">ROS2 패키지 노드 생성</a></li>
  </ol>
</details>

## 1. 개발 환경 설정
<a id="개발-환경-설정"></a>

### 1-1. ubuntu20.04 설치
+ Rufus usb만들기 (https://ckrmsckrmstjdwkdwnd123.tistory.com/5)
+ 데스크탑에 ubuntu설치 (https://ckrmsckrmstjdwkdwnd123.tistory.com/6)
+ Ubuntu 설치가 완료된 후 터미널에서 창분할을 할 수 있도록 되어있는 Terminator를 설치한다.

`ctrl+shift+T`(터미널 열기)
```
sudo apt update # Terminator를 설치하기 전 데비안 패키지의 인덱스 정보를 업데이트
sudo apt install terminator # Terminator설치
```
+ 자주 쓰이는 Terminator 단축키
>
>`Ctrl+ Shift+O`: 터미널을 수평으로 분할
>
>`Ctrl+ Shift+E` : 터미널을 세로로 나누기 ## 실행이 안될 때 ```ibus-setup``` 에서 Emoji annotation 설정을 삭제해준다
>
>`Ctrl + Shift + W` : 현재 패널 닫기
>
>`Ctrl + Shift + T` : 새 탭 열기
>
>`Alt+방향키` : 현재 터미널에서 방향키 입력 방향의 터미널로 이동한다.

## 1-2. ROS2_foxy 설치
+ ### Set locale(지역 설정)
```
locale # UTF-8 인코딩을 사용하는지 점검

sudo apt update && sudo apt install locales
sudo locale-gen en_US en_US.UTF-8
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
export LANG=en_US.UTF-8

locale # 시스템 설정 확인
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
ROS2-foxy 설치 방법

>데스크톱 설치(추천): ROS2, RViz, 데모, 튜토리얼
>```
>sudo apt install ros-foxy-desktop python3-argcomplete
>```
>ROS-Base 설치(RViz, Gazebo가 포함되지 않기에 비추천): 통신 라이브러리, 메시지 패키지, 명령줄 도구. GUI 도구 없음.
>```
>sudo apt install ros-foxy-ros-base python3-argcomplete
>```
개발 도구(필수): ROS 패키지를 빌드하기 위한 컴파일러 및 기타 도구
```
sudo apt install ros-dev-tools
```
+ ### Environment setup(환경 설정)
ROS2를 사용하기 위해서는 현재 터미널 세션을 ROS2환경으로 초기화 시켜주어야 한다.
```
source /opt/ros/foxy/setup.bash
```
터미널을 새로 열 때마다 환경설정을 해주기 귀찮다면 ```vi```, ```vim```,```nano```, ```gedit``` 중 원하는 텍스트 편집기를 사용하여 ```.bashrc``` 파일을 수정해주어야 한다. (```vi```, ```vim```은 TUI, GUI, CLI 환경 모두에서 사용이 가능하고 ```gedit```은 GUI환경에서만 사용이 가능하다.)
```
gedit ~/.bashrc # ~(틸드)은 현재 사용자의 홈 디렉토리를 나타낸다.
```
.bashrc 파일의 맨 밑 줄에 ```source /opt/ros/foxy/setup.bash```를 추가하고 ctrl+S(저장)를 해주게 되면 터미널을 새로 열거나 창을 분할할 때마다 ros2 환경설정이 적용된다. 이후로는 모두 환경설정이 되었다는 가정하에 진행하겠다.

설치 확인을 위해서 ROS2를 다운받을 때 제공되는 기본 예제 패키지를 사용한다.
```
ros2 run demo_nodes_cpp talker # 토픽, 서비스 등 ROS 2 기능을 사용하는 방법을 보여주기 위해 C++로 작성된 예제 노드
```
새로운 터미널을 킨 후 아래 노드를 실행시킨다
```
ros2 run demo_nodes_py listener # 토픽, 서비스 등 ROS 2 기능을 사용하는 방법을 보여주기 위해 Python으로 작성된 예제 노드
```
위 두개의 노드를 실행시키면 서로 통신이 되는 것을 볼 수 있다.(talker가 없으면 listner가 동작하지 않음)

노드 간 통신을 확인하기 위해 시각화 도구인```rqt_graph```을 사용한다.

통신 목록을 확인하기 위해서는 ```ros2 topic list``` , ```ros2 service list```를 사용한다.

## 1-3. 통합 개발 환경(IDE)구축
ROS를 패키지를 효과적으로 생성하고 구동하기 위해 통합 개발환경 Tool을 사용 하는 것을 추천한다.

+ visual studio code 설치

https://code.visualstudio.com/Download - 이 링크에 들어가 .deb파일을 다운받아 설치한다.

+ User settings 설정

'settings.json'은 VSCode의 사용자별 글로벌 환경 설정을 지정하는 파일이다. 이 파일에 기술된 설정들은 모든 작업 공간(workspace)에서 적용된다.  ~/.config/Code/User/ 에 위치한 'settings.json' 에 다음과 같이 설정하면 된다.
```
cd ~/.config/Code/User # 경로 설정
code settings.jason  # vscode로 settings.jason 파일 열기
```
settings.jason 파일에 아래 코드를 작성한다.
```
{
  "cmake.configureOnOpen": false,
  "editor.minimap.enabled": false,
  "editor.mouseWheelZoom": true,
  "editor.renderControlCharacters": true,
  "editor.rulers": [100],
  "editor.tabSize": 2,
  "files.associations": {
    "*.repos": "yaml",
    "*.world": "xml",
    "*.xacro": "xml"
  },
  "files.insertFinalNewline": true,
  "files.trimTrailingWhitespace": true,
  "terminal.integrated.scrollback": 1000000,
  "workbench.iconTheme": "vscode-icons",
  "workbench.editor.pinnedTabSizing": "compact",
  "ros.distro": "foxy",
  "colcon.provideTasks": true
}
```
+ C/C++ properties 설정

C/C++ 관련 설정이다. 현재 지정한 작업 공간 (여기서는 ~/robot_ws)의 운영체제는 무엇인지, include 폴더의 경로는 어떻게 되는지, C/C++ 규칙은 어떤 표준을 기준을 사용할지의 여부, 컴파일의 경로 등을 설정하게 된다.
```
cd ~/robot_ws/.vscode/
code c_cpp_properties.json
```
c_cpp_properties.json 파일에 아래 코드를 작성한다.
```
{
  "configurations": [
    {
      "name": "Linux",
      "includePath": [
        "${default}",
        "${workspaceFolder}/**",
        "/opt/ros/foxy/include/**"
      ],
      "defines": [],
      "compilerPath": "/usr/bin/g++",
      "cStandard": "c99",
      "cppStandard": "c++14",
      "intelliSenseMode": "linux-gcc-x64"
    }
  ],
  "version": 4
}
```
+ Task 설정

Task는 vsCode에서는 외부 프로그램을 Command Line Interface (CLI) 을 통해 연동하게 하는 기능이다.
아래의 내용은 ROS 2에서 빌드할 때 사용되는 colcon과 관려한 build, test, clean 작업을 Task로 만들었다. 이를 통해 VScode에서 `Ctrl + Shift + b`로 빌드할 수 있고 아래와 같이 기본 설정 이외의 Task도 실행할 수 있다.
`Ctrl + Shift + p` > Tasks: Run Task > 지정한 Task 선택
```
cd ~/robot_ws/.vscode
code tasks.json
```
tasks.json 파일에 아래 코드를 작성한다.
```
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "colcon: build",
      "type": "shell",
      "command": "colcon build --cmake-args '-DCMAKE_BUILD_TYPE=Debug'",
      "problemMatcher": [],
      "group": {
        "kind": "build",
        "isDefault": true
      }
    },
    {
      "label": "colcon: test",
      "type": "shell",
      "command": "colcon test && colcon test-result"
    },
    {
      "label": "colcon: clean",
      "type": "shell",
      "command": "rm -rf build install log"

    }
  ]
}
```
+ Launch 설정

VSCode에서의 Launch는 'Run and Debug' (Ctrl + Shift + d)에서 사용되는 실행 명령어로 언어별, 디버거별로 설정이 가능하고 세부 옵션으로 Launch가 실행되기 전 사용할 Task를 지정하거나 콘솔 기능을 설정할 수도 있다. 아래 코드는 ROS 2에서 많이 사용되는 Python과 C++ 언어에 맞추어 VSCode의 디버깅 툴을 지정하였다.
```
cd ~/robot_ws/.vscode
code launch.json
```
launch.json 파일에 아래 코드를 작성한다.
```
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Debug-rclpy(debugpy)",
      "type": "python",
      "request": "launch",
      "program": "${file}",
      "console": "integratedTerminal"
    },
    {
      "name": "Debug-rclcpp(gbd)",
      "type": "cppdbg",
      "request": "launch",
      "program": "${workspaceFolder}/install/${input:package}/lib/${input:package}/${input:node}",
      "args": [],
      "preLaunchTask": "colcon: build",
      "stopAtEntry": true,
      "cwd": "${workspaceFolder}",
      "externalConsole": false,
      "MIMode": "gdb",
      "setupCommands": [
        {
          "description": "Enable pretty-printing for gdb",
          "text": "-enable-pretty-printing",
          "ignoreFailures": true
        }
      ]
    }
  ],
  "inputs": [
    {
      "id": "package",
      "type": "promptString",
      "description": "package name",
      "default": "topic_service_action_rclcpp_example"
    },
    {
      "id": "node",
      "type": "promptString",
      "description": "node name",
      "default": "argument"
    }
  ]
}
```
## 2. ROS2 패키지 노드 생성
<a id=ROS2-패키지-노드-생성></a>





