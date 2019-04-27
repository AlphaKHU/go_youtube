# Youtube URL to frame images
=======
# Youtube URL to frame images
- 유튜브 영상을 프레임 단위로 저장하는 기능을 구현하기 위한 레파지토리입니다.
- 유튜브 영상을 다운받는데 다소 시간이 걸립니다.
- 입력한 초단위(정수)로 프레임을 저장하기때문에 연속된 프레임을 저장할 수 없습니다.
- 이미지 프레임들은 frame폴더에 frame + (프레임번호).jpg 로 저장됩니다.

#### 실행 방법 및 실행 옵션

- Input

  ```python
  $ python frameExtract.py
  $ Enter url to get video : (pleass enter youtube url here)
  $ How long interval do you want(second)? : (please enter integer(1~n))
  ```

  - 프레임을 얻고자 하는 유튜브 동영상의 URL을 입력합니다.
  - 프레임을 얻고자 하는 시간간격을 초단위로 입력합니다(30fps기준).

- Output

  ```python
  $ (Youtube video title)
  $ Creating.../frame/frame0.jpg
  $ Creating.../frame/frame30.jpg
  $ Creating.../frame/frame60.jpg
  ...
  ```

  - 인터벌을 1로 입력했다면 위와 같은 결과가 출력됩니다(인터벌 * 30번째 프레임 저장)
  - 동영상은 다운받아 프레임을 저장한다음 삭제됩니다.


##### 문제점
- 동영상의 원래제목에 ' . ' 이 포함된경우 파일을 찾을 수 없다고 함
- 특정 URL에 대해 패턴 오류가 나는 경우가 있음. 이때는 pytube의 extract.py파일의 120번째줄을 아래와 같이 주석처리 해주면 됨
   ```python
  120 	#    r'\W[\'"]?t[\'"]?: ?[\'"](.+?)[\'"]', watch_html,
  ```

## Develop enviornment
=======
#### Develop enviornment
- Window10
- Visual studio code
- Python2.7.2 (Python3.6.4)
- Module : cv2 , os , pytube

#### Ref
- https://wondy1128.tistory.com/148
