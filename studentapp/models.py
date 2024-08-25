from django.db import models

class StudentDetails(models.Model):
    challan_no = models.CharField(max_length=50)
    account_no = models.CharField(max_length=50)
    student_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    entry_no = models.CharField(max_length=50, unique=True,primary_key=True)
    degree = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    semester = models.CharField(max_length=50)
    due_date = models.DateField()
    admission_fee = models.FloatField(default=0.0)
    tuition_fee = models.FloatField(default=0.0)
    registration_fee = models.FloatField(default=0.0)
    library_security_fee = models.FloatField(default=0.0)
    examination_fee = models.FloatField(default=0.0)
    masjid_fund = models.FloatField(default=0.0)
    science_lab_charges = models.FloatField(default=0.0)
    sports_fund = models.FloatField(default=0.0)
    computer_fund = models.FloatField(default=0.0)
    university_other_funds = models.FloatField(default=0.0)
    processing_fee = models.FloatField(default=0.0)

    class Meta:
        db_table = 'student_details'
