#A very simple way to detect column wildcard usage
import os,glob

#path to the folder where the sql files are located
path = '/Users/sutimurturkan/Desktop/SQLCHECK/sqlqueries-master'

def get_sql_files():
    result = glob.glob(os.path.join(path, '*.sql'))
    return result

def get_file_name(file):
    title = file.split('/')[-1]
    return(title)

def read_sql_files(file):
    f = open(file,"r")
    return f.read()

def query_file(index):
    x = []
    for file in get_sql_files():
        x.append(read_sql_files(file))
    return x[index]

def get_list_of_lines(array):
    array = "".join(array)
    array = array.splitlines()
    return array

def get_list_of_words(line):
    words = line.split(" ")
    words = [x.lower() for x in words]
    return words

def is_column_wildcard(list):
    for i in range(1,len(list)):
        if (list[i-1], list[i]) == ('select','*'):
            return "Column Wildcard Usage"
        else:
            return "No Antipatterns Detected"

def main():
    for i in range(len(get_sql_files())):
        print(get_file_name(get_sql_files()[i]))
        for line in get_list_of_lines(query_file(i)):
            word_list = get_list_of_words(line)
            print(is_column_wildcard(word_list))
        print("------------------------------------")


if __name__ == "__main__":
    main()