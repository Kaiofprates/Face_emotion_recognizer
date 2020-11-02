from fer import FER
import matplotlib.pyplot as plt


def main():
    detector = FER(mtcnn=True)
    img = plt.imread('./assets/Robin_Williams.jpg')
    result = detector.detect_emotions(img)
    print(result)

if __name__ == "__main__":
    main()