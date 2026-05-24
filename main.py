from utils import organiser, show_report

def main():
    input_path = input("Enter the path of the directory: ") #C:\Users\User\Desktop\My_Projects\python\Учебные проекты\ProjectsWithFiles\Organiser_Files\Screenshots
    output_path = input("Enter the path of the output directory: ") #C:\Users\User\Desktop\My_Projects\python\Учебные проекты\ProjectsWithFiles\Organiser_Files\output_directory
    show_report(input_path)
    print("Do you want to start organiser? (y/n)")
    user_choice = input(">>>")
    if user_choice.lower().strip() == "y":
        print("\nStarting organiser...\n")
        organiser(input_path, output_path)
    else:
        return

if __name__ == "__main__":
    main()