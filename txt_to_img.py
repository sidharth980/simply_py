from PIL import Image
import numpy as np
import math


class Text_Image:
    def convert_to_image(self,data:str,file_name:str,l=8):
        if l<8:l=8
        if not self.__check_argument(data,file_name,l):
            print("Invalid Argumet")
            return None
        try:
            word_in_ascii = np.array(list(map(ord,data)))
        except:
            print('Error in converting to ascii')
            print("Character not in ascii")
            return None
        self.save_image(word_in_ascii,file_name,self.__check_length(len(word_in_ascii)))
    
    def __check_argument(self,data,file_name,l):
        if not isinstance(data,str):
            print("Data Incorrrect Format")
            return False
        if not isinstance(l,int):
            print("Length not an Integer")
            return False
        if not isinstance(file_name,str):
            print("File Name is Not a string")
            return False
        return True
    
    def __format_ascii(self,word_in_ascii):
        word_in_ascii = np.pad(word_in_ascii,(0,3-len(word_in_ascii)%3),'constant')
        return word_in_ascii.reshape((len(word_in_ascii)//3,3))
        
    def __check_length(self,lenght):
        if lenght>192:
            print("Warning Length too low")
            return math.ceil((lenght/3)**0.5)
        return 8

    def save_image(self,word_in_ascii,file_name,l = 8):
        word_in_ascii = self.__format_ascii(word_in_ascii)
        data = np.zeros((l,l, 3), dtype=np.uint8)
        count = 0
        for x in range(len(word_in_ascii)):
            count = x//l
            data[count][x%l]= word_in_ascii[x]
        img = Image.fromarray(data, 'RGB')
        img.save(file_name+'.png')
        img.show()

    def read_image(self,file_name):
        if not isinstance(file_name,str):
            print("Incorrect Argument")
            return None
        mg = np.array(Image.open(file_name+'.png')).ravel()
        # l = len(mg)
        # print(np.array(mg),l)
        data = ""
        for x in mg: data+=chr(x)
        print(data)

    def convert_to_image_encrypted(self,data,file_name):
        word_in_ascii = np.array(list(map(ord,data)))
        print(word_in_ascii)
        key = word_in_ascii[0]*10
        word_in_ascii = (word_in_ascii+key)/4
        print(word_in_ascii)
        print(word_in_ascii*4-key)
            

sample = Text_Image()
# print(sample.__check_length(200))
# sample.convert_to_image("hello how are you , this is sidharth","my")
# sample.read_image('my')
# sample.convert_to_image_encrypted("hello",'my')


# essay = """
# An essay is, generally, a piece of writing that gives the author's own argument, but the definition is vague, overlapping with those of a letter, a paper, an article, a pamphlet, and a short story. Essays have been sub-classified as formal and informal: formal essays are characterized by "serious purpose, dignity, logical organization, length," whereas the informal essay is characterized by "the personal element (self-revelation, individual tastes and experiences, confidential manner), humor, graceful style, rambling structure, unconventionality or novelty of theme," etc.[1]

# Essays are commonly used as literary criticism, political manifestos, learned arguments, observations of daily life, recollections, and reflections of the author. Almost all modern essays are written in prose, but works in verse have been dubbed essays (e.g., Alexander Pope's An Essay on Criticism and An Essay on Man). While brevity usually defines an essay, voluminous works like John Locke's An Essay Concerning Human Understanding and Thomas Malthus's An Essay on the Principle of Population are counterexamples.

# In some countries (e.g., the United States and Canada), essays have become a major part of formal education.[2] Secondary students are taught structured essay formats to improve their writing skills; admission essays are often used by universities in selecting applicants, and in the humanities and social sciences essays are often used as a way of assessing the performance of students during final exams.

# The concept of an "essay" has been extended to other media beyond writing. A film essay is a movie that often incorporates documentary filmmaking styles and focuses more on the evolution of a theme or idea. A photographic essay covers a topic with a linked series of photographs that may have accompanying text or captions."""

# sample.convert_to_image(essay,"essay")
# sample.read_image("essay")
