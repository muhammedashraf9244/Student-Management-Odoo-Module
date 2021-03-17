from odoo import models, fields, api, _


class Student(models.Model):
    _name = 'student.student'
    _description = 'Student Information'

    name = fields.Char(string='Name', required=True, index=True, translator=True)
    active = fields.Boolean(string='Active', defalut=True)
    image = fields.Image("Image")
    uni_no = fields.Char(string="Ministry University No.", index=True, required=True, copy=False)
    seat_no = fields.Char("Seat No.", copy=False)
    birth_date = fields.Date(string="Date of Birth", required=True)
    age = fields.Integer(string="Age")
    gender = fields.Selection([("male", "Male"), ("female", "Female")], "Gender", default="male")
    result_ids = fields.One2many("school.results.detail", "student_id", "School Results")
    hobbies_ids = fields.Many2many("hobbies.detail", "student_hobbies_rel", "student_id", "hobbies_id",
                                   "Hobbies Information")
    responsible_id = fields.Many2one("res.partner", "Responsible Person / Next of Kin")
    email = fields.Char(related="responsible_id.email", string="NOK Email", )
    phone = fields.Char(related="responsible_id.phone", string="NOK Contact")
    # degree_id = fields.Many2one("degree.detail", "Degree to Register For")
    ref = fields.Reference(selection=[("res.partner","Partner"),("res.users","User"),
    ("student.student","Student")],string="Reference")
    first_date = fields.Date("First Registration Date")
    last_date = fields.Datetime("Last Registration Date", readonly=True)
    # degree_id = fields.Many2one("degree.detail", "Degree to Register For")
    reg_fees = fields.Float("Registration Fees", default="0.0")
    tut_fees = fields.Float("Tuition Fees ($)", default="0.0")
    total_fees = fields.Float("Total Fees ($)",store=True, readonly=True, compute='_get_total_fees')
    ref_link = fields.Char("External Link")
    health_issues = fields.Selection([("yes", "Yes"), ("no", "No")], "Health Issues", default="no")
    health_notes = fields.Text("Health Issue(s) Details", copy=False)
    template = fields.Html("Template")
    # Represents state of student
    state = fields.Selection([('draft','Draft'),
                              ('medical_interview', 'Medical Interview'),
                              ('academic_interview', 'Academic Interview'),
                             ('first_register', 'First Year Registered'),
                             ('second_register', 'Second Year Registered'),
                             ('third_register', 'Third Year Registered'),
                             ('fourth_register', 'Fourth Year Registered'),
                             ('dismiss', 'Dismissed'),
                             ('alumni', 'Alumni')], "Status", readonly=True, default="draft")

    @api.depends('reg_fees', 'tut_fees')
    def _get_total_fees(self):
        if self.tut_fees or self.reg_fees:
            self.total_fees = self.tut_fees + self.reg_fees


class SchoolResultsDetail(models.Model):

    _name = 'school.results.detail'
    _description = "Student's student secondary education results."

    student_id = fields.Many2one("student.student", "Student", ondelete="cascade")
    subject_id = fields.Many2one("school.results.subject", "Subject")
    result = fields.Float("Result", required=True)


class SchoolResultsSubject(models.Model):

    _name = 'school.results.subject'
    _description = "Student's student secondary education subjects."

    name = fields.Char("Subject", required=True)


class HobbiesDetail(models.Model):

    _name = 'hobbies.detail'
    _description = "Student Hobbies"

    name = fields.Char("Name", required=True)