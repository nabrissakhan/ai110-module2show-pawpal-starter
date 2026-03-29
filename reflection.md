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

- Task:
  - Attributes: description, duration, priority, category, preferred_time, completed
  - Methods: mark_complete(), update_task()

- Scheduler:
  - Methods: generate_daily_plan(), sort_tasks(), filter_tasks(), explain_plan(), detect_conflicts()

- What classes did you include, and what responsibilities did you assign to each?

**b. Design changes**

- Did your design change during implementation?

Yes, my design changed slightly during the skeleton stage.

- If yes, describe at least one change and why you made it.

 Originally, task management responsibilities were placed in the Owner class, but I moved them to the Pet class because tasks belong directly to a specific pet. I also added a tasks list to the Pet class and simplified the Scheduler so it generates a schedule from the Owner object instead of requiring separate pet and task inputs. These changes made the design more modular and easier to implement.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
