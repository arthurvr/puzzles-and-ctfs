import pandas as pd
import cv2                # https://pypi.org/project/opencv-python/

# From the challenge text:
# "the real hint will be given when you find what the columns mean"
# Let's see what the mean values translate to?
file = pd.read_csv('the_data_scientist.csv')
meanvalues = ''.join([
    chr(int(round(x))) for x in file.mean()
])
print(meanvalues)

# Which prints the following:
# "SET ALL VALUES BETWEEN 64 AND 65 TO BLACK AND SCAN IT"

file = (file < 64) | (file > 65)
cv2.imwrite('flag.png', file.to_numpy() * 255);

# Which generates a QR code containing the flag! (You can scan this code using countless online tools, no need to get your phone out)
