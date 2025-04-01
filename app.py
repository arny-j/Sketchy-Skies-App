from tkinter import *
from tkinter import messagebox
from ttkbootstrap import Style
from ttkbootstrap.constants import *
from ttkbootstrap.widgets import Button, Frame, Label
from tkinter import ttk
from PIL import Image, ImageTk
from datetime import datetime

# Initialize ttkbootstrap style
style = Style(theme="superhero") 
root = style.master
root.title("Sketchy Skies Database")
root.geometry("1100x650")

# Set a global font for tkinter widgets
root.option_add("*Font", "Lato 12")

# Create a frame for the form
frame = Frame(root)
frame.pack(pady=30, padx=20, fill="both", expand=True)

# Clear frame function
def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()
        
# Navigation history stack
navigation_stack = []

# Back function
def go_back():
    if len(navigation_stack) > 1:  # Ensure there's a previous page to go back to
        navigation_stack.pop()  # Remove the current page
        previous_page = navigation_stack[-1]  # Get the previous page
        previous_page()  # Call the previous page function

# Create the landing page function
def landing_page():
    # Push the current page to the navigation stack
    navigation_stack.append(landing_page)

    clear_frame(frame)

    # Configure the parent frame
    frame.rowconfigure(0, weight=1)
    frame.columnconfigure(0, weight=1)  
    frame.columnconfigure(1, weight=3)  

    # Create a list box for records on the left
    listbox_frame = Frame(frame)
    listbox_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    listbox_label = Label(listbox_frame, text="Records:")
    listbox_label.pack(anchor="w", padx=5, pady=5)

    record_listbox = Listbox(listbox_frame, height=20, width=30)
    record_listbox.pack(fill="both", expand=True, padx=5, pady=5)

    # Add some fake records to the list box
    for i in range(1, 11):
        record_listbox.insert(END, f"Record {i}")

    # Add a "Create" button below the list box
    create_button = Button(listbox_frame, text="Create", width=20, bootstyle="success", command=newRecord, padding=(5, 20))
    create_button.pack(pady=10)

    # Create a details view on the right
    details_frame = ttk.LabelFrame(frame, text="Record Details", padding=(16, 7))
    details_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
    
    # Configure grid weights for details_frame for responsiveness
    details_frame.columnconfigure(0, weight=1)
    details_frame.columnconfigure(1, weight=2) 

    # Hardcoded details
    name_label = Label(details_frame, text="Flight Name:")
    name_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
    name_value = Label(details_frame, text="-")
    name_value.grid(row=0, column=1, padx=10, pady=10, sticky="w")

    description_label = Label(details_frame, text="Flight Description:")
    description_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
    description_value = Text(details_frame, wrap="word", height=5, width=40, padx=5, pady=5)
    description_value.insert("1.0", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. " * 10)
    description_value.config(state="disabled")  # Make the Text widget read-only
    description_value.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

    flight_type_label = Label(details_frame, text="Flight Type:")
    flight_type_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
    flight_type_value = Label(details_frame, text="-")
    flight_type_value.grid(row=2, column=1, padx=10, pady=10, sticky="w")

    date_label = Label(details_frame, text="Record Date:")
    date_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")
    date_value = Label(details_frame, text="-")
    date_value.grid(row=3, column=1, padx=10, pady=10, sticky="w")

    # Add an image field with a fixed size and border
    image_frame = Frame(details_frame, width=200, height=200, borderwidth=2, relief="groove")
    image_frame.grid(row=4, column=0, columnspan=2, pady=10, sticky="n")
    image_frame.grid_propagate(False)  # Prevent the frame from resizing

    # Placeholder for the image
    image_label = Label(image_frame)
    image_label.pack(fill="both", expand=True, padx=5, pady=5)

    # Load and display a sample image (replace 'sample_image.png' with your image path)
    try:
        sample_image = Image.open("#")  # Replace with your image path
        sample_image = sample_image.resize((150, 150))
        sample_image_tk = ImageTk.PhotoImage(sample_image)
        image_label.config(image=sample_image_tk)
        image_label.image = sample_image_tk  # Keep a reference to avoid garbage collection
    except FileNotFoundError:
        image_label.config(text="No Image")

    # Add "Update" and "Delete" buttons side by side at the bottom of the details frame
    button_frame = Frame(details_frame)
    button_frame.grid(row=5, column=0, columnspan=2, pady=20, sticky="s")

    update_button = Button(button_frame, text="Update", width=20, bootstyle="secondary", command=lambda: messagebox.showinfo("Update", "Update operation"), padding=(5, 20))
    update_button.grid(row=0, column=0, padx=5)

    delete_button = Button(button_frame, text="Delete", width=20, bootstyle="danger", command=lambda: messagebox.showinfo("Delete", "Delete operation"), padding=(5, 20))
    delete_button.grid(row=0, column=1, padx=5)

    # Configure grid weights for responsiveness
    details_frame.columnconfigure(0, weight=2)
    details_frame.columnconfigure(1, weight=3)
# Create a new record function
def newRecord():
    # Push the current page to the navigation stack
    navigation_stack.append(newRecord)

    clear_frame(frame)

    # Configure the parent frame to center the form
    frame.rowconfigure(0, weight=1)  # Space above the form
    frame.rowconfigure(1, weight=0)  # Row for the form itself
    frame.rowconfigure(2, weight=1)  # Space below the form
    frame.columnconfigure(0, weight=1)  # Space to the left of the form
    frame.columnconfigure(1, weight=0)  # Column for the form itself
    frame.columnconfigure(2, weight=1)  # Space to the right of the form

    # Create a labeled frame for the form
    form_frame = ttk.LabelFrame(frame, text="New Record", padding=(16, 7))
    form_frame.grid(row=1, column=1, padx=20, pady=20, sticky="nsew")  # Centered in the grid

    # Record name label and entry
    name_label = Label(form_frame, text="Flight Name:")
    name_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
    name_entry = Entry(form_frame, width=50)
    name_entry.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

    # Flight type label and combobox
    flight_type_label = Label(form_frame, text="Flight Type:")
    flight_type_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
    flight_type_combo = ttk.Combobox(
        form_frame,
        values=["Commercial", "Private", "Cargo", "Military", "Exploratory"],
        width=47,
        state="readonly",
    )
    flight_type_combo.set("Select Flight Type")
    flight_type_combo.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

    # Record description label and text field
    description_label = Label(form_frame, text="Flight Description:")
    description_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
    description_entry = Text(form_frame, width=50, height=5, wrap="word")
    description_entry.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

    # Record date label
    date_label = Label(form_frame, text="Record Date:")
    date_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")

    # Create a frame to hold the dropdowns and their labels
    date_frame = Frame(form_frame)
    date_frame.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

    # Add labels for Day, Month, and Year above the combo boxes
    day_label = Label(date_frame, text="Day")
    day_label.grid(row=0, column=0, padx=5, pady=5)

    month_label = Label(date_frame, text="Month")
    month_label.grid(row=0, column=1, padx=5, pady=5)

    year_label = Label(date_frame, text="Year")
    year_label.grid(row=0, column=2, padx=5, pady=5)

    # Get current year for default selection
    current_year = datetime.now().year

    # Day dropdown (1-31)
    day_combo = ttk.Combobox(date_frame, values=list(range(1, 32)), width=5, bootstyle="info")
    day_combo.set(datetime.now().day)
    day_combo.grid(row=1, column=0, padx=5)

    # Month dropdown (1-12)
    month_combo = ttk.Combobox(date_frame, values=list(range(1, 13)), width=5, bootstyle="info")
    month_combo.set(datetime.now().month)
    month_combo.grid(row=1, column=1, padx=5)

    # Year dropdown (current year ± 10)
    year_combo = ttk.Combobox(date_frame, values=list(range(current_year, current_year + 16)), width=8, bootstyle="info")
    year_combo.set(current_year)
    year_combo.grid(row=1, column=2, padx=5)

    # Image URL label and entry
    image_url_label = Label(form_frame, text="Image URL:")
    image_url_label.grid(row=4, column=0, padx=10, pady=10, sticky="w")
    image_url_entry = Entry(form_frame, width=50)
    image_url_entry.grid(row=4, column=1, padx=10, pady=10, sticky="ew")

    # Save button
    save_button = Button(form_frame, text="Save", width=20, bootstyle="success", padding=(5, 20))
    save_button.grid(row=5, column=0, columnspan=2, pady=20)

    # Configure grid weights for responsiveness within the form
    form_frame.columnconfigure(0, weight=1)
    form_frame.columnconfigure(1, weight=3)


# Load the image using Pillow
# image = Image.open("arrow_back.png")
# back_arrow_image_resized = image.resize((12, 12))  # Resize to 24x24 pixels
# back_arrow_image = ImageTk.PhotoImage(back_arrow_image_resized)

# Add a Back button with the resized image
back_button = Button(
    root,
    text="Back",
    bootstyle="secondary",
    command=go_back
)
back_button.place(x=8, y=8)

landing_page()
root.mainloop()