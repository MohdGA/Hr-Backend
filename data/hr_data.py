from models.hr import hrModel
from models.leave import leaveModel
from models.performance import performanceModel
from datetime import date

hr_list = [
    hrModel(name = "Ahmed", department = "IT", salary = 600, user_id = 1),
    hrModel(name = "Mohammed", department = "Marketing", salary = 1000, user_id = 1),
    hrModel(name = "Hussain", department = "management", salary = 1600, user_id = 1),
]


leave_list = [
    leaveModel(type = 'vacation',start_date=date(2025, 9, 25), end_date=date(2025, 9, 30), status = 'Approved', hr_id = 1),
    leaveModel(type = 'issue at home',start_date=date(2025, 10, 3), end_date=date(2025, 10, 10), status = 'Approved', hr_id = 2)
]

performance_list = [
    performanceModel(review_date = date(2025, 9, 27), rating = 9, comments = "great job", hr_id = 1)
]