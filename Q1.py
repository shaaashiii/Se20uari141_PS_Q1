def fcfs_scheduling(processes):
    n = len(processes)
    completion_time = [0] * n
    waiting_time = [0] * n
    turnaround_time = [0] * n

    # Calculate completion time for each process
    completion_time[0] = processes[0][2]
    for i in range(1, n):
        completion_time[i] = completion_time[i - 1] + processes[i][2]

    # Calculate waiting time and turnaround time
    for i in range(n):
        turnaround_time[i] = completion_time[i] - processes[i][1]
        waiting_time[i] = turnaround_time[i] - processes[i][2]

    # Calculate average waiting time and average turnaround time
    avg_waiting_time = sum(waiting_time) / n
    avg_turnaround_time = sum(turnaround_time) / n

    return waiting_time, turnaround_time, avg_waiting_time, avg_turnaround_time

def sjf_scheduling(processes):
    n = len(processes)
    processes.sort(key=lambda x: x[2])
    completion_time = [0] * n
    waiting_time = [0] * n
    turnaround_time = [0] * n

    completion_time[0] = processes[0][2]
    for i in range(1, n):
        completion_time[i] = completion_time[i - 1] + processes[i][2]

    for i in range(n):
        turnaround_time[i] = completion_time[i] - processes[i][1]
        waiting_time[i] = turnaround_time[i] - processes[i][2]

    avg_waiting_time = sum(waiting_time) / n
    avg_turnaround_time = sum(turnaround_time) / n

    return waiting_time, turnaround_time, avg_waiting_time, avg_turnaround_time

def priority_scheduling(processes):
    n = len(processes)
    processes.sort(key=lambda x: x[3])
    completion_time = [0] * n
    waiting_time = [0] * n
    turnaround_time = [0] * n

    completion_time[0] = processes[0][2]
    for i in range(1, n):
        completion_time[i] = completion_time[i - 1] + processes[i][2]

    for i in range(n):
        turnaround_time[i] = completion_time[i] - processes[i][1]
        waiting_time[i] = turnaround_time[i] - processes[i][2]

    avg_waiting_time = sum(waiting_time) / n
    avg_turnaround_time = sum(turnaround_time) / n

    return waiting_time, turnaround_time, avg_waiting_time, avg_turnaround_time

def round_robin_scheduling(processes, time_quantum):
    n = len(processes)
    remaining_time = [process[2] for process in processes]
    waiting_time = [0] * n
    turnaround_time = [0] * n
    current_time = 0

    while any(remaining_time):
        for i in range(n):
            if remaining_time[i] > 0:
                if remaining_time[i] <= time_quantum:
                    current_time += remaining_time[i]
                    turnaround_time[i] = current_time - processes[i][1]
                    remaining_time[i] = 0
                else:
                    current_time += time_quantum
                    remaining_time[i] -= time_quantum

    for i in range(n):
        waiting_time[i] = turnaround_time[i] - processes[i][2]

    avg_waiting_time = sum(waiting_time) / n
    avg_turnaround_time = sum(turnaround_time) / n

    return waiting_time, turnaround_time, avg_waiting_time, avg_turnaround_time


if __name__ == "__main__":
    # Define the processes as (process_id, arrival_time, burst_time, priority)
    processes = [(1, 0, 24, 3), (2, 4, 3, 1), (3, 5, 3, 4), (4, 6, 12, 2)]
      
    print("FCFS Scheduling:")
    fcfs_waiting_time, fcfs_turnaround_time, fcfs_avg_waiting_time, fcfs_avg_turnaround_time = fcfs_scheduling(processes)
    for i in range(len(processes)):
        print(f"Process P{processes[i][0]} - Waiting Time: {fcfs_waiting_time[i]}, Turnaround Time: {fcfs_turnaround_time[i]}")
    print(f"Average Waiting Time: {fcfs_avg_waiting_time}")
    print(f"Average Turnaround Time: {fcfs_avg_turnaround_time}")
    print()

    print("SJF Scheduling:")
    sjf_waiting_time, sjf_turnaround_time, sjf_avg_waiting_time, sjf_avg_turnaround_time = sjf_scheduling(processes)
    for i in range(len(processes)):
        print(f"Process P{processes[i][0]} - Waiting Time: {sjf_waiting_time[i]}, Turnaround Time: {sjf_turnaround_time[i]}")
    print(f"Average Waiting Time: {sjf_avg_waiting_time}")
    print(f"Average Turnaround Time: {sjf_avg_turnaround_time}")
    print()

    print("Priority Scheduling:")
    priority_waiting_time, priority_turnaround_time, priority_avg_waiting_time, priority_avg_turnaround_time = priority_scheduling(processes)
    for i in range(len(processes)):
        print(f"Process P{processes[i][0]} - Waiting Time: {priority_waiting_time[i]}, Turnaround Time: {priority_turnaround_time[i]}")
    print(f"Average Waiting Time: {priority_avg_waiting_time}")
    print(f"Average Turnaround Time: {priority_avg_turnaround_time}")
    print()

    time_quantum = 4
    print(f"Round Robin Scheduling (Time Quantum: {time_quantum}):")
    rr_waiting_time, rr_turnaround_time, rr_avg_waiting_time, rr_avg_turnaround_time = round_robin_scheduling(processes, time_quantum)
    for i in range(len(processes)):
        print(f"Process P{processes[i][0]} - Waiting Time: {rr_waiting_time[i]}, Turnaround Time: {rr_turnaround_time[i]}")
    print(f"Average Waiting Time: {rr_avg_waiting_time}")
    print(f"Average Turnaround Time: {rr_avg_turnaround_time}")

    algorithms = {
        'FCFS': fcfs_avg_turnaround_time,
        'SJF': sjf_avg_turnaround_time,
        'Priority': priority_avg_turnaround_time,
        'RR (Time Quantum 4)': rr_avg_turnaround_time
    }

    min_algorithm = min(algorithms, key=algorithms.get)
    min_avg_turnaround_time = algorithms[min_algorithm]
    print(f"Most suitable algorithm is {min_algorithm}")

