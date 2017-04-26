def is_valid(new, bottom):
    if not bottom:
        return True
    return all([new[i] < bottom[i] for i in range(3)])


def wrap(boxes):
    stackMap = [0] * len(boxes)
    boxes.sort(key=lambda l: l[1])

    def place(boxes, bottom=None, offset=0):
        if offset > len(boxes) - 1:
            return 0

        new_bottom = boxes[offset]

        height_with_new = 0

        if bottom is None or is_valid(new_bottom, bottom):
            if stackMap[offset] == 0:
                stackMap[offset] = place(boxes, new_bottom, offset + 1) + new_bottom[1]
            height_with_new = stackMap[offset]

        height_without_new = place(boxes, bottom, offset + 1)

        return max(height_with_new, height_without_new)

    return place(boxes)


bs = [[3, 1, 3], [1, 4, 1], [2, 5, 2]]

print(wrap(bs))