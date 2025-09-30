import json

def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data_helper(videos):
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file, indent=4)

def list_all_videos(videos):
    print("\n" + "*" * 70)
    if not videos:
        print("No videos found.")
    else:
        for index, video in enumerate(videos, start=1):
            print(f"{index}. {video['name']}, Duration: {video['time']}")
    print("*" * 70 + "\n")

def add_video(videos):
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    videos.append({"name": name, "time": time})
    save_data_helper(videos)
    print("✅ Video added successfully!")

def update_video(videos):
    list_all_videos(videos)
    try:
        index = int(input("Enter the video number to update: "))
        if 1 <= index <= len(videos):
            name = input("Enter the new video name: ")
            time = input("Enter the new video time: ")
            videos[index - 1] = {"name": name, "time": time}
            save_data_helper(videos)
            print("✅ Video updated successfully!")
        else:
            print("Invalid index selected")
    except ValueError:
        print("❌ Please enter a valid number.")

def delete_video(videos):
    list_all_videos(videos)
    try:
        index = int(input("Enter the video number to be deleted: "))
        if 1 <= index <= len(videos):
            del videos[index - 1]
            save_data_helper(videos)
            print("🗑️ Video deleted successfully!")
        else:
            print("Invalid video index selected")
    except ValueError:
        print("❌ Please enter a valid number.")

def main():
    videos = load_data()   # ✅ Load existing videos
    while True:
        print("\n Youtube Manager | Choose an option ")
        print("1. List all YouTube Videos")
        print("2. Add a YouTube Video")
        print("3. Update a YouTube Video")
        print("4. Delete a YouTube Video")
        print("5. Exit the app")   # ✅ fixed numbering

        choice = input("Enter your choice: ")

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
                print("👋 Exiting... Goodbye!")
                break
            case _:
                print("Invalid Choice")

if __name__ == "__main__":
    main()
