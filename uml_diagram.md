## PawPal+ UML Diagram

```mermaid
classDiagram
  class Owner {
    +String ownerId
    +String name
    +String preferredScheduleStyle
    +int dailyAvailableMinutes
    +addPet(pet)
    +updatePreferences(style, minutes)
    +getAllTasks()
  }

  class Pet {
    +String petId
    +String name
    +String species
    +int age
    +String notes
    +addTask(task)
    +editTask(taskId, updates)
    +removeTask(taskId)
    +viewTasks()
    +updateInfo(name, age, notes)
  }

  class Task {
    +String taskId
    +String title
    +int durationMinutes
    +int priority
    +String preferredTime
    +String status
    +editTask(updates)
    +markComplete()
  }

  class Scheduler {
    +generateDailySchedule(owner)
    +rankTasksByPriorityAndFit(tasks, availableMinutes)
    +buildTimeline(tasks)
    +explainPlan()
  }

  Owner "1" o-- "1..*" Pet : owns
  Pet "1" o-- "0..*" Task : has care tasks
  Scheduler ..> Owner : uses preferences
  Scheduler ..> Task : selects and orders