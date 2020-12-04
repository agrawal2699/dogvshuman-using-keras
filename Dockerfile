from ubuntu:18.04
run apt-get update
run apt install vim -y
run apt install python3.7 -y
run apt install python3-pip -y
run pip3 install --upgrade pip
run pip3 install numpy pandas
run pip3 install keras==2.1.5
run pip3 install tensorflow==1.5.0
run pip3 install opencv-python==3.2.0.8
run pip3 install imutils==0.4.6
run pip3 install pillow==4.1.1
run pip3 install h5py==2.7.1
RUN apt install libgl1-mesa-glx -y
copy . /root/
