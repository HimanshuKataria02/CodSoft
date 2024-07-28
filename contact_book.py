import tkinter as tk
from tkinter import messagebox

class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.contacts = {}

        # Create frames
        self.frame1 = tk.Frame(self.root)
        self.frame1.pack(fill="x")
        self.frame2 = tk.Frame(self.root)
        self.frame2.pack(fill="x")
        self.frame3 = tk.Frame(self.root)
        self.frame3.pack(fill="x")

        # Create labels and entries
        tk.Label(self.frame1, text="Name:").pack(side="left")
        self.name_entry = tk.Entry(self.frame1)
        self.name_entry.pack(side="left")
        tk.Label(self.frame1, text="Phone Number:").pack(side="left")
        self.phone_entry = tk.Entry(self.frame1)
        self.phone_entry.pack(side="left")
        tk.Label(self.frame1, text="Email:").pack(side="left")
        self.email_entry = tk.Entry(self.frame1)
        self.email_entry.pack(side="left")
        tk.Label(self.frame1, text="Address:").pack(side="left")
        self.address_entry = tk.Entry(self.frame1)
        self.address_entry.pack(side="left")

        # Create buttons
        tk.Button(self.frame2, text="Add Contact", command=self.add_contact).pack(side="left")
        tk.Button(self.frame2, text="View Contact List", command=self.view_contacts).pack(side="left")
        tk.Button(self.frame2, text="Search Contact", command=self.search_contact).pack(side="left")
        tk.Button(self.frame2, text="Update Contact", command=self.update_contact).pack(side="left")
        tk.Button(self.frame2, text="Delete Contact", command=self.delete_contact).pack(side="left")

        # Create text box
        self.text_box = tk.Text(self.frame3)
        self.text_box.pack(fill="both", expand=True)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()
        if name and phone:
            self.contacts[name] = {"phone": phone, "email": email, "address": address}
            self.name_entry.delete(0, "end")
            self.phone_entry.delete(0, "end")
            self.email_entry.delete(0, "end")
            self.address_entry.delete(0, "end")
            messagebox.showinfo("Success", "Contact added successfully")
        else:
            messagebox.showerror("Error", "Please enter name and phone number")

    def view_contacts(self):
        self.text_box.delete(1.0, "end")
        for name, details in self.contacts.items():
            self.text_box.insert("end", f"Name: {name}, Phone: {details['phone']}\n")

    def search_contact(self):
        name = self.name_entry.get()
        if name in self.contacts:
            details = self.contacts[name]
            messagebox.showinfo("Contact Found", f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}, Address: {details['address']}")
        else:
            messagebox.showerror("Error", "Contact not found")

    def update_contact(self):
        name = self.name_entry.get()
        if name in self.contacts:
            phone = self.phone_entry.get()
            email = self.email_entry.get()
            address = self.address_entry.get()
            self.contacts[name] = {"phone": phone, "email": email, "address": address}
            messagebox.showinfo("Success", "Contact updated successfully")
        else:
            messagebox.showerror("Error", "Contact not found")

    def delete_contact(self):
        name = self.name_entry.get()
        if name in self.contacts:
            del self.contacts[name]
            messagebox.showinfo("Success", "Contact deleted successfully")
        else:
            messagebox.showerror("Error", "Contact not found")

root = tk.Tk()
contact_book = ContactBook(root)
root.mainloop()