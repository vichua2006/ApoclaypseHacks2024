# APOCALIFT

### Inspiration

Image that you're a zombie apocalypse survivor, about to explore an unknown region that is potentially filled to the brim with nasty zombies. Navigating that region yourself is not only dangerous, but also time-consuming. So, what do you do? 

Introducing Apocalift!

![image of logo](https://github.com/vichua2006/ApoclaypseHacks2024/blob/main/APOCALIFT/apocalift/static/logo-no-background.png)

### What it does

Our platform provides a remote-controlled drone and RC vehicle rental made tailored for zombie apocalypse survivors, enabling them to explore, monitor, or navigate zombie-infested terrains safely from a distance. Users can control vehicles remotely, accessing real-time video and telemetry data along with maps to assist in various mission-based rentals. These vehicles can be used for a variety of tasks, such as scouting, resource collection, and even defence!

### Tech Stack
web app was built with Flask for the backend, and vanilla JavaScript in frontend, which detects user keypresses and sends them to the backend. From there, data is transmitted to an ESP32 via serial communication, then passed wirelessly to another ESP32. This second ESP32 interprets the signals and controls the movement of the RC car. A Raspberry Pi is used to capture and host a video feed on the local network, which is then displayed to the users on the web app.

### Video Interview + Demo
[Google Drive](https://drive.google.com/file/d/1-vGJD3u7TuKRaUj2j0Wwj25fixyB8XSa/view)
