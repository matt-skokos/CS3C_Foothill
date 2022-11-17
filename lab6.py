from html.parser import HTMLParser


class ListCollector(HTMLParser):
    __data_list = []

    def __init__(self):
        super().__init__()
        self.parser = HTMLParser()
        self.html_string = ''
        self.in_list = False

    def create_string(self):
        html_string = ''
        with open('w3c.html', 'r', encoding='utf-8') as file:
            html_string = file.read()
            return html_string

    def handle_starttag(self, tag, attrs):
        if tag == 'li':
            self.in_list == True
            print("Start tag:", tag)
            for attr in attrs:
                print("     attr:", attr)

    def handle_endtag(self, tag):
        if tag == 'li':
            self.in_list == True
            print("End tag  :", tag)

    def handle_data(self, data):
        if self.in_list:
            self.__data_list.append(data)

    def get_lists(self):
        """ Returns a list containing all the created lists."""
        print(self.__data_list)
        return f"{self.__data_list}"
        # if tag == 'li':
        #     self.handle_starttag(tag)
        #     self.handle_endtag(tag)
        #     # print("End tag  :", tag)
        # self.parser.feed(self.create_string())


def main():
    p1 = ListCollector()
    p1.feed(p1.create_string())
    p1.get_lists()


if __name__ == "__main__":
    main()
