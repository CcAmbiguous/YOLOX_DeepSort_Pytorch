from tracker import Tracker
from detector import Detector
import imutils, argparse, cv2, time
import os
from glob import glob

class Debug:
    def mainProgram(self):
        start_time = time.time()
        tracker = Tracker(model='yolox-s', ckpt='weights/yolox_s.pth', filter_class=['person'])
        cap = cv2.VideoCapture('object/test.mp4')  # 运行视频
        #cap = cv2.VideoCapture(0)  # 打开摄像头
        name = 'demo'
        fps = int(cap.get(cv2.CAP_PROP_FPS))
        n = 0
        count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        # print('fps:', fps)
        t = int(1000 / fps)
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        videoWriter = None

        while True:
            _, im = cap.read()
            if im is None:
                break
            im = imutils.resize(im, height=500)
            image, _ = tracker.update(im)

            if videoWriter is None:
                fourcc = cv2.VideoWriter_fourcc(
                    'm', 'p', '4', 'v')  # opencv3.0
                videoWriter = cv2.VideoWriter(
                    'result/result1.mp4', fourcc, fps, (image.shape[1], image.shape[0]))#结果保存路径
            n = n + 1
            s = int((n / count) * 100)
            if n % 5 == 0:
                print(n, '/', count, '   ', s, '%')
            videoWriter.write(image)
            cv2.imshow(name, image)
            cv2.waitKey(t)

            if cv2.getWindowProperty(name, cv2.WND_PROP_AUTOSIZE) < 1:
                break
                # except Exception as e:
                #     print(e)
                #     break

        cap.release()
        videoWriter.release()
        cv2.destroyAllWindows()
        end_time = time.time()
        print(f"time is : {end_time - start_time} s")

if __name__ == "__main__":
    mian = Debug()
    mian.mainProgram()
