import os
from tkinter import filedialog, Tk, Label, Button, Entry, messagebox, Frame
from PIL import Image, ImageTk

# Resize function
def resize_images():
    folder_path = filedialog.askdirectory(title="📂 Select Image Folder")
    if not folder_path:
        return

    try:
        width = int(width_entry.get())
        height = int(height_entry.get())
    except ValueError:
        messagebox.showerror("❌ Invalid Input", "Please enter numeric width and height.")
        return

    output_folder = os.path.join(folder_path, "resized_images")
    os.makedirs(output_folder, exist_ok=True)

    count = 0
    for filename in os.listdir(folder_path):
        if filename.lower().endswith((".jpg", ".jpeg", ".png", ".bmp", ".webp")):
            img_path = os.path.join(folder_path, filename)
            try:
                img = Image.open(img_path)
                img_resized = img.resize((width, height))
                base_name = os.path.splitext(filename)[0]
                output_path = os.path.join(output_folder, base_name + ".png")
                img_resized.save(output_path)
                count += 1
            except Exception as e:
                print(f"Error with {filename}: {e}")

    messagebox.showinfo("✅ Done", f"{count} images resized and saved to:\n{output_folder}")

# GUI setup
app = Tk()
app.title("🖼️ Image Resizer Pro")
app.geometry("500x380")
app.configure(bg="#A04BA4")
app.resizable(False, False)

# Icon
icon_path = os.path.join(os.getcwd(), "icon.ico")
if os.path.exists(icon_path):
    try:
        app.iconbitmap(icon_path)
    except:
        print("Icon load failed.")

# Container frame with drop shadow effect
main_frame = Frame(app, bg="white", bd=2, relief="groove")
main_frame.place(relx=0.5, rely=0.5, anchor="center", width=420, height=320)

# Header
Label(main_frame, text="🛠️ Batch Image Resizer Tool", bg="white",
      font=("Segoe UI", 16, "bold"), fg="#2b2b2b").pack(pady=(20, 10))

# Width input
Label(main_frame, text="Width (px):", bg="white", font=("Segoe UI", 11)).pack()
width_entry = Entry(main_frame, font=("Segoe UI", 12), justify="center", bd=2, relief="groove")
width_entry.pack(pady=(0, 10), ipady=3)
width_entry.insert(0, "300")

# Height input
Label(main_frame, text="Height (px):", bg="white", font=("Segoe UI", 11)).pack()
height_entry = Entry(main_frame, font=("Segoe UI", 12), justify="center", bd=2, relief="groove")
height_entry.pack(pady=(0, 15), ipady=3)
height_entry.insert(0, "300")

# Resize Button
Button(main_frame, text="📁 Select Folder & Resize", font=("Segoe UI", 12, "bold"),
       bg="#4CAF50", fg="white", activebackground="#45a049", cursor="hand2",
       command=resize_images).pack(pady=10, ipadx=10, ipady=5)

# Footer
Label(main_frame, text="Converted images saved in 'resized_images' folder",
      bg="white", fg="gray", font=("Segoe UI", 9, "italic")).pack(pady=(5, 0))

# Start GUI
app.mainloop()
