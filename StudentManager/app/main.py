from app.repository.assignmentFileRepository import AssignmentFileRepository

from app.repository.problemFileRepository import ProblemFileRepository
from app.repository.studentFileRepository import StudentFileRepository
from app.service.assignmentService import AssignmentService
from app.service.problemService import ProblemService
from app.service.studentService import StudentService
from app.ui.consola import Consola



if __name__ == '__main__':
    #testAll()

    studentFileRepository = StudentFileRepository("C:/Users/alexandru/Documents/GitHub/Python/StudentManager/app/txtFiles/student.txt")
    problemFileRepository = ProblemFileRepository("C:/Users/alexandru/Documents/GitHub/Python/StudentManager/app/txtFiles/problem.txt")
    assignmentFileRepository = AssignmentFileRepository("C:/Users/alexandru/Documents/GitHub/Python/StudentManager/app/txtFiles/assignment.txt")

    studentService = StudentService(studentFileRepository)
    problemService = ProblemService(problemFileRepository)
    assignmentService = AssignmentService(assignmentFileRepository, studentFileRepository, problemFileRepository)

    consola = Consola(studentService, problemService, assignmentService)
    consola.menu()
