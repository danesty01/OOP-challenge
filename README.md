# 🐶 Digital Pet – Python OOP Challenge

Welcome to the *Digital Pet* project! This fun and interactive challenge is built with Python using Object-Oriented Programming (OOP) principles. In this project, you'll create your own virtual pet that can eat, sleep, play, and even learn tricks!

---

## 📁 Project Structure


digital-pet/
├── pet.py        # Contains the Pet class
├── main.py       # Main script to interact with your pet
├── README.md     # Project documentation


---

## 🎯 Objective

Create a Pet class with attributes and methods that simulate real-life pet behaviors.

### 🐾 Pet Attributes:
- name – the name of your pet
- hunger – ranges from 0 (full) to 10 (very hungry)
- energy – ranges from 0 (tired) to 10 (fully rested)
- happiness – ranges from 0 to 10
- tricks – a list to store tricks (bonus feature)

### 🧩 Pet Methods:
- eat() – Decreases hunger by 3 (min 0), increases happiness by 1 (max 10)
- sleep() – Increases energy by 5 (max 10)
- play() – Decreases energy by 2 (min 0), increases happiness by 2 (max 10), increases hunger by 1 (max 10)
- get_status() – Displays the pet's current state
- train(trick) – Teaches a new trick and adds it to the list of learned tricks
- show_tricks() – Displays all the tricks the pet has learned

---

## ✅ Sample Output

bash
Creating pet: Max
Max is eating...
Max is playing...
Max is sleeping...

Max's current status:
Hunger: 2
Energy: 8
Happiness: 9
Tricks: ['roll over', 'play dead']


---

## 🚀 How to Run

1. *Clone the repository:*
   bash
   git clone https://github.com/your-username/digital-pet.git
   cd digital-pet
   

2. *Run the program:*
   bash
   python main.py
   

---

## 💡 Tips

- Use min() and max() to keep attribute values between 0 and 10.
- Handle edge cases (e.g., avoid letting the pet play if energy is 0).

---

## 📸 Submission

To complete the challenge:
- Fork or clone the repo.
- Make your changes.
- Submit the GitHub repo *OR* zip the folder and include a screenshot of the output.

---

## 👥 Collaborators

Thanks to the following collaborator(s) for helping run and test the program and take screenshots:

- [SAMIRA HASSANNOOR] – Ran the program and provided output screenshots
creaturesofcomfort1999@gmail.com

Feel free to add more if others contribute!
---

## 🐕 Happy Coding & Have Fun with Your Pet! 🎉
