def processGrades(in_filename, out_filename):
    """
    Reads 'in_filename' (each valid line: "name score").
    Writes "name: PASS" / "name: FAIL" to 'out_filename' (score >= 60 = PASS).

    - Malformed lines (missing score / non-numeric score) are SKIPPED.
    - If the input file cannot be opened, print an error message and return None
      (do NOT crash).
    - Returns the number of students successfully written.
    """
    # TODO
    try:
        f_in = open(in_filename, 'r')
        f_out = open(out_filename, 'w')
        count = 0
        for line in f_in:
            line = line.split()
            if len(line) != 2 or not isinstance(line[1], int):
                continue
            count += 1
            if line[1] >= 60:
                f_out.write('{}, (PASS)'.format(line[0]))
            else:
                f_out.write('{}, (FAIL)'.format(line[0]))
        f_in.close()
        f_out.close()
        return count
    except OSError:
        return None