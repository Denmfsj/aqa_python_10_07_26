from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


from core.db.sqlalchemy.base_class import Base

class Employee(Base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    department_id = Column(Integer, ForeignKey('departments.id'))

    # Встановлення відношення "багато до одного" з таблицею Department
    department = relationship("Department", back_populates="employees")


    def __str__(self):
        return f'id={self.id}, name={self.name}, department={self.department}'
