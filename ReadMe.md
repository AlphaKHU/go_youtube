# Youtube URL to frame images

## How to use(EN)
- Enter youtube URL to download
- Enter how long interval you want to split the video (in seconds)
- Automatically save frames by split-second and delete video

## How to use(KO)
- 프레임을 얻고자 하는 유튜브 영상의 url을 입력합니다
- 몇 초 간격(인터벌)으로 프레임을 얻을지 입력합니다(초단위/ 입력한 초 * 30 번째 프레임을 저장함)
- 영상을 다운받은 후, 입력한(인터벌)번째 프레임을 모두 저장하고, 다운받은 영상을 삭제합니다 

##### 실행 방법 및 실행 옵션

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

## Develop enviornment
- Window10
- Visual studio code
- Python2.7.2 (Python3.6.4)
- Module : cv2 , os , pytube

-from https://wondy1128.tistory.com/148
