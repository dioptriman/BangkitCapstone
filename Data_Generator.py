import pandas as pd
import cv2
import numpy as np

req_images = pd.read_csv('Annotation.csv')
fin_images = req_images.drop_duplicates(subset='filename', keep='last')



def generate_images():
    source_images = fin_images['filename'].to_list()

    images = []

    for i in source_images:
        path = 'train/' + i
        input_image = cv2.imread(path)
        input_image = cv2.resize(input_image, (96, 96))
        images.append(input_image)
#       cv2.imwrite('img_t.jpg',input_image)

    images = np.array(images)

    print('images_shape:', images.shape)
    return images, source_images

model_input_images, source_images = generate_images()

fin_images.loc[:, ['width_ratio']] = fin_images['width']/96
fin_images.loc[:, ['height_ratio']] = fin_images['height']/96
fin_images.loc[:, ['xmin']] = fin_images['xmin']/fin_images['width_ratio']
fin_images.loc[:, ['xmax']] = fin_images['xmax']/fin_images['width_ratio']
fin_images.loc[:, ['ymin']] = fin_images['ymin']/fin_images['height_ratio']
fin_images.loc[:, ['ymax']] = fin_images['ymax']/fin_images['height_ratio']


def generate_keypoints():
    keypoint_features = []

    for i in source_images:
        try:
            print(i)
            image_name = i
            mask = fin_images[fin_images['filename'] == image_name]
            mask = mask.values.tolist()
            print(mask)
            keypoints = (mask[0][4:8])
            # print(keypoints)
            newList = [int(x) / 96 for x in keypoints]
            # print(newList)
            keypoint_features.append(newList)
        except:
            print('error !')
    keypoint_features = np.array(keypoint_features, dtype=float)
    return keypoint_features