def is_valid(new, last):
    if not last:
        return True
    return all([new[i] < last[i] for i in range(3)])


def place(boxes, last=None, height=0):
    heights = [height]

    for box in boxes:
        if is_valid(box, last):
            rest = list(boxes)
            rest.remove(box)
            heights.append(place(rest, box, height + box[1]))

    return max(heights)


bs = [[1, 1, 1], [2, 5, 2], [3, 1, 3]]

print(place(bs))
