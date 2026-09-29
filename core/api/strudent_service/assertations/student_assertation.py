class StudentAssertBase:


    def check_student_response_structure(self, student: dict):

        assert student['id'] > 0
        assert len(student['name']) > 0
        assert student['score'] > 0
        assert student['score'] <=  100
        assert len(student['score_name']) > 0
        assert student['created_date'] > 0
        assert len(student['updated_date']) > 0


    def check_students_is_sorted_by_parameter(self, students: list, sorted_param: str):

        is_reverse_sorting = sorted_param.startswith('-') # якщо починаеться з -, то значить це desc(reverse)


        sorted_list = sorted(students,
                             # прибрати мінус з початку, якщо він там є
                             key=lambda x: x[sorted_param.lstrip('-')],
                             reverse=is_reverse_sorting)

        is_sorted = sorted_list == students
        assert is_sorted, f'List is not sorted by {sorted_param}'
