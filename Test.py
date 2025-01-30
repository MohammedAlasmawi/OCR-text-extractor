import os

def create_project_structure(base_dir):
    structure = {
        "controllers": ["__init__.py", "file_controller.py"],
        "models": ["__init__.py", "pdf_processor.py", "response.py"],
        "services": ["__init__.py", "ocr_service.py", "file_service.py"],
        "templates": ["index.html"],
        "uploads": [],
        "utils": ["__init__.py", "exceptions.py"],
    }

    os.makedirs(base_dir, exist_ok=True)
    open(os.path.join(base_dir, "app.py"), "w").close()
    open(os.path.join(base_dir, "requirements.txt"), "w").close()

    for folder, files in structure.items():
        folder_path = os.path.join(base_dir, folder)
        os.makedirs(folder_path, exist_ok=True)
        for file in files:
            open(os.path.join(folder_path, file), "w").close()

    print(f"Project structure for {base_dir} created successfully!")

# Create project
create_project_structure("ocr_app")
