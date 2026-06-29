import json
import csv
from reportlab.pdfgen import canvas

name = input("Enter Student Name: ")
skill = input("Enter Skill: ")

student = {
    "name": name,
    "skill": skill
}

# JSON Save
with open("students.json", "w") as file:
    json.dump(student, file, indent=4)

# CSV Save
with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Skill"])
    writer.writerow([name, skill])

# PDF Generate
pdf = canvas.Canvas("report.pdf")

pdf.drawString(100, 750, "Student Report")
pdf.drawString(100, 720, f"Name: {name}")
pdf.drawString(100, 690, f"Skill: {skill}")

pdf.save()

print("Project Completed Successfully!")

