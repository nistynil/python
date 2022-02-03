class MemberCard:
        def __init__(self, name, phone_number):
                self.name = name
                self.phone_number = phone_number
        def print_info(self):
                print("---------------------------")
                print("Name: ", self.name)
                print("Phone Number: ", self.phone_number)
                print("---------------------------")
#        def modify_info(self, Modname, Modphone_number):
#                self.name = Modname
#                self.phone_number = Modphone_number

class Books:
        def __init__(self, BookName, BookCategory, BookWriter):
                self.BookName = BookName
                self.BookCategory = BookCategory
                self.BookWriter = BookWriter
        def print_info(self):
                print("---------------------------")
                print("도서명: ", self.BookName)
                print("분류: ", self.BookCategory)
                print("지은이: ", self.BookWriter)
                print("---------------------------")

def set_MemberCard(name, phone_number):
    Member = MemberCard(name, phone_number)
    return Member

def print_MemberCard(MemberCard_list):
    for Member in MemberCard_list:
        Member.print_info()

def delete_MemberCard(MemberCard_list, name, phone_number):
    for i, Member in enumerate(MemberCard_list):
        if Member.name == name and Member.phone_number == phone_number:
            del MemberCard_list[i]
            print("회원 정보가 삭제되었습니다.")

def set_Books(BookName, BookCategory, BookWriter):
    Book = Books(BookName, BookCategory, BookWriter)
    return Book

def print_Books(Book_list):
    for Book in Book_list:
        Book.print_info()

def delete_Books(Book_list, BookName, BookWriter):
    for i, Book in enumerate(Book_list):
        if Book.BookName == BookName and Book.BookWriter == BookWriter:
            del Book_list[i]
            print("도서 정보가 삭제되었습니다.")


def print_menu():
    print("1. 회원 등록")
    print("2. 회원 정보 출력")
    print("3. 회원 삭제")
    print("5. 도서 정보 등록")
    print("6. 도서 정보 출력")
    print("7. 도서 정보 삭제")
    print("10. 도서 대출 (미구현)")
    print("11. 도서 반납 (미구현)")
    print("99. 종료")
    menu = input("무엇을 하시겠습니까?: ")
    return int(menu)

def run():
    MemberCard_list = []
    Book_list = []
    while 1:
        menu = print_menu()
        if menu == 1:
            name = input("등록할 회원의 이름을 입력해주세요: ")
            phone_number = input("등록할 회원의 전화번호를 입력해주세요: ")
            Member = set_MemberCard(name, phone_number)
            MemberCard_list.append(Member)
        elif menu == 2:
            print_MemberCard(MemberCard_list)
        elif menu == 3:
            name = input("삭제할 회원의 이름을 입력해주세요: ")
            phone_number = input("삭제할 회원의 전화번호를 입력해주세요: ")
            delete_MemberCard(MemberCard_list, name, phone_number)
        elif menu == 5:
            BookName = input("등록할 도서명을 입력해주세요: ")
            BookCategory = input("등록할 도서의 분류를 입력해주세요: ")
            BookWriter = input("등록할 도서의 지은이를 입력해주세요: ")
            Book = set_Books(BookName, BookCategory, BookWriter)
            Book_list.append(Book)
        elif menu == 6:
            print_Books(Book_list)
        elif menu == 7:
            BookName = input("삭제할 도서명을 입력해주세요: ")
            BookWriter = input("삭제할 도서의 지은이를 입력해주세요: ")
            delete_Books(Book_list, BookName, BookWriter)

        elif menu == 99:
            break

if __name__ == "__main__":
    run()
