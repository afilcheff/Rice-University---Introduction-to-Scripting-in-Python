"""
Project for Week 4 of "Python Data Representations".
Find differences in file contents.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""
import string

IDENTICAL = -1

DUMMY_Z = 'qwe'
DUMMY_X= 'qwe asd'
DUMMY_C = 'qwa'


def singleline_diff(line1, line2):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
    Output:
      Returns the index where the first difference between
      line1 and line2 occurs.

      Returns IDENTICAL if the two lines are the same.
    """
    if line1 == line2:
        return IDENTICAL
    else:
        if len(line1) > len(line2):
            smaller_line = line2
        else:
            smaller_line = line1
        if len(smaller_line) == 0:
            return 0
        
        for char in range(len(smaller_line)):
            if line1[char] == line2[char]:
                if char == (len(smaller_line)-1):
                    dummy_char1 = char+1
                    return dummy_char1
            else:
                return char


#Some simple tests:
#print(singleline_diff(DUMMY_Z,DUMMY_C))
#print(singleline_diff(DUMMY_Z,DUMMY_X))
#print(singleline_diff(DUMMY_Z,DUMMY_V))

# Expected output:
## 2
## 3
## 0

DUMMY_V = ''
DUMMY_Q = 'qwe\neq'

def singleline_diff_format(line1, line2, idx):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
      idx   - index at which to indicate difference
    Output:
      Returns a three line formatted string showing the location
      of the first difference between line1 and line2.

      If either input line contains a newline or carriage return,
      then returns an empty string.

      If idx is not a valid index, then returns an empty string.
    """
    dummy_list1 = []
    dummy_list2 = []
    for char1 in line1:
        dummy_list1.append(char1)
    for char2 in line2:
        dummy_list2.append(char2)
    min_len= min((len(line1), len(line2)))
    if idx > min_len:
        return ''
    elif '\n' in dummy_list1:
        return ''
    elif '\n' in dummy_list2:
        return ''
    elif idx == -1:
        return ''
    else:
        dummy_singlediff = line1 + '\n' + ((idx)*('=') + '^') + '\n' + line2 + '\n'
        return dummy_singlediff
        
    

#Some simple tests:
#print(singleline_diff_format(DUMMY_Q, DUMMY_Z, singleline_diff(DUMMY_Q, DUMMY_Z)))
#print(singleline_diff_format(DUMMY_C, DUMMY_Z, singleline_diff(DUMMY_C, DUMMY_Z)))
#print(singleline_diff_format(DUMMY_X, DUMMY_Z, singleline_diff(DUMMY_X, DUMMY_Z)))
#print(singleline_diff_format('abc','abd',1))

# Expected output:
## ''
## qwa '\n' ==^ '\n' qwe '\n'
## qwe asd '\n' ===^ 'n\' qwe '\n'
## ''



def multiline_diff(lines1, lines2):
    """
    Inputs:
      lines1 - list of single line strings
      lines2 - list of single line strings
    Output:
      Returns a tuple containing the line number (starting from 0) and
      the index in that line where the first difference between lines1
      and lines2 occurs.

      Returns (IDENTICAL, IDENTICAL) if the two lists are the same.
    """
    if lines1 == lines2:
        return (IDENTICAL, IDENTICAL)
    else:
        if len(lines1) > len(lines2):
            smaller_lines = lines2
        else:
            smaller_lines = lines1
        if len(smaller_lines) == 0: 
            return 0, 0
        
        
        for line in range(len(smaller_lines)):
            if lines1[line] == lines2[line]:
                if line == (len(smaller_lines) - 1):
                    dummy_lane = line + 1
                    return dummy_lane, 0
            else:
                dummy_lane2 = singleline_diff(lines1[line], lines2[line])
                return line, dummy_lane2

#Some simple tests:
#print(multiline_diff(['1\n','3\n'], ['1\n', '2\n']))
#print(multiline_diff(['a'], ['b']))
#print(multiline_diff(['line1', 'line2'], ['line1', 'line2', 'line3']))

# Expected output:
## (1,0)
## (0,0)
## (2,0)

def get_file_lines(filename):
    """
    Inputs:
      filename - name of file to read
    Output:
      Returns a list of lines from the file named filename.  Each
      line will be a single line string with no newline ('\n') or
      return ('\r') characters.

      If the file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    list_lines = []
    openfile = open(filename, 'rt')
    read_file = openfile.readlines()
    openfile.close()
        
    for line in read_file:
        #list_lines.append(line[:-1])
        list_lines.append(line.strip('\n'))
    return list_lines

#Tests:
#print(get_file_lines('file1.txt'))

#Expected output:
## ['engineering classes', 'science classes']

def file_diff_format(filename1, filename2):
    """
    Inputs:
      filename1 - name of first file
      filename2 - name of second file
    Output:
      Returns a four line string showing the location of the first
      difference between the two files named by the inputs.

      If the files are identical, the function instead returns the
      string "No differences\n".

      If either file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    file1 = get_file_lines(filename1)
    file2 = get_file_lines(filename2)
    if file1 == file2:
        return 'No differences\n'
    else:
        dummy_diff = multiline_diff(file1, file2)
        dummy_line = dummy_diff[0]
        dummy_inx = dummy_diff[1]
        dummy_format = singleline_diff_format(file1[dummy_line], file2[dummy_line], dummy_inx)
        dude = 'Line ' + str(dummy_line) + ':\n' + dummy_format
        return dude

#print(file_diff_format('file8.txt', 'file9.txt')) - cant fix this error
print(file_diff_format('file1.txt', file2.txt)

    
