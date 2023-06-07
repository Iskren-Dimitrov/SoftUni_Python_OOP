from unittest import TestCase, main

from project.student import Student


class StudentTest(TestCase):
    def setUp(self):
        self.student = Student("some name")
        self.student_with_courses = Student("some name", {"math": ["some note"]})

    def test_initialization_class_attributes(self):
        self.assertEqual("some name", self.student.name)
        self.assertEqual({}, self.student.courses)
        self.assertEqual({"math": ["some note"]}, self.student_with_courses.courses)

    def test_when_course_name_is_in_courses(self):
        result = self.student_with_courses.enroll("math", ["another note"])

        self.assertEqual({"math": ["some note", "another note"]}, self.student_with_courses.courses)
        self.assertEqual("Course already added. Notes have been updated.", result)

    def test_when_add_course_note_is_Y(self):
        result = self.student.enroll("some name", ["some note"], "Y")

        self.assertEqual({"some name": ["some note"]}, self.student.courses)
        self.assertEqual("Course and course notes have been added.", result)

    def test_when_add_course_note_is_blank_space(self):
        result = self.student.enroll("some name", ["some note"])

        self.assertEqual({"some name": ["some note"]}, self.student.courses)
        self.assertEqual("Course and course notes have been added.", result)

    def test_when_course_is_added(self):
        result = self.student.enroll("some name", [], "N")

        self.assertEqual({"some name": []}, self.student.courses)
        self.assertEqual("Course has been added.", result)

    def test_when_course_name_in_courses_append_notes(self):
        result = self.student_with_courses.add_notes("math", "other note")

        self.assertEqual({"math": ["some note", "other note"]}, self.student_with_courses.courses)
        self.assertEqual("Notes have been updated", result)

    def test_when_course_name_not_in_courses(self):
        with self.assertRaises(Exception) as ex:
            self.student_with_courses.add_notes("biology", "some note")

        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_when_course_name_in_course_we_pop_course_name(self):
        result = self.student_with_courses.leave_course("math")

        self.assertEqual({}, self.student_with_courses.courses)
        self.assertEqual("Course has been removed", result)

    def test_when_course_name_not_in_courses_ex_error(self):
        with self.assertRaises(Exception) as ex:
            self.student_with_courses.leave_course("chemistry")

        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))


if __name__ == "__main__":
    main()
