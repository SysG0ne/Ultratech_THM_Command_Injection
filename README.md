# Ultratech_THM_Command_Injection
A basic python script to run few linux comands using **command injection** vulnerability present in **UltraTech** box in **TryHackMe**.
(Just a project for self-satisfaction)

### Note:
It is **NOT** recommended to use this script until you found the vulnerability in the actual box. This is just to help in exploiting

## How to Use:
1. -h for help

       ./cmd_injection_ultratech.py -h
   
  ![output for -h command](https://github.com/SysG0ne/Ultratech_THM_Command_Injection/assets/155179084/50feb79d-46ca-4cec-9667-7b489af95a36)

2. Execute

       ./cmd_injection_ultratech.py -ip HOST_IP -lp LPORT

  ![output of execute](https://github.com/SysG0ne/Ultratech_THM_Command_Injection/assets/155179084/17874ed9-f5fe-4152-bfc8-758b0cdf5169)


## How does it work:
- It exploit the *Command Injection* vulnerability to pass the commands
- The Python Script runs the below steps with every command
    - Run the command and save the output to **/tmp/demo** (victim machine)
    - Opens a **nc** listener at the port provided during the execution
    - Transfer the file over the **nc** connection and save at **/tmp/demo** (attack machine)
    - Show the ouput from the **/tmp/demo** created
- deletes the files in both victim and attack machine
