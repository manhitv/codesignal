'''
You have some tasks in your Asana account. For each ith of them you know its deadlinesi, which is the last day by which it should be completed. As you can see in your calendar, today's date is day. Asana labels each task in accordance with its due date:
If the task is due today or it's already overdue, it is labeled as Today;
If the task is due within a week but not today - that is, its deadline is somewhere between day + 1 and day + 7 both inclusive - it is labeled as Upcoming;
All other tasks are labeled as Later;
Given an array of deadlines and today's date day, your goal is to find the number of tasks with each label type and return it as an array with the format [Today, Upcoming, Later], where Today, Upcoming and Later are the number of tasks that correspond to that label.
*Example:
For deadlines = [1, 2, 3, 4, 5] and day = 2, the output should be tasksTypes(deadlines, day) = [2, 3, 0].
Today is day 2, so tasks with deadlines at 1 and 2 are labeled as Today. The other three tasks should be completed within a week, so they should be labeled as Upcoming. There are no tasks labeled as Later.
For deadlines = [1, 2, 4, 2, 10, 3, 1, 4, 5, 4, 9, 8] and day = 1, the output should be tasksTypes(deadlines, day) = [2, 8, 2].
Today is day 1, which means that the two tasks with a deadline of 1 are labeled as Today. Tasks with deadlines 10 and 9 are labeled as Later, since their deadlines are more than 7 days ahead. The other eight tasks are labeled as Upcoming.
'''
def tasksTypes(deadlines, day):
    today, upcome, later = 0, 0, 0    
    for ele in deadlines:
        if ele <= day:
            today += 1
        elif ele <= day + 7:
            upcome += 1
        else:
            later += 1
    return [today, upcome, later]

'''
Asana is exploring a smart-workload feature designed to streamline task assignment between coworkers. Newly created tasks will be automatically assigned to the team member with the lightest workload. For the ith person, the following information is known:
names[i] - their name, a string containing only uppercase and lowercase letters;
statuses[i] - their vacation indicator status, which is true if the person is on a vacation, or false otherwise;
projects[i] - the number of projects they are currently involved in;
tasks[i] - the number of tasks assigned to them.
If a person's vacation indicator value is set to true, this means they are on vacation and cannot be assigned new tasks. Conversely, a vacation indicator value of false means they are open to receive task assignments.
Asana sorts team members according to their availability. Person A has a higher availability than person B if they have fewer tasks to do than B, or if these numbers are equal but A has fewer assigned projects than B. Put another way, we can say that person A has a higher availability than person B if their (tasks[A], projects[B]) pair is less than the same pair for B.
Your task is to find the name of the person with the highest availability. It is guaranteed that there is exactly one such person.
*Example:
For names = ["John", "Martin"], statuses = [false, false], projects = [2, 1], and tasks = [16, 5],
the output should be smartAssigning(names, statuses, projects, tasks) = "Martin".
The arguments represent information about two team members:
"John", with statuses[0] = false, projects[0] = 2 and tasks[0] = 16;
"Martin", with statuses[1] = false, projects[1] = 1 and tasks[1] = 5.
Here John and Martin's vacation indicators are both false, so both of them are open to new assignments. Martin is only assigned 5 tasks while John is assigned 16, so Martin has the highest availability.
For names = ["John", "Martin"], statuses = [false, true], projects = [2, 1], and tasks = [6, 5],
the output should be smartAssigning(names, statuses, projects, tasks) = "John".
The arguments stand for the following team members:
"John", with statuses[0] = false, projects[0] = 2 and tasks[0] = 1;
"Martin", with statuses[1] = true, projects[1] = 1 and tasks[1] = 5.
In this example Martin cannot be assigned any new tasks because his vacation indicator is true. Therefore, "John" has the highest availability.
For names = ["John", "Martin"], statuses = [false, false], projects = [1, 2], and tasks = [6, 6],
the output should be smartAssigning(names, statuses, projects, tasks) = "John".
In this case:
"John", with statuses[0] = false, projects[0] = 1 and tasks[0] = 6;
"Martin", with statuses[1] = false, projects[1] = 2 and tasks[1] = 6.
Both John and Martin's vacation indicators are false, and the number of tasks each of them is assigned is 6. However, John is only involved in 1 project, while Martin is involved in 2, meaning that John has the highest availability.
'''
def smartAssigning(names, statuses, projects, tasks):
    
    index = []
    pr = []
    count = 0
    for i in range(len(names)):
        if statuses[i]:
            del names[i], statuses[i], projects[i], tasks[i]
            return smartAssigning(names, statuses, projects, tasks)
        if tasks[i] == min(tasks):
            count += 1
            index.append(i)
    if count == 1:
        return names[tasks.index(min(tasks))]
    for j in index:
        pr.append(projects[j])
    return names[projects.index(min(pr))]
