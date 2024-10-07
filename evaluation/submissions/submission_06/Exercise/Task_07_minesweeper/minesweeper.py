def annotate(minefield):
    # Function body starts here
    rows = len(minefield)
    cols = len(minefield[0]) if rows > 0 else 0
    result = [[' ' for _ in range(cols)] for _ in range(rows)]

    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    for r in range(rows):
        for c in range(cols):
            if minefield[r][c] == '*':
                result[r][c] = '*'
            else:
                count = 0
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and minefield[nr][nc] == '*':
                        count += 1
                if count > 0:
                    result[r][c] = str(count)

    return [''.join(row) for row in result]
