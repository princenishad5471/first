import json
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# ================= Helper Functions =================
def load_data():
    """Load saved videos from file"""
    try:
        with open('youtube.txt', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data(videos):
    """Save videos to file"""
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file, indent=4)

def list_all_videos(videos):
    """List all videos with numbering"""
    print("\n" + "*" * 70)
    if not videos:
        print(Fore.YELLOW + "No videos found.")
    else:
        for index, video in enumerate(videos, start=1):
            print(Fore.CYAN + f"{index}. {video['name']} | Duration: {video['time']} mins")
    print("*" * 70 + "\n")

def add_video(videos):
    """Add a new video"""
    name = input("Enter video name: ")
    time = input("Enter video duration in minutes: ")
    videos.append({"name": name, "time": int(time)})
    save_data(videos)
    print(Fore.GREEN + "Video added successfully!")

def update_video(videos):
    """Update existing video"""
    list_all_videos(videos)
    if not videos:
        return
    try:
        index = int(input("Enter the video number to update: "))
        if 1 <= index <= len(videos):
            name = input("Enter the new video name: ")
            time = int(input("Enter the new video time in minutes: "))
            videos[index - 1] = {"name": name, "time": time}
            save_data(videos)
            print(Fore.GREEN + "Video updated successfully!")
        else:
            print(Fore.RED + "Invalid index selected")
    except ValueError:
        print(Fore.RED + "Invalid input. Please enter a number.")

def delete_video(videos):
    """Delete a video"""
    list_all_videos(videos)
    if not videos:
        return
    try:
        index = int(input("Enter the video number to delete: "))
        if 1 <= index <= len(videos):
            deleted = videos.pop(index - 1)
            save_data(videos)
            print(Fore.GREEN + f"Deleted video: {deleted['name']}")
        else:
            print(Fore.RED + "Invalid index selected")
    except ValueError:
        print(Fore.RED + "Invalid input. Please enter a number.")

def search_video(videos):
    """Search videos by keyword"""
    keyword = input("Enter keyword to search: ").lower()
    results = [v for v in videos if keyword in v['name'].lower()]
    print("\nSearch Results:")
    list_all_videos(results)

def sort_videos(videos):
    """Sort videos by name or duration"""
    print("Sort by: 1) Name  2) Duration")
    choice = input("Enter choice: ")
    if choice == "1":
        sorted_videos = sorted(videos, key=lambda x: x['name'].lower())
    elif choice == "2":
        sorted_videos = sorted(videos, key=lambda x: x['time'])
    else:
        print(Fore.RED + "Invalid choice")
        return
    list_all_videos(sorted_videos)

def total_watch_time(videos):
    """Calculate total watch time"""
    total = sum(v['time'] for v in videos)
    print(Fore.MAGENTA + f"\nTotal Watch Time: {total} minutes ({total/60:.2f} hours)\n")

# ================= Main App =================
def main():
    videos = load_data()
    while True:
        print(Fore.BLUE + "\n📺 YouTube Manager | Choose an option")
        print("1. List all YouTube Videos")
        print("2. Add a YouTube Video")
        print("3. Update a YouTube Video")
        print("4. Delete a YouTube Video")
        print("5. Search Videos")
        print("6. Sort Videos")
        print("7. Total Watch Time")
        print("8. Exit")

        choice = input(Fore.YELLOW + "Enter your choice: ")

        match choice:
            case "1":
                list_all_videos(videos)
            case "2":
                add_video(videos)
            case "3":
                update_video(videos)
            case "4":
                delete_video(videos)
            case "5":
                search_video(videos)
            case "6":
                sort_videos(videos)
            case "7":
                total_watch_time(videos)
            case "8":
                print(Fore.GREEN + "Goodbye! 👋")
                break
            case _:
                print(Fore.RED + "Invalid Choice")

if __name__ == "__main__":
    main()
