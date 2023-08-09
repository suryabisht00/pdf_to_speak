import PyPDF2
import pyttsx3


if __name__ == "__main__":
    pdf_file_path = 'Introduction to Algorithms, Third Edition ( PDFDrive ).pdf'
    pdf_file = open(pdf_file_path, 'rb')
    pdf_reader = PyPDF2.PdfReader(pdf_file)


class index:
    def short_list(self):
        # Initialize an empty string to store the extracted text
        extracted_text = ''
        # Loop through each page and extract text
        for page_num in range(15):
            page = pdf_reader.pages[page_num]
            extracted_text += page.extract_text()
            if "Index" in extracted_text:
                break

            extracted_text = extracted_text.lower()
            # with open("dem0.txt","a",encoding='UTF-8') as  f:
            #     f.write(extracted_text)
        
        return extracted_text

def option1():
    select_topic = index()
    show_index=select_topic.short_list()
    print(show_index)



class speaker:
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    def speak(self):
        page_no = int(input("Enter the page number \n"))
        page_no -= 1
        from_page = pdf_reader.pages[page_no]

        # extracting the text from the PDF
        text = from_page.extract_text()

        return text , page_no
        
def option2():
    output_sound = speaker()    
    text ,page_num = output_sound.speak()
   # reading the text
    speak = pyttsx3.init()
    speak.say(f'You are currently Reading from page number {page_num+1}')
    speak.runAndWait()
    # print(text)# uncomment for see the text.
    speak.say(text)
    speak.runAndWait()



class Continiue_Reading:
    def start_to_last(self):
        P_number = int(input("Enter the Page number :-\n"))
        count = True
        # Loop through each page for continus reading
        for page_num in range(P_number-1,len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            extracted_text = page.extract_text()
            # print(extracted_text)#for print the output uncomment these
            speak = pyttsx3.init()
            if count == True :
                speak.say(f'You are currently Reading from page number {P_number}')
                speak.runAndWait()
                count = False
            speak.say(extracted_text)
            speak.runAndWait()
            speak.say(f'Next page and page number is {P_number+1}')
            speak.runAndWait()

           
        return extracted_text

def option3():
    opt3 = Continiue_Reading()
    opt3.start_to_last()


while True:
    option = input('\n\n\n\nEnter option you want(1,2,3):-\n 1:-show index \t 2:-read a specific page \t 3:-read continious from a page \t 4:-QUIT \n \t :-')
    if option =="1":
        option1()
    elif option == "2":
        option2()
    elif option == '3':
        option3()
    elif option == '4':
        break
    else:
        speak = pyttsx3.init()
        speak.say("Please enter the right option")
        speak.runAndWait()