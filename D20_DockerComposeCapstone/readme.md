# 📊 System Resource Monitor (Docker Capstone)

A microservices-based application that monitors real-time system health (CPU, RAM, Disk) and visualizes it on a live web dashboard. This project demonstrates the "Sidecar" pattern using Docker containers sharing a volume.

## 🏗️ Architecture
The system consists of two isolated containers orchestrated by **Docker Compose**:

1.  **Backend (Python Monitor):**
    * Uses `psutil` to fetch system metrics (CPU, RAM, Disk).
    * Generates a dynamic HTML report every 5 seconds.
    * Writes data to a shared Docker Volume (`/shared_data`).

2.  **Frontend (Nginx Web Server):**
    * Mounts the same shared volume.
    * Serves the generated `index.html` to the browser via HTTP.

## 🚀 How to Run
Prerequisites: Docker & Docker Compose installed.

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YOUR-USERNAME/learning-devops.git](https://github.com/YOUR-USERNAME/learning-devops.git)
    cd learning-devops/day20_capstone
    ```

2.  **Start the Application:**
    ```bash
    docker-compose up --build
    ```

3.  **View the Dashboard:**
    Open your browser and go to:
    👉 **http://localhost:8080**

4.  **Stop the Application:**
    Press `Ctrl+C` in the terminal, then run:
    ```bash
    docker-compose down
    ```

## 🛠️ Technologies Used
* **Containerization:** Docker, Dockerfile
* **Orchestration:** Docker Compose (YAML)
* **Scripting:** Python 3.9 (psutil library)
* **Web Server:** Nginx (Alpine Linux)
* **Concepts:** Shared Volumes, Container Networking, Environment Variables

## 📸 Snapshot
* **CPU:** Real-time percentage
* **RAM:** Memory usage
* **Disk:** Root volume usage