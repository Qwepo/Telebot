import sqlite3


class SQL:
    def __init__(self, database):
        self.connect = sqlite3.connect(database)
        self.cursor = self.connect

    # Add link
    def add(self, id_user, url):
        with self.connect:
            # First, we check whether there is such a user, if not, we add it along with the link
            if not self.chek_user_for_data_base(id_user):
                self.cursor.execute("INSERT INTO link VALUES(?, ?)", (id_user, url))

            else:
                for i in self.cursor.execute("SELECT URL FROM link WHERE ID = ?", (id_user,)):
                    index = ''.join(map(str, i[0]))
                self.cursor.execute("UPDATE link SET URL = ? WHERE ID = ?", (url + '\n' + index, id_user))

    # Getting links as a string
    def get_links(self, id_user):
        with self.connect:
            for i in self.cursor.execute("SELECT URL FROM link WHERE ID = ?", (id_user,)):
                links = ''.join(map(str, i))
        return links

    # Write links to the list for convenient work in the parser
    def list_link(self, id_user):
        list_link = [x for x in self.get_links(id_user).split()]

        return list_link

    # Check for the presence of a user in the database
    def chek_user_for_data_base(self, id_user):
        with self.connect:
            return self.cursor.execute("SELECT * FROM link WHERE ID = ?", (id_user,)).fetchall()

    # Deleting the user and links
    def dell_user_and_links(self, id_user):
        with self.connect:
            self.cursor.execute("DELETE FROM link WHERE ID = ?", (id_user,))
