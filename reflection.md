# PawPal+ Project Reflection

## 1. System Design

Three core actions that a user should be able to perform in PawPal+ are the following:
- Owner and pet information should be able to be entered.
- Manage and add pet care tasks that include and are not limited to:
    - Feeding
    - Walks
    - Medications
    - Grooming
    - Enrichment activities
- Generate and be able to view the plan for daily care on the basis of priority tasks, time that is available, and other preferences from the owner.

**a. Initial design**

My initial UML design included four main classes: Owner, Pet, Task, and Scheduler. The Owner class stores owner information, scheduling preferences, available time, and the pets associated with that owner. The Pet class stores information about each pet and the care tasks assigned to it. The Task class represents an individual pet care activity, including title, duration, priority, preferred time, and status. The Scheduler class is responsible for organizing tasks into a daily plan based on available time, priority, and preferences.

I chose this structure because it separates responsibilities clearly. Owner manages pets, Pet manages tasks, Task represents an individual care activity, and Scheduler handles the planning logic.

- Briefly describe your initial UML design.
My initial UML design includes the following four main classes: Owner, Pet, Task, and Scheduler.
- Owner:
    - Attributes: name, available_time, preferences, pets
    - Methods: add_pet(), get_all_tasks(), update_preferences()

- Pet:
    - Attributes: name, species, age, tasks
    - Methods: add_task(), edit_task(), remove_task(), get_tasks()

-Task:
    - Attributes: title, duration_minutes, priority, preferred_time, status
    - Methods: mark_complete(), edit_task()

- Scheduler:
    - Methods: generate_daily_schedule(), rank_tasks_by_priority_and_fit(), build_timeline(), explain_plan()

- What classes did you include, and what responsibilities did you assign to each?

The system includes four main classes: Owner, Pet, Task, and Scheduler, each with clearly defined responsibilities.

- Owner: Responsible for storing owner information, managing preferences, and maintaining a list of pets. It also provides access to all tasks across pets through get_all_tasks().

- Pet: Represents an individual pet and manages its associated tasks. It handles adding, editing, removing, and viewing tasks.

- Task: Represents a single pet care activity. It stores details such as title, duration, priority, preferred time, and status, and includes methods to update or mark a task as complete.

- Scheduler: Acts as the logic layer of the system. It retrieves tasks from the Owner, prioritizes them based on importance and available time, generates a daily schedule, formats the output, and explains how the plan was created.

**b. Design changes**

- Did your design change during implementation?

Yes, my design changed slightly during the skeleton stage.

- If yes, describe at least one change and why you made it.

 Originally, task management responsibilities were placed in the Owner class, but I moved them to the Pet class because tasks belong directly to a specific pet. I also added a tasks list to the Pet class and simplified the Scheduler so it generates a schedule from the Owner object instead of requiring separate pet and task inputs. These changes made the design more modular and easier to implement.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?

-Available time (daily_available_minutes)
-Task priority (higher priority tasks first)
-Task duration (must fit within remaining time)

- How did you decide which constraints mattered most?

Priority was treated as most important because critical tasks (like medication) should always be completed before lower-priority activities like enrichment.

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.

One tradeoff is that the scheduler prioritizes high-priority tasks even if that means some lower-priority tasks are skipped entirely.

- Why is that tradeoff reasonable for this scenario?

This is reasonable because in the care of pets, essential tasks such as medication and feeding are critical and more important than the optional ones. This is especially the case when time is limited.

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?

AI was used for:

    - Brainstorming the UML design (Owner, Pet, Task, Scheduler)
    - Generating the initial class skeleton
    - Refining relationships between classes
    - Assisting with method structure and debugging

- What kinds of prompts or questions were most helpful?

The most helpful prompts were those that asked AI to:

    - Simplify the design
    - Convert UML into Python classes
    - Review relationships between objects

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.

One example was when AI initially placed task management in the Owner class. This was adjusted so that tasks belong to the Pet class instead.

- How did you evaluate or verify what the AI suggested?

This change was made after evaluating the real-world relationship: tasks are tied directly to pets, not the owner. The design was verified by testing whether task operations felt intuitive and modular.

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?

Key behaviors tested:

    - Adding pets to an owner
    - Adding tasks to a pet
    - Aggregating tasks across pets
    - Generating a schedule within time limits
    - Ensuring higher priority tasks are selected first

- Why were these tests important?

These tests were important to confirm that the scheduling logic behaves correctly under constraints.

**b. Confidence**

- How confident are you that your scheduler works correctly?

I am confident the scheduler works correctly for the main use case, including prioritization and time constraints.

- What edge cases would you test next if you had more time?

If given more time, I would test:

    - Edge cases where no tasks fit within available time
    - Tasks with equal priority
    - Extremely large task lists
    - Invalid inputs (e.g., negative duration)

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

The system design and separation of responsibilities worked well. Breaking the system into Owner, Pet, Task, and Scheduler made the implementation clean and manageable.

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

If iterating further, I would:

    - Improve scheduling logic (e.g., consider preferred time more strongly)
    - Add better explanations for why tasks were skipped
    - Enhance the UI to allow editing and removing tasks

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?

A key takeaway is that designing a clear system structure before coding makes implementation much easier. Additionally, AI is most effective when used as a collaborator rather than blindly accepting its suggestions.

VS Code Copilot features such as Inline Chat and Agent Mode were especially effective for generating class skeletons and refining method implementations. Using separate chat sessions for different phases (design, implementation, testing) helped keep the workflow organized and prevented mixing high-level design decisions with low-level debugging tasks.