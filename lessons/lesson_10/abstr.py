from abc import ABC, abstractmethod


class DbConnector(ABC):

    # open connection
    # close connection

    @abstractmethod
    def open_connection(self):
        pass

    @abstractmethod
    def close_connection(self):
        pass

    def execute_request(self, query):
        self.open_connection()
        print(f'executing.... {query}')
        self.close_connection()


class Postrges(DbConnector):

    def open_connection(self):
        print('opening connection')

    # def close_connection(self):
    #     print('Closing connection ...')


DbConnector()
print('start .... ')
pq = Postrges()
pq.execute_request('select ...')

