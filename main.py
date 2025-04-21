
goals = ["Fit", "Japanese"]
weighting = [1, 1]
progress_input = [["84.60", "68", "84.60"], ["10"]]
progress_is = []

def calculate_progress():
    for x in progress_input:
        if len(x) == 3:
            start_value = float(x[0])
            end_value = float(x[1])
            is_value = float(x[2])
            progress_percent = (start_value - is_value) / (start_value - end_value) * 100
            progress_is.append(progress_percent)
        else:
            progress_is.append(float(x[0]))

def calculate_overall_progress():
    amount_goals = len(goals)
    all_progress = 0
    for progress in progress_is:
        all_progress += progress
    return all_progress / amount_goals

def display_overview():
    print(f"\nOverall progress: {calculate_overall_progress()}%\n")
    print("Progress in details:")
    print(f"You are working on {len(goals)} Projects")
    for x in range(len(goals)):
        if progress_input[x] == 2:
            print(f"{goals[x]}: {progress_input[x][0]} / {progress_input[x][2]}: {progress_is[x]}%")
        else:
            print(f"{goals[x]}: {progress_is[x]}%")

def main():
    if len(goals) != len(weighting) != len(progress_input):
        print("Unequal lengths in input arrays")
        return
    calculate_progress()
    display_overview()

main()