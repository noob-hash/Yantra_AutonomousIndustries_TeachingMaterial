# Yantra Autonomous Industry

Welcome to the training repository developed for the Yantra 9.0 event organized by the Robotics Association of Nepal (RAN). This repository is dedicated to preparing participants for the Yantra Autonomous Industry (A.I.) competition.

## Objective

The primary goal of this repository is to provide a starting point for participants to kickstart their journey into autonomous robotics. The code included here serves as a rudimentary introduction, offering foundational concepts to help participants grasp essential elements. It is crucial to note that the code in this repository is not intended for use in the final competition; instead, it acts as a preliminary resource for participants to build upon.

## Key Points

* This repository is part of the pre-competition training program.
* The code provided is basic and serves as an initial introduction to autonomous robotics.
* Participants are encouraged to understand and expand upon this foundation to develop their competitive bots for the Yantra 9.0 competition.

## Important Note

The code included here is not finalized for competition use. Participants are expected to leverage this repository as a learning tool, gaining comprehension and insights to create robust and competitive solutions for the upcoming event.

## Setup and installation
### Downloading Locally
In CMD(Command Prompt) go to a folder you want to download the files in then do the following command

```git clone https://github.com/noob-hash/Yantra_AutonomousIndustries_TeachingMaterial.git```

![image](https://github.com/noob-hash/Yantra_AutonomousIndustries_TeachingMaterial/assets/80933227/e0cf9419-ccee-42f1-9e57-970e03713779)

After the folder has been downloaded you can use VScode to open the downloaded folder.

You may have seen the .env environment in the code you can try to use the same environment but if it doesn't work delete that folder and create your environment.

### Creating environment
If you need to create a virtual environment you can do so in vs code or through the command prompt just ensure you have installed Python before.
The virtual environment ensures that all packages are bundled up and not mixed with another project meaning isolation.

Then use the following command to create a virtual environment

``` python -m venv <<environment_name>> ```

e.g. ```python -m venv .env```

### Using an environment
To use the created environment you just need to execute the activate file inside the environment simplest way to do it is:

``` .\<<environment_name>>\Scripts\activate.ps1 ```

Or if you are in Linux, bash or terminal (Raspberry Pi) try:

``` source <<environment_name>>\Scripts\activate.ps1 ```

e.g. ``` .\.env\Scripts\ativate.ps1 ```

or ``` source .env\Scripts\ativate.ps1 ```

If you get the following error
![image](https://github.com/noob-hash/Yantra_Swarmonoid-trainingMaterial/assets/80933227/6e6c6ec2-c5de-4244-9711-11a15b294f87)
Run PowerShell as administrator, you can find it by searching on the search bar
Then on PowerShell run the following command:

```Set-ExecutionPolicy Unrestricted -Force```

This will allow the running of scripts in the system.

### Installing Libaries
You need to install a few libraries to run these commands which are listed in the requirements.txt file. You can install all of them using the following command:

```pip install -r .\requirements.txt```

Make sure the path to requirements.txt is correct.

### Note
If you see the following when running files on your computer, it is intended as RPi.GPIO library is for Raspberry Pi devices and that code is for hardware control as such it is not intended to run on computers.

![image](https://github.com/noob-hash/Yantra_AutonomousIndustries_TeachingMaterial/assets/80933227/7a85eb0b-5083-4088-91a4-d9dbbd00d763)

In case you try to install RPi.GPIO libary on computer you might see following error. It is also because your device is not a Raspberry Pi device as such intended in your computer devices.

![image](https://github.com/noob-hash/Yantra_AutonomousIndustries_TeachingMaterial/assets/80933227/d3777963-d1c1-4b4b-8a95-7efc6af2b779)

Uncomment RPi.GPIO on requirements.txt file if you are installing on Raspberry Pi.

### Other Errors
If you find an error when trying to run the Python code such as:
![image](https://github.com/noob-hash/Yantra_Swarmonoid-trainingMaterial/assets/80933227/dcd78b40-2c25-4600-ac60-2c2e30097289)

It means that you have not selected your environment's Python interpreter to select it you need to do the following:
In VS code press and hold: Ctrl + Shift + P
Here search for a Python interpreter like so:

![image](https://github.com/noob-hash/Yantra_Swarmonoid-trainingMaterial/assets/80933227/2919460d-7ccb-4c8a-bb5c-d36c43da883b)

There select the interpreter in your environment

![image](https://github.com/noob-hash/Yantra_Swarmonoid-trainingMaterial/assets/80933227/e52617a3-f859-4ed4-b019-d4b27a9bbc11)

If you encounter any other error feel free to add a new issue:

![image](https://github.com/noob-hash/Yantra_AutonomousIndustries_TeachingMaterial/assets/80933227/58abc62d-a4fe-48ee-a9a3-8e724302ce1b)
