# APOCALIFT

### Inspiration

Image that you're a zombie apocalypse survivor, about to explore an unknown region that is potentially filled to the brim with nasty zombies. Navigating that region yourself is not only dangerous, but also time-consuming. So, what do you do? 

Introducing Apocalift!

![image of logo](.\APOCALIFT\apocalift\static\logo-no-background.png)

### What it does

Our platform provides a remote-controlled drone and RC vehicle rental made tailored for zombie apocalypse survivors, enabling them to explore, monitor, or navigate zombie-infested terrains safely from a distance. Users can control vehicles remotely, accessing real-time video and telemetry data along with maps to assist in various mission-based rentals. These vehicles can be used for a variety of tasks, such as scouting, resource collection, and even defence!

### Tech Stack
The web app was build with Flask, with vanilla Javascript in frontend that detects user keypress and passes the keys to backend. From there, data is transmitted to an ESP32 via serial communication, then passed wirelessly to another ESP32, who interprets the signal and controls the movement of the RC car. A Raspberry Pi is used to capture and host a video feed on the local network, which is then displayed to the users on the web app.

### Video Demo
coming soon