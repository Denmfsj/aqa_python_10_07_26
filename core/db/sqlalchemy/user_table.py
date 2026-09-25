from sqlalchemy import Column, Integer, String

from core.db.sqlalchemy.base_class import Base

# Визначення моделі даних (таблиці) за допомогою класу
class User(Base):
    __tablename__ = 'users_orm'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)


    def __str__(self):
        return f'instance of User: id={self.id}, name={self.name}, age={self.age}'






# class CompanyData(SqlRunner):
#
#
#     def __init__(self):
#         self.tabnle_name = 'company_data'
#         self.logger = loggin.getLogger()
#
#
#     def get_company_data_by_company_id(self, cid):
#
#         sql_q = f'select * from {self.tabnle_name} where cid = {cid}'
#         return self.execute_quesry(sql_q)
#
#
#     def get_largets_company_id(self):
#
#         sql_q = f'select * from {self.tabnle_name} where order by market_cap desc'
#         return self.execute_quesry(sql_q)
#
#
#
# # -----------------------
# # test: tests.api_tests.get_company
#
# class TestGetCompany(BaseTestRunner):
#
#     def test_get_company_api_comparing_with_db(self):
#         cid = 1111
#         company_from_api = self.company_ctrl.get_company(cid)  # дані з api
#         company_from_db = CompanyData().get_company_data_by_company_id(cid)
#
#         self.assertation.company_db_and_api_data(company_from_api, company_from_db)
#
#     def test_get_top_10_companies(self):
#         company_from_api = self.company_ctrl.get_companies(page_size=10)  # дані з api
#         company_from_db = CompanyData().get_largets_company_id()
#
#         self.assertation.company_db_and_api_data(company_from_api, company_from_db)