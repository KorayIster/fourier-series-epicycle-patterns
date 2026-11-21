**- HOW IT WORKS -**

**Code:**

To start this project, implement the following libraries: **Pygame**, and **math**. To do this we use the command, "import"
-     import Pygame
      import math
**Visual Set-Up**:

Now we have to tell Pygame our set display mode for our window of visualization. To do this we must initialize the Pygame modules that we need for this program using **pygame.init()**. Finally we edit the screen display as well as the animation clock. I set my display mode to 800x600:
-     pygame.init()
      screen = pygame.display.set_mode((800, 600))
      clock = pygame.time.Clock()

**Variables**:

To use our math library later in the code, start by defining the variables needed such as the properties of a circle and time.

-     center_x = 200
      center_y = 300
      radius = 100
      time = 0
      wave = []
      num_circles = 5

**Loop**:

Next, we must loop our program so we will create a **Boolean variable** that allows for the program to stay open and then branch off of that by beginning a loop that repeats as long as running is **True**.
-     running = True
      while running:
  **User-Input**:

  To actually allow the user to do stuff in the program, we have to give Pygame a set of events the user can interact with.

-     for event in pygame.event.get():
          if event.type == game pygame.QUIT:
            running = False
          if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
              num_circles += 1
            if event.key == pygame.K_DOWN:
              num_circles = max(1, num_circles -1)
