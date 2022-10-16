import cv2
import json

img = cv2.imread('md-d-1.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY_INV)

x = [148, 440, 734, 1028, 1320]
ans_list = ['A', 'B', 'C', 'D', 'E']
answers = {}
q = 1

# Extracting Answers
for row in range(2):

    for col in range(5):

        y1 = 268 + row * 922

        # for one block
        for i in range(20):
            x1 = x[col]
            ans = []

            # for one row (one answer)
            for j in range(5):
                cell = thresh[y1:y1 + 39, x1:x1 + 31]
                count = cv2.countNonZero(cell)
                #                 cv2.putText(img, str(count), (x1,y1), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 1)
                if count > 500:
                    ans.append(ans_list[j])
                x1 += 37

            answers[q] = ans

            q += 1
            y1 += 44

# print(answers)

# Serializing json
json_object = json.dumps(answers, indent=4)

# Writing to sample.json
with open("result.json", "w") as outfile:
    outfile.write(json_object)