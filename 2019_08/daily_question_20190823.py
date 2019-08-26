'''
You are given a hash table where the key is a course code,
and the value is a list of all the course codes that are prerequisites for the key.
Return a valid ordering in which we can complete the courses.
If no such ordering exists, return NULL.

Example:
{
  'CSC300': ['CSC100', 'CSC200'],
  'CSC200': ['CSC100'],
  'CSC100': []
}

This input should return the order that we need to take these courses:
 ['CSC100', 'CSC200', 'CSCS300']
'''

def courses_to_take(course_to_prereqs):
    taken = []
    changed = True

    while (changed):
        changed = False

        for course in course_to_prereqs.keys():
            prereqs = courses[course]
            prereq_satisfied = True
            
            for prereq in prereqs:
                prereq_satisfied = prereq_satisfied and (prereq in taken)

            if (prereq_satisfied and (course not in taken)):
                taken.append(course)
                changed = True

    if (len(taken) == len(course_to_prereqs.keys())):
        return taken
    else:
        return NULL

courses = {
  'CSC300': ['CSC100', 'CSC200'],
  'CSC200': ['CSC100'],
  'CSC100': []
}
print (courses_to_take(courses))
# ['CSC100', 'CSC200', 'CSC300']
