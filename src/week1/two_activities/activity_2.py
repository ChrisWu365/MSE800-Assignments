import numpy as np

def student_scores():
    """ 2- Activity : You are given the test scores of 5 students across 3 subjects in a 2D NumPy array. Each row represents a student, and each column a subject. See below:
 
            scores = np.array([
                [78, 85, 90],
                [88, 79, 92],
                [84, 76, 88],
                [90, 93, 94],
                [75, 80, 70]
            ])
 
        Tasks:
        1. Calculate and print the average score for each student.
        2. Calculate and print the average score for each subject.
        3. Identify the student (row index) with the highest total score.
        4. Add 5 bonus points to the third subject for all students.
    """
    scores = np.array([
        [78, 85, 90],
        [88, 79, 92],
        [84, 76, 88],
        [90, 93, 94],
        [75, 80, 70]
        ])
    

    np.set_printoptions(precision=2)
    # Calculate and print the average score for each student.
    student_average_score_arr = scores.mean(axis=1)
    print("The average score for each student: ", student_average_score_arr)
    # Calculate and print the average score for each subject.
    subject_average_score_arr = scores.mean(axis=0)
    print("The average score for each subject: ", subject_average_score_arr)
    # Identify the student (row index) with the highest total score.
    # np.argmax(student_average_score_arr) can also identify the student (row index) with the highest total score.
    print("The student (row index) with the highest total score: ", np.argmax(scores.sum(axis=1)))
    # Add 5 bonus points to the third subject for all students.
    scores[:, 2] += 5
    print("After adding 5 bonus points to the third subject for all students, the scores: ", scores)

if __name__ == '__main__':
    student_scores()