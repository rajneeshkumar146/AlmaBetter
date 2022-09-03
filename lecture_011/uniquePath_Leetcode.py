def mazePath(sr, sc, er, ec, ans):
    if sr == er and sc == ec:
        return 1

    count = 0
    if sr + 1 <= er:  # Horizontal
        count += mazePath(sr + 1, sc, er, ec)

    if sr + 1 <= er and sc + 1 <= ec:  # Diagonal
        count += mazePath(sr + 1, sc + 1, er, ec)

    if sc + 1 <= ec:  # Vertical
        count += mazePath(sr, sc + 1, er, ec)

    return count