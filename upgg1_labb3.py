import string
import operator

#Extract text from txt file

def read_file(file):
    f = open(file, "r")
    file_contents = str(f.read())
    
    f.close()
    return file_contents
    
#read_file(HP_txt)

def lower_casing(file_contents):
    file_contents_lower = file_contents.lower()
    
    return file_contents_lower

#lower_casing(read_file("C:\\Users\\algot\\Downloads\\HP.txt"))
def cleaner(file_contents):
    new_string = ""
    for char in file_contents:
        if char.isalpha() or char == " " or char == "\n":
            new_string += char if char != "\n" else " "
    
    return new_string
    
    

#cleaner("Jag j395///&")

def text_lister(file_contents_lower):
    word_list = file_contents_lower.split()
    
    return word_list


def list_lenth(word_list):
    list_len = len(word_list)
    
    return list_len

def create_dict(word_list):
    word_dictionary = dict.fromkeys(word_list, 0)
    
    return word_dictionary

def dict_length(dict):
    dict_len = len(dict)
    
    return dict_len

#dict_length({"hej", "jo", "bruh"})

def count_words(word_list, word_dictionary):
    for word in word_list:
        word_dictionary[word] += 1
    
    return word_dictionary



def max_key(counted_dictionary):
    if counted_dictionary == {}:
        return "Inga ord förekommer"
    else:
        max_value_key = max(counted_dictionary, key=counted_dictionary.get)
        return max_value_key


def calculate_words(txt_file):
    original_text = read_file(txt_file)
    lower_case_text = lower_casing(original_text)
    clean_text = cleaner(lower_case_text)
    word_list = text_lister(clean_text)
    word_count = list_lenth(word_list)
    word_dict = create_dict(word_list)
    unique_word_count = dict_length(word_dict)
    count_word_dict = count_words(word_list, word_dict)
    most_frequent_word = max_key(count_word_dict)
    if most_frequent_word == "Inga ord förekommer":
        most_frequent_word_count = 0
    else:
        most_frequent_word_count = count_word_dict[most_frequent_word]
    #print("Antal ord: \n", word_count)
    #print("Antal olika ord: \n", unique_word_count)
    #print("Vanligaste ordet är: \n", most_frquent_word, "\n", "som förekommer: \n", count_word_dict[most_frquent_word], "gånger")
    return [word_count, unique_word_count, most_frequent_word, most_frequent_word_count] 

    
#bibel = "C:\\Users\\algot\\Downloads\\bible.txt"



test1 = "C:\\Users\\algot\\Test_filer\\test1.txt" #Vanlig text
test2 = "C:\\Users\\algot\\Test_filer\\test2.txt" #Siffror
test3 = "C:\\Users\\algot\\Test_filer\\test3.txt" #Special tecken
test4 = "C:\\Users\\algot\\Test_filer\\test4.txt" #Tommt 
test5 = "C:\\Users\\algot\\Test_filer\\test5.txt" #Bara mellanslag



def test_file():
    print("Test of calcutlated words")
    textcases_expected = {test1 : [6, 3, "heter", 3], 
                          test2 : [0, 0, "Inga ord förekommer", 0], 
                          test3 : [0, 0, "Inga ord förekommer", 0], 
                          test4 : [0, 0, "Inga ord förekommer", 0], 
                          test5 : [0, 0, "Inga ord förekommer", 0]}
    for i in textcases_expected:
        if calculate_words(i) != textcases_expected[i]:
            print(i, "ger svaren", calculate_words(i), ", men vi förväntade oss svaren", textcases_expected[i])
    print("Test slutfört")

test_file()
