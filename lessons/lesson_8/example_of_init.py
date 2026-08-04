#
#
# class BaseGoogleController:
#
#
#     def read_document(self):
#
#         res = google_lib.open(doc_id=self.document_id, shhet_name=self.tab_name)
#
#         return self.serialize_res(res)
#
#     @staticmethod
#     def serialize_res(res):
#         ...
#     return serialized_res
#
#
#
#
# class GoogleFinParams(BaseGoogleController):  # для конкретного документа по урл
#
#
#     def __init__(self):
#
#         self.document_id = settings.DOCUMENT_FIN_PARAMS_ID  # в файл з параметрами проекта
#         self.tab_name = settings.DOCUMENT_FIN_PARAMS_TAB_NAME  # в файл з параметрами проекта
#
#
#     def get_total_value_for_quartal(self, year, quater):
#
#         doc_data = self.read_document()
#         ...
#         return
#
#
#     def get_all_data_from_column(self, column_name):
#         pass